import re

def rewrite_button(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # BusTickets
    if "BusTickets" in path:
        text = re.sub(
            r'background: s\.booked \? "#e0e0e0" : sel \? "#f59e0b" : \(isSleeper \? "#fef08a" : "#dcfce7"\),',
            r'background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (s.seatType === "BUSINESS" || s.seatType === "VIP" ? "#bfdbfe" : isSleeper ? "#fef08a" : "#bbf7d0"),',
            text
        )
    else:
        # Airline & Train
        text = re.sub(
            r'background: s\.booked \? "#e0e0e0" : sel \? "#f59e0b" : \([^()]*"BUSINESS"[^()]*\),',
            r'background: s.booked ? "#e0e0e0" : sel ? "#f59e0b" : (["BUSINESS", "VIP"].includes(s.seatType) ? "#bfdbfe" : s.seatType === "SLEEPER" ? "#fef08a" : "#bbf7d0"),',
            text
        )
        text = re.sub(
            r'borderBottom: s\.booked \? "6px solid #ccc" : sel \? "6px solid #d97706" : \([^()]*"BUSINESS"[^()]*\),',
            r'borderBottom: s.booked ? "6px solid #ccc" : sel ? "6px solid #d97706" : (["BUSINESS", "VIP"].includes(s.seatType) ? "6px solid #60a5fa" : s.seatType === "SLEEPER" ? "6px solid #eab308" : "6px solid #4ade80"),',
            text
        )

    if "TrainTickets" in path:
        text = text.replace('||', '  ').replace('✈', '||') # Clean up any existing ones

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)

import glob
for file in ["d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\AirlineTickets.jsx", 
             "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\TrainTickets.jsx", 
             "d:\\clone repo\\WebProject\\my-react-app\\src\\Page\\BusTickets.jsx"]:
    rewrite_button(file)
