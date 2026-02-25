import { PiAirplaneTilt } from "react-icons/pi";
import { MdOutlineTrain } from "react-icons/md";
import { IoIosBus } from "react-icons/io";
import { MdOutlinePercent } from "react-icons/md";
import { useLanguage } from "../context/LanguageContext";

const Sidebar = ({ isOpen }) => {
  const { t } = useLanguage();

  return (
    <aside
      style={{
        width: isOpen ? "220px" : "0",
        overflow: "hidden",
        background: "#ffffff",
        padding: isOpen ? "20px" : "0",
        boxShadow: isOpen ? "2px 0 10px rgba(0,0,0,0.05)" : "none",
        height: "calc(100vh - 70px)",
        transition: "0.3s",
        color:"black"
      }}
    >
      <div style={{ opacity: isOpen ? 1 : 0, transition: "0.2s" }}>
        <div style={{ padding: "14px 20px" }}><PiAirplaneTilt />  {t.flight}</div>
        <div style={{ padding: "14px 20px" }}><MdOutlineTrain />  {t.train}</div>
        <div style={{ padding: "14px 20px" }}><IoIosBus />  {t.bus}</div>
        <div style={{ padding: "14px 20px" }}><MdOutlinePercent /> {t.package}</div>
      </div>
    </aside>
  );
};

export default Sidebar;