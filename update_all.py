import re

with open("f:/acantix/index.html", "r", encoding="utf-8") as f:
    text = f.read()


# 1. HEAD Replace
old_head_match = re.search(r'<title>.*?</title>.*?<link rel="canonical" href="https://acantix.com/" />\s*<link rel="stylesheet" href="dist/output.css">', text, re.DOTALL)
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
    text = text.replace(old_head, new_head)

# 2. Update Nav "Get Onboard" -> "Get Your AI Strategy Blueprint"
text = text.replace('Get\\n                Onboard →</a>', 'Get Your AI Strategy Blueprint →</a>')
text = text.replace('Get Onboard\\n            →</a>', 'Get Your AI Strategy Blueprint\\n            →</a>')
# Ensure single-line formats also match
text = text.replace('Get Onboard →</a>', 'Get Your AI Strategy Blueprint →</a>')

# 3. Mobile Nav (Get Onboard)
# Some might have specific spaces.
text = re.sub(r'>Get Onboard\s*→</a>', r'>Get Your AI Strategy Blueprint\n            →</a>', text)

# 4. Hero Text
old_hero = r"Your<br />Growth and Transformation<br /><em>Partner</em>"
new_hero = r"Build, modernise, and scale your systems <br />with AI<br /><em class=\"bg-[#f5e642] px-1.5 italic\">in weeks, not months</em>"
text = re.sub(old_hero, new_hero, text, flags=re.DOTALL)

old_hero_sub = "We build fast, scalable, secure solutions that help businesses grow, adapt, and stay ahead."
new_hero_sub = "Acantix helps businesses design, build, and scale AI-driven systems — faster, smarter, and with measurable impact."
text = text.replace(old_hero_sub, new_hero_sub)

text = re.sub(
    r'(<a href="#contact"[^>]*>)\s*Get Onboard\s*(<svg)',
    r'\1\nTalk to an Expert                    \2',
    text, flags=re.DOTALL
)

# 5. Insert PROCESS before SERVICES
process_html = """
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
            <!-- Steps: 2 cols on mobile, 4 on desktop -->
            <div class="grid grid-cols-2 md:grid-cols-4 gap-8 relative">
                <!-- Connecting line — desktop only -->
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
            <!-- Callout -->
            <div class="mt-12 border border-[#e5e5e5] rounded-2xl bg-[#fafafa] p-6 md:p-8 flex flex-col md:flex-row items-start md:items-center gap-5 hover:border-[#bbb] hover:shadow-lg transition-all">
                <p class="text-sm text-[#1a1a1a] leading-[1.75] flex-1"><strong>Our four capabilities function as a unified model combining </strong> strategy, guidance, design, and delivery to drive real outcomes.We deploy elite teams to solve complex challenges across fast-changing, high-stakes industries.</p>
                <a href="#contact" class="flex-shrink-0 bg-[#1a1a1a] text-white px-6 py-3 rounded-full text-sm font-bold hover:shadow-lg hover:-translate-y-1 transition-all whitespace-nowrap w-full md:w-auto text-center">Start Your Engagement →</a>
            </div>
        </div>
    </section>

    <!-- ══ SERVICES ══ -->
"""
if "<!-- ══ PROCESS ══ -->" not in text:
    text = text.replace('<!-- ══ SERVICES ══ -->', process_html.strip())


# 6. SERVICES Section Text Replacements
text = text.replace(
    'End-to-end digital services —\n                    four missions to impact.',
    'End-to-end digital services —\n                    four missions to impact.'
)

# Replace ADVISORY with Solutioning for the second service (Architecture & Solution Design)
old_advisory_head = r'<div class="font-mono text-\[9px\] tracking-\[\.22em\] text-white/50 mb-0\.5">ADVISORY</div>\s*<div class="text-white font-bold text-base">Strategic Advisory</div>'
new_advisory_head = r'<div class="font-mono text-[9px] tracking-[.22em] text-white/50 mb-0.5">Solutioning</div>\n                            <div class="text-white font-bold text-base">Architecture & Solution Design</div>'
text = re.sub(old_advisory_head, new_advisory_head, text)

text = text.replace(
    'Expert guidance on enterprise architecture, cloud strategy, and agile scaling. We help CTOs navigate complex technical decisions with clarity and confidence.',
    'Translate strategy into scalable, future-ready systems.\n\nWe design the right architecture, technology stack, and execution approach to ensure your solution is built to scale.'
)

# Engineering section update
text = text.replace(
    'Full-cycle software engineering — from\n                            product design and backend architecture to cloud infrastructure and delivery.',
    'Build robust, scalable applications from idea to production.\n\nWe develop mobile, web, and SaaS platforms with speed, quality, and long-term scalability in mind..'
)

old_engineering_head = r'<div class="font-mono text-\[9px\] tracking-\[\.22em\] text-white/50 mb-0\.5">ENGINEERING</div>\s*<div class="text-white font-bold text-base">Software Engineering</div>'
new_engineering_head = r'<div class="font-mono text-[9px] tracking-[.22em] text-white/50 mb-0.5">SOFTWARE ENGINEERING</div>\n                            <div class="text-white font-bold text-base">Product & Platform Engineering</div>'
text = re.sub(old_engineering_head, new_engineering_head, text)

# Solutioning -> AI and Digital Transformation
old_solutioning_head = r'<div class="font-mono text-\[9px\] tracking-\[\.22em\] text-white/50 mb-0\.5">SOLUTIONING</div>\s*<div class="text-white font-bold text-base">End-to-End Solutioning</div>'
new_solutioning_head = r'<div class="font-mono text-[9px] tracking-[.22em] text-white/50 mb-0.5">AI and Digital Transformation</div>\n                            <div class="text-white font-bold text-base">AI & Automation Systems</div>'
text = re.sub(old_solutioning_head, new_solutioning_head, text)

text = text.replace(
    'Bespoke solutions combining consulting\n                            intelligence with engineering execution — we own the entire solution lifecycle.',
    'Deploy AI systems that drive efficiency and intelligence.\n\nFrom automation to predictive analytics, we build AI-powered solutions that reduce costs and improve decision-making.'
)


# 7. CONTACT update
text = text.replace("OPEN\n                    CHANNEL", "Strategy, \nMeet Execution. Execution Meets Value")
text = text.replace("OPEN CHANNEL", "Strategy, Meet Execution. Execution Meets Value")
text = text.replace(
    "Fill out your details and we'll get you to your destination.",
    "Whether you have a project or a partnership in mind. \nLet’s connect and we’re here to answer any questions your team may have. \n\n"
)

# 8. FOOTER update
text = text.replace(
    "Better strategy, better engineering, done right. Guiding\n                    enterprises to their true north.",
    "Acantix helps businesses design, build, and scale AI-driven systems faster, smarter, and with measurable impact. Guiding\n                    enterprises to their true north."
)

# 9. JSON LD Scripts
jsonLD = """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Acantix",
  "url": "https://acantix.com",
  "logo": "https://acantix.com/icon.svg",
  "description": "Acantix provides AI consulting, software engineering, and digital transformation solutions.",
  "sameAs": [
    "https://www.linkedin.com/company/acantix"
  ]
}
</script>
    <script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Service",
  "serviceType": "AI Consulting and Software Development",
  "provider": {
    "@type": "Organization",
    "name": "Acantix"
  },
  "areaServed": "Global",
  "description": "AI system development, application modernization, consulting, and engineering services."
}
</script>
</body>"""
if "application/ld+json" not in text:
    text = text.replace("</body>", jsonLD)


with open("f:/acantix/index.html", "w", encoding="utf-8") as f:
    f.write(text)

print("Updates applied to index.html successfully.")
