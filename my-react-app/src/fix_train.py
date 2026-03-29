import re

path = "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\TrainTickets.jsx"

with open(path, "r", encoding="utf-8") as f:
    text = f.read()

# 1. Add getSeatPrice
if "const getSeatPrice" not in text:
    text = text.replace("const TrainTickets = () => {", """const getSeatPrice = (base, type) => {
  let price = Number(base || 0);
  if (type === "VIP") price *= 2;
  else if (type === "BUSINESS") price += 100000;
  else if (type === "SLEEPER") price += 50000;
  return price;
};

const TrainTickets = () => {""")

# 2. Update all prices
text = re.sub(
    r'Number\(\(selectedTrip\.price \|\| 0\) \* selectedSeatIds\.length\)',
    r'seats.filter(s => selectedSeatIds.includes(s.id)).reduce((sum, s) => sum + getSeatPrice(selectedTrip.price, s.seatType), 0)',
    text
)

# 3. Update the empty state cost display (price / ghế)
text = text.replace(
    r'{Number(selectedTrip.price || 0).toLocaleString("vi-VN")} đ / ghế',
    r'{selectedSeatIds.length === 0 ? `${Number(selectedTrip.price || 0).toLocaleString("vi-VN")} đ / ghế` : `${seats.filter(s => selectedSeatIds.includes(s.id)).reduce((sum, s) => sum + getSeatPrice(selectedTrip.price, s.seatType), 0).toLocaleString("vi-VN")} đ`}'
)

# 4. Filters logic
pattern = r"\{cls === \"SLEEPER\" \|\| cls === \"BUSINESS\" \? `🌟 Giường nằm` : `💺 Ghế thường`\}"
text = text.replace(pattern, "{cls === \"BUSINESS\" ? \"🔵 Thương gia\" : cls === \"VIP\" ? \"🟣 VIP\" : cls === \"SLEEPER\" ? \"🌟 Giường nằm\" : cls === \"ECONOMY\" ? \"🟢 Phổ thông\" : `💺 ${cls}`}")

# 5. UI shape for Train
pattern_ui = r'(return \(\s*)(<div style=\{\{ overflowX: "auto" \}\}>)(\s*<div style=\{\{ display: "flex", gap: 6, marginBottom: 8, paddingLeft: 48 \}\}>)'
replacement_ui = r'''\1<div style={{ 
                        overflowX: "auto", background: "#f8f9fa", padding: "20px 30px", 
                        borderRadius: "12px", border: "4px solid #4f7cff", borderLeft: "20px solid #4f7cff",
                        boxShadow: "0 4px 15px rgba(0,0,0,0.1)", position: "relative",
                        minWidth: "fit-content", margin: "0 auto"
                      }}>
                        <div style={{ textAlign: "left", marginBottom: 20, color: "#4f7cff", fontSize: "18px", fontWeight: "bold" }}>🚂 Đầu Tàu & Toa Xe</div>\3'''
text = re.sub(pattern_ui, replacement_ui, text, count=1)

# 6. Colors for standard seat logic inside mapping
# Before
# style={{ width: 44, height: 38, borderRadius: 6, border: "none", cursor: s.booked ? "not-allowed" : "pointer",
# background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (s.seatType === "BUSINESS" ? "#dbeafe" : "#dcfce7"),

old_btn = r'style=\{\{ width: 44, height: 38, borderRadius: 6, border: "none", cursor: s\.booked \? "not-allowed" : "pointer",\s*background: s\.booked \? "#e0e0e0" : sel \? "#f59e0b" : \(s\.seatType === "BUSINESS" \? "#dbeafe" : "#dcfce7"\),\s*color: s\.booked \? "#aaa" : sel \? "#fff" : "#333", fontWeight: 600, fontSize: 11 \}\}'
new_btn = r'''style={{ 
        width: 44, height: s.seatType === "BUSINESS" || s.seatType === "VIP" ? 48 : 40, 
        borderRadius: "8px 8px 4px 4px", border: "1px solid rgba(0,0,0,0.1)", 
        cursor: s.booked ? "not-allowed" : "pointer",
        background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (["BUSINESS", "VIP"].includes(s.seatType) ? "#bfdbfe" : s.seatType === "SLEEPER" ? "#fef08a" : "#bbf7d0"),
        color: s.booked ? "#aaa" : sel ? "#fff" : "#333", fontWeight: 700, fontSize: 12,
        borderBottom: s.booked ? "6px solid #ccc" : sel ? "6px solid #d97706" : (["BUSINESS", "VIP"].includes(s.seatType) ? "6px solid #60a5fa" : s.seatType === "SLEEPER" ? "6px solid #eab308" : "6px solid #4ade80"),
        transition: "all 0.2s"
    }}'''
text = re.sub(old_btn, new_btn, text)

# 7. Replace the airplane icon safely
# It's an airplane emoji in <div style={{ width: 32, textAlign: "center", color: "#ccc", fontSize: 10 }}>✈</div>
text = text.replace('✈', '&nbsp;&nbsp;&nbsp;')

with open(path, "w", encoding="utf-8") as f:
    f.write(text)
