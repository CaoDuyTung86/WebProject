import re

files = [
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx",
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\TrainTickets.jsx",
    "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\BusTickets.jsx"
]

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
                         "https://images.unsplash.com/photo-1621996346565-e3dbc646d9a9?q=80&w=400&auto=format&fit=crop", 
                         "https://images.unsplash.com/photo-1603133872878-684f208fb84b?q=80&w=400&auto=format&fit=crop", 
                         "https://images.unsplash.com/photo-1585032226651-759b368d7246?q=80&w=400&auto=format&fit=crop", 
                         "https://images.unsplash.com/photo-1555126634-323283e090fa?q=80&w=400&auto=format&fit=crop"  
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
                             <div style={{ fontWeight: 700, fontSize: 13, color: "#333", lineHeight: 1.4, minHeight: 40 }}>{s.serviceName}</div>
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

for path in files:
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    # Simple block replacement for meals
    # Find start and end exactly based on distinct strings:
    start_tag = '<div style={{ border: "1px solid #fef3c7"'
    # find the start of meals block
    idx_start = text.find(start_tag)
    if idx_start != -1:
        # We need to find the end of this div block. It ends right before the insurance block.
        # Insurance block starts with: `{[{cat: categories.insurance`
        idx_end = text.find('{[{cat: categories.insurance', idx_start)
        
        if idx_end != -1:
            # But the new insurance block in `update_ui_v2` became `{[{cat: categories.insurance, icon`
            # and may be mapped. Wait, the meal block is enclosed in its own div.
            # To be safe, just replace the entire slice between idx_start and idx_end-1.
            text = text[:idx_start] + detailed_meal + '\n\n' + ' ' * 22 + text[idx_end:]


    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
