package com.booking.api.service;

import com.booking.api.dto.SeatResponse;
import com.booking.api.dto.TripSearchResponse;
import com.booking.api.entity.Seat;
import com.booking.api.entity.Trip;
import com.booking.api.repository.SeatRepository;
import com.booking.api.repository.TicketRepository;
import com.booking.api.repository.TripRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDate;
import java.time.LocalDateTime;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class TripService {

    private final TripRepository tripRepository;
    private final SeatRepository seatRepository;
    private final TicketRepository ticketRepository;

    @Transactional(readOnly = true)
    public List<TripSearchResponse> searchTrips(String from,
                                                String to,
                                                LocalDate date,
                                                String type,
                                                Integer passengers) {
        LocalDateTime startOfDay = date.atStartOfDay();
        LocalDateTime endOfDay = date.plusDays(1).atStartOfDay().minusNanos(1);

        String vehicleType = (type == null || type.isBlank()) ? null : type;

        List<Trip> trips = tripRepository.searchTrips(from, to, startOfDay, endOfDay, vehicleType);

        return trips.stream().map(trip -> {
            int totalSeats = trip.getVehicle().getTotalSeats() != null
                    ? trip.getVehicle().getTotalSeats()
                    : 0;
            long bookedCount = ticketRepository.countByTripId(trip.getId());
            int availableSeats = Math.max(0, totalSeats - (int) bookedCount);

            // nếu có tham số passengers thì lọc đủ chỗ
            if (passengers != null && availableSeats < passengers) {
                return null;
            }

            return new TripSearchResponse(
                    trip.getId(),
                    trip.getRoute().getOrigin(),
                    trip.getRoute().getDestination(),
                    trip.getDepartureTime(),
                    trip.getArrivalTime(),
                    trip.getPrice(),
                    trip.getVehicle().getVehicleType(),
                    trip.getVehicle().getProvider().getProviderName(),
                    totalSeats,
                    availableSeats
            );
        }).filter(r -> r != null).collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public List<SeatResponse> getSeatsForTrip(Long tripId) {
        Trip trip = tripRepository.findById(tripId)
                .orElseThrow(() -> new IllegalArgumentException("Trip not found"));

        List<Seat> seats = seatRepository.findByVehicleId(trip.getVehicle().getId());

        return seats.stream()
                .map(seat -> {
                    boolean booked = ticketRepository.existsByTripIdAndSeatId(tripId, seat.getId());
                    return new SeatResponse(
                            seat.getId(),
                            seat.getSeatNumber(),
                            seat.getSeatType(),
                            booked
                    );
                })
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public TripSearchResponse getTripDetail(Long tripId) {
        Trip trip = tripRepository.findById(tripId)
                .orElseThrow(() -> new IllegalArgumentException("Trip not found"));

        int totalSeats = trip.getVehicle().getTotalSeats() != null
                ? trip.getVehicle().getTotalSeats()
                : 0;
        long bookedCount = ticketRepository.countByTripId(trip.getId());
        int availableSeats = Math.max(0, totalSeats - (int) bookedCount);

        return new TripSearchResponse(
                trip.getId(),
                trip.getRoute().getOrigin(),
                trip.getRoute().getDestination(),
                trip.getDepartureTime(),
                trip.getArrivalTime(),
                trip.getPrice(),
                trip.getVehicle().getVehicleType(),
                trip.getVehicle().getProvider().getProviderName(),
                totalSeats,
                availableSeats
        );
    }
}

