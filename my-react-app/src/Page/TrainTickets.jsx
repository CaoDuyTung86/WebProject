import React, { useState } from "react";
import { useLanguage } from "../context/LanguageContext";
import Header from "../LayOut/Header";
import Sidebar from "../components/Sidebar";

const TrainTickets = () => {
  const { t } = useLanguage();
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

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
            <h1 style={{ 
              fontSize: "32px", 
              fontWeight: "700", 
              color: "#333",
              marginBottom: "30px"
            }}>
              {t.train}
            </h1>
            <div style={{
              background: "#fff",
              borderRadius: "12px",
              padding: "40px",
              textAlign: "center",
              boxShadow: "0 4px 15px rgba(0,0,0,0.05)"
            }}>
              <p style={{ fontSize: "18px", color: "#666" }}>
                {t.train === "Vé tàu hỏa" ? "Nội dung trang vé tàu hỏa" :
                 t.train === "Train Tickets" ? "Train tickets content" :
                 t.train === "鉄道チケット" ? "鉄道チケットの内容" : "火車票內容"}
              </p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default TrainTickets;