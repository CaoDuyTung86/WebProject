package com.booking.api.service;

import com.booking.api.dto.BookingRequest;
import com.booking.api.dto.BookingResponse;
import com.booking.api.entity.*;
import com.booking.api.exception.BookingException;
import com.booking.api.exception.ResourceNotFoundException;
import com.booking.api.mapper.BookingMapper;
import com.booking.api.repository.*;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.time.LocalDateTime;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

@Service
@RequiredArgsConstructor
public class BookingService {

    private final BookingRepository bookingRepository;
    private final UserRepository userRepository;
    private final TripRepository tripRepository;
    private final SeatRepository seatRepository;
    private final TicketRepository ticketRepository;
    private final AdditionalServiceRepository additionalServiceRepository;
    private final BookingMapper bookingMapper;

    @Transactional
    public BookingResponse createBooking(String email, BookingRequest request) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user"));

        Trip trip = tripRepository.findById(request.getTripId())
                .orElseThrow(() -> new ResourceNotFoundException("Chuyến đi", request.getTripId()));

        List<Ticket> tickets = new ArrayList<>();
        double totalPrice = 0;

        for (Long seatId : request.getSeatIds()) {
            Seat seat = seatRepository.findById(seatId)
                    .orElseThrow(() -> new ResourceNotFoundException("Ghế", seatId));

            if (ticketRepository.existsByTripIdAndSeatId(trip.getId(), seat.getId())) {
                throw new BookingException("Ghế " + seat.getSeatNumber() + " đã được đặt cho chuyến này");
            }

            Ticket ticket = new Ticket();
            ticket.setTrip(trip);
            ticket.setSeat(seat);
            ticket.setPrice(trip.getPrice());
            tickets.add(ticket);

            totalPrice += trip.getPrice();
        }

        Booking booking = new Booking();
        booking.setUser(user);
        booking.setBookingDate(LocalDateTime.now());
        booking.setTotalPrice(totalPrice);
        booking.setStatus("PENDING");

        if (request.getAdditionalServiceIds() != null && !request.getAdditionalServiceIds().isEmpty()) {
            List<AdditionalService> services = additionalServiceRepository.findAllById(request.getAdditionalServiceIds());
            booking.setAdditionalServices(services);
            double servicesTotal = services.stream().mapToDouble(s -> s.getPrice() != null ? s.getPrice() : 0).sum();
            booking.setTotalPrice(totalPrice + servicesTotal);
        } else {
            booking.setAdditionalServices(Collections.emptyList());
        }

        for (Ticket ticket : tickets) {
            ticket.setBooking(booking);
        }
        booking.setTickets(tickets);

        bookingRepository.save(booking);

        return bookingMapper.toBookingResponse(booking, trip);
    }

    @Transactional(readOnly = true)
    public List<BookingResponse> getMyBookings(String email) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user"));

        List<Booking> bookings = bookingRepository.findByUserIdOrderByBookingDateDesc(user.getId());

        return bookings.stream()
                .map(booking -> {
                    Trip trip = null;
                    if (booking.getTickets() != null && !booking.getTickets().isEmpty()) {
                        trip = booking.getTickets().get(0).getTrip();
                    }
                    return bookingMapper.toBookingResponse(booking, trip);
                })
                .collect(Collectors.toList());
    }

    @Transactional(readOnly = true)
    public BookingResponse getBookingDetail(String email, Long bookingId) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user"));

        Booking booking = bookingRepository.findById(bookingId)
                .orElseThrow(() -> new ResourceNotFoundException("Booking", bookingId));

        if (!booking.getUser().getId().equals(user.getId())) {
            throw new BookingException("Bạn không có quyền xem booking này");
        }

        Trip trip = null;
        if (booking.getTickets() != null && !booking.getTickets().isEmpty()) {
            trip = booking.getTickets().get(0).getTrip();
        }

        return bookingMapper.toBookingResponse(booking, trip);
    }

    @Transactional
    public BookingResponse cancelBooking(String email, Long bookingId) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user"));

        Booking booking = bookingRepository.findById(bookingId)
                .orElseThrow(() -> new ResourceNotFoundException("Booking", bookingId));

        if (!booking.getUser().getId().equals(user.getId())) {
            throw new BookingException("Bạn không có quyền hủy booking này");
        }

        if ("CANCELLED".equals(booking.getStatus())) {
            throw new BookingException("Booking này đã được hủy trước đó");
        }

        booking.setStatus("CANCELLED");
        bookingRepository.save(booking);

        Trip trip = null;
        if (booking.getTickets() != null && !booking.getTickets().isEmpty()) {
            trip = booking.getTickets().get(0).getTrip();
        }

        return bookingMapper.toBookingResponse(booking, trip);
    }
}
