import os
import glob

print("Patching mobile nav...")
for file_path in glob.glob(r'f:\acantix\**\*.html', recursive=True):
    # Ignore node_modules, chatbot
    if 'node_modules' in file_path or 'chatbot' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    patched = content.replace(
        '<a href="case-studies.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Case Studies</a>',
        '<a href="/stack.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Stack</a>\n        <a href="case-studies.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Case Studies</a>'
    )
    patched = patched.replace(
        '<a href="/case-studies.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Case Studies</a>',
        '<a href="/stack.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Stack</a>\n        <a href="/case-studies.html" onclick="closeMenu()"\n            class="py-3 border-b border-[#e5e5e5] font-semibold text-[#1a1a1a] no-underline">Case Studies</a>'
    )

    if patched != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(patched)

print("Done patching mobile nav")
