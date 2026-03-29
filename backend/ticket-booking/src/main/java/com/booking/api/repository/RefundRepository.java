package com.booking.api.repository;

import com.booking.api.entity.Refund;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.query.Param;

import java.util.List;

public interface RefundRepository extends JpaRepository<Refund, Long> {

    List<Refund> findByBookingId(Long bookingId);

    List<Refund> findByStatus(String status);

    @Query("SELECT r FROM Refund r WHERE r.booking.user.id = :userId ORDER BY r.requestedAt DESC")
    List<Refund> findByUserId(@Param("userId") Long userId);

    @Query("SELECT r FROM Refund r JOIN r.booking b JOIN b.tickets t WHERE t.trip.vehicle.provider.id = :providerId ORDER BY r.requestedAt DESC")
    List<Refund> findByProviderId(@Param("providerId") Long providerId);

    @Query("SELECT r FROM Refund r WHERE r.status = 'PENDING' ORDER BY r.requestedAt DESC")
    List<Refund> findAllPending();
}
