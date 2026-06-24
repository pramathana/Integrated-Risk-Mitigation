import re
import sys

def apply_light_mode(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # 1. Add [data-theme="light"] to CSS
        light_theme_css = """
    [data-theme="light"] {
      --bg-base: #f8f9fa;
      --bg-surface: #ffffff;
      --bg-surface-hover: #f1f5f9;
      --border-subtle: rgba(0, 0, 0, 0.1);

      --text-primary: #111827;
      --text-secondary: #4b5563;
      --text-tertiary: #6b7280;

      --accent-primary: #2563eb;
      --accent-glow: rgba(37, 99, 235, 0.2);

      --risk-moderate-bg: rgba(245, 158, 11, 0.2);
      --risk-moderate-text: #d97706;
      --risk-lowmod-bg: rgba(56, 189, 248, 0.2);
      --risk-lowmod-text: #0284c7;
      --risk-low-bg: rgba(52, 211, 153, 0.2);
      --risk-low-text: #059669;
    }
"""
        if '[data-theme="light"]' not in content:
            # Insert after the :root block
            root_end = content.find('}', content.find(':root {')) + 1
            content = content[:root_end] + light_theme_css + content[root_end:]

        # 2. Add transition to * selector
        if 'transition: all 0.3s ease;' not in content and 'transition: background-color' not in content:
            # Add to * selector
            star_idx = content.find('* {')
            if star_idx != -1:
                padding_end = content.find('padding: 0;', star_idx) + len('padding: 0;')
                content = content[:padding_end] + '\n      transition: background-color 0.3s ease, color 0.3s ease, border-color 0.3s ease, box-shadow 0.3s ease, fill 0.3s ease, stroke 0.3s ease;' + content[padding_end:]

        # 3. Insert toggle button in header
        toggle_button_html = """
        <button id="themeToggleBtn" onclick="toggleTheme()" style="
              background: var(--bg-surface);
              color: var(--text-primary);
              border: 1px solid var(--border-subtle);
              padding: 0.4rem 0.6rem;
              border-radius: 8px;
              cursor: pointer;
              display: flex;
              align-items: center;
              justify-content: center;
              font-size: 1.25rem;
              transition: all 0.3s ease;
            " title="Toggle Theme">
          ☀️
        </button>
        """
        
        # Modify the div containing the select to use flex and gap
        if '<div style="margin-left: auto">' in content:
            content = content.replace(
                '<div style="margin-left: auto">',
                '<div style="margin-left: auto; display: flex; align-items: center; gap: 1rem;">'
            )
            # Insert button before the select
            select_idx = content.find('<select id="langSwitcher"')
            if select_idx != -1 and 'themeToggleBtn' not in content:
                content = content[:select_idx] + toggle_button_html + content[select_idx:]

        # 4. Javascript toggle function
        js_logic = """
    // Theme Toggle Logic
    function toggleTheme() {
      const htmlEl = document.documentElement;
      const themeBtn = document.getElementById('themeToggleBtn');
      if (htmlEl.getAttribute('data-theme') === 'light') {
        htmlEl.removeAttribute('data-theme');
        themeBtn.innerHTML = '☀️';
      } else {
        htmlEl.setAttribute('data-theme', 'light');
        themeBtn.innerHTML = '🌙';
      }
    }
"""
        if 'function toggleTheme()' not in content:
            script_idx = content.find('<script>')
            if script_idx != -1:
                content = content[:script_idx + 8] + js_logic + content[script_idx + 8:]

        # 5. Refactor #ffffff and #ccc to CSS variables
        content = re.sub(r'color:\s*#ffffff;?', 'color: var(--text-primary);', content, flags=re.IGNORECASE)
        content = re.sub(r'color:\s*#ccc;?', 'color: var(--text-secondary);', content, flags=re.IGNORECASE)
        
        # For ECharts color properties
        content = re.sub(r'color:\s*"#ffffff"', 'color: "var(--text-primary)"', content, flags=re.IGNORECASE)
        content = re.sub(r"color:\s*'#ffffff'", "color: 'var(--text-primary)'", content, flags=re.IGNORECASE)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("Successfully applied light mode logic.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    apply_light_mode('c:\\ANTIGRAVITY IDE FOLDER\\Dashboard Mitigasi Risiko Terintegrasi\\index.html')
