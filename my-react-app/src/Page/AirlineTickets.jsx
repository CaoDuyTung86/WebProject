import React, { useState } from "react";
import { useLanguage } from "../context/LanguageContext";
import Header from "../LayOut/Header";
import Sidebar from "../components/Sidebar"; 

const AirlineTickets = () => {
  const { t } = useLanguage();
  const [isSidebarOpen, setIsSidebarOpen] = useState(true); 
  const [from, setFrom] = useState("HAN");
  const [to, setTo] = useState("SGN");
  const [date, setDate] = useState("");
  const [passengers, setPassengers] = useState(1);
  const [trips, setTrips] = useState([]);
  const [selectedTrip, setSelectedTrip] = useState(null);
  const [seats, setSeats] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  const API_BASE = "http://localhost:8080/api";

  const handleSearch = async (e) => {
    e.preventDefault();
    if (!from || !to || !date) {
      setError("Vui lòng nhập đầy đủ điểm đi, điểm đến và ngày đi");
      return;
    }
    setError("");
    setLoading(true);
    setSelectedTrip(null);
    setSeats([]);

    try {
      const params = new URLSearchParams({
        from,
        to,
        date,
        type: "PLANE",
        passengers: String(passengers || 1),
      });

      const res = await fetch(`${API_BASE}/trips/search?${params.toString()}`);
      if (!res.ok) {
        const text = await res.text();
        throw new Error(text || `Lỗi HTTP ${res.status}`);
      }
      const data = await res.json();
      setTrips(data);
    } catch (err) {
      console.error(err);
      setError("Không tìm được chuyến bay. Vui lòng thử lại hoặc kiểm tra backend.");
    } finally {
      setLoading(false);
    }
  };

  const handleSelectTrip = async (trip) => {
    setSelectedTrip(trip);
    setSeats([]);
    setError("");
    setLoading(true);

    try {
      const res = await fetch(`${API_BASE}/trips/${trip.id}/seats`);
      if (!res.ok) {
        const text = await res.text();
        throw new Error(text || `Lỗi HTTP ${res.status}`);
      }
      const data = await res.json();
      setSeats(data);
    } catch (err) {
      console.error(err);
      setError("Không tải được danh sách ghế. Vui lòng thử lại.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <div style={{ minHeight: "100vh", backgroundColor: "#f8f9fa" }}>
     
      <Header setIsSidebarOpen={setIsSidebarOpen} />
      
      <div style={{ display: "flex" }}>
        
        <Sidebar isOpen={isSidebarOpen} />
        
        
        <div style={{ 
          flex: 1,
          padding: "100px 24px 24px 24px",
          marginLeft: isSidebarOpen ? "220px" : "0",
          transition: "margin-left 0.3s",
          backgroundColor: "#f8f9fa"
        }}>
          <div style={{ maxWidth: "1200px", margin: "0 auto" }}>
            <h1
              style={{
                fontSize: "32px",
                fontWeight: "700",
                color: "#333",
                marginBottom: "30px",
              }}
            >
              {t.flight}
            </h1>

            <div
              style={{
                background: "#fff",
                borderRadius: "12px",
                padding: "24px",
                boxShadow: "0 4px 15px rgba(0,0,0,0.05)",
                marginBottom: "24px",
              }}
            >
              <form
                onSubmit={handleSearch}
                style={{
                  display: "grid",
                  gridTemplateColumns: "repeat(4, minmax(0, 1fr))",
                  gap: "16px",
                  alignItems: "end",
                }}
              >
                <div>
                  <label style={{ display: "block", marginBottom: 8, fontWeight: 500 }}>
                    {t.from} (VD: HAN)
                  </label>
                  <input
                    type="text"
                    value={from}
                    onChange={(e) => setFrom(e.target.value.toUpperCase())}
                    style={{
                      width: "100%",
                      padding: "8px 12px",
                      borderRadius: 8,
                      border: "1px solid #ddd",
                    }}
                  />
                </div>

                <div>
                  <label style={{ display: "block", marginBottom: 8, fontWeight: 500 }}>
                    {t.to} (VD: SGN)
                  </label>
                  <input
                    type="text"
                    value={to}
                    onChange={(e) => setTo(e.target.value.toUpperCase())}
                    style={{
                      width: "100%",
                      padding: "8px 12px",
                      borderRadius: 8,
                      border: "1px solid #ddd",
                    }}
                  />
                </div>

                <div>
                  <label style={{ display: "block", marginBottom: 8, fontWeight: 500 }}>
                    {t.departureDate}
                  </label>
                  <input
                    type="date"
                    value={date}
                    onChange={(e) => setDate(e.target.value)}
                    style={{
                      width: "100%",
                      padding: "8px 12px",
                      borderRadius: 8,
                      border: "1px solid #ddd",
                    }}
                  />
                </div>

                <div>
                  <label style={{ display: "block", marginBottom: 8, fontWeight: 500 }}>
                    {t.passengers}
                  </label>
                  <input
                    type="number"
                    min={1}
                    value={passengers}
                    onChange={(e) => setPassengers(Number(e.target.value) || 1)}
                    style={{
                      width: "100%",
                      padding: "8px 12px",
                      borderRadius: 8,
                      border: "1px solid #ddd",
                      marginBottom: 8,
                    }}
                  />
                  <button
                    type="submit"
                    style={{
                      width: "100%",
                      padding: "10px 12px",
                      borderRadius: 8,
                      border: "none",
                      backgroundColor: "#ff6b00",
                      color: "#fff",
                      fontWeight: 600,
                      cursor: "pointer",
                    }}
                    disabled={loading}
                  >
                    {loading ? "Đang tìm kiếm..." : t.search}
                  </button>
                </div>
              </form>

              {error && (
                <p style={{ marginTop: 16, color: "red" }}>
                  {error}
                </p>
              )}
            </div>

            {trips.length > 0 && (
              <div
                style={{
                  background: "#fff",
                  borderRadius: 12,
                  padding: 24,
                  boxShadow: "0 4px 15px rgba(0,0,0,0.05)",
                  marginBottom: 24,
                }}
              >
                <h2
                  style={{
                    fontSize: 20,
                    fontWeight: 600,
                    marginBottom: 16,
                  }}
                >
                  Danh sách chuyến bay
                </h2>
                <div style={{ display: "flex", flexDirection: "column", gap: 12 }}>
                  {trips.map((trip) => (
                    <button
                      key={trip.id}
                      onClick={() => handleSelectTrip(trip)}
                      style={{
                        textAlign: "left",
                        padding: 16,
                        borderRadius: 10,
                        border: "1px solid #eee",
                        backgroundColor:
                          selectedTrip && selectedTrip.id === trip.id ? "#fff7ec" : "#fff",
                        cursor: "pointer",
                      }}
                    >
                      <div
                        style={{
                          display: "flex",
                          justifyContent: "space-between",
                          marginBottom: 8,
                        }}
                      >
                        <div>
                          <div style={{ fontWeight: 600 }}>
                            {trip.origin} → {trip.destination}
                          </div>
                          <div style={{ fontSize: 13, color: "#666" }}>
                            Khởi hành: {trip.departureTime}
                          </div>
                        </div>
                        <div style={{ textAlign: "right" }}>
                          <div style={{ fontWeight: 700, color: "#ff6b00" }}>
                            {trip.price?.toLocaleString("vi-VN")} đ
                          </div>
                          <div style={{ fontSize: 13, color: "#666" }}>
                            Còn {trip.availableSeats}/{trip.totalSeats} chỗ
                          </div>
                        </div>
                      </div>
                      <div style={{ fontSize: 13, color: "#666" }}>
                        {trip.providerName} · {trip.vehicleType}
                      </div>
                    </button>
                  ))}
                </div>
              </div>
            )}

            {selectedTrip && (
              <div
                style={{
                  background: "#fff",
                  borderRadius: 12,
                  padding: 24,
                  boxShadow: "0 4px 15px rgba(0,0,0,0.05)",
                }}
              >
                <h2
                  style={{
                    fontSize: 20,
                    fontWeight: 600,
                    marginBottom: 16,
                  }}
                >
                  Danh sách ghế (chỉ hiển thị, chưa đặt vé)
                </h2>
                {loading && seats.length === 0 && <p>Đang tải ghế...</p>}
                {!loading && seats.length === 0 && (
                  <p>Chưa có dữ liệu ghế cho chuyến này.</p>
                )}
                {seats.length > 0 && (
                  <div
                    style={{
                      display: "grid",
                      gridTemplateColumns: "repeat(auto-fill, minmax(60px, 1fr))",
                      gap: 8,
                    }}
                  >
                    {seats.map((seat) => (
                      <div
                        key={seat.id}
                        style={{
                          padding: "8px 4px",
                          borderRadius: 8,
                          textAlign: "center",
                          fontSize: 12,
                          border: "1px solid #ddd",
                          backgroundColor: seat.booked ? "#eee" : "#e6fff2",
                          color: seat.booked ? "#999" : "#0a7b38",
                        }}
                      >
                        {seat.seatNumber}
                      </div>
                    ))}
                  </div>
                )}
              </div>
            )}
          </div>
        </div>
      </div>
    </div>
  );
};

export default AirlineTickets;