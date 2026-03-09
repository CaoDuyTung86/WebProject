package com.booking.api.service;

import com.booking.api.dto.UserResponse;
import com.booking.api.dto.UserUpdateRequest;
import com.booking.api.entity.User;
import com.booking.api.exception.ResourceNotFoundException;
import com.booking.api.mapper.UserMapper;
import com.booking.api.repository.UserRepository;
import lombok.RequiredArgsConstructor;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

@Service
@RequiredArgsConstructor
public class UserService {

    private final UserRepository userRepository;
    private final UserMapper userMapper;

    @Transactional(readOnly = true)
    public UserResponse getProfile(String email) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user với email: " + email));

        return userMapper.toUserResponse(user);
    }

    @Transactional
    public UserResponse updateProfile(String email, UserUpdateRequest request) {
        User user = userRepository.findByEmail(email)
                .orElseThrow(() -> new ResourceNotFoundException("Không tìm thấy user với email: " + email));

        if (request.getFullName() != null) {
            user.setFullName(request.getFullName());
        }
        if (request.getPhone() != null) {
            user.setPhone(request.getPhone());
        }

        userRepository.save(user);

        return userMapper.toUserResponse(user);
    }
}
