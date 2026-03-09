package com.booking.api.util;

import javax.crypto.Mac;
import javax.crypto.spec.SecretKeySpec;
import java.net.URLEncoder;
import java.nio.charset.StandardCharsets;
import java.time.LocalDateTime;
import java.time.format.DateTimeFormatter;
import java.util.Map;
import java.util.SortedMap;
import java.util.TreeMap;

public class VNPayUtil {

    private VNPayUtil() {
    }

    /**
     * Tạo HMAC SHA512 hash
     */
    public static String hmacSHA512(String key, String data) {
        try {
            Mac hmac = Mac.getInstance("HmacSHA512");
            SecretKeySpec secretKeySpec = new SecretKeySpec(key.getBytes(StandardCharsets.UTF_8), "HmacSHA512");
            hmac.init(secretKeySpec);
            byte[] hash = hmac.doFinal(data.getBytes(StandardCharsets.UTF_8));

            StringBuilder sb = new StringBuilder();
            for (byte b : hash) {
                sb.append(String.format("%02x", b));
            }
            return sb.toString();
        } catch (Exception e) {
            throw new RuntimeException("Lỗi tạo HMAC SHA512", e);
        }
    }

    /**
     * Tạo query string từ map (đã sort theo key)
     */
    public static String buildQueryString(SortedMap<String, String> params) {
        StringBuilder queryString = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) {
            if (entry.getValue() != null && !entry.getValue().isEmpty()) {
                try {
                    String key = URLEncoder.encode(entry.getKey(), StandardCharsets.US_ASCII.toString());
                    String value = URLEncoder.encode(entry.getValue(), StandardCharsets.US_ASCII.toString());
                    queryString.append(key).append("=").append(value).append("&");
                } catch (Exception e) {
                    // ignore
                }
            }
        }
        if (queryString.length() > 0) {
            queryString.setLength(queryString.length() - 1);
        }
        return queryString.toString();
    }

    /**
     * Tạo hash data string
     * Từ VNPay v2.1.0, hashData chính là chuỗi ký tự nối bằng & với format
     * key=value (được URLEncoder)
     */
    public static String buildHashData(SortedMap<String, String> params) {
        StringBuilder hashData = new StringBuilder();
        for (Map.Entry<String, String> entry : params.entrySet()) {
            if (entry.getValue() != null && !entry.getValue().isEmpty()) {
                hashData.append(entry.getKey()).append("=").append(entry.getValue()).append("&");
            }
        }
        if (hashData.length() > 0) {
            hashData.setLength(hashData.length() - 1);
        }
        return hashData.toString();
    }

    /**
     * Format ngày giờ theo định dạng VNPay yêu cầu: yyyyMMddHHmmss
     */
    public static String formatDateTime(LocalDateTime dateTime) {
        return dateTime.format(DateTimeFormatter.ofPattern("yyyyMMddHHmmss"));
    }

    /**
     * Validate secure hash từ VNPay callback
     */
    public static boolean validateHash(Map<String, String> params, String hashSecret) {
        String vnpSecureHash = params.get("vnp_SecureHash");
        if (vnpSecureHash == null)
            return false;

        SortedMap<String, String> sortedParams = new TreeMap<>(params);
        sortedParams.remove("vnp_SecureHash");
        sortedParams.remove("vnp_SecureHashType");

        String hashData = buildHashData(sortedParams);
        String calculatedHash = hmacSHA512(hashSecret, hashData);

        return calculatedHash.equalsIgnoreCase(vnpSecureHash);
    }
}
