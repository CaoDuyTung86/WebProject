"""
Refactor inline style hardcoded colors to CSS Variables for dark-mode support.
Targets the most common patterns used across all JSX files.
"""
import os, re, glob

# Color mapping: old hardcoded value -> CSS variable
REPLACEMENTS = [
    # Backgrounds
    ('backgroundColor: "#f8f9fa"', 'backgroundColor: "var(--bg-main)"'),
    ('backgroundColor: "#f3f4f6"', 'backgroundColor: "var(--bg-main)"'),
    ('backgroundColor: "#f5f7fb"', 'backgroundColor: "var(--bg-main)"'),
    ('background: "#f8f9fa"', 'background: "var(--bg-main)"'),
    ('background: "#f3f4f6"', 'background: "var(--bg-main)"'),
    ('background: "#f5f7fb"', 'background: "var(--bg-main)"'),
    
    ('backgroundColor: "#fff"', 'backgroundColor: "var(--bg-card)"'),
    ('backgroundColor: "#ffffff"', 'backgroundColor: "var(--bg-card)"'),
    ('background: "#fff"', 'background: "var(--bg-card)"'),
    ('background: "#ffffff"', 'background: "var(--bg-card)"'),
    
    ('background: "#f8f9ff"', 'background: "var(--bg-input)"'),
    ('backgroundColor: "#f8f9ff"', 'backgroundColor: "var(--bg-input)"'),
    ('background: "#f9fafb"', 'background: "var(--bg-input)"'),
    ('backgroundColor: "#f9fafb"', 'backgroundColor: "var(--bg-input)"'),
    
    ('backgroundColor: "#f5f5f5"', 'backgroundColor: "var(--bg-hover)"'),
    ('backgroundColor: "#f5f5ff"', 'backgroundColor: "var(--bg-hover)"'),
    ('background: "#f5f5f5"', 'background: "var(--bg-hover)"'),
    
    ('background: "#f0f0f0"', 'background: "var(--bg-tag)"'),
    ('backgroundColor: "#f0f0f0"', 'backgroundColor: "var(--bg-tag)"'),
    
    # Text colors
    ('color: "#333"', 'color: "var(--text-main)"'),
    ('color: "#333333"', 'color: "var(--text-main)"'),
    ('color: "#1a1a2e"', 'color: "var(--text-main)"'),
    
    ('color: "#666"', 'color: "var(--text-secondary)"'),
    ('color: "#555"', 'color: "var(--text-secondary)"'),
    ('color: "#666666"', 'color: "var(--text-secondary)"'),
    
    ('color: "#999"', 'color: "var(--text-muted)"'),
    ('color: "#aaa"', 'color: "var(--text-muted)"'),
    ('color: "#888"', 'color: "var(--text-muted)"'),
    ('color: "#999999"', 'color: "var(--text-muted)"'),
    
    ('color: "#111827"', 'color: "var(--text-heading)"'),
    ('color: "#111"', 'color: "var(--text-heading)"'),
    
    # Borders
    ('border: "1px solid #eee"', 'border: "1px solid var(--border-light)"'),
    ('border: "1px solid #e0e7ff"', 'border: "1px solid var(--border-main)"'),
    ('border: "2px solid #e0e7ff"', 'border: "2px solid var(--border-main)"'),
    ('borderBottom: "1px solid #f0f0f0"', 'borderBottom: "1px solid var(--border-light)"'),
    ('borderTop: "1px solid #eee"', 'borderTop: "1px solid var(--border-light)"'),
    ('borderTop: "2px solid #f0f0f0"', 'borderTop: "2px solid var(--border-light)"'),
    ('border: "1px solid #ddd"', 'border: "1px solid var(--border-input)"'),
    ('border: "1.5px solid #d1d5db"', 'border: "1.5px solid var(--border-input)"'),
    
    # Shadows (boxShadow)
    ('boxShadow: "0 4px 15px rgba(0,0,0,0.05)"', 'boxShadow: "var(--shadow-md)"'),
    ('boxShadow: "0 2px 10px rgba(0,0,0,0.08)"', 'boxShadow: "var(--shadow-sm)"'),
    ('boxShadow: "0 8px 30px rgba(0,0,0,0.15)"', 'boxShadow: "var(--shadow-lg)"'),
    ('boxShadow: "0 10px 30px rgba(0,0,0,0.08)"', 'boxShadow: "var(--shadow-card)"'),
    
    # Primary blue
    ('color: "#4f7cff"', 'color: "var(--primary)"'),
    ('background: "#4f7cff"', 'background: "var(--primary)"'),
    ('backgroundColor: "#4f7cff"', 'backgroundColor: "var(--primary)"'),
    
    # Hover background on card
    ('backgroundColor: "#eff6ff"', 'backgroundColor: "var(--bg-accent)"'),
    ('background: "#eff6ff"', 'background: "var(--bg-accent)"'),
]

# onMouseEnter/Leave handlers that set .style props directly (e.g. e.target.style.backgroundColor = "#f5f5f5")
STYLE_PROP_REPLACEMENTS = [
    ('style.backgroundColor = "#f5f5f5"', 'style.backgroundColor = "var(--bg-hover)"'),
    ('style.backgroundColor = "#f5f5ff"', 'style.backgroundColor = "var(--bg-hover)"'),
    ('style.backgroundColor = "#fff"', 'style.backgroundColor = "var(--bg-card)"'),
    ('style.backgroundColor = "#ffffff"', 'style.backgroundColor = "var(--bg-card)"'),
    ('style.backgroundColor = "#eff6ff"', 'style.backgroundColor = "var(--bg-accent)"'),
    ('style.backgroundColor = "#f0f0f0"', 'style.backgroundColor = "var(--bg-tag)"'),
    ('style.background = "#fff"', 'style.background = "var(--bg-card)"'),
    ('style.backgroundColor = "#3a5fd0"', 'style.backgroundColor = "var(--primary-hover)"'),
    ('style.background = "#3a5fd0"', 'style.background = "var(--primary-hover)"'),
    ('style.backgroundColor = "#4f7cff"', 'style.backgroundColor = "var(--primary)"'),
    ('style.background = "#4f7cff"', 'style.background = "var(--primary)"'),
]

# Files to process
src = r'd:\clone repo\WebProject\my-react-app\src'
patterns = [
    os.path.join(src, 'Page', '*.jsx'),
    os.path.join(src, 'components', '*.jsx'),
    os.path.join(src, 'LayOut', '*.jsx'),
]

files = []
for p in patterns:
    files.extend(glob.glob(p))

total_changes = 0
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original = content
    for old, new in REPLACEMENTS + STYLE_PROP_REPLACEMENTS:
        content = content.replace(old, new)
    
    if content != original:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        changes = sum(1 for old, new in REPLACEMENTS + STYLE_PROP_REPLACEMENTS if old in original)
        total_changes += changes
        print(f"  Updated: {os.path.basename(filepath)} ({changes} pattern types)")

print(f"\nDone! {total_changes} total pattern types replaced across {len(files)} files.")
