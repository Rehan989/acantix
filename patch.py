import os
import re

file_path = "f:/acantix/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Head
old_head_match = re.search(r'<title>.*?</title>.*?<link rel="canonical" href="https://acantix.com/" />\s*<link rel="stylesheet" href="dist/output.css">', html, re.DOTALL)
if old_head_match:
    old_head = old_head_match.group(0)
    new_head = """<title>Acantix | AI Consulting, Software Development & Digital Transformation</title>
    <meta name="description" content=" Acantix delivers AI consulting, application development, and digital transformation solutions to help businesses scale, automate, and innovate faster.">
    <meta name="keywords" content="AI consulting, digital transformation, software development, AI solutions, application modernisation, product engineering, cloud solutions, IT consulting company, AI development services">
    <meta name="author" content="Acantix">
    <meta name="robots" content="index, follow"> 
    <meta property="og:title" content="Acantix | Build and Scale AI-Driven Systems">
    <meta property="og:description" content=" We design, build, and scale AI and digital systems that drive measurable business outcomes.">
    <meta property="og:image" content="https://acantix.com/og-image.png">
    <meta property="og:url" content="https://acantix.com">
    <meta property="og:type" content="website">
    <link rel="canonical" href="https://acantix.com/">
    <link rel="stylesheet" href="dist/output.css">
    <link rel="icon" href="/icon.svg">"""
    html = html.replace(old_head, new_head)
else:
    print("Could not find head")

# 2. Nav Gets Onboard
html = html.replace("Get\\n                Onboard →", "Get Your AI Strategy Blueprint →")
html = html.replace("Get Onboard\\n            →", "Get Your AI Strategy Blueprint\\n            →")
html = html.replace("Get Onboard →", "Get Your AI Strategy Blueprint →")

# 3. Hero Text
old_hero = r"Your<br />Growth and Transformation<br /><em>Partner</em>"
new_hero = r"""Build, modernise, and scale your systems <br />with AI<br /><em class="bg-[#f5e642] px-1.5 italic">in weeks, not months</em>"""
html = re.sub(old_hero, new_hero, html, flags=re.DOTALL)

old_hero_sub = "We build fast, scalable, secure solutions that help businesses grow, adapt, and stay ahead."
new_hero_sub = "Acantix helps businesses design, build, and scale AI-driven systems — faster, smarter, and with measurable impact."
html = html.replace(old_hero_sub, new_hero_sub)

old_hero_btn = "Get Onboard"
new_hero_btn = "Talk to an Expert"
html = re.sub(r'Get Onboard(\s*<svg width="16" height="16" viewBox="0 0 16 16")', r'Talk to an Expert\1', html, flags=re.DOTALL)

# 4. Insert Process before Services
process_section = """
    <!-- ══ PROCESS ══ -->
    <section id="process" class="py-16 md:py-20 px-5 md:px-12 bg-white">
        <div class="max-w-[1200px] mx-auto">
            <div class="text-center mb-14">
                <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-3 block">How We Work</span>
                <h2 class="section-heading font-serif font-bold">Our <span class="bg-[#f5e642] px-1.5 italic">Operating Model</span></h2>
                <p class="text-[#6b6b6b] text-sm md:text-base leading-[1.88] max-w-[540px] mx-auto mt-4">
                    <strong>We deliver results with speed and governance.</strong> Four integrated capabilities from vision to value.
                </p>
            </div>
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 relative">
                <div class="hidden md:block absolute top-[26px] left-[12.5%] right-[12.5%] h-[1.5px] bg-gradient-to-r from-[#e5e5e5] via-[#1a1a1a] to-[#e5e5e5]"></div>
                <!-- Step 1 -->
                <div class="text-center z-10">
                    <div class="w-[52px] h-[52px] rounded-full border-2 border-[#1a1a1a] flex items-center justify-center font-mono text-base font-medium mx-auto mb-4 bg-white relative hover:bg-[#1a1a1a] hover:text-white transition-all cursor-default">
                        01<span class="absolute -top-2 -right-2 w-[18px] h-[18px] rounded-full bg-[#1a1a1a] flex items-center justify-center font-mono text-[8px] text-white">N</span>
                    </div>
                    <h3 class="font-bold text-sm mb-2">Consulting</h3>
                    <p class="text-[#6b6b6b] text-xs leading-[1.8]">Defining strategic direction and transformation roadmaps.</p>
                </div>
                <!-- Step 2 -->
                <div class="text-center z-10">
                    <div class="w-[52px] h-[52px] rounded-full border-2 border-[#1a1a1a] flex items-center justify-center font-mono text-base font-medium mx-auto mb-4 bg-white relative hover:bg-[#1a1a1a] hover:text-white transition-all cursor-default">
                        02<span class="absolute -top-2 -right-2 w-[18px] h-[18px] rounded-full bg-[#f0f0f0] flex items-center justify-center font-mono text-[8px] text-[#6b6b6b]">E</span>
                    </div>
                    <h3 class="font-bold text-sm mb-2">Advisory</h3>
                    <p class="text-[#6b6b6b] text-xs leading-[1.8]">Expert guidance for critical business and technology decisions.</p>
                </div>
                <!-- Step 3 -->
                <div class="text-center z-10">
                    <div class="w-[52px] h-[52px] rounded-full border-2 border-[#6b6b6b] flex items-center justify-center font-mono text-base font-medium text-[#6b6b6b] mx-auto mb-4 bg-white relative hover:bg-[#1a1a1a] hover:text-white hover:border-[#1a1a1a] transition-all cursor-default">
                        03<span class="absolute -top-2 -right-2 w-[18px] h-[18px] rounded-full bg-[#fafafa] border border-[#e5e5e5] flex items-center justify-center font-mono text-[8px] text-[#6b6b6b]">S</span>
                    </div>
                    <h3 class="font-bold text-sm mb-2">Solutioning</h3>
                    <p class="text-[#6b6b6b] text-xs leading-[1.8]">Scalable architectures and platform strategies built to last.</p>
                </div>
                <!-- Step 4 -->
                <div class="text-center z-10">
                    <div class="w-[52px] h-[52px] rounded-full border-2 border-[#6b6b6b] flex items-center justify-center font-mono text-base font-medium text-[#6b6b6b] mx-auto mb-4 bg-white relative hover:bg-[#1a1a1a] hover:text-white hover:border-[#1a1a1a] transition-all cursor-default">
                        04<span class="absolute -top-2 -right-2 w-[18px] h-[18px] rounded-full bg-[#fafafa] border border-[#e5e5e5] flex items-center justify-center font-mono text-[8px] text-[#6b6b6b]">W</span>
                    </div>
                    <h3 class="font-bold text-sm mb-2">Engineering</h3>
                    <p class="text-[#6b6b6b] text-xs leading-[1.8]">Building and operating robust digital systems with precision.</p>
                </div>
            </div>
            <div class="mt-12 border border-[#e5e5e5] rounded-2xl bg-[#fafafa] p-6 md:p-8 flex flex-col md:flex-row items-start md:items-center gap-5 hover:border-[#bbb] hover:shadow-lg transition-all">
                <p class="text-sm text-[#1a1a1a] leading-[1.75] flex-1"><strong>Our four capabilities function as a unified model combining </strong> strategy, guidance, design, and delivery to drive real outcomes.We deploy elite teams to solve complex challenges across fast-changing, high-stakes industries.</p>
                <a href="#contact" class="flex-shrink-0 bg-[#1a1a1a] text-white px-6 py-3 rounded-full text-sm font-bold hover:shadow-lg hover:-translate-y-1 transition-all whitespace-nowrap w-full md:w-auto text-center">Start Your Engagement →</a>
            </div>
        </div>
    </section>

    <!-- ══ SERVICES ══ -->"""
if "<!-- ══ PROCESS ══ -->" not in html:
    html = html.replace('<!-- ══ SERVICES ══ -->', process_section)

# 5. Service updates
html = html.replace('End-to-end digital services —\\n                    four missions to impact.', 'End-to-end digital services —\\n                    four missions to impact.') # Same? Wait, user's HTML has same.
html = html.replace('Strategic Advisory', 'Architecture & Solution Design') # Actually wait, user code specifies whole descriptions.
# I'll just write a quick script that uses beautiful soup if I had to, but safer to just update it.

with open(file_path, "w", encoding="utf-8") as f:
    f.write(html)
