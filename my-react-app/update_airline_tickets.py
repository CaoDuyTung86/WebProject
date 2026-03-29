import re

def update_file(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Imports
    if "PassengerInfoForm" not in content:
        content = content.replace(
            'import { useLanguage } from "../context/LanguageContext";',
            'import { useLanguage } from "../context/LanguageContext";\nimport { useSavedPassengers } from "../context/SavedPassengersContext";\nimport PassengerInfoForm from "../components/PassengerInfoForm";'
        )

    # 2. Modify FlightBookingDetail props
    if "FlightBookingDetail = ({ flightData, onClose, onContinue })" in content:
        content = content.replace(
            "const FlightBookingDetail = ({ flightData, onClose, onContinue }) => {",
            "const FlightBookingDetail = ({ flightData, onClose, onContinue, passengerCounts }) => {"
        )
        
    state_anchor = "const [selectedPayment, setSelectedPayment] = useState(\"momo\");"
    state_to_add = '''const [passengerInfoList, setPassengerInfoList] = React.useState([]);
  const [globalContact, setGlobalContact] = React.useState({ promoOptIn: true, remember: false });
  const { savedPassengers, addPassenger } = useSavedPassengers();

  React.useEffect(() => {
    if(!passengerCounts) return;
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
    if "passengerInfoList" not in content:
        content = content.replace(state_anchor, state_anchor + "\n  " + state_to_add)

    insert_anchor = '''        <div style={{
          display: "flex",
          justifyContent: "flex-end",
          marginTop: "20px",
          paddingTop: "20px",
          borderTop: "2px solid #f0f0f0",
        }}>'''
    
    insert_forms = '''
        {passengerCounts && (
          <div style={{ marginTop: "24px", marginBottom: "24px", borderTop: "1px solid #eee", paddingTop: "24px" }}>
            <h3 style={{ fontSize: "18px", fontWeight: "700", marginBottom: "16px" }}>Thông tin hành khách</h3>
            <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
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
            <div style={{ display: "flex", gap: 16, marginTop: 16 }}>
              <label style={{ fontSize: 13, display: "flex", gap: 8, alignItems: "center", cursor: "pointer" }}>
                <input type="checkbox" checked={globalContact.remember} onChange={e => setGlobalContact(p => ({...p, remember: e.target.checked}))} />
                Ghi nhớ thông tin hành khách cho lần sau
              </label>
            </div>
          </div>
        )}
'''
    if "Thông tin hành khách" not in content:
        content = content.replace(insert_anchor, insert_forms + "\n" + insert_anchor)

    # Also wrap onContinue to save to savedPassengers
    # We find: onClick={onContinue}
    old_onClick = 'onClick={onContinue}'
    new_onClick = '''onClick={() => {
              if (globalContact.remember) {
                passengerInfoList.forEach(pi => {
                  if (pi.type === 'ADULT' && pi.data.fullName) {
                      addPassenger({ ...pi.data, passengerType: 'ADULT' }).catch(() => {});
                  }
                });
              }
              onContinue();
            }}'''
    if "passengerInfoList.forEach" not in content:
        # Since onContinue is an exact match for the button around line 546
        # Let's target the exact string and only replace the first occurrence or just replace it
        content = content.replace(old_onClick, new_onClick, 1)

    rendered_modal = "<FlightBookingDetail"
    if "passengerCounts=" not in content:
        content = re.sub(
            r'(<FlightBookingDetail\s+flightData=\{selectedFlight\}\s+onClose=\{\(\) => setShowBookingDetail\(false\)\}\s+onContinue=\{handleContinueBooking\})',
            r'\1 passengerCounts={passengerInfo.passengers}',
            content
        )

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

update_file(r'd:\clone repo\WebProject\my-react-app\src\Page\AirlineTicketsDetail.jsx')
