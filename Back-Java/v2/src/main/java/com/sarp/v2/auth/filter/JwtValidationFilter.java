package com.sarp.v2.auth.filter;

import java.io.IOException;
import java.util.Arrays;
import java.util.Collection;
import java.util.HashMap;
import java.util.Map;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.web.authentication.www.BasicAuthenticationFilter;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.sarp.v2.auth.SimpleGrantedAuthorityJsonCreator;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.JwtException;
import io.jsonwebtoken.Jwts;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import static com.sarp.v2.auth.TokenJwtConfig.*;

public class JwtValidationFilter extends BasicAuthenticationFilter{

    public JwtValidationFilter(AuthenticationManager authenticationManager) {
        super(authenticationManager);
    }

@Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain chain)
            throws IOException, ServletException {

        // Extraer el header de autorización
        String header = request.getHeader(HEADER_AUTHORIZATION);
        
        // Si no hay token o no tiene el formato esperado, continuar sin autenticación
        if (header == null || !header.startsWith(PREFIX_TOKEN)) {
            chain.doFilter(request, response);
            return;
        }

        // Extraer el token sin el prefijo
        String token = header.replace(PREFIX_TOKEN, "");

        try {
            // Validar y extraer información del token
            Claims claims = Jwts.parser().verifyWith(SECRET_KEY).build().parseSignedClaims(token).getPayload();
            String username = claims.getSubject();
            Object authoritiesClaims = claims.get("authorities");

            // Convertir los roles/autoridades desde el token a objetos GrantedAuthority
            Collection<? extends GrantedAuthority> roles = Arrays.asList(new ObjectMapper()
                .addMixIn(SimpleGrantedAuthority.class, SimpleGrantedAuthorityJsonCreator.class)
                .readValue(authoritiesClaims.toString().getBytes(), SimpleGrantedAuthority[].class));

            // Crear un token de autenticación con el username y roles extraídos del JWT
            UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(
                username, 
                null, // Credenciales ya validadas, no necesitamos la contraseña
                roles);

            // Establecer la autenticación en el contexto de seguridad
            SecurityContextHolder.getContext().setAuthentication(authenticationToken);
            
            // Continuar con la cadena de filtros
            chain.doFilter(request, response);

        } catch (JwtException e) {
            // Manejar errores de validación del token
            Map<String, String> body = new HashMap<>();
            body.put("error", e.getMessage());
            body.put("message", "Error en el token");

            // Devolver respuesta de error 401 (Unauthorized)
            response.getWriter().write(new ObjectMapper().writeValueAsString(body));
            response.setStatus(401);
            response.setContentType(CONTENT_TYPE);
        }
    }    
}
