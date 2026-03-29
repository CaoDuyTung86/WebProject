const fs = require('fs');
let c = fs.readFileSync('src/Page/AdminRevenue.jsx', 'utf8');
c = c.replace(/const t = \(type \|\| ""\)\.toLowerCase\(\);/g, 'const t_local = (type || "").toLowerCase();');
c = c.replace(/t\.includes/g, 't_local.includes');
c = c.replace('const revenueByTypeMap = { t.flight: 0, t.bus: 0, t.train: 0 };', 'const revenueByTypeMap = { [t.flight]: 0, [t.bus]: 0, [t.train]: 0 };');
c = c.replace('const t = getMappedType(item.providerType);', 'const t_type = getMappedType(item.providerType);').replace('revenueByTypeMap[t] +=', 'revenueByTypeMap[t_type] +=');
fs.writeFileSync('src/Page/AdminRevenue.jsx', c, 'utf8');

let c2 = fs.readFileSync('src/Page/ProviderRefunds.jsx', 'utf8');
c2 = c2.replace(/import { useLanguage } from "..\/context\/LanguageContext";\nimport { useLanguage } from "..\/context\/LanguageContext";/, 'import { useLanguage } from "../context/LanguageContext";');
c2 = c2.replace(/import { useLanguage } from "..\/context\/LanguageContext";\r?\nimport { useLanguage } from "..\/context\/LanguageContext";/, 'import { useLanguage } from "../context/LanguageContext";');
c2 = c2.replace('import Sidebar from "../components/Sidebar";\nimport { useLanguage } from "../context/LanguageContext";', 'import Sidebar from "../components/Sidebar";');
c2 = c2.replace('import Sidebar from "../components/Sidebar";\r\nimport { useLanguage } from "../context/LanguageContext";', 'import Sidebar from "../components/Sidebar";');
fs.writeFileSync('src/Page/ProviderRefunds.jsx', c2, 'utf8');
console.log('Fixed syntax issues');