import re

with open("d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx", "r", encoding="utf-8") as f:
    content = f.read()

pattern = r'(return \(\s*<div style=\{\{ overflowX: "auto" \}\}>)(.*?)(<div style=\{\{ display: "flex", gap: 16, marginTop: 12, fontSize: 12, color: "#666" \}\}>)'

replacement = """\\1
                      <div style={{
                        background: "#f0f2f5",
                        padding: "40px 20px 20px",
                        borderRadius: "120px 120px 40px 40px",
                        border: "4px solid #cbd5e1",
                        position: "relative",
                        minWidth: "fit-content",
                        margin: "0 auto 20px",
                        boxShadow: "inset 0 0 20px rgba(0,0,0,0.05)"
                      }}>
                        {/* Buồng lái máy bay */}
                        <div style={{ textAlign: "center", marginBottom: 30, color: "#94a3b8", fontSize: "20px", fontWeight: "bold" }}>✈ Mũi Máy Bay</div>
                        
                        <div style={{ display: "flex", gap: 6, marginBottom: 12, paddingLeft: 48, justifyContent: "center" }}>
                          {leftCols.map(c => <div key={c} style={{ width: 44, textAlign: "center", fontWeight: 700, color: "#888", fontSize: 12 }}>{c}</div>)}
                          <div style={{ width: 40 }} /> {/* Lối đi giữa */}
                          {rightCols.map(c => <div key={c} style={{ width: 44, textAlign: "center", fontWeight: 700, color: "#888", fontSize: 12 }}>{c}</div>)}
                        </div>
                        {rows.map(row => (
                          <div key={row} style={{ display: "flex", gap: 6, marginBottom: 8, alignItems: "center", justifyContent: "center" }}>
                            <div style={{ width: 36, textAlign: "center", fontWeight: 700, color: "#aaa", fontSize: 12 }}>{row}</div>
                            {leftCols.map(col => {
                              const s = smap.get(`${row}${col}`);
                              if (!s) return <div key={col} style={{ width: 44, height: 44 }} />;
                              const sel = selectedSeatIds.includes(s.id);
                              const isBusiness = s.seatType === "BUSINESS";
                              return (
                                <button key={s.id} type="button" onClick={() => toggleSeat(s)} disabled={s.booked}
                                  title={`${s.seatNumber} ${s.seatType || "ECONOMY"} ${s.booked ? "(Đã đặt)" : ""}`}
                                  style={{
                                    width: 44, height: isBusiness ? 54 : 44, borderRadius: isBusiness ? "12px 12px 4px 4px" : "8px 8px 4px 4px", border: "none", cursor: s.booked ? "not-allowed" : "pointer",
                                    background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (isBusiness ? "#dbeafe" : "#dcfce7"),
                                    color: s.booked ? "#aaa" : sel ? "#fff" : "#333", fontWeight: 700, fontSize: 12,
                                    borderBottom: s.booked ? "4px solid #ccc" : sel ? "4px solid #d97706" : isBusiness ? "4px solid #93c5fd" : "4px solid #86efac",
                                    transition: "all 0.2s"
                                  }}>
                                  {s.booked ? "✗" : s.seatNumber}
                                </button>
                              );
                            })}
                            <div style={{ width: 40, textAlign: "center", color: "#ccc", fontSize: 10 }}></div>
                            {rightCols.map(col => {
                              const s = smap.get(`${row}${col}`);
                              if (!s) return <div key={col} style={{ width: 44, height: 44 }} />;
                              const sel = selectedSeatIds.includes(s.id);
                              const isBusiness = s.seatType === "BUSINESS";
                              return (
                                <button key={s.id} type="button" onClick={() => toggleSeat(s)} disabled={s.booked}
                                  title={`${s.seatNumber} ${s.seatType || "ECONOMY"} ${s.booked ? "(Đã đặt)" : ""}`}
                                  style={{
                                    width: 44, height: isBusiness ? 54 : 44, borderRadius: isBusiness ? "12px 12px 4px 4px" : "8px 8px 4px 4px", border: "none", cursor: s.booked ? "not-allowed" : "pointer",
                                    background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (isBusiness ? "#dbeafe" : "#dcfce7"),
                                    color: s.booked ? "#aaa" : sel ? "#fff" : "#333", fontWeight: 700, fontSize: 12,
                                    borderBottom: s.booked ? "4px solid #ccc" : sel ? "4px solid #d97706" : isBusiness ? "4px solid #93c5fd" : "4px solid #86efac",
                                    transition: "all 0.2s"
                                  }}>
                                  {s.booked ? "✗" : s.seatNumber}
                                </button>
                              );
                            })}
                          </div>
                        ))}
                      </div>
                      \\3"""

m = re.search(pattern, content, flags=re.DOTALL)
if m:
    with open("d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx", "w", encoding="utf-8") as f:
        new_content = content[:m.start()] + re.sub(pattern, replacement, content[m.start():m.end()], flags=re.DOTALL) + content[m.end():]
        f.write(new_content)
    print("SUCCESS AIRLINE")
else:
    print("PATTERN NOT FOUND AIRLINE")
