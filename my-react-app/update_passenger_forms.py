import os

def check_and_replace(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 1. Imports
    if "PassengerInfoForm" not in content:
        content = content.replace(
            'import { useLanguage } from "../context/LanguageContext";',
            'import { useLanguage } from "../context/LanguageContext";\nimport { useSavedPassengers } from "../context/SavedPassengersContext";\nimport PassengerInfoForm from "../components/PassengerInfoForm";'
        )
        content = content.replace(
            'import { IoMdSearch } from "react-icons/io";',
            'import { IoMdSearch } from "react-icons/io";\nimport { FiChevronDown } from "react-icons/fi";'
        )

    # 2. Passengers State
    s1 = 'const [passengers, setPassengers] = useState(1);'
    r1 = '''const [passengerCounts, setPassengerCounts] = useState({ adult: 1, child: 0, infant: 0 });
  const [showPassengersDropdown, setShowPassengersDropdown] = useState(false);
  const passengers = passengerCounts.adult + passengerCounts.child;'''
    if "passengerCounts" not in content:
        content = content.replace(s1, r1)

    # 3. Passenger Info State
    s2_start = 'const [passengerInfo, setPassengerInfo] = useState({'
    s2_end = '});'
    # Find the block
    idx_start = content.find(s2_start)
    if idx_start != -1 and "passengerInfoList" not in content:
        idx_end = content.find(s2_end, idx_start) + len(s2_end)
        old_state = content[idx_start:idx_end]
        r2 = '''const [passengerInfoList, setPassengerInfoList] = useState([]);
  const [globalContact, setGlobalContact] = useState({ promoOptIn: true, remember: false });
  const { savedPassengers, addPassenger } = useSavedPassengers();

  useEffect(() => {
    const newList = [];
    for (let i = 0; i < passengerCounts.adult; i++) newList.push({ type: "ADULT", data: {} });
    for (let i = 0; i < passengerCounts.child; i++) newList.push({ type: "CHILD", data: {} });
    for (let i = 0; i < passengerCounts.infant; i++) newList.push({ type: "INFANT", data: {} });
    setPassengerInfoList(prev => newList.map((item, idx) => prev[idx] ? { ...item, data: prev[idx].data } : item));
  }, [passengerCounts]);

  const handlePassengerChange = (index, type, data) => {
    setPassengerInfoList(prev => {
      const copy = [...prev];
      copy[index] = { ...copy[index], data };
      return copy;
    });
  };'''
        content = content.replace(old_state, r2)

    # 4. Input replacement in Search
    s_inp = '''<input type="number" min={1} max={9} value={passengers}
                    onChange={(e) => setPassengers(Math.max(1, Number(e.target.value) || 1))}
                    style={{
                      width: "100%", padding: "10px 14px", borderRadius: 10, border: "2px solid #e0e7ff",
                      background: "#f8f9ff", fontSize: 15, marginBottom: 10, boxSizing: "border-box"
                    }}
                  />'''
    # We'll just find the general block by splitting and searching
    inp_start = '<input type="number" min={1} max={9} value={passengers}'
    idx_inp = content.find(inp_start)
    if idx_inp != -1:
        idx_inp_end = content.find('/>', idx_inp) + 2
        old_inp = content[idx_inp:idx_inp_end]
        r_inp = '''<div style={{ position: "relative", marginBottom: 10 }}>
                    <div
                      onClick={() => setShowPassengersDropdown(!showPassengersDropdown)}
                      style={{ width: "100%", padding: "10px 14px", borderRadius: 10, border: "2px solid #e0e7ff",
                        background: "#fff", fontSize: 15, cursor: "pointer", display: "flex", justifyContent: "space-between", alignItems: "center", boxSizing: "border-box" }}
                    >
                      <span>{passengerCounts.adult} {t.adult || 'Người lớn'}, {passengerCounts.child} {t.child || 'Trẻ em'}, {passengerCounts.infant} {t.infant || 'Em bé'}</span>
                      <FiChevronDown />
                    </div>
                    {showPassengersDropdown && (
                      <div style={{ position: "absolute", top: "100%", left: 0, right: 0, background: "#fff", borderRadius: 12, boxShadow: "0 8px 30px rgba(0,0,0,0.15)", zIndex: 100, padding: 16, marginTop: 4 }}>
                         {['adult', 'child', 'infant'].map(type => (
                           <div key={type} style={{ display: "flex", justifyContent: "space-between", alignItems: "center", marginBottom: 12 }}>
                             <div>
                               <div style={{ fontWeight: 600 }}>{type === 'adult' ? t.adult || 'Người lớn' : type === 'child' ? t.child || 'Trẻ em' : t.infant || 'Em bé'}</div>
                               <div style={{ fontSize: 12, color: "#666" }}>{type === 'adult' ? '>12 tuổi' : type === 'child' ? '2-11 tuổi' : '<2 tuổi'}</div>
                             </div>
                             <div style={{ display: "flex", alignItems: "center", gap: 12 }}>
                               <button type="button" disabled={passengerCounts[type] <= (type === 'adult' ? 1 : 0)} onClick={() => setPassengerCounts(p => ({...p, [type]: p[type] - 1}))} style={{ width: 28, height: 28, borderRadius: "50%", border: "1px solid #ddd", background: "#fff", cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center" }}>-</button>
                               <span style={{ fontWeight: 600, width: 16, textAlign: "center" }}>{passengerCounts[type]}</span>
                               <button type="button" onClick={() => setPassengerCounts(p => ({...p, [type]: p[type] + 1}))} style={{ width: 28, height: 28, borderRadius: "50%", border: "1px solid #ddd", background: "#fff", cursor: "pointer", display: "flex", alignItems: "center", justifyContent: "center" }}>+</button>
                             </div>
                           </div>
                         ))}
                      </div>
                    )}
                  </div>'''
        content = content.replace(old_inp, r_inp)

    # Validation Replace
    val_start = 'const validatePassenger = () => {'
    val_idx = content.find(val_start)
    if val_idx != -1 and "for (const [idx, pi] of passengerInfoList.entries()) {" not in content:
        val_end_str = 'return null;\n  };'
        val_idx_end = content.find(val_end_str, val_idx) + len(val_end_str)
        old_val = content[val_idx:val_idx_end]
        r_val = '''const validatePassenger = () => {
    for (const [idx, pi] of passengerInfoList.entries()) {
        const d = pi.data || {};
        const isAdult = pi.type === 'ADULT';
        if (!d.fullName || d.fullName.trim() === '') return `Vui lòng nhập họ tên cho ${isAdult ? 'người lớn' : pi.type === 'CHILD' ? 'trẻ em' : 'em bé'} ${idx + 1}.`;
        if (!d.dateOfBirth || !/^\d{2}\/\d{2}\/\d{4}$/.test(d.dateOfBirth)) return `Ngày sinh hành khách ${idx + 1} không hợp lệ. Vui lòng nhập định dạng DD/MM/YYYY.`;
        if (!d.gender) return `Vui lòng chọn giới tính cho hành khách ${idx + 1}.`;
        
        if (isAdult) {
            if (!d.email || !/^\S+@\S+\.\S+$/.test(d.email)) return `Email của người lớn không hợp lệ.`;
            if (!d.phone || !/^\d{9,10}$/.test(d.phone.replace(/\D/g, ''))) return `SĐT người lớn không hợp lệ.`;
            if (!d.idNumber) return `Vui lòng nhập CCCD/Hộ chiếu cho người lớn.`;
        }
    }
    return null;
  };'''
        content = content.replace(old_val, r_val)

    # Render Forms
    s_form_start = '<div style={{ display: "grid", gridTemplateColumns: "1fr 1fr", gap: 14 }}>'
    s_form_end = '</div>\n\n                  <div style={{ display: "flex", gap: 16, marginTop: 14 }}>'
    idx_form = content.find(s_form_start)
    if idx_form != -1 and "PassengerInfoForm" not in content[idx_form:idx_form+500]:
        idx_form_end = content.find(s_form_end, idx_form) + len(s_form_end)
        old_form = content[idx_form:idx_form_end]
        r_form = '''<div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
                    {passengerInfoList.map((pi, idx) => (
                      <PassengerInfoForm
                         key={idx}
                         type={pi.type}
                         index={idx}
                         data={pi.data}
                         onChange={handlePassengerChange}
                         savedPassengers={savedPassengers}
                         onSelectSaved={(i, t, p) => handlePassengerChange(i, t, {
                            ...p, 
                            fullName: p.fullName || "", 
                            phone: p.phone || "",
                            email: p.email || "",
                            idNumber: p.idNumber || "",
                            dateOfBirth: p.dateOfBirth || "",
                            gender: p.gender || "",
                            nationality: p.nationality || "Việt Nam"
                         })}
                      />
                    ))}
                  </div>

                  <div style={{ display: "flex", gap: 16, marginTop: 14 }}>'''
        content = content.replace(old_form, r_form)

    # Checkboxes
    content = content.replace('checked={passengerInfo.promoOptIn} onChange={e => setPassengerInfo(p => ({...p, promoOptIn: e.target.checked}))}', 'checked={globalContact.promoOptIn} onChange={e => setGlobalContact(p => ({...p, promoOptIn: e.target.checked}))}')
    content = content.replace('checked={passengerInfo.remember} onChange={e => setPassengerInfo(p => ({...p, remember: e.target.checked}))}', 'checked={globalContact.remember} onChange={e => setGlobalContact(p => ({...p, remember: e.target.checked}))}')

    # Summary
    sum_start = '<div style={{ border: "1px solid #e0e7ff", borderRadius: 12, padding: 16, marginBottom: 14, background: "#f9fafb" }}>\n                    <div style={{ fontWeight: 700, marginBottom: 8, color: "#4f7cff" }}>👤 Hành khách</div>'
    sum_end = '</div>'
    
    idx_sum = content.find(sum_start)
    if idx_sum != -1 and "passengerInfoList.map" not in content[idx_sum:idx_sum+400]:
        idx_sum_end = content.find(sum_end, idx_sum + len(sum_start)) + len(sum_end)
        old_sum = content[idx_sum:idx_sum_end]
        r_sum = '''<div style={{ border: "1px solid #e0e7ff", borderRadius: 12, padding: 16, marginBottom: 14, background: "#f9fafb" }}>
                    <div style={{ fontWeight: 700, marginBottom: 8, color: "#4f7cff" }}>👤 Hành khách</div>
                    {passengerInfoList.map((pi, idx) => (
                      <div key={idx} style={{ fontSize: 13, marginBottom: 8, paddingBottom: 8, borderBottom: idx < passengerInfoList.length - 1 ? "1px dashed #ccc" : "none" }}>
                        <b>{pi.data.fullName || `Hành khách ${idx+1}`}</b> ({pi.type === 'ADULT' ? 'Người lớn' : pi.type === 'CHILD' ? 'Trẻ em' : 'Em bé'})
                        {pi.type === 'ADULT' && <div style={{ color: "#888", marginTop: 2 }}>{pi.data.email} · {pi.data.phone ? `+84 ${pi.data.phone}` : ''}</div>}
                        <div style={{ marginTop: 2 }}>Ngày sinh: {pi.data.dateOfBirth} | Giới tính: {pi.data.gender === 'Male' ? 'Nam' : pi.data.gender === 'Female' ? 'Nữ' : 'Khác'}</div>
                      </div>
                    ))}
                  </div>'''
        content = content.replace(old_sum, r_sum)
        
    # useEffect passengerInfo.remember -> save trigger
    eff_start = 'useEffect(() => {\n    if (passengerInfo.remember)'
    eff_idx = content.find(eff_start)
    if eff_idx != -1:
        eff_end = '}, [passengerInfo]);'
        eff_end_idx = content.find(eff_end, eff_idx) + len(eff_end)
        old_eff = content[eff_idx:eff_end_idx]
        r_eff = ''
        content = content.replace(old_eff, r_eff)

    eff2_start = 'useEffect(() => {\n    try {\n      const saved ='
    eff2_idx = content.find(eff2_start)
    if eff2_idx != -1:
        eff2_end = '}, []);'
        eff2_end_idx = content.find(eff2_end, eff2_idx) + len(eff2_end)
        old_eff2 = content[eff2_idx:eff2_end_idx]
        r_eff2 = ''
        content = content.replace(old_eff2, r_eff2)

    # booking result trigger
    bk_start = 'setBookingResult(data);'
    if "globalContact.remember" not in content[content.find(bk_start):content.find(bk_start)+200]:
        content = content.replace(bk_start, '''setBookingResult(data);
      if (globalContact.remember) {
        passengerInfoList.forEach(pi => {
           if (pi.type === 'ADULT' && pi.data.fullName) {
               addPassenger({ ...pi.data, passengerType: 'ADULT' }).catch(() => {});
           }
        });
      }''')

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

check_and_replace(r'd:\clone repo\WebProject\my-react-app\src\Page\TrainTickets.jsx')
check_and_replace(r'd:\clone repo\WebProject\my-react-app\src\Page\BusTickets.jsx')
