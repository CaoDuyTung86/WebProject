import React, { createContext, useState, useContext, useEffect } from 'react';


const translations = {
  vi: {
    // Header
    app: "Ứng dụng",
    search: "Tìm kiếm",
    support: "CSKH",
    login: "Đăng nhập/Đăng ký",
    
    // Auth Modal
    authTitle: "Đăng nhập / Đăng ký",
    emailPlaceholder: "Vui lòng nhập địa chỉ email",
    continueWithEmail: "Tiếp tục với email",
    or: "Hoặc",
    loginWithGoogle: "Đăng nhập bằng Google",
    loginWithFacebook: "Đăng nhập với Facebook",
    loginWithApple: "Đăng nhập với Apple",
    qrText: "Sử dụng ứng dụng để",
    qrHighlight: "đăng nhập bằng mã QR",
    
    // Password Step
    createAccount: "Tạo Tài Khoản",
    setPassword: "Đặt mật khẩu cho tài khoản mới của bạn:",
    password: "Mật khẩu",
    passwordRequirement: "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ cái, chữ số và ký hiệu",
    registerAndLogin: "Đăng ký và Đăng nhập",
    notYou: "Không phải bạn?",
    termsPrefix: "Bằng việc đăng nhập hoặc đăng ký, bạn được xem như đã đồng ý với",
    termsAndConditions: "Điều Kiện Và Điều Khoản",
    privacyPolicy: "Tuyên Bố Quyền Riêng Tự",
    of: "của",
    
    // Language
    selectLanguage: "Chọn ngôn ngữ",
    language: "Ngôn ngữ",
    
    // Errors
    emailRequired: "Vui lòng nhập địa chỉ email",
    emailInvalid: "Email phải là Gmail (có đuôi @gmail.com)",
    passwordRequired: "Vui lòng nhập mật khẩu",
    passwordInvalid: "Mật khẩu phải có ít nhất 8 ký tự, bao gồm chữ cái, chữ số và ký hiệu",
    registerSuccess: "Đăng ký tài khoản {email} thành công!",

    // Booking Tabs
    flight: "Vé máy bay",
    train: "Vé tàu hỏa",
    bus: "Xe khách",
    package: "Đặt theo gói",
    bookingContent: "Nội dung đặt vé cho:",

    // Sidebar
    flight: "Vé máy bay",
    train: "Vé tàu hỏa",
    bus: "Xe khách",
    package: "Đặt theo gói",

  },


  en: {
    // Header
    app: "App",
    search: "Search",
    support: "Support",
    login: "Login/Register",
    
    // Auth Modal
    authTitle: "Login / Register",
    emailPlaceholder: "Please enter your email",
    continueWithEmail: "Continue with email",
    or: "Or",
    loginWithGoogle: "Login with Google",
    loginWithFacebook: "Login with Facebook",
    loginWithApple: "Login with Apple",
    qrText: "Use app to",
    qrHighlight: "login with QR code",
    
    // Password Step
    createAccount: "Create Account",
    setPassword: "Set password for your new account:",
    password: "Password",
    passwordRequirement: "Password must be at least 8 characters, including letters, numbers and symbols",
    registerAndLogin: "Register & Login",
    notYou: "Not you?",
    termsPrefix: "By logging in or registering, you agree to the",
    termsAndConditions: "Terms & Conditions",
    privacyPolicy: "Privacy Policy",
    of: "of",
    
    // Language
    selectLanguage: "Select language",
    language: "Language",
    
    // Errors
    emailRequired: "Please enter your email",
    emailInvalid: "Email must be Gmail (with @gmail.com)",
    passwordRequired: "Please enter password",
    passwordInvalid: "Password must be at least 8 characters, including letters, numbers and symbols",
    registerSuccess: "Account {email} registered successfully!",
    
    // Booking Tabs
    flight: "Flight Tickets",
    train: "Train Tickets",
    bus: "Bus Tickets",
    package: "Package Booking",
    bookingContent: "Booking content for:",

    // Sidebar
    flight: "Flight Tickets",
    train: "Train Tickets",
    bus: "Bus Tickets",
    package: "Package Booking",

  },


  ja: {
    // Header
    app: "アプリ",
    search: "検索",
    support: "サポート",
    login: "ログイン/登録",
    
    // Auth Modal
    authTitle: "ログイン / 登録",
    emailPlaceholder: "メールアドレスを入力してください",
    continueWithEmail: "メールで続ける",
    or: "または",
    loginWithGoogle: "Googleでログイン",
    loginWithFacebook: "Facebookでログイン",
    loginWithApple: "Appleでログイン",
    qrText: "アプリを使用して",
    qrHighlight: "QRコードでログイン",
    
    // Password Step
    createAccount: "アカウント作成",
    setPassword: "新しいアカウントのパスワードを設定:",
    password: "パスワード",
    passwordRequirement: "パスワードは8文字以上で、文字、数字、記号を含む必要があります",
    registerAndLogin: "登録してログイン",
    notYou: "違う方ですか？",
    termsPrefix: "ログインまたは登録により、",
    termsAndConditions: "利用規約",
    privacyPolicy: "プライバシーポリシー",
    of: "に同意したものとみなされます",
    
    // Language
    selectLanguage: "言語を選択",
    language: "言語",
    
    // Errors
    emailRequired: "メールアドレスを入力してください",
    emailInvalid: "メールはGmail（@gmail.com）である必要があります",
    passwordRequired: "パスワードを入力してください",
    passwordInvalid: "パスワードは8文字以上で、文字、数字、記号を含む必要があります",
    registerSuccess: "アカウント {email} が正常に登録されました",

    // Booking Tabs
    flight: "航空券",
    train: "鉄道チケット",
    bus: "バスチケット",
    package: "パッケージ予約",
    bookingContent: "予約内容:",

    // Sidebar
    flight: "航空券",
    train: "鉄道チケット",
    bus: "バスチケット",
    package: "パッケージ予約",


  },
  zh: {
    // Header
    app: "應用程式",
    search: "搜尋",
    support: "客服",
    login: "登入/註冊",
    
    // Auth Modal
    authTitle: "登入 / 註冊",
    emailPlaceholder: "請輸入電子郵件",
    continueWithEmail: "繼續使用電子郵件",
    or: "或",
    loginWithGoogle: "使用Google登入",
    loginWithFacebook: "使用Facebook登入",
    loginWithApple: "使用Apple登入",
    qrText: "使用應用程式",
    qrHighlight: "使用QR碼登入",
    
    // Password Step
    createAccount: "創建帳戶",
    setPassword: "為您的新帳戶設置密碼：",
    password: "密碼",
    passwordRequirement: "密碼必須至少8個字符，包含字母、數字和符號",
    registerAndLogin: "註冊並登入",
    notYou: "不是您嗎？",
    termsPrefix: "通過登入或註冊，您被視為已同意",
    termsAndConditions: "條款與條件",
    privacyPolicy: "隱私權政策",
    of: "的",
    
    // Language
    selectLanguage: "選擇語言",
    language: "語言",
    
    // Errors
    emailRequired: "請輸入電子郵件",
    emailInvalid: "電子郵件必須是Gmail（帶@gmail.com）",
    passwordRequired: "請輸入密碼",
    passwordInvalid: "密碼必須至少8個字符，包含字母、數字和符號",
    registerSuccess: "帳戶 {email} 註冊成功！",

    // Booking Tabs
    flight: "機票",
    train: "火車票",
    bus: "巴士票",
    package: "套裝預訂",
    bookingContent: "預訂內容:",

    // Sidebar
    flight: "機票",
    train: "火車票",
    bus: "巴士票",
    package: "套裝預訂",


  }
};

const LanguageContext = createContext();

export const LanguageProvider = ({ children }) => {
  const [currentLanguage, setCurrentLanguage] = useState({
    code: 'vi',
    name: 'Tiếng Việt',
    flag: null 
  });
  const [t, setT] = useState(translations.vi);

  useEffect(() => {
    const savedLanguage = localStorage.getItem("language");
    if (savedLanguage) {
      const lang = JSON.parse(savedLanguage);
      setCurrentLanguage(lang);
      setT(translations[lang.code] || translations.vi);
      document.documentElement.lang = lang.code;
    }
  }, []);

  const changeLanguage = (language) => {
    setCurrentLanguage(language);
    setT(translations[language.code]);
    localStorage.setItem("language", JSON.stringify(language));
    document.documentElement.lang = language.code;
    window.dispatchEvent(new CustomEvent('languageChange', { detail: { language: language.code } }));
  };

  return (
    <LanguageContext.Provider value={{ currentLanguage, t, changeLanguage, translations }}>
      {children}
    </LanguageContext.Provider>
  );
};

export const useLanguage = () => {
  const context = useContext(LanguageContext);
  if (!context) {
    throw new Error('useLanguage must be used within a LanguageProvider');
  }
  return context;
};