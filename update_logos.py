import re

with open(r'f:\acantix\logo.svg', 'r', encoding='utf-8') as f:
    logo_svg = f.read()
with open(r'f:\acantix\icon.svg', 'r', encoding='utf-8') as f:
    icon_svg = f.read()

# Make SVGs inline scaleable
logo_svg_inline = logo_svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '').replace('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="348" height="134">', '<svg width="120" height="46" viewBox="0 0 348 134" version="1.1" xmlns="http://www.w3.org/2000/svg" class="brand-logo">')
icon_svg_inline = icon_svg.replace('<?xml version="1.0" encoding="UTF-8"?>\n', '').replace('<svg version="1.1" xmlns="http://www.w3.org/2000/svg" width="100" height="100">', '<svg width="44" height="44" viewBox="0 0 100 100" version="1.1" xmlns="http://www.w3.org/2000/svg" class="brand-icon">')

# Simple regex to replace nav SVG (the logo inside <a href="#" class="logo">)
nav_regex = re.compile(r'<a href="#" class="logo">[\s\S]*?<svg[\s\S]*?</svg>[\s\S]*?<span class="logo-text">Acantix</span>\s*</a>')
footer_regex = re.compile(r'<div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">\s*<svg[\s\S]*?</svg>\s*<span[\s\S]*?>Acantix</span>\s*</div>')

nav_replacement = f'''<a href="#" class="logo">
                {icon_svg_inline}
                <span class="logo-text">Acantix</span>
            </a>'''
            
footer_replacement = f'''<div style="display:flex;align-items:center;gap:10px;margin-bottom:16px;">
                        {logo_svg_inline}
                    </div>'''

files = [r'f:\acantix\index.html', r'f:\acantix\careers.html', r'f:\acantix\case-studies.html']
for filepath in files:
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    content = nav_regex.sub(nav_replacement, content)
    content = footer_regex.sub(footer_replacement, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filepath}')
