import os

filepath = r'd:\clone repo\WebProject\my-react-app\src\Page\AdminRevenue.jsx'

with open(filepath, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find the line with isSidebarOpen and insert useLanguage() after it
new_lines = []
for i, line in enumerate(lines):
    new_lines.append(line)
    if 'const [isSidebarOpen, setIsSidebarOpen] = useState(true);' in line:
        new_lines.append('  const { t } = useLanguage();\r\n')

with open(filepath, 'w', encoding='utf-8') as f:
    f.writelines(new_lines)

print(f"Done! File now has {len(new_lines)} lines")
