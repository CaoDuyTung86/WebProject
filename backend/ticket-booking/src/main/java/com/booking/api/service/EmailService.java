package com.booking.api.service;

import jakarta.mail.MessagingException;
import jakarta.mail.internet.MimeMessage;
import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.mail.javamail.MimeMessageHelper;
import org.springframework.stereotype.Service;

@Service
@RequiredArgsConstructor
@Slf4j
public class EmailService {

    private final JavaMailSender mailSender;

    public void sendResetPasswordEmail(String toEmail, String otpCode) {
        try {
            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true, "UTF-8");

            helper.setTo(toEmail);
            helper.setSubject("Yêu cầu khôi phục mật khẩu - Datxe.com");

            String htmlContent = "<div style='font-family: Arial, sans-serif; padding: 20px; color: #333; max-width: 600px; margin: 0 auto;'>"
                    + "<h2 style='color: #4f7cff;'>Khôi phục mật khẩu</h2>"
                    + "<p>Xin chào,</p>"
                    + "<p>Bạn đã yêu cầu khôi phục mật khẩu tại hệ thống Datxe.com. Vui lòng sử dụng mã OTP gồm 6 chữ số dưới đây để tiếp tục:</p>"
                    + "<div style='background-color: #f4f7f6; border-radius: 8px; padding: 15px; text-align: center; margin: 20px 0;'>"
                    + "<h1 style='letter-spacing: 5px; color: #333; margin: 0; font-size: 32px;'>" + otpCode + "</h1>"
                    + "</div>"
                    + "<p style='color: #d9534f; font-weight: bold;'>Lưu ý: Mã OTP này sẽ hết hạn sau 15 phút.</p>"
                    + "<p>Nếu bạn không thực hiện yêu cầu này, vui lòng bỏ qua email này hoặc liên hệ bộ phận hỗ trợ.</p>"
                    + "<hr style='border: 1px solid #eee; margin-top: 30px;'/>"
                    + "<p style='font-size: 12px; color: #888;'>Trân trọng,<br/>Đội ngũ Datxe.com</p>"
                    + "</div>";

            helper.setText(htmlContent, true);
            mailSender.send(message);
            
            log.info("Reset password email sent successfully to {}", toEmail);
        } catch (MessagingException e) {
            log.error("Failed to send reset password email to {}", toEmail, e);
            throw new RuntimeException("Lỗi máy chủ khi gửi email khôi phục mật khẩu.");
        }
    }

    public void sendVerificationEmail(String toEmail, String otpCode) {
        try {
            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true, "UTF-8");

            helper.setTo(toEmail);
            helper.setSubject("Xác thực tài khoản của bạn - Datxe.com");

            String htmlContent = "<div style='font-family: Arial, sans-serif; padding: 20px; color: #333; max-width: 600px; margin: 0 auto;'>"
                    + "<h2 style='color: #20c997;'>Chào mừng bạn đến với Datxe.com!</h2>"
                    + "<p>Xin chào,</p>"
                    + "<p>Cảm ơn bạn đã đăng ký tài khoản tại hệ thống của chúng tôi. Vui lòng sử dụng mã xác nhận dưới đây để hoàn tất việc đăng ký:</p>"
                    + "<div style='background-color: #f0fff4; border: 1px solid #c6f6d5; border-radius: 8px; padding: 15px; text-align: center; margin: 20px 0;'>"
                    + "<h1 style='letter-spacing: 5px; color: #2f855a; margin: 0; font-size: 32px;'>" + otpCode + "</h1>"
                    + "</div>"
                    + "<p>Mã này có hiệu lực trong vòng 24 giờ.</p>"
                    + "<p>Nếu bạn không thực hiện đăng ký này, vui lòng bỏ qua email này.</p>"
                    + "<hr style='border: 1px solid #eee; margin-top: 30px;'/>"
                    + "<p style='font-size: 12px; color: #888;'>Trân trọng,<br/>Đội ngũ Datxe.com</p>"
                    + "</div>";

            helper.setText(htmlContent, true);
            mailSender.send(message);
            
            log.info("Verification email sent successfully to {}", toEmail);
        } catch (MessagingException e) {
            log.error("Failed to send verification email to {}", toEmail, e);
            throw new RuntimeException("Lỗi máy chủ khi gửi email xác thực.");
        }
    }

    public void sendBookingConfirmation(String toEmail, Long bookingId, Double totalPrice, String seats) {
        try {
            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true, "UTF-8");

            helper.setTo(toEmail);
            helper.setSubject("Xác nhận đặt vé thành công #" + bookingId + " - Datxe.com");

            String htmlContent = "<div style='font-family: Arial, sans-serif; padding: 20px; color: #333; max-width: 600px; margin: 0 auto;'>"
                    + "<h2 style='color: #4f7cff;'>Cảm ơn bạn đã đặt vé!</h2>"
                    + "<p>Xin chào,</p>"
                    + "<p>Chúng tôi đã nhận được thanh toán và xác nhận đặt vé của bạn. Dưới đây là thông tin chi tiết:</p>"
                    + "<div style='background-color: #f9fafb; border: 1px solid #e5e7eb; border-radius: 8px; padding: 15px; margin: 20px 0;'>"
                    + "<p><strong>Mã Booking:</strong> #" + bookingId + "</p>"
                    + "<p><strong>Ghế đã đặt:</strong> " + (seats != null ? seats : "Không có") + "</p>"
                    + "<p><strong>Tổng thanh toán:</strong> <span style='color: #ff6b00; font-weight: bold;'>" + String.format("%,.0f đ", totalPrice) + "</span></p>"
                    + "</div>"
                    + "<div style='background-color: #eff6ff; border-left: 4px solid #4f7cff; padding: 10px 15px; margin: 20px 0;'>"
                    + "<strong>✨ Quà tặng đặc biệt:</strong><br/>"
                    + "Sử dụng mã giảm giá <strong>WELCOME20</strong> cho chuyến đi tiếp theo để nhận ưu đãi 20%!"
                    + "</div>"
                    + "<p>Nếu bạn có bất kỳ câu hỏi nào, vui lòng liên hệ tổng đài hỗ trợ.</p>"
                    + "<hr style='border: 1px solid #eee; margin-top: 30px;'/>"
                    + "<p style='font-size: 12px; color: #888;'>Trân trọng,<br/>Đội ngũ Datxe.com</p>"
                    + "</div>";

            helper.setText(htmlContent, true);
            mailSender.send(message);
            
            log.info("Booking confirmation email sent successfully to {}", toEmail);
        } catch (MessagingException e) {
            log.error("Failed to send booking confirmation email to {}", toEmail, e);
        }
    }

    public void sendSurveyEmail(String toEmail, Long bookingId) {
        try {
            MimeMessage message = mailSender.createMimeMessage();
            MimeMessageHelper helper = new MimeMessageHelper(message, true, "UTF-8");

            helper.setTo(toEmail);
            helper.setSubject("Đánh giá chuyến đi #" + bookingId + " - Datxe.com");

            String htmlContent = "<div style='font-family: Arial, sans-serif; padding: 20px; color: #333; max-width: 600px; margin: 0 auto;'>"
                    + "<h2 style='color: #f59e0b;'>Bạn có hài lòng với chuyến đi?</h2>"
                    + "<p>Xin chào,</p>"
                    + "<p>Hy vọng bạn đã có một trải nghiệm tuyệt vời cùng Datxe.com cho chuyến đi vừa qua (Mã Booking: #" + bookingId + ").</p>"
                    + "<p>Chúng tôi luôn nỗ lực cải thiện dịch vụ mỗi ngày và rất mong nhận được những góp ý, đánh giá chân thành từ bạn.</p>"
                    + "<div style='text-align: center; margin: 30px 0;'>"
                    + "<a href='http://localhost:5174/quan-ly-ve' style='background-color: #ff6b00; color: white; padding: 12px 25px; text-decoration: none; border-radius: 6px; font-weight: bold;'>Đánh giá ngay</a>"
                    + "</div>"
                    + "<p>Xin chân thành cảm ơn thời gian của quý khách.</p>"
                    + "<hr style='border: 1px solid #eee; margin-top: 30px;'/>"
                    + "<p style='font-size: 12px; color: #888;'>Trân trọng,<br/>Đội ngũ Datxe.com</p>"
                    + "</div>";

            helper.setText(htmlContent, true);
            mailSender.send(message);
            
            log.info("Survey email sent successfully to {}", toEmail);
        } catch (MessagingException e) {
            log.error("Failed to send survey email to {}", toEmail, e);
        }
    }
}
