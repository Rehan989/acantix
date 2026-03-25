import os
import glob
import re

base_dir = r"f:\acantix"

# 1. Update Careers page moving text
careers_path = os.path.join(base_dir, "careers.html")
with open(careers_path, 'r', encoding='utf-8') as f:
    careers_content = f.read()

# Replace ticker styles in Careers
careers_content = careers_content.replace(
    '''<span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> NOW HIRING <span class="text-white/15">◈</span> DEEP WORK FIRST <span class="text-white/15">◈</span> JOIN ACANTIX <span class="text-white/15">◈</span> SHAPE AGENTIC AI <span class="text-white/15">◈</span> SYSTEMS NOT SILOS</span>''',
    '''<span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white font-bold"><span class="text-white font-bold">◈</span> NOW HIRING <span class="text-white font-bold">◈</span> DEEP WORK FIRST <span class="text-white font-bold">◈</span> JOIN ACANTIX <span class="text-white font-bold">◈</span> SHAPE AGENTIC AI <span class="text-white font-bold">◈</span> SYSTEMS NOT SILOS</span>'''
)

with open(careers_path, 'w', encoding='utf-8') as f:
    f.write(careers_content)

# 2. Update Stack page Culture Stack
stack_path = os.path.join(base_dir, "stack.html")
with open(stack_path, 'r', encoding='utf-8') as f:
    stack_content = f.read()

# Change Culture Stack container background from bg-[#1a1a1a] to bg-[#fafafa]
stack_content = stack_content.replace(
    '''<div class="border border-[#e5e5e5] rounded-3xl p-8 md:p-12 relative overflow-hidden flex flex-col md:flex-row gap-8 items-start hover:shadow-lg transition-all group bg-[#1a1a1a]">''',
    '''<div class="border border-[#e5e5e5] rounded-3xl p-8 md:p-12 relative overflow-hidden flex flex-col md:flex-row gap-8 items-start hover:shadow-lg transition-all group bg-[#fafafa]">'''
)
# Big C letter opacity and color
stack_content = stack_content.replace(
    '''<div class="absolute -right-10 -top-10 opacity-5 group-hover:opacity-[0.08] transition-opacity">
                        <div class="text-[180px] font-serif font-black leading-none text-white">C</div>
                    </div>''',
    '''<div class="absolute -right-10 -top-10 opacity-5 group-hover:opacity-10 transition-opacity">
                        <div class="text-[180px] font-serif font-black leading-none text-[#1a1a1a]">C</div>
                    </div>'''
)
# Icon box
stack_content = stack_content.replace(
    '''<div class="shrink-0 w-16 h-16 rounded-2xl bg-white/10 border border-white/10 flex items-center justify-center group-hover:-translate-y-1 transition-transform">
                        <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor">''',
    '''<div class="shrink-0 w-16 h-16 rounded-2xl bg-white border border-[#e5e5e5] flex items-center justify-center group-hover:-translate-y-1 transition-transform">
                        <svg class="w-8 h-8 text-[#1a1a1a]" fill="none" viewBox="0 0 24 24" stroke="currentColor">'''
)
# Top small text
stack_content = stack_content.replace(
    '''<div class="font-mono text-[10px] text-white/50 tracking-[.25em] mb-2 uppercase">Values That Drive Us</div>''',
    '''<div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] mb-2 uppercase">Values That Drive Us</div>'''
)
# Title
stack_content = stack_content.replace(
    '''<h3 class="text-2xl md:text-3xl font-bold text-white mb-6 font-serif">Culture Stack</h3>''',
    '''<h3 class="text-2xl md:text-3xl font-bold text-[#1a1a1a] mb-6 font-serif">Culture Stack</h3>'''
)
# The Grid Items - we will regex substitute them because there are three
stack_content = stack_content.replace(
    '''<h4 class="text-sm font-bold text-white uppercase tracking-wider mb-2">''',
    '''<h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2">'''
)
stack_content = stack_content.replace(
    '''<p class="text-white/60 text-sm leading-relaxed">''',
    '''<p class="text-[#6b6b6b] text-sm leading-relaxed">'''
)

with open(stack_path, 'w', encoding='utf-8') as f:
    f.write(stack_content)

# 3. Update all HTML files: Remove Contact link in nav, add Chat icon to Talk to Riya, change Talk to Riya href to voiceflow open
html_files = glob.glob(os.path.join(base_dir, '**', '*.html'), recursive=True)

chat_svg = '''<svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="mr-1"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"></path></svg>'''

for fpath in html_files:
    # skip test files
    if 'chatbot\\\\test.html' in fpath:
        continue
    
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Contact link
    content = re.sub(
        r'<a\s+href="[^"]*#contact"\s*class="text-\[#6b6b6b\]\s*text-sm\s*font-medium\s*hover:text-\[#1a1a1a\]\s*transition-colors">Contact</a>\s*',
        '',
        content
    )

    # Mobile Contact link
    content = re.sub(
        r'<a\s+href="[^"]*#contact"\s*onclick="closeMenu\(\)"\s*class="py-3\s*border-b\s*border-\[#e5e5e5\]\s*font-semibold\s*text-\[#1a1a1a\]\s*no-underline">Contact</a>\s*',
        '',
        content
    )

    # Add chat SVG to desktop Talk to Riya
    content = re.sub(
        r'(<a\s+href="[^"]*"\s*[^>]*)(class="inline-flex[^>]+>)\s*Talk to Riya\s*</a>',
        lambda m: m.group(1).replace('href="/#contact"', 'href="#" onclick="window.voiceflow.chat.open(); return false;"').replace('href="#contact"', 'href="#" onclick="window.voiceflow.chat.open(); return false;"') + m.group(2) + chat_svg + "Talk to Riya</a>",
        content
    )

    # Add chat SVG to mobile Talk to Riya
    content = re.sub(
        r'(<a\s+href="[^"]*"\s*[^>]*)(class="mt-3\s*bg-\[#1a1a1a\][^>]+>)\s*Talk to Riya\s*</a>',
        lambda m: m.group(1).replace('href="/#contact"', 'href="#" onclick="window.voiceflow.chat.open(); return false;"').replace('href="#contact"', 'href="#" onclick="window.voiceflow.chat.open(); return false;"') + 'class="mt-3 bg-[#1a1a1a] text-white py-3 px-5 rounded-full font-bold text-center no-underline inline-flex justify-center items-center gap-2">' + chat_svg + "Talk to Riya</a>",
        content
    )

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)

print("Done")
