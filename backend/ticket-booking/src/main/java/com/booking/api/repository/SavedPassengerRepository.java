package com.booking.api.repository;

import com.booking.api.entity.SavedPassenger;
import org.springframework.data.jpa.repository.JpaRepository;

import java.util.List;

public interface SavedPassengerRepository extends JpaRepository<SavedPassenger, Long> {
    List<SavedPassenger> findByUserId(Long userId);
    void deleteByIdAndUserId(Long id, Long userId);
}
