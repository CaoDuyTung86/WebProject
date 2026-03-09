package com.booking.api.controller;

import com.booking.api.dto.UserResponse;
import com.booking.api.dto.UserUpdateRequest;
import com.booking.api.service.UserService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
@RequiredArgsConstructor
public class UserController {

    private final UserService userService;

    @GetMapping("/me")
    public ResponseEntity<UserResponse> getMyProfile(
            @AuthenticationPrincipal UserDetails userDetails) {
        UserResponse response = userService.getProfile(userDetails.getUsername());
        return ResponseEntity.ok(response);
    }

    @PutMapping("/me")
    public ResponseEntity<UserResponse> updateMyProfile(
            @AuthenticationPrincipal UserDetails userDetails,
            @RequestBody UserUpdateRequest request) {
        UserResponse response = userService.updateProfile(userDetails.getUsername(), request);
        return ResponseEntity.ok(response);
    }
}
