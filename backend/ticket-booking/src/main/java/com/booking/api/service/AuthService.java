package com.booking.api.service;

import com.booking.api.dto.AuthResponse;
import com.booking.api.dto.ForgotPasswordRequest;
import com.booking.api.dto.GoogleLoginRequest;
import com.booking.api.dto.LoginRequest;
import com.booking.api.dto.RegisterRequest;
import com.booking.api.dto.ResetPasswordRequest;
import com.booking.api.entity.User;
import com.booking.api.exception.DuplicateResourceException;
import com.booking.api.repository.UserRepository;
import com.booking.api.security.JwtService;
import lombok.RequiredArgsConstructor;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.BadCredentialsException;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.core.authority.SimpleGrantedAuthority;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Collections;

@Service
@RequiredArgsConstructor
public class AuthService {

    private final UserRepository userRepository;
    private final PasswordEncoder passwordEncoder;
    private final JwtService jwtService;
    private final AuthenticationManager authenticationManager;

    @Transactional
    public AuthResponse register(RegisterRequest request) {
        if (userRepository.existsByEmail(request.getEmail())) {
            throw new DuplicateResourceException("Email đã được sử dụng: " + request.getEmail());
        }

        User user = new User();
        user.setFullName(request.getFullName());
        user.setEmail(request.getEmail());
        user.setPassword(passwordEncoder.encode(request.getPassword()));
        user.setPhone(request.getPhone());
        user.setRole("ROLE_USER");

        userRepository.save(user);

        var userDetails = new org.springframework.security.core.userdetails.User(
                user.getEmail(),
                user.getPassword(),
                Collections.singletonList(new SimpleGrantedAuthority(user.getRole())));
        String token = jwtService.generateToken(userDetails);

        return new AuthResponse(token, user.getEmail(), user.getFullName(), user.getRole());
    }

    public AuthResponse login(LoginRequest request) {
        try {
            authenticationManager.authenticate(
                    new UsernamePasswordAuthenticationToken(
                            request.getEmail(),
                            request.getPassword()));
        } catch (Exception e) {
            throw new BadCredentialsException("Email hoặc mật khẩu không đúng");
        }

        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new BadCredentialsException("Email hoặc mật khẩu không đúng"));

        var userDetails = new org.springframework.security.core.userdetails.User(
                user.getEmail(),
                user.getPassword(),
                Collections.singletonList(new SimpleGrantedAuthority(user.getRole())));
        String token = jwtService.generateToken(userDetails);

        return new AuthResponse(token, user.getEmail(), user.getFullName(), user.getRole());
    }

    @Transactional(readOnly = true)
    public void forgotPassword(ForgotPasswordRequest request) {
        userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new IllegalArgumentException("Không tìm thấy người dùng với email: " + request.getEmail()));
        // Demo: ở môi trường thực tế sẽ gửi email chứa link đặt lại mật khẩu
    }

    @Transactional
    public void resetPassword(ResetPasswordRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseThrow(() -> new IllegalArgumentException("Không tìm thấy người dùng với email: " + request.getEmail()));

        user.setPassword(passwordEncoder.encode(request.getNewPassword()));
        userRepository.save(user);
    }

    @Transactional
    public AuthResponse googleLogin(GoogleLoginRequest request) {
        User user = userRepository.findByEmail(request.getEmail())
                .orElseGet(() -> {
                    User newUser = new User();
                    newUser.setEmail(request.getEmail());
                    newUser.setFullName(request.getFullName());
                    newUser.setRole("ROLE_USER");
                    // Người dùng đăng nhập Google có thể chưa cần mật khẩu trong demo
                    return userRepository.save(newUser);
                });

        var userDetails = new org.springframework.security.core.userdetails.User(
                user.getEmail(),
                user.getPassword() != null ? user.getPassword() : "",
                Collections.singletonList(new SimpleGrantedAuthority(user.getRole())));
        String token = jwtService.generateToken(userDetails);

        return new AuthResponse(token, user.getEmail(), user.getFullName(), user.getRole());
    }
}
