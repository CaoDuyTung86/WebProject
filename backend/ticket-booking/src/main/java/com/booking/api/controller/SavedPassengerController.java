package com.booking.api.controller;

import com.booking.api.dto.SavedPassengerDTO;
import com.booking.api.service.SavedPassengerService;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.security.core.annotation.AuthenticationPrincipal;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/api/saved-passengers")
@RequiredArgsConstructor
public class SavedPassengerController {

    private final SavedPassengerService savedPassengerService;

    @GetMapping
    public ResponseEntity<List<SavedPassengerDTO>> list(
            @AuthenticationPrincipal UserDetails userDetails) {
        return ResponseEntity.ok(savedPassengerService.getByUser(userDetails.getUsername()));
    }

    @PostMapping
    public ResponseEntity<SavedPassengerDTO> create(
            @AuthenticationPrincipal UserDetails userDetails,
            @RequestBody SavedPassengerDTO dto) {
        return ResponseEntity.ok(savedPassengerService.create(userDetails.getUsername(), dto));
    }

    @PutMapping("/{id}")
    public ResponseEntity<SavedPassengerDTO> update(
            @AuthenticationPrincipal UserDetails userDetails,
            @PathVariable Long id,
            @RequestBody SavedPassengerDTO dto) {
        return ResponseEntity.ok(savedPassengerService.update(userDetails.getUsername(), id, dto));
    }

    @DeleteMapping("/{id}")
    public ResponseEntity<Void> delete(
            @AuthenticationPrincipal UserDetails userDetails,
            @PathVariable Long id) {
        savedPassengerService.delete(userDetails.getUsername(), id);
        return ResponseEntity.noContent().build();
    }
}
