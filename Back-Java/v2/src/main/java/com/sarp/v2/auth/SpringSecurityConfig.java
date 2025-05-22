package com.sarp.v2.auth;

import java.util.Arrays;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.web.servlet.FilterRegistrationBean;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.core.Ordered;
import org.springframework.http.HttpMethod;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.crypto.bcrypt.BCryptPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.web.cors.CorsConfiguration;
import org.springframework.web.cors.CorsConfigurationSource;
import org.springframework.web.cors.UrlBasedCorsConfigurationSource;
import org.springframework.web.filter.CorsFilter;

import com.sarp.v2.auth.filter.JwtAuthenticationFilter;
import com.sarp.v2.auth.filter.JwtValidationFilter;

@Configuration
public class SpringSecurityConfig {

    @Autowired
    private AuthenticationConfiguration authenticationConfiguration;

    @Bean
    AuthenticationManager authenticationManager() throws Exception{
        return authenticationConfiguration.getAuthenticationManager();
    }

    @Bean
    PasswordEncoder passwordEncoder(){
        return new BCryptPasswordEncoder();
    }    

    @Bean
    SecurityFilterChain filterChain(HttpSecurity http) throws Exception{
        return http.authorizeHttpRequests( authz -> 
            authz
            // Rutas públicas (sin autenticación)
            .requestMatchers(HttpMethod.GET, "/api/users", "/api/users/page/{page}").permitAll()
            // Rutas para usuarios autenticados con rol USER o ADMIN
            .requestMatchers(HttpMethod.GET, "/api/users/{id}").hasAnyRole("USER", "ADMIN")
            // Rutas sólo para administradores
            .requestMatchers(HttpMethod.POST, "/api/users").hasRole("ADMIN")
            .requestMatchers(HttpMethod.PUT, "/api/users/{id}").hasRole("ADMIN")
            .requestMatchers(HttpMethod.DELETE, "/api/users/{id}").hasRole("ADMIN")
            // Cualquier otra ruta requiere autenticación
            .anyRequest().authenticated())
            // Configuración CORS
            .cors(cors -> cors.configurationSource(configurationSource()))
            // Filtros JWT para autenticación y validación
            .addFilter(new JwtAuthenticationFilter(authenticationManager()))
            .addFilter(new JwtValidationFilter(authenticationManager()))
            // Deshabilitar CSRF ya que usamos tokens JWT
            .csrf(config -> config.disable())
            // Configurar política de sesión sin estado
            .sessionManagement( management -> management.sessionCreationPolicy(SessionCreationPolicy.STATELESS))
            .build();
    }

    @Bean
    CorsConfigurationSource configurationSource(){
        CorsConfiguration config = new CorsConfiguration();
        // Configuración de orígenes permitidos
        config.setAllowedOriginPatterns(Arrays.asList( "*"));
        config.setAllowedOrigins(Arrays.asList( "http://localhost:4200"));
        // Métodos HTTP permitidos
        config.setAllowedMethods(Arrays.asList("POST", "GET", "PUT", "DELETE"));
        // Headers permitidos
        config.setAllowedHeaders(Arrays.asList("Authorization", "Content-Type"));
        // Permitir credenciales (cookies, auth headers)
        config.setAllowCredentials(true);

        UrlBasedCorsConfigurationSource source = new UrlBasedCorsConfigurationSource();
        source.registerCorsConfiguration("/**", config);
        
        return source;
    }    

    @Bean
    FilterRegistrationBean<CorsFilter> corsFilter() {
        FilterRegistrationBean<CorsFilter> corsBean = new FilterRegistrationBean<CorsFilter>(
            new CorsFilter(this.configurationSource()));
        // Asignar la mayor prioridad al filtro
        corsBean.setOrder(Ordered.HIGHEST_PRECEDENCE);

        return corsBean;
    }
}
