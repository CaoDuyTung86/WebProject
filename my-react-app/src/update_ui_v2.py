import re
import os

files = [
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx",
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\TrainTickets.jsx",
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\BusTickets.jsx"
]

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Update SLEEPER color to BLUE (#bfdbfe for bg, #60a5fa for border)
    # The current regex for bg might be (["BUSINESS", "VIP"].includes(...) ? "#bfdbfe" : ... === "SLEEPER" ? "#fef08a" : ...)
    text = text.replace('["BUSINESS", "VIP"].includes(s.seatType) ? "#bfdbfe"', '["BUSINESS", "VIP", "SLEEPER"].includes(s.seatType) ? "#bfdbfe"')
    text = text.replace('(["BUSINESS", "VIP"].includes(s.seatType) ? "6px solid #60a5fa"', '(["BUSINESS", "VIP", "SLEEPER"].includes(s.seatType) ? "6px solid #60a5fa"')
    text = text.replace('s.seatType === "SLEEPER" ? "#fef08a"', 'false ? "#fef08a"')
    text = text.replace('s.seatType === "SLEEPER" ? "6px solid #eab308"', 'false ? "6px solid #eab308"')

    # For standard inline seat mapping inside map() check if the string matches cleanly
    text = text.replace('s.seatType === "BUSINESS" || s.seatType === "VIP" ? "#bfdbfe" : isSleeper ? "#fef08a"', 's.seatType === "BUSINESS" || s.seatType === "VIP" || isSleeper ? "#bfdbfe" : false ? "#fef08a"')

    # 2. Detail the promo code entry
    promo_block = r'''<div style=\{\{ border: "1px dashed #d1d5db", borderRadius: 12, padding: 16, marginBottom: 14 \}\}>
\s*<div style=\{\{ fontWeight: 700, marginBottom: 10 \}\}>🎫 \{t\.promoCodeLabel\}</div>
\s*<div style=\{\{ display: "flex", gap: 8 \}\}>
\s*<input value=\{promoCode\} onChange=\{e => setPromoCode\(e\.target\.value\.toUpperCase\(\)\)\} placeholder="..."
\s*style=\{\{ flex: 1, padding: "10px 12px", borderRadius: 8, border: "1px solid #ddd", fontSize: 14 \}\} />
\s*<button type="button" style=\{\{ padding: "10px 16px", borderRadius: 8, border: "1px solid #4f7cff", background: "#eff6ff", color: "#4f7cff", fontWeight: 700, cursor: "pointer" \}\}>\{t\.applyPromo\}</button>
\s*</div>
\s*<div style=\{\{ fontSize: 12, color: "#888", marginTop: 6 \}\}>\{t\.promoInstruction\}</div>
\s*</div>'''

    detailed_promo = r'''<div style={{ position: "relative", border: "2px dashed #ff4500", borderRadius: 12, padding: "20px", marginBottom: 14, background: "linear-gradient(to right, #fff5f0, #fff)" }}>
                      <div style={{ position: "absolute", left: -8, top: "50%", transform: "translateY(-50%)", width: 16, height: 16, borderRadius: "50%", background: "#fff", borderRight: "2px dashed #ff4500" }}></div>
                      <div style={{ position: "absolute", right: -8, top: "50%", transform: "translateY(-50%)", width: 16, height: 16, borderRadius: "50%", background: "#fff", borderLeft: "2px dashed #ff4500" }}></div>
                      <div style={{ fontWeight: 800, color: "#ff4500", fontSize: 16, marginBottom: 12, display: "flex", alignItems: "center", gap: 8 }}>
                          <span style={{ fontSize: 22 }}>🎟️</span> {t.promoCodeLabel}
                      </div>
                      <div style={{ display: "flex", gap: 10 }}>
                        <input value={promoCode} onChange={e => setPromoCode(e.target.value.toUpperCase())} placeholder="Nhập mã ưu đãi..."
                          style={{ flex: 1, padding: "12px 16px", borderRadius: 8, border: "1px solid #fca5a5", fontSize: 15, fontWeight: "bold", color: "#b91c1c", textTransform: "uppercase" }} />
                        <button type="button" disabled={!promoCode} style={{ padding: "12px 24px", borderRadius: 8, border: "none", background: promoCode ? "#ff4500" : "#fca5a5", color: "#fff", fontWeight: 800, cursor: promoCode ? "pointer" : "not-allowed", transition: "all 0.2s" }}>
                          {t.applyPromo}
                        </button>
                      </div>
                      <div style={{ display: "flex", alignItems: "center", gap: 6, fontSize: 12, color: "#991b1b", marginTop: 10 }}>
                        <span style={{ fontStyle: "italic" }}>💡 Mẹo: Nhận mã tại trang Ưu Đãi để được giảm tới 50%</span>
                      </div>
                    </div>'''

    text = re.sub(promo_block, detailed_promo, text)

    # 3. Meals Component Customization
    old_meal = r'''<div style=\{\{ border: "1px solid #fef3c7", borderRadius: 12, padding: 16, background: "#f9fafb" \}\}>
\s*<div style=\{\{ display: "flex", alignItems: "center", gap: 10, marginBottom: 12 \}\}>
\s*<span style=\{\{ fontSize: 24 \}\}>🍱</span>
\s*<div><div style=\{\{ fontWeight: 700, fontSize: 15 \}\}>\{t\.meal\}</div><div style=\{\{ fontSize: 12, color: "#888" \}\}>Chọn món ăn trên chuyến đi</div></div>
\s*</div>
\s*<div style=\{\{ display: "flex", flexWrap: "wrap", gap: 10 \}\}>
\s*<label.*?Không chọn suất ăn
\s*</label>
\s*\{categories\.meal\.map.*?\}</label>
\s*\)\)\}
\s*</div>
\s*</div>'''

    detailed_meal = r'''<div style={{ border: "1px solid #fef3c7", borderRadius: 12, padding: "20px", background: "#f9fafb" }}>
                  <div style={{ display: "flex", alignItems: "center", justifyContent: "space-between", marginBottom: 16 }}>
                    <div style={{ display: "flex", alignItems: "center", gap: 10 }}>
                      <span style={{ fontSize: 28 }}>🍱</span>
                      <div>
                        <div style={{ fontWeight: 800, fontSize: 16, color: "#b45309" }}>{t.meal}</div>
                        <div style={{ fontSize: 13, color: "#888" }}>Suất ăn nóng hổi, chuẩn vị nhà hàng</div>
                      </div>
                    </div>
                  </div>
                  
                  <div style={{ marginBottom: 16 }}>
                    <label style={{ display: "inline-flex", alignItems: "center", gap: 8, padding: "10px 20px", borderRadius: 30,
                      border: `2px solid ${!selectedServiceIds.some(id => categories.meal.map(s=>s.id).includes(id)) ? "#f59e0b" : "#ddd"}`,
                      background: !selectedServiceIds.some(id => categories.meal.map(s=>s.id).includes(id)) ? "#fffbeb" : "#fff",
                      cursor: "pointer", fontWeight: 700, color: !selectedServiceIds.some(id => categories.meal.map(s=>s.id).includes(id)) ? "#d97706" : "#555" }}>
                      <input type="radio" name="meal" style={{ display: "none" }}
                        checked={!selectedServiceIds.some(id => categories.meal.map(s=>s.id).includes(id))}
                        onChange={() => setSingleServiceInCategory(null, categories.meal)} />
                      ✖ Không chọn suất ăn
                    </label>
                  </div>

                  <div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 16 }}>
                    {categories.meal.map((s, index) => {
                       const images = [
                         "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?q=80&w=400&auto=format&fit=crop", // Pasta
                         "https://images.unsplash.com/photo-1603133872878-684f208fb84b?q=80&w=400&auto=format&fit=crop", // Fried rice
                         "https://images.unsplash.com/photo-1585032226651-759b368d7246?q=80&w=400&auto=format&fit=crop", // Noodles
                         "https://images.unsplash.com/photo-1555126634-323283e090fa?q=80&w=400&auto=format&fit=crop"  // Bun xao
                       ];
                       const img = images[index % images.length];
                       const isSelected = selectedServiceIds.includes(s.id);
                       return (
                         <div key={s.id} onClick={() => setSingleServiceInCategory(s.id, categories.meal)} 
                           style={{ borderRadius: 12, overflow: "hidden", border: `2px solid ${isSelected ? "#f59e0b" : "#eee"}`, 
                           background: isSelected ? "#fffbeb" : "#fff", cursor: "pointer", position: "relative", transition: "all 0.2s",
                           boxShadow: isSelected ? "0 4px 12px rgba(245, 158, 11, 0.2)" : "0 2px 8px rgba(0,0,0,0.05)" }}>
                           <div style={{ height: 120, backgroundImage: `url(${img})`, backgroundSize: "cover", backgroundPosition: "center" }} />
                           <div style={{ padding: 12 }}>
                             <div style={{ fontWeight: 700, fontSize: 13, color: "#333", lineHeight: 1.4, minHeight: 36 }}>{s.serviceName}</div>
                             <div style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginTop: 8 }}>
                               <span style={{ color: "#d97706", fontWeight: 800, fontSize: 14 }}>{Number(s.price||0).toLocaleString("vi-VN")} VND</span>
                               <div style={{ width: 24, height: 24, borderRadius: "50%", background: isSelected ? "#f59e0b" : "#f3f4f6", 
                                 display: "flex", alignItems: "center", justifyContent: "center", color: isSelected ? "#fff" : "#9ca3af", fontWeight: "bold" }}>
                                 {isSelected ? "✓" : "+"}
                               </div>
                             </div>
                           </div>
                         </div>
                       );
                    })}
                  </div>
                </div>'''

    text = re.sub(old_meal, detailed_meal, text, flags=re.DOTALL)

    # 4. Insurance Details Component
    old_ins = r'''\{cat: categories\.insurance, icon: "🛡️", title: "Bảo hiểm du lịch", sub: "Bảo vệ chuyến đi của bạn", color: "#f0fdf4", border: "#bbf7d0"\}'''
    new_ins = r'''{cat: categories.insurance, icon: "🛡️", title: "Bảo hiểm du lịch", sub: "Chi trả y tế tới 2 tỷ VNĐ, Trễ chuyến/Hủy chuyến, Mất hành lý", color: "#f0fdf4", border: "#22c55e", highlighted: true}'''
    text = text.replace(old_ins, new_ins)

    # Fix the rendering logic of insurance to show highlights if highlighted=true
    # Search for: <div style={{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 }}>
    # And replace the mapping rendering
    
    ins_map_old = r'''<div key=\{title\} style=\{\{ border: `1px solid \$\{border\}`, borderRadius: 12, padding: 16, background: "#f9fafb" \}\}>
\s*<div style=\{\{ display: "flex", alignItems: "center", gap: 10, marginBottom: 10 \}\}>
\s*<span style=\{\{ fontSize: 24 \}\}>\{icon\}</span>
\s*<div><div style=\{\{ fontWeight: 700, fontSize: 15 \}\}>\{title\}</div><div style=\{\{ fontSize: 12, color: "#888" \}\}>\{sub\}</div></div>
\s*</div>
\s*\{cat\.map\(s => \(
\s*<label.*?\{Number\(s\.price\|\|0\) === 0 \? "Miễn phí" : `\$\{Number\(s\.price\|\|0\)\.toLocaleString\("vi-VN"\)\} đ`\}
\s*</span>
\s*</label>
\s*\)\)\}
\s*</div>'''

    ins_map_new = r'''<div key={title} style={{ border: highlighted ? `2px solid ${border}` : `1px solid ${border}`, borderRadius: 12, padding: 16, background: highlighted ? "#f0fdf4" : "#f9fafb", position: "relative", overflow: "hidden" }}>
                            {highlighted && <div style={{ position: "absolute", top: 12, right: -25, background: "#ef4444", color: "#fff", fontSize: 10, fontWeight: 800, padding: "4px 24px", transform: "rotate(45deg)", boxShadow: "0 2px 4px rgba(0,0,0,0.2)" }}>NÊN MUA</div>}
                            <div style={{ display: "flex", alignItems: "flex-start", gap: 12, marginBottom: 14 }}>
                              <span style={{ fontSize: 32, background: "#fff", borderRadius: "50%", padding: 4, boxShadow: "0 2px 6px rgba(0,0,0,0.05)" }}>{icon}</span>
                              <div><div style={{ fontWeight: 800, fontSize: 16, color: highlighted ? "#15803d" : "#333", marginBottom: 4 }}>{title}</div><div style={{ fontSize: 13, color: highlighted ? "#166534" : "#666", lineHeight: 1.5 }}>{sub}</div></div>
                            </div>
                            <div style={{ display: "flex", flexDirection: "column", gap: 8 }}>
                            {cat.map(s => (
                              <label key={s.id} onClick={() => toggleService(s.id)} style={{ display: "flex", alignItems: "center", justifyContent: "space-between",
                                padding: "14px 16px", borderRadius: 10, background: selectedServiceIds.includes(s.id) ? color : "#fff",
                                border: `2px solid ${selectedServiceIds.includes(s.id) ? border : "#e5e7eb"}`,
                                cursor: "pointer", transition: "all 0.2s", boxShadow: selectedServiceIds.includes(s.id) ? "0 4px 10px rgba(34,197,94,0.15)" : "none" }}>
                                <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                                  <div style={{ width: 22, height: 22, borderRadius: "50%", border: `2px solid ${selectedServiceIds.includes(s.id) ? border : "#ccc"}`,
                                    background: selectedServiceIds.includes(s.id) ? border : "#fff",
                                    display: "flex", alignItems: "center", justifyContent: "center", color: "#fff", fontSize: 12 }}>
                                    {selectedServiceIds.includes(s.id) ? "✓" : ""}
                                  </div>
                                  <div>
                                    <div style={{ fontWeight: 700, color: "#333", fontSize: 14 }}>{s.serviceName}</div>
                                  </div>
                                </div>
                                <span style={{ fontWeight: 800, fontSize: 15, color: selectedServiceIds.includes(s.id) ? border : "#666" }}>
                                  {Number(s.price||0) === 0 ? "Miễn phí" : `${Number(s.price||0).toLocaleString("vi-VN")} đ`}
                                </span>
                              </label>
                            ))}
                            </div>
                          </div>'''

    text = re.sub(ins_map_old, ins_map_new, text, flags=re.DOTALL)
    
    # We also need to add `highlighted` to the map destructing: map(({cat, icon, title, sub, color, border, highlighted})
    text = text.replace('map(({cat, icon, title, sub, color, border})', 'map(({cat, icon, title, sub, color, border, highlighted})')

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

