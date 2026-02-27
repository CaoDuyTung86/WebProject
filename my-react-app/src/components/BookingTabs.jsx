// src/components/BookingTabs.jsx
import { useState } from "react";
import { PiAirplaneTilt } from "react-icons/pi";
import { MdOutlineTrain, MdOutlinePercent } from "react-icons/md";
import { IoIosBus } from "react-icons/io";
import { useLanguage } from "../context/LanguageContext";
import FlightSearch from "./FlightSearch";
import TrainSearch from "./TrainSearch";
import BusSearch from "./BusSearch";

const BookingTabs = () => {
  const [active, setActive] = useState(0);
  const { t } = useLanguage();

  const tabs = [
    { icon: <PiAirplaneTilt />, label: t.flight },
    { icon: <MdOutlineTrain />, label: t.train },
    { icon: <IoIosBus />, label: t.bus },
    { icon: <MdOutlinePercent />, label: t.package },
  ];

  return (
    <div
      style={{
        background: "#ffffff",
        borderRadius: "20px",
        padding: "30px",
        boxShadow: "0 10px 30px rgba(0,0,0,0.08)",
        color: "black"
      }}
    >
      {/* Tabs */}
      <div
        style={{
          display: "flex",
          background: "#e9ecef",
          borderRadius: "999px",
          padding: "6px",
          marginBottom: "30px",
        }}
      >
        {tabs.map((tab, index) => (
          <div
            key={index}
            onClick={() => setActive(index)}
            style={{
              flex: 1,
              textAlign: "center",
              padding: "10px",
              borderRadius: "999px",
              cursor: "pointer",
              background: active === index ? "#4f7cff" : "transparent",
              color: active === index ? "#fff" : "#333",
              transition: "0.3s",
              display: "flex",
              flexDirection: "column",
              alignItems: "center",
              gap: "4px",
            }}
          >
            <span style={{ fontSize: "24px" }}>{tab.icon}</span>
            <span style={{ fontSize: "14px", fontWeight: "500" }}>{tab.label}</span>
          </div>
        ))}
      </div>

      {/* Content */}
      {active === 0 && <FlightSearch />}
      {active === 1 && <TrainSearch />}
      {active === 2 && <BusSearch />}
      {active === 3 && (
        <div
          style={{
            height: "200px",
            border: "2px dashed #dee2e6",
            borderRadius: "14px",
            display: "flex",
            alignItems: "center",
            justifyContent: "center",
            color: "#999",
            fontSize: "18px",
          }}
        >
          {t.bookingContent} <b style={{ marginLeft: 6, color: "#4f7cff" }}>{tabs[active].label}</b>
        </div>
      )}
    </div>
  );
};

export default BookingTabs;