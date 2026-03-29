import re

def update_file(path, is_airline=False, is_train=False):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # 1. Add getSeatPrice at top of component if not present
    if "const getSeatPrice" not in text:
        comp_name = "AirlineTickets" if is_airline else "TrainTickets" if is_train else "BusTickets"
        decl = f"const {comp_name} = () => {{"
        text = text.replace(decl, f"""const getSeatPrice = (base, type) => {{
  let price = Number(base || 0);
  if (type === "VIP") price *= 2;
  else if (type === "BUSINESS") price += 100000;
  else if (type === "SLEEPER") price += 50000;
  return price;
}};

{decl}""")

    # 2. Replace the old price calculations across the board
    text = re.sub(
        r'Number\(\(selectedTrip\.price \|\| 0\) \* selectedSeatIds\.length\)',
        r'seats.filter(s => selectedSeatIds.includes(s.id)).reduce((sum, s) => sum + getSeatPrice(selectedTrip.price, s.seatType), 0)',
        text
    )

    # 3. For Bus: Fix the empty state display that says "Price / ghế"
    text = text.replace(
        r'{seats.filter(s => selectedSeatIds.includes(s.id)).reduce((sum, s) => sum + getSeatPrice(selectedTrip.price, s.seatType), 0).toLocaleString("vi-VN")} đ / ghế',
        r'{selectedSeatIds.length === 0 ? `${Number(selectedTrip.price || 0).toLocaleString("vi-VN")} đ / ghế` : `${seats.filter(s => selectedSeatIds.includes(s.id)).reduce((sum, s) => sum + getSeatPrice(selectedTrip.price, s.seatType), 0).toLocaleString("vi-VN")} đ`}'
    )
    
    # 4. For Bus & Train: Fix duplicate class labels
    if not is_airline:
        pattern = r"\{cls === \"SLEEPER\" \|\| cls === \"BUSINESS\" \? `🌟 Giường nằm` : `💺 Ghế thường`\}"
        text = text.replace(pattern, "{cls === \"SLEEPER\" || cls === \"BUSINESS\" ? `🌟 Giường nằm` : cls === \"ECONOMY\" ? `💺 Ghế thường` : `💺 ${cls}`}")

    with open(path, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"Updated {path}")

base = "d:\\clone repo\\WebProject\\my-react-app\\src\\Page"
update_file(f"{base}\\BusTickets.jsx")
update_file(f"{base}\\AirlineTickets.jsx", is_airline=True)
update_file(f"{base}\\TrainTickets.jsx", is_train=True)
