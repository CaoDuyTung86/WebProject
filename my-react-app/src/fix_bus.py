import re

with open("d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\BusTickets.jsx", "r", encoding="utf-8") as f:
    content = f.read()

# Capture the exact seatClass section to replace
pattern = r'(\{selectedTrip && step === "seatClass" && \(\n\s*<div style=\{\{ display: "grid", gridTemplateColumns: "1fr 320px", gap: 20 \}\}>\n\s*<div.*?)(?=\{selectedTrip && step === "extras" && \()'

replacement = """{selectedTrip && step === "seatClass" && (
              <div style={{ display: "grid", gridTemplateColumns: "1fr 320px", gap: 20 }}>
                <div style={{ background: "#fff", borderRadius: 12, padding: 24, boxShadow: "0 4px 15px rgba(0,0,0,0.05)" }}>
                  <h2 style={{ fontSize: 18, fontWeight: 700, marginBottom: 4 }}>Bước 1: Chọn hạng vé & ghế ngồi</h2>
                  <p style={{ color: "#666", fontSize: 13, marginBottom: 16 }}>Chọn hạng sau đó bấm vào ghế muốn ngồi.</p>

                  {loading && <p style={{ color: "#888" }}>{t.loadingSeatmap}</p>}

                  {!loading && (() => {
                    const classTypes = [...new Set(seats.map(s => s.seatType || "ECONOMY"))];
                    return (
                      <div style={{ display: "flex", gap: 10, marginBottom: 16, flexWrap: "wrap" }}>
                        <button type="button" onClick={() => setSelectedSeatClass("")} style={{
                          padding: "8px 18px", borderRadius: 20, border: `2px solid ${!selectedSeatClass ? "#4f7cff" : "#ddd"}`,
                          background: !selectedSeatClass ? "#4f7cff" : "#fff", color: !selectedSeatClass ? "#fff" : "#333",
                          fontWeight: 600, cursor: "pointer",
                        }}>Tất cả</button>
                        {classTypes.map(cls => (
                          <button key={cls} type="button" onClick={() => setSelectedSeatClass(cls)} style={{
                            padding: "8px 18px", borderRadius: 20,
                            border: `2px solid ${selectedSeatClass === cls ? "#4f7cff" : "#ddd"}`,
                            background: selectedSeatClass === cls ? "#4f7cff" : "#fff",
                            color: selectedSeatClass === cls ? "#fff" : "#333",
                            fontWeight: 600, cursor: "pointer",
                          }}>{cls === "SLEEPER" || cls === "BUSINESS" ? `🌟 Giường nằm` : `💺 Ghế thường`}</button>
                        ))}
                      </div>
                    );
                  })()}

                  {!loading && seats.length > 0 && (() => {
                    const filteredSeats = selectedSeatClass
                      ? seats.filter(s => (s.seatType || "ECONOMY") === selectedSeatClass)
                      : seats;

                    const parse = (sn) => { const m = String(sn || "").match(/^(\d+)([A-Za-z])$/); return m ? { row: +m[1], col: m[2].toUpperCase() } : null; };
                    const items = filteredSeats.map(s => { const p = parse(s.seatNumber); return p ? { ...s, ...p } : null; }).filter(Boolean);
                    const cols = [...new Set(items.map(i => i.col))].sort();
                    const rows = [...new Set(items.map(i => i.row))].sort((a, b) => a - b);
                    const smap = new Map(items.map(i => [`${i.row}${i.col}`, i]));

                    const half = Math.ceil(cols.length / 2);
                    const leftCols = cols.slice(0, half);
                    const rightCols = cols.slice(half);

                    return (
                      <div style={{ 
                        overflowX: "auto", 
                        background: "#fafafa", 
                        padding: "30px", 
                        borderRadius: "24px", 
                        border: "3px solid #ccc",
                        position: "relative",
                        minWidth: "fit-content",
                        margin: "0 auto"
                      }}>
                        <div style={{ textAlign: "center", marginBottom: 20, color: "#aaa", fontSize: 24 }}>Đầu xe</div>
                        <div style={{ display: "flex", gap: 16, marginBottom: 8, paddingLeft: 48, justifyContent: "center" }}>
                          {leftCols.map(c => <div key={c} style={{ width: 44, textAlign: "center", fontWeight: 700, color: "#888", fontSize: 12 }}>{c}</div>)}
                          <div style={{ width: 40 }} /> 
                          {rightCols.map(c => <div key={c} style={{ width: 44, textAlign: "center", fontWeight: 700, color: "#888", fontSize: 12 }}>{c}</div>)}
                        </div>
                        {rows.map(row => (
                          <div key={row} style={{ display: "flex", gap: 16, marginBottom: 12, alignItems: "center", justifyContent: "center" }}>
                            <div style={{ width: 32, textAlign: "center", fontWeight: 700, color: "#aaa", fontSize: 12 }}>{row}</div>
                            {leftCols.map(col => {
                              const s = smap.get(`${row}${col}`);
                              if (!s) return <div key={col} style={{ width: 44, height: 60 }} />;
                              const sel = selectedSeatIds.includes(s.id);
                              const isSleeper = s.seatType === "SLEEPER" || s.seatType === "BUSINESS";
                              return (
                                <button key={s.id} type="button" onClick={() => toggleSeat(s)} disabled={s.booked}
                                  title={`${s.seatNumber} ${s.seatType || "ECONOMY"} ${s.booked ? "(Đã đặt)" : ""}`}
                                  style={{
                                    width: 44, height: isSleeper ? 64 : 44, borderRadius: isSleeper ? "8px" : "12px", border: "none", cursor: s.booked ? "not-allowed" : "pointer",
                                    background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (isSleeper ? "#fef08a" : "#dcfce7"),
                                    color: s.booked ? "#aaa" : sel ? "#fff" : "#444", fontWeight: 700, fontSize: 12,
                                    boxShadow: sel ? "0 4px 10px rgba(245, 158, 11, 0.4)" : "0 2px 4px rgba(0,0,0,0.1)",
                                    transition: "all 0.2s"
                                  }}>
                                  {isSleeper && !s.booked && !sel && <div style={{fontSize: 10, marginBottom: 2}}>🛏️</div>}
                                  <div>{s.booked ? "✗" : s.seatNumber}</div>
                                </button>
                              );
                            })}
                            <div style={{ width: 40, textAlign: "center", color: "#ddd", fontSize: 12 }}>||</div>
                            {rightCols.map(col => {
                              const s = smap.get(`${row}${col}`);
                              if (!s) return <div key={col} style={{ width: 44, height: 60 }} />;
                              const sel = selectedSeatIds.includes(s.id);
                              const isSleeper = s.seatType === "SLEEPER" || s.seatType === "BUSINESS";
                              return (
                                <button key={s.id} type="button" onClick={() => toggleSeat(s)} disabled={s.booked}
                                  title={`${s.seatNumber} ${s.seatType || "ECONOMY"} ${s.booked ? "(Đã đặt)" : ""}`}
                                  style={{
                                    width: 44, height: isSleeper ? 64 : 44, borderRadius: isSleeper ? "8px" : "12px", border: "none", cursor: s.booked ? "not-allowed" : "pointer",
                                    background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (isSleeper ? "#fef08a" : "#dcfce7"),
                                    color: s.booked ? "#aaa" : sel ? "#fff" : "#444", fontWeight: 700, fontSize: 12,
                                    boxShadow: sel ? "0 4px 10px rgba(245, 158, 11, 0.4)" : "0 2px 4px rgba(0,0,0,0.1)",
                                    transition: "all 0.2s"
                                  }}>
                                  {isSleeper && !s.booked && !sel && <div style={{fontSize: 10, marginBottom: 2}}>🛏️</div>}
                                  <div>{s.booked ? "✗" : s.seatNumber}</div>
                                </button>
                              );
                            })}
                          </div>
                        ))}
                        <div style={{ display: "flex", gap: 16, marginTop: 24, fontSize: 12, color: "#666", justifyContent: "center", flexWrap: "wrap" }}>
                          <span style={{display: "flex", alignItems: "center", gap: 4}}><span style={{ display: "inline-block", width: 14, height: 14, background: "#dcfce7", borderRadius: 3 }} />Ghế thường</span>
                          <span style={{display: "flex", alignItems: "center", gap: 4}}><span style={{ display: "inline-block", width: 14, height: 14, background: "#fef08a", borderRadius: 3 }} />Giường nằm</span>
                          <span style={{display: "flex", alignItems: "center", gap: 4}}><span style={{ display: "inline-block", width: 14, height: 14, background: "#f59e0b", borderRadius: 3 }} />Đang chọn</span>
                          <span style={{display: "flex", alignItems: "center", gap: 4}}><span style={{ display: "inline-block", width: 14, height: 14, background: "#e0e0e0", borderRadius: 3 }} />Bị đặt</span>
                        </div>
                      </div>
                    );
                  })()}

                  {!loading && seats.length === 0 && <p style={{ color: "#888" }}>{t.noSeatData}</p>}

                  {error && <p style={{ color: "red", marginTop: 12 }}>{error}</p>}
                  <div style={{ display: "flex", justifyContent: "space-between", marginTop: 20 }}>
                    <button type="button" onClick={() => setStep("chooseTrip")} style={{ padding: "10px 24px", borderRadius: 8, border: "1px solid #ddd", background: "#fff", fontWeight: 700, cursor: "pointer" }}>← Quay lại</button>
                    <button type="button" onClick={goToExtras} style={{ padding: "10px 28px", borderRadius: 8, border: "none", background: "#4f7cff", color: "#fff", fontWeight: 700, cursor: "pointer" }}>Tiếp theo →</button>
                  </div>
                </div>

                <div style={{ background: "#fff", borderRadius: 12, padding: 20, boxShadow: "0 4px 15px rgba(0,0,0,0.05)", height: "fit-content" }}>
                  <div style={{ fontWeight: 700, fontSize: 15, marginBottom: 12, borderBottom: "1px solid #eee", paddingBottom: 10 }}>Thông tin đặt chỗ</div>
                  <div style={{ fontSize: 13, color: "#444", lineHeight: 1.9 }}>
                    <div><b>{selectedTrip.origin}</b> → <b>{selectedTrip.destination}</b></div>
                    <div style={{ color: "#888", marginBottom: 6 }}>{selectedTrip.departureTime}</div>
                    <div style={{ background: "#f8f9fa", padding: 10, borderRadius: 8 }}>
                      <div style={{ marginBottom: 4 }}>Ghế: <b style={{color: "#4f7cff"}}>{selectedSeatIds.length === 0 ? "Chưa chọn" : seats.filter(s => selectedSeatIds.includes(s.id)).map(s => s.seatNumber).join(", ")}</b></div>
                      <div style={{ fontWeight: 700, color: "#ff6b00", fontSize: 15 }}>{Number(selectedTrip.price || 0).toLocaleString("vi-VN")} đ / ghế</div>
                    </div>
                  </div>
                </div>
              </div>
            )}

            {selectedTrip && step === "passenger" && (
              <div style={{ display: "grid", gridTemplateColumns: "1fr 320px", gap: 20 }}>
                <div style={{ background: "#fff", borderRadius: 12, padding: 24, boxShadow: "0 4px 15px rgba(0,0,0,0.05)" }}>
                  <h2 style={{ fontSize: 18, fontWeight: 700, marginBottom: 4 }}>Bước 2: Thông tin hành khách</h2>
                  <p style={{ color: "#666", fontSize: 13, marginBottom: 20 }}>Nhập thông tin cá nhân của hành khách. Các ô có dấu * là bắt buộc.</p>

                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>
                    {[{ label: "Họ *", key: "lastName" }, { label: "Tên & tên đệm *", key: "firstName" }].map(f => (
                      <div key={f.key}>
                        <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>{f.label}</label>
                        <input
                          value={passengerInfo[f.key]}
                          onChange={e => setPassengerInfo(p => ({ ...p, [f.key]: toLatinUpper(e.target.value) }))}
                          style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14, letterSpacing: 1 }} />
                      </div>
                    ))}
                    <div>
                      <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Ngày sinh *</label>
                      <input
                        value={passengerInfo.dob}
                        onChange={e => setPassengerInfo(p => ({ ...p, dob: formatDob(e.target.value) }))}
                        placeholder="__/__/____"
                        inputMode="numeric"
                        maxLength={10}
                        style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14, letterSpacing: 2 }}
                      />
                    </div>
                    <div>
                      <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Quốc tịch</label>
                      <select value={passengerInfo.nationality} onChange={e => setPassengerInfo(p => ({ ...p, nationality: e.target.value }))}
                        style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14 }}>
                        {["Việt Nam", "Nhật Bản", "Hàn Quốc", "Anh", "Mỹ", "Úc", "Khác"].map(c => <option key={c}>{c}</option>)}
                      </select>
                    </div>
                    <div>
                      <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Số điện thoại *</label>
                      <div style={{ display: "flex", gap: 8 }}>
                        <input readOnly value="+84" style={{ width: 64, padding: "10px 8px", borderRadius: 8, border: "1px solid #ddd", background: "#f5f5f5", textAlign: "center" }} />
                        <input value={passengerInfo.phoneDigits} onChange={e => setPassengerInfo(p => ({ ...p, phoneDigits: e.target.value.replace(/\D/g, "") }))} placeholder="912345678"
                          style={{ flex: 1, padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14 }} />
                      </div>
                    </div>
                    <div style={{ gridColumn: "1 / -1" }}>
                      <label style={{ display: "block", fontSize: 13, fontWeight: 600, marginBottom: 6 }}>Email *</label>
                      <input value={passengerInfo.email} onChange={e => setPassengerInfo(p => ({ ...p, email: e.target.value }))} type="email"
                        style={{ width: "100%", padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14 }} />
                    </div>
                  </div>

                  <div style={{ display: "flex", gap: 16, marginTop: 14 }}>
                    <label style={{ fontSize: 13, display: "flex", gap: 8, alignItems: "center", cursor: "pointer" }}>
                      <input type="checkbox" checked={passengerInfo.promoOptIn} onChange={e => setPassengerInfo(p => ({ ...p, promoOptIn: e.target.checked }))} />
                      Nhận thông tin khuyến mãi
                    </label>
                    <label style={{ fontSize: 13, display: "flex", gap: 8, alignItems: "center", cursor: "pointer" }}>
                      <input type="checkbox" checked={passengerInfo.remember} onChange={e => setPassengerInfo(p => ({ ...p, remember: e.target.checked }))} />
                      Lưu thông tin cho lần sau
                    </label>
                  </div>

                  {error && <p style={{ color: "red", marginTop: 12 }}>{error}</p>}
                  <div style={{ display: "flex", justifyContent: "space-between", marginTop: 20 }}>
                    <button type="button" onClick={() => setStep("seatClass")} style={{ padding: "10px 24px", borderRadius: 8, border: "1px solid #ddd", background: "#fff", fontWeight: 700, cursor: "pointer" }}>← Quay lại</button>
                    <button type="button" onClick={goToExtrasFromPassenger} style={{ padding: "10px 28px", borderRadius: 8, border: "none", background: "#4f7cff", color: "#fff", fontWeight: 700, cursor: "pointer" }}>Tiếp theo →</button>
                  </div>
                </div>

                <div style={{ background: "#fff", borderRadius: 12, padding: 20, boxShadow: "0 4px 15px rgba(0,0,0,0.05)", height: "fit-content" }}>
                  <div style={{ fontWeight: 700, fontSize: 15, marginBottom: 12, borderBottom: "1px solid #eee", paddingBottom: 10 }}>Thông tin đặt chỗ</div>
                  <div style={{ fontSize: 13, color: "#444", lineHeight: 1.9 }}>
                    <div><b>{selectedTrip.origin}</b> → <b>{selectedTrip.destination}</b></div>
                    <div style={{ color: "#888", marginBottom: 6 }}>{selectedTrip.departureTime}</div>
                    <div style={{ background: "#f8f9fa", padding: 10, borderRadius: 8 }}>
                      <div style={{ marginBottom: 4 }}>Ghế: <b style={{color: "#4f7cff"}}>{selectedSeatIds.length === 0 ? "Chưa chọn" : seats.filter(s => selectedSeatIds.includes(s.id)).map(s => s.seatNumber).join(", ")}</b></div>
                      <div style={{ fontWeight: 700, color: "#ff6b00", fontSize: 15 }}>{Number(selectedTrip.price || 0).toLocaleString("vi-VN")} đ / ghế</div>
                    </div>
                  </div>
                </div>
              </div>
            )}
"""

m = re.search(pattern, content, flags=re.DOTALL)
if m:
    with open("d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\BusTickets.jsx", "w", encoding="utf-8") as f:
        new_content = content[:m.start()] + replacement + content[m.end():]
        f.write(new_content)
    print("SUCCESS")
else:
    print("PATTERN NOT FOUND")

