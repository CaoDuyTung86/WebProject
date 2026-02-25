
import React, { useState, useEffect } from "react";
import { IoIosPhonePortrait } from "react-icons/io";
import { MdOutlinePhone } from "react-icons/md";
import { IoChevronDown } from "react-icons/io5";
import Auth from "../Page/Auth"; 
import { useLanguage } from "../context/LanguageContext";
import { AiOutlineGlobal } from "react-icons/ai";
import VNFlag from "../Picture/flags/vn.png";
import UKFlag from "../Picture/flags/uk.png";
import JPFlag from "../Picture/flags/jp.png";
import TWFlag from "../Picture/flags/tw.png";

const Header = ({ setIsSidebarOpen }) => {
  const [isAuthOpen, setIsAuthOpen] = useState(false);
  const [isLanguageOpen, setIsLanguageOpen] = useState(false);
  const { currentLanguage, t, changeLanguage } = useLanguage();

  const languages = [
    { code: 'vi', name: 'Tiếng Việt', flag: VNFlag },
    { code: 'en', name: 'English', flag: UKFlag },
    { code: 'ja', name: '日本語', flag: JPFlag },
    { code: 'zh', name: '繁體中文', flag: TWFlag },
  ];

  
  useEffect(() => {
    const langWithFlag = languages.find(lang => lang.code === currentLanguage.code);
    if (langWithFlag && currentLanguage.flag !== langWithFlag.flag) {
      currentLanguage.flag = langWithFlag.flag;
    }
  }, [currentLanguage.code]);

  const handleLanguageSelect = (language) => {
    changeLanguage(language);
    setIsLanguageOpen(false);
  };

  useEffect(() => {
    const handleClickOutside = (event) => {
      if (!event.target.closest('.language-selector')) {
        setIsLanguageOpen(false);
      }
    };
    document.addEventListener('click', handleClickOutside);
    return () => document.removeEventListener('click', handleClickOutside);
  }, []);

  return (
    <>
      <header
        style={{
          position: "fixed",
          top: 0,
          left: 0,
          width: "100%",
          height: "70px",
          background: "#fff",
          display: "flex",
          alignItems: "center",
          justifyContent: "space-between",
          padding: "0 24px",
          boxShadow: "0 2px 10px rgba(0,0,0,0.08)",
          zIndex: 1000,
          color: "black",
        }}
      >
        <div style={{ display: "flex", alignItems: "center", gap: "16px" }}>
          <button
            onClick={() => setIsSidebarOpen((prev) => !prev)}
            style={{
              fontSize: "22px",
              background: "none",
              border: "none",
              cursor: "pointer",
              color: "black",
            }}
          >
            ☰
          </button>
          <h2 style={{ margin: 0, color: "#20c997" }}>Datxe.com</h2>
        </div>

        <input
          placeholder={t.search}
          style={{
            width: "300px",
            padding: "8px 12px",
            borderRadius: "8px",
            border: "1px solid #ddd",
            backgroundColor: "white",
            position: "relative",
            right: "220px",
          }}
        />

        <div style={{ display: "flex", alignItems: "center", gap: "16px", position: "relative", right: "50px" }}>
          <span style={{ display: "flex", alignItems: "center", gap: "4px", cursor: "pointer" }}>
            <IoIosPhonePortrait /> {t.app}
          </span>

          <div className="language-selector" style={{ position: "relative" }}>
            <span 
              style={{ 
                display: "flex", 
                alignItems: "center", 
                gap: "8px", 
                cursor: "pointer",
                padding: "4px 12px",
                borderRadius: "20px",
                backgroundColor: isLanguageOpen ? "#f0f0f0" : "transparent",
                border: "1px solid #e0e0e0",
              }}
              onClick={(e) => {
                e.stopPropagation();
                setIsLanguageOpen(!isLanguageOpen);
              }}
            >
              <img 
                src={currentLanguage.flag} 
                alt={currentLanguage.code} 
                style={{ 
                  width: "24px", 
                  height: "24px", 
                  objectFit: "cover",
                  borderRadius: "50%",
                }} 
              />
              <span style={{ fontSize: "14px", fontWeight: "500" }}>{currentLanguage.code.toUpperCase()}</span>
              <IoChevronDown style={{ 
                fontSize: "14px", 
                color: "#666",
                transform: isLanguageOpen ? "rotate(180deg)" : "rotate(0)",
                transition: "transform 0.3s"
              }} />
            </span>

            {isLanguageOpen && (
              <div
                style={{
                  position: "absolute",
                  top: "45px",
                  right: 0,
                  width: "250px",
                  backgroundColor: "#fff",
                  borderRadius: "12px",
                  boxShadow: "0 8px 30px rgba(0,0,0,0.15)",
                  zIndex: 1001,
                  padding: "12px",
                }}
              >
                <h3 style={{ 
                  margin: "0 0 12px 8px", 
                  fontSize: "16px", 
                  fontWeight: "600",
                  color: "#333",
                  display: "flex",
                  alignItems: "center",
                  gap: "8px"
                }}>
                  <span><AiOutlineGlobal /></span> {t.selectLanguage}
                </h3>
                
                <div style={{ 
                  display: "flex", 
                  flexDirection: "column",
                  gap: "4px"
                }}>
                  {languages.map((lang) => (
                    <button
                      key={lang.code}
                      style={{
                        padding: "10px 12px",
                        border: "none",
                        borderRadius: "8px",
                        background: currentLanguage.code === lang.code ? "#e8f4ff" : "transparent",
                        cursor: "pointer",
                        fontSize: "14px",
                        color: "#333",
                        textAlign: "left",
                        transition: "all 0.2s",
                        display: "flex",
                        alignItems: "center",
                        gap: "12px",
                        width: "100%",
                      }}
                      onClick={() => handleLanguageSelect(lang)}
                      onMouseEnter={(e) => {
                        if (currentLanguage.code !== lang.code) {
                          e.target.style.backgroundColor = "#f5f5f5";
                        }
                      }}
                      onMouseLeave={(e) => {
                        if (currentLanguage.code !== lang.code) {
                          e.target.style.backgroundColor = "transparent";
                        }
                      }}
                    >
                      <img 
                        src={lang.flag} 
                        alt={lang.code} 
                        style={{ 
                          width: "24px", 
                          height: "16px", 
                          objectFit: "cover",
                          borderRadius: "2px",
                        }} 
                      />
                      <span style={{ fontWeight: currentLanguage.code === lang.code ? "600" : "400" }}>
                        {lang.name}
                      </span>
                      {currentLanguage.code === lang.code && (
                        <span style={{ marginLeft: "auto", color: "#20c997", fontSize: "16px" }}>✓</span>
                      )}
                    </button>
                  ))}
                </div>
              </div>
            )}
          </div>

          <span style={{ display: "flex", alignItems: "center", gap: "4px", cursor: "pointer" }}>
            <MdOutlinePhone /> {t.support}
          </span>

          <button
            onClick={() => setIsAuthOpen(true)}
            style={{
              padding: "8px 14px",
              borderRadius: "8px",
              border: "none",
              background: "#4f7cff",
              color: "#fff",
              cursor: "pointer",
              fontWeight: "600"
            }}
          >
            {t.login}
          </button>
        </div>
      </header>

      <Auth isOpen={isAuthOpen} onClose={() => setIsAuthOpen(false)} />
    </>
  );
};

export default Header;