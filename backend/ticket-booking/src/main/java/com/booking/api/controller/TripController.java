package com.booking.api.controller;

import com.booking.api.dto.SeatResponse;
import com.booking.api.dto.TripSearchResponse;
import com.booking.api.service.TripService;
import lombok.RequiredArgsConstructor;
import org.springframework.format.annotation.DateTimeFormat;
import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.RestController;

import java.time.LocalDate;
import java.util.List;

@RestController
@RequestMapping("/api/trips")
@RequiredArgsConstructor
@CrossOrigin // có thể cấu hình origin cụ thể trong WebConfig
public class TripController {

    private final TripService tripService;

    @GetMapping("/search")
    public List<TripSearchResponse> searchTrips(
            @RequestParam("from") String from,
            @RequestParam("to") String to,
            @RequestParam("date") @DateTimeFormat(iso = DateTimeFormat.ISO.DATE) LocalDate date,
            @RequestParam(value = "type", required = false) String type,
            @RequestParam(value = "passengers", required = false) Integer passengers
    ) {
        return tripService.searchTrips(from, to, date, type, passengers);
    }

    @GetMapping("/{tripId}")
    public TripSearchResponse getTripDetail(@PathVariable Long tripId) {
        return tripService.getTripDetail(tripId);
    }

    @GetMapping("/{tripId}/seats")
    public List<SeatResponse> getSeats(@PathVariable Long tripId) {
        return tripService.getSeatsForTrip(tripId);
    }
}

