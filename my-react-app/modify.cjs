const fs = require('fs');

const replaceInFile = (file, replacements) => {
  let content = fs.readFileSync(file, 'utf8');
  replacements.forEach(([search, replace]) => {
    content = content.split(search).join(replace);
  });
  fs.writeFileSync(file, content, 'utf8');
};

// MyBookings.jsx
replaceInFile('src/Page/MyBookings.jsx', [
  ['Lịch sử đặt vé của bạn', '{t.yourBookings}'],
  ['Bạn chưa có chuyến đi nào. Hãy đặt vé ngay nhé!', '{t.noBookings}'],
  ['const statusText = bk.status === "PAID" ? "Đã thanh toán" : bk.status === "CONFIRMED" ? "Đã xác nhận" : bk.status === "COMPLETED" ? "Đã hoàn thành" : bk.status === "CANCELLED" ? "Đã hủy" : "Chờ thanh toán (5 phút)";', 'const statusText = bk.status === "PAID" ? t.paid : bk.status === "CONFIRMED" ? t.confirmed : bk.status === "COMPLETED" ? t.completed : bk.status === "CANCELLED" ? t.cancelled : t.pendingPayment;'],
  ['>Mã vé: ', '>{t.ticketCode}: '],
  ['>• Đặt lúc: ', '>• {t.bookedAt}: '],
  ['>🎫 Danh sách hành khách<', '>&nbsp;🎫 {t.passengerList}<'],
  ['>Chưa có tên<', '>{t.noName}<'],
  ['Ghế: ', '{t.seat}: '],
  ['>• Đã hủy<', '>• {t.cancelled}<'],
  ['>Hủy vé<', '>{t.cancelTicket}<'],
  ['Được hoàn: ', '{t.refundedAmount}: '],
  ['>Hoàn thành<', '>{t.completeBookingBtn}<'],
  ['>Thanh toán ngay<', '>{t.payNowBtn}<'],
  ['>Yêu cầu hoàn tiền<', '>{t.requestRefundBtn}<'],
  ['>Gửi Đánh Giá ⭐️<', '>{t.submitReviewBtn}<'],
  ['>Xác nhận hủy vé<', '>{t.cancelTicketConfirmTitle}<'],
  ['Bạn có chắc muốn hủy vé này? Giá vé sẽ được trừ khỏi tổng đơn hàng.', '{t.cancelTicketConfirmDesc}'],
  ['⏳ Đang chờ duyệt hoàn tiền', '⏳ {t.pendingFilter}'],
  ['if(window.confirm("Bạn xác nhận chuyến đi này đã hoàn thành?"))', 'if(window.confirm(t.confirmComplete))']
]);

// ProviderRefunds.jsx
replaceInFile('src/Page/ProviderRefunds.jsx', [
  ['import Sidebar from "../components/Sidebar";', 'import Sidebar from "../components/Sidebar";\nimport { useLanguage } from "../context/LanguageContext";'],
  ['const navigate = useNavigate();', 'const navigate = useNavigate();\n  const { t } = useLanguage();'],
  ['PENDING: { bg: "#fef3c7", color: "#ca8a04", text: "Chờ duyệt" }', 'PENDING: { bg: "#fef3c7", color: "#ca8a04", text: t.pendingFilter }'],
  ['APPROVED: { bg: "#dcfce7", color: "#16a34a", text: "Đã duyệt" }', 'APPROVED: { bg: "#dcfce7", color: "#16a34a", text: t.approvedFilter }'],
  ['REJECTED: { bg: "#fee2e2", color: "#dc2626", text: "Từ chối" }', 'REJECTED: { bg: "#fee2e2", color: "#dc2626", text: t.rejectedFilter }'],
  ['COMPLETED: { bg: "#dcfce7", color: "#16a34a", text: "Đã hoàn" }', 'COMPLETED: { bg: "#dcfce7", color: "#16a34a", text: t.completed }'],
  ['>Quản lý Yêu cầu Hoàn tiền<', '>{t.refundManagement}<'],
  ['{ key: "ALL", label: "Tất cả"', '{ key: "ALL", label: t.allFilter'],
  ['{ key: "PENDING", label: "Chờ duyệt"', '{ key: "PENDING", label: t.pendingFilter'],
  ['{ key: "APPROVED", label: "Đã duyệt"', '{ key: "APPROVED", label: t.approvedFilter'],
  ['{ key: "REJECTED", label: "Từ chối"', '{ key: "REJECTED", label: t.rejectedFilter'],
  ['>Không có yêu cầu hoàn tiền nào.<', '>{t.noRefunds}<'],
  ['Yêu cầu #{r.id}', 'Req #{r.id}'],
  ['<b>Lý do:</b>', '<b>{t.refundReason}:</b>'],
  ['<b>Ghi chú Provider:</b>', '<b>{t.providerNoteText}:</b>'],
  ['Gửi lúc: ', '{t.sentAt}: '],
  ['Xử lý lúc: ', '{t.processedAt}: '],
  ['>✓ Duyệt<', '>{t.approveRefund}<'],
  ['>✕ Từ chối<', '>{t.rejectRefund}<'],
  ['>Từ chối yêu cầu hoàn tiền<', '>{t.rejectTitle}<'],
  ['Lý do từ chối (tùy chọn)', '{t.rejectReasonLabel}'],
  ['>Xác nhận Từ chối<', '>{t.rejectConfirmBtn}<'],
  ['>Hủy<', '>{t.cancelBtn}<'],
  ['>Đang xử lý...<', '>{t.processing}<']
]);

// AdminReviews.jsx
replaceInFile('src/Page/AdminReviews.jsx', [
  ['"Danh sách Đánh giá (Nhà cung cấp)" : "Quản lý Đánh giá"', 't.providerReviews : t.adminReviews'],
  ['placeholder="Tìm kiếm theo hành trình, hãng, hoặc nội dung..."', 'placeholder={t.searchPlaceholder}'],
  ['>Người dùng<', '>{t.userCol}<'],
  ['>Nhà cung cấp<', '>{t.providerCol}<'],
  ['>Hành trình<', '>{t.journeyCol}<'],
  ['>Số sao<', '>{t.rating}<'],
  ['>Bình luận<', '>{t.commentText}<'],
  ['>Không tìm thấy đánh giá.<', '>{t.noReviews}<']
]);

// AdminRevenue.jsx
replaceInFile('src/Page/AdminRevenue.jsx', [
  ['import { PieChart', 'import { useLanguage } from "../context/LanguageContext";\nimport { PieChart'],
  ['const { token, user, isAuthenticated } = useAuth();', 'const { token, user, isAuthenticated } = useAuth();\n  const { t } = useLanguage();'],
  ['>Thống kê doanh thu<', '>{t.revenueTitle}<'],
  ['>TỔNG DOANH THU HỆ THỐNG<', '>{t.totalRevenue.toUpperCase()}<'],
  ['>Doanh thu theo dịch vụ<', '>{t.revenueByService}<'],
  ['>Chi tiết doanh thu Nhà cung cấp<', '>{t.revenueByService}<'],
  ['"Máy bay"', 't.flight'],
  ['"Xe khách"', 't.bus'],
  ['"Tàu hỏa"', 't.train'],
  ['>Tên nhà cung cấp<', '>{t.providerCol}<'],
  ['>Tổng doanh thu<', '>{t.totalRevenue}<']
]);

// OrderByPackage.jsx
replaceInFile('src/Page/OrderByPackage.jsx', [
  ['>Tour Yêu thích<', '>{t.favoriteTours}<']
]);

console.log("Replaced successfully!");