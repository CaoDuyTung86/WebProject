import { useState } from "react";
import Header from "../LayOut/Header";
import Sidebar from "../components/Sidebar";
import BookingTabs from "../components/BookingTabs";

const Home = () => {
  const [isSidebarOpen, setIsSidebarOpen] = useState(true);

  return (
    <div style={{ minHeight: "100vh", background: "#f5f7fb" }}>
     
      <Header setIsSidebarOpen={setIsSidebarOpen} />

      
      <div style={{ display: "flex", marginTop: "70px", position: "relative" }}>
        
        <Sidebar isOpen={isSidebarOpen} />

        
        <main
          style={{
            flex: 1,
            padding: "40px",
            marginLeft: isSidebarOpen ? "220px" : "0", 
            transition: "margin-left 0.3s",
            width: "100%",
          }}
        >
          <BookingTabs />
        </main>
      </div>
    </div>
  );
};

export default Home;