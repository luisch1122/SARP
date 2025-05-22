package com.sarp.v2.auth.filter;

import java.io.IOException;
import java.util.Collection;
import java.util.Date;
import java.util.HashMap;
import java.util.Map;

import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.Authentication;
import org.springframework.security.core.AuthenticationException;
import org.springframework.security.core.GrantedAuthority;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;

import com.fasterxml.jackson.core.exc.StreamReadException;
import com.fasterxml.jackson.databind.DatabindException;
import com.fasterxml.jackson.databind.ObjectMapper;
import com.sarp.v2.entities.User;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;

import static com.sarp.v2.auth.TokenJwtConfig.*;


public class JwtAuthenticationFilter extends UsernamePasswordAuthenticationFilter {

    private AuthenticationManager authenticationManager;

    public JwtAuthenticationFilter(AuthenticationManager authenticationManager) {
        this.authenticationManager = authenticationManager;
    }

    @Override
    public Authentication attemptAuthentication(HttpServletRequest request, HttpServletResponse response)
            throws AuthenticationException {
        
                String username = null;
                String password = null;

                try {
                    // Extrae usuario y contraseña del JSON en el cuerpo de la petición
                    User user = new ObjectMapper().readValue(request.getInputStream(), User.class);
                    username = user.getUsername();
                    password = user.getPassword();
                } catch (StreamReadException e) {
                    e.printStackTrace();
                } catch (DatabindException e) {
                    e.printStackTrace();
                } catch (IOException e) {
                    e.printStackTrace();
                }

                // Crea token de autenticación con las credenciales extraídas
                UsernamePasswordAuthenticationToken authenticationToken = new UsernamePasswordAuthenticationToken(username, password);

                // Delega la autenticación al AuthenticationManager
            return this.authenticationManager.authenticate(authenticationToken);
    }

@Override
    protected void successfulAuthentication(HttpServletRequest request, HttpServletResponse response, FilterChain chain,
        Authentication authResult) throws IOException, ServletException {
            
            // Obtiene el usuario autenticado
            org.springframework.security.core.userdetails.User user = (org.springframework.security.core.userdetails.User) authResult.getPrincipal();
            String username = user.getUsername();
            Collection<? extends GrantedAuthority> roles = authResult.getAuthorities();

            // Comprueba si el usuario tiene rol de administrador
            boolean isAdmin = roles.stream().anyMatch(role -> role.getAuthority().equals("ROLE_ADMIN"));

            // Construye los claims (información adicional) del token
            Claims claims = Jwts
                .claims()
                .add("authorities", new ObjectMapper().writeValueAsString(roles))
                .add("Username", username)
                .add("isAdmin", isAdmin)
                .build();

            // Genera el token JWT
            String jwt = Jwts.builder()
                .subject(username)
                .claims(claims)
                .signWith(SECRET_KEY)
                .issuedAt(new Date())
                .expiration(new Date(System.currentTimeMillis() + 3600000)) // 1 hora
                .compact();

            // Agrega el token al encabezado de la respuesta
            response.addHeader(HEADER_AUTHORIZATION, PREFIX_TOKEN + jwt);

            // Construye el cuerpo de la respuesta JSON
            Map<String, String> body = new HashMap<>();
            body.put("token", jwt);
            body.put("username", username);
            body.put("message", String.format("Hola %s has iniciado sesion con exito", username));

            // Envía la respuesta con el token y mensaje
            response.getWriter().write(new ObjectMapper().writeValueAsString(body));
            response.setContentType(CONTENT_TYPE);
            response.setStatus(200);
    }
    
    @Override
    protected void unsuccessfulAuthentication(HttpServletRequest request, HttpServletResponse response,
            AuthenticationException failed) throws IOException, ServletException {
        
        // Construye el cuerpo de la respuesta de error
        Map<String, String> body = new HashMap<>();
        body.put("message", "Error en la autentificacion con el username o password incorrecto!");
        body.put("error", failed.getMessage());
        
        // Envía la respuesta con el error
        response.getWriter().write(new ObjectMapper().writeValueAsString(body));
        response.setContentType(CONTENT_TYPE);
        response.setStatus(401);
    }
}
