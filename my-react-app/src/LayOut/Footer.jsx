// src/components/Footer.jsx
import React from "react";
import { useLanguage } from "../context/LanguageContext";
import { FaCcVisa, FaCcMastercard, FaPaypal, FaGooglePay, FaApplePay } from "react-icons/fa";
import { SiAmericanexpress } from "react-icons/si";
import { useLocation } from "react-router-dom";

const Footer = () => {
  const { t } = useLanguage();
  const location = useLocation();
  const isAuthPage = location.pathname === "/auth";

  return (
    <footer style={{
      backgroundColor: "#f8f9fa",
      borderTop: "1px solid #e9ecef",
      padding: "48px 24px 24px",
      marginTop: "60px",
      marginLeft: !isAuthPage ? "220px" : "0",
      transition: "margin-left 0.3s",
      width: !isAuthPage ? "calc(100% - 220px)" : "100%",
      boxSizing: "border-box",
    }}>
      <div style={{
        maxWidth: "1200px",
        margin: "0 auto",
        width: "100%",
      }}>
        {/* Main Footer Grid */}
        <div style={{
          display: "grid",
          gridTemplateColumns: "repeat(4, 1fr)",
          gap: "40px",
          marginBottom: "40px",
          width: "100%",
        }}>
          {/* Column 1: Contact Us */}
          <div style={{ width: "100%" }}>
            <h4 style={{
              fontSize: "16px",
              fontWeight: "700",
              color: "#333",
              marginBottom: "20px",
              textTransform: "uppercase",
              letterSpacing: "0.5px",
            }}>
              {t.contactUs}
            </h4>
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.customerCare}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.serviceGuarantee}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.moreServiceInfo}
                </a>
              </li>
            </ul>
          </div>

          {/* Column 2: About Datxe.com */}
          <div style={{ width: "100%" }}>
            <h4 style={{
              fontSize: "16px",
              fontWeight: "700",
              color: "#333",
              marginBottom: "20px",
              textTransform: "uppercase",
              letterSpacing: "0.5px",
            }}>
              {t.aboutUs}
            </h4>
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.aboutUs}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.news}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.careers}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.termsConditions}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.privacyPolicy}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.aboutGroup}
                </a>
              </li>
            </ul>
          </div>

          {/* Column 3: Other Services */}
          <div style={{ width: "100%" }}>
            <h4 style={{
              fontSize: "16px",
              fontWeight: "700",
              color: "#333",
              marginBottom: "20px",
              textTransform: "uppercase",
              letterSpacing: "0.5px",
            }}>
              {t.otherServices}
            </h4>
            <ul style={{ listStyle: "none", padding: 0, margin: 0 }}>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.investorRelations}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.rewards}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.affiliateProgram}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.listProperty}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.listProperty}
                </a>
              </li>
              <li style={{ marginBottom: "12px" }}>
                <a href="#" style={{ 
                  color: "#666", 
                  textDecoration: "none", 
                  fontSize: "14px",
                  transition: "color 0.2s",
                  display: "inline-block",
                }}
                onMouseEnter={(e) => e.target.style.color = "#4f7cff"}
                onMouseLeave={(e) => e.target.style.color = "#666"}
                >
                  {t.security}
                </a>
              </li>
            </ul>
          </div>

          {/* Column 4: Payment Methods & Partners */}
          <div style={{ width: "100%" }}>
            <h4 style={{
              fontSize: "16px",
              fontWeight: "700",
              color: "#333",
              marginBottom: "20px",
              textTransform: "uppercase",
              letterSpacing: "0.5px",
            }}>
              {t.paymentMethods}
            </h4>
            <div style={{ 
              display: "flex", 
              gap: "12px", 
              flexWrap: "wrap", 
              marginBottom: "30px",
              alignItems: "center",
            }}>
              <FaCcVisa size={36} color="#1A1F71" />
              <FaCcMastercard size={36} color="#EB001B" />
              <SiAmericanexpress size={36} color="#2E77BC" />
              <FaPaypal size={36} color="#003087" />
              <FaGooglePay size={36} color="#4285F4" />
              <FaApplePay size={36} color="#000000" />
            </div>

            <h4 style={{
              fontSize: "16px",
              fontWeight: "700",
              color: "#333",
              marginBottom: "20px",
              textTransform: "uppercase",
              letterSpacing: "0.5px",
            }}>
              {t.ourPartners}
            </h4>
            <div style={{ 
              display: "flex", 
              gap: "20px", 
              alignItems: "center", 
              marginBottom: "24px",
              flexWrap: "wrap",
            }}>
              <span style={{ 
                fontSize: "18px", 
                fontWeight: "600", 
                color: "#4285F4",
                background: "#fff",
                padding: "6px 16px",
                borderRadius: "30px",
                border: "2px solid #4285F4",
              }}>
                Google
              </span>
              <span style={{ 
                fontSize: "18px", 
                fontWeight: "600", 
                color: "#00aa6c",
                background: "#fff",
                padding: "6px 16px",
                borderRadius: "30px",
                border: "2px solid #00aa6c",
              }}>
                DatXeVisor
              </span>
            </div>
          </div>
        </div>

        {/* Copyright */}
        <div style={{
          borderTop: "1px solid #e0e0e0",
          paddingTop: "24px",
          textAlign: "center",
          color: "#888",
          fontSize: "13px",
          lineHeight: "1.6",
        }}>
          <p style={{ margin: 0 }}>
            {t.copyright}
          </p>
        </div>
      </div>
    </footer>
  );
};

export default Footer;