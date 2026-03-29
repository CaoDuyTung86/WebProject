import re

def fix_airline():
    path = "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Replace wrapper
    pattern = r'(return \(\s*)(<div style=\{\{ overflowX: "auto" \}\}>)(\s*<div style=\{\{ display: "flex", gap: 6, marginBottom: 8, paddingLeft: 48 \}\}>)'
    replacement = r'''\1<div style={{ 
                        overflowX: "auto", background: "#f0f2f5", padding: "50px 30px 30px", 
                        borderRadius: "150px 150px 30px 30px", border: "5px solid #cbd5e1",
                        boxShadow: "inset 0 10px 20px rgba(0,0,0,0.05)", position: "relative",
                        minWidth: "fit-content", margin: "0 auto"
                      }}>
                        <div style={{ textAlign: "center", marginBottom: 30, color: "#94a3b8", fontSize: "20px", fontWeight: "bold" }}>✈ Mũi Máy Bay</div>\3'''
    
    # Just replace the 1st occurrence in the seatClass section
    text = re.sub(pattern, replacement, text, count=1)
    
    # Change color
    text = replace_colors(text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def fix_train():
    path = "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\TrainTickets.jsx"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    pattern = r'(return \(\s*)(<div style=\{\{ overflowX: "auto" \}\}>)(\s*<div style=\{\{ display: "flex", gap: 6, marginBottom: 8, paddingLeft: 48 \}\}>)'
    replacement = r'''\1<div style={{ 
                        overflowX: "auto", background: "#f8f9fa", padding: "20px 30px", 
                        borderRadius: "12px", border: "4px solid #4f7cff", borderLeft: "20px solid #4f7cff",
                        boxShadow: "0 4px 15px rgba(0,0,0,0.1)", position: "relative",
                        minWidth: "fit-content", margin: "0 auto"
                      }}>
                        <div style={{ textAlign: "left", marginBottom: 20, color: "#4f7cff", fontSize: "18px", fontWeight: "bold" }}>🚂 Đầu Tàu & Toa Xe</div>\3'''
    
    text = re.sub(pattern, replacement, text, count=1)
    
    text = replace_colors(text)

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

def replace_colors(text):
    # This is to make seats look more like seats instead of solid blocks.
    # Replace standard styling
    old_btn = r'style=\{\{ width: 44, height: 38, borderRadius: 6, border: "none", cursor: s\.booked \? "not-allowed" : "pointer",\s*background: s\.booked \? "#e0e0e0" : sel \? "#f59e0b" : \(s\.seatType === "BUSINESS" \? "#dbeafe" : "#dcfce7"\),\s*color: s\.booked \? "#aaa" : sel \? "#fff" : "#333", fontWeight: 600, fontSize: 11 \}\}'
    new_btn = r'''style={{ 
        width: 44, height: s.seatType === "BUSINESS" ? 48 : 40, 
        borderRadius: "8px 8px 4px 4px", border: "1px solid rgba(0,0,0,0.1)", 
        cursor: s.booked ? "not-allowed" : "pointer",
        background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (s.seatType === "BUSINESS" ? "#bfdbfe" : "#bbf7d0"),
        color: s.booked ? "#aaa" : sel ? "#fff" : "#333", fontWeight: 700, fontSize: 12,
        borderBottom: s.booked ? "6px solid #ccc" : sel ? "6px solid #d97706" : (s.seatType === "BUSINESS" ? "6px solid #60a5fa" : "6px solid #4ade80"),
        transition: "all 0.2s"
    }}'''
    return re.sub(old_btn, new_btn, text)

fix_airline()
fix_train()
