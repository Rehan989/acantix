import os
import glob
import re

print("Patching HTML files...")

for file_path in glob.glob(r'f:\acantix\**\*.html', recursive=True):
    if 'node_modules' in file_path or 'chatbot' in file_path or 'dist' in file_path:
        continue

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    patched = content

    # 1. Update Desktop CTA
    old_desktop_cta = r'<a href="#contact"([^>]*)>\s*Get Your AI Strategy Blueprint\s*→</a>'
    new_desktop_cta = r'<a href="#" onclick="window.voiceflow.chat.open(); return false;"\1>Talk to Riya</a>'
    patched = re.sub(old_desktop_cta, new_desktop_cta, patched, flags=re.IGNORECASE)

    # If it was split in multiple lines occasionally, try this:
    old_desktop_cta2 = r'<a href="#contact"([^>]*)>\s*Get Your AI Strategy Blueprint\s*<br\s*/>\s*→</a>'
    new_desktop_cta2 = r'<a href="#" onclick="window.voiceflow.chat.open(); return false;"\1>Talk to Riya</a>'
    patched = re.sub(old_desktop_cta2, new_desktop_cta2, patched, flags=re.IGNORECASE)

    # 2. Update Mobile CTA
    old_mobile_cta = r'<a href="#contact" onclick="closeMenu\(\)"([^>]*)>\s*Get Your AI Strategy Blueprint\s*→</a>'
    new_mobile_cta = r'<a href="#" onclick="closeMenu(); window.voiceflow.chat.open(); return false;"\1>Talk to Riya</a>'
    patched = re.sub(old_mobile_cta, new_mobile_cta, patched, flags=re.IGNORECASE)

    old_mobile_cta2 = r'<a href="#contact" onclick="closeMenu\(\)"([^>]*)>\s*Get Your AI Strategy Blueprint\n\s*→</a>'
    new_mobile_cta2 = r'<a href="#" onclick="closeMenu(); window.voiceflow.chat.open(); return false;"\1>Talk to Riya</a>'
    patched = re.sub(old_mobile_cta2, new_mobile_cta2, patched, flags=re.IGNORECASE)

    # Also handle index.html where lines 388-390 don't match exactly because of newline?
    # Let's just do an exact replace for the button texts if the above regex fails, but regex is better.
    # We can also do string replace for the specific HTML parts seen in index.html
    patched = patched.replace(
        '>Get Your AI Strategy Blueprint →</a>',
        '>Talk to Riya</a>'
    ).replace(
        '>Get Your AI Strategy Blueprint\n            →</a>',
        '>Talk to Riya</a>'
    )
    
    # Handle Desktop Nav
    patched = re.sub(
        r'<a href="#contact"\s*(class="inline-flex items-center gap-2 px-5[^>]+)>Talk to Riya</a>',
        r'<a href="#" onclick="window.voiceflow.chat.open(); return false;" \1>Talk to Riya</a>',
        patched
    )

    # Handle Mobile Nav
    patched = re.sub(
        r'<a href="#contact" onclick="closeMenu\(\)"\s*(class="mt-3 bg-\[\#1a1a1a[^>]+)>Talk to Riya</a>',
        r'<a href="#" onclick="closeMenu(); window.voiceflow.chat.open(); return false;" \1>Talk to Riya</a>',
        patched
    )


    # 3. Update the Voiceflow Hide Script to also hide .vfrc-launcher
    patched = patched.replace(
        "const els = root.querySelectorAll('.vfrc-footer__links-powered-by-container');",
        "const els = root.querySelectorAll('.vfrc-footer__links-powered-by-container, .vfrc-launcher');"
    )
    
    patched = patched.replace(
        "if (n.matches && n.matches('.vfrc-footer__links-powered-by-container')) {",
        "if (n.matches && (n.matches('.vfrc-footer__links-powered-by-container') || n.matches('.vfrc-launcher'))) {"
    )
    
    # Update querySelector to querySelectorAll in the mutation observer
    # const inside = n.querySelector && n.querySelector('.vfrc-footer__links-powered-by-container');
    # if (inside) { inside.style.display = 'none'; changed = true; }
    
    patched = patched.replace(
        "const inside = n.querySelector && n.querySelector('.vfrc-footer__links-powered-by-container');\n                if (inside) { inside.style.display = 'none'; changed = true; }",
        "if (n.querySelectorAll) {\n                  const insides = n.querySelectorAll('.vfrc-footer__links-powered-by-container, .vfrc-launcher');\n                  if (insides && insides.length) { insides.forEach(e => e.style.display = 'none'); changed = true; }\n                }"
    )

    if patched != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(patched)
        print(f"Updated {file_path}")

print("Done patching HTML files!")
