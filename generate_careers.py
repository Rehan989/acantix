import re

with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav = text[:nav_end]
footer_start = text.find('<!-- ══ CONTACT ══ -->')
footer_and_scripts = text[footer_start:]

careers_body = """
    <!-- TICKER -->
    <div class="bg-[#1a1a1a] py-1.5 mt-[60px] overflow-hidden">
        <div class="ticker-track flex whitespace-nowrap">
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> NOW HIRING <span class="text-white/15">◈</span> DEEP WORK FIRST <span class="text-white/15">◈</span> JOIN ACANTIX <span class="text-white/15">◈</span> SHAPE AGENTIC AI <span class="text-white/15">◈</span> SYSTEMS NOT SILOS</span>
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> NOW HIRING <span class="text-white/15">◈</span> DEEP WORK FIRST <span class="text-white/15">◈</span> JOIN ACANTIX <span class="text-white/15">◈</span> SHAPE AGENTIC AI <span class="text-white/15">◈</span> SYSTEMS NOT SILOS</span>
        </div>
    </div>
    
    <!-- ═══ CAREERS HERO ═══ -->
    <section class="py-24 md:py-32 bg-[#fafafa] text-center">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="inline-block font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-5">
                Join Acantix
            </div>
            <h1 class="font-serif font-normal leading-[1.12] tracking-tight mb-5 text-[clamp(2.5rem,4vw,3.8rem)] text-[#1a1a1a]">
                We don't just hire.<br/> Careers aren't jobs —<br/>
                <em class="bg-[#f5e642] px-1.5 italic font-normal">they're journeys of building impact.</em>
            </h1>
            <p class="text-[#6b6b6b] text-[1.05rem] md:text-[1.1rem] max-w-[700px] mx-auto mb-10 leading-[1.85]">
                At Acantix, we create technologies that think, adapt, and scale. Our products aren't just smart, 
                they're agentic, autonomous and purpose-built for real-world impact. We're building a company for 
                deep thinkers, restless builders and clear communicators.
            </p>
        </div>
    </section>

    <hr class="border-[#e5e5e5]" />

    <!-- ═══ CULTURE & VALUES ═══ -->
    <section class="py-24 md:py-32 bg-white">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="text-center mb-16">
                <h2 class="font-serif font-bold text-[#1a1a1a] text-[clamp(2rem,3.5vw,3.2rem)] leading-tight">It's not about the tools.<br/><span class="text-[#6b6b6b] font-normal italic px-1.5">It's about the people behind them.</span></h2>
                <p class="text-[#1a1a1a] mt-5 font-medium">We don't run job ads, We don't chase resume</p>
            </div>
            <div class="grid grid-cols-1 md:grid-cols-2 gap-8">
                <div class="border border-[#e5e5e5] rounded-xl p-8 bg-[#fafafa] shadow-sm hover:shadow-md hover:border-[#bbb] transition-all">
                    <h3 class="text-xl font-bold mb-3 text-[#1a1a1a]">Deep Work First</h3>
                    <p class="text-[#6b6b6b] leading-[1.7] text-sm md:text-base">We respect focus, async thinking, and flow. Our work patterns are designed for clarity and momentum—not noise.</p>
                </div>
                <div class="border border-[#e5e5e5] rounded-xl p-8 bg-[#fafafa] shadow-sm hover:shadow-md hover:border-[#bbb] transition-all">
                    <h3 class="text-xl font-bold mb-3 text-[#1a1a1a]">Growth Without Permission</h3>
                    <p class="text-[#6b6b6b] leading-[1.7] text-sm md:text-base">You don't need a promotion to explore. Team members self-initiate projects, experiments, and ideas. We help shape them into product-grade realities.</p>
                </div>
                <div class="border border-[#e5e5e5] rounded-xl p-8 bg-[#fafafa] shadow-sm hover:shadow-md hover:border-[#bbb] transition-all">
                    <h3 class="text-xl font-bold mb-3 text-[#1a1a1a]">Systems, Not Silos</h3>
                    <p class="text-[#6b6b6b] leading-[1.7] text-sm md:text-base">Engineering works closely with design, product, data, and research. We're small enough to move fast and smart enough to stay aligned.</p>
                </div>
                <div class="border border-[#e5e5e5] rounded-xl p-8 bg-[#fafafa] shadow-sm hover:shadow-md hover:border-[#bbb] transition-all">
                    <h3 class="text-xl font-bold mb-3 text-[#1a1a1a]">Merit wins Culture</h3>
                    <p class="text-[#6b6b6b] leading-[1.7] text-sm md:text-base">Its not about democracy, its Meritocracy. We're hiring for passion not for roles.</p>
                </div>
            </div>
        </div>
    </section>

    <hr class="border-[#e5e5e5]" />

    <!-- ═══ OPEN ROLES ═══ -->
    <section class="py-24 md:py-32 bg-[#fafafa]">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="mb-14">
                <h2 class="font-serif font-bold text-[#1a1a1a] text-[clamp(2rem,3.5vw,3.2rem)]">Open Positions</h2>
            </div>
            <div class="flex flex-col gap-5">
                <!-- AI Engineer -->
                <div class="border border-[#e5e5e5] rounded-xl bg-white flex flex-col md:flex-row items-start md:items-center p-8 justify-between hover:border-[#bbb] hover:shadow-sm transition-all gap-6">
                    <div class="flex items-start md:items-center gap-6">
                        <div class="text-[#888] font-mono text-xl font-bold mt-1 md:mt-0">01</div>
                        <div>
                            <h3 class="text-xl font-bold text-[#1a1a1a] mb-2">AI Engineer</h3>
                            <p class="text-[#6b6b6b] max-w-[600px] leading-relaxed text-sm md:text-base">Build and deploy agentic systems for real-time decisions. Work with LLMs, edge-AI, and domain-specific models.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="shrink-0 px-6 py-3 rounded-full border-[1.5px] border-[#1a1a1a] text-sm font-semibold hover:bg-[#1a1a1a] hover:text-white transition-all">Apply Now</a>
                </div>
                
                <!-- Product Designer -->
                <div class="border border-[#e5e5e5] rounded-xl bg-white flex flex-col md:flex-row items-start md:items-center p-8 justify-between hover:border-[#bbb] hover:shadow-sm transition-all gap-6">
                    <div class="flex items-start md:items-center gap-6">
                        <div class="text-[#888] font-mono text-xl font-bold mt-1 md:mt-0">02</div>
                        <div>
                            <h3 class="text-xl font-bold text-[#1a1a1a] mb-2">Product Designer</h3>
                            <p class="text-[#6b6b6b] max-w-[600px] leading-relaxed text-sm md:text-base">Shape the feel and function of agent-first tools. Experience in motion, systems thinking, and data UI is a plus.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="shrink-0 px-6 py-3 rounded-full border-[1.5px] border-[#1a1a1a] text-sm font-semibold hover:bg-[#1a1a1a] hover:text-white transition-all">Apply Now</a>
                </div>

                <!-- Platform Engineer -->
                <div class="border border-[#e5e5e5] rounded-xl bg-white flex flex-col md:flex-row items-start md:items-center p-8 justify-between hover:border-[#bbb] hover:shadow-sm transition-all gap-6">
                    <div class="flex items-start md:items-center gap-6">
                        <div class="text-[#888] font-mono text-xl font-bold mt-1 md:mt-0">03</div>
                        <div>
                            <h3 class="text-xl font-bold text-[#1a1a1a] mb-2">Platform Engineer</h3>
                            <p class="text-[#6b6b6b] max-w-[600px] leading-relaxed text-sm md:text-base">Help us scale safely. Secure, observable, resilient infrastructure is your craft.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="shrink-0 px-6 py-3 rounded-full border-[1.5px] border-[#1a1a1a] text-sm font-semibold hover:bg-[#1a1a1a] hover:text-white transition-all">Apply Now</a>
                </div>
            </div>
            
            <div class="mt-16 p-10 bg-[#1a1a1a] rounded-2xl text-center text-white shadow-xl relative overflow-hidden">
                <div class="absolute inset-0 opacity-[0.05] pointer-events-none">
                    <svg viewBox="0 0 100 100" preserveAspectRatio="none" class="w-full h-full"><line x1="0" y1="50" x2="100" y2="50" stroke="#fff" stroke-width="0.5"/><line x1="50" y1="0" x2="50" y2="100" stroke="#fff" stroke-width="0.5"/><circle cx="50" cy="50" r="30" fill="none" stroke="#fff" stroke-width="0.5"/><circle cx="50" cy="50" r="45" fill="none" stroke="#fff" stroke-width="0.5"/></svg>
                </div>
                <h3 class="text-2xl font-bold mb-4 relative z-10">Don't see a perfect fit?</h3>
                <p class="text-white/70 max-w-[500px] mx-auto mb-8 relative z-10">Tell us what excites you and where you want to make an impact.</p>
                <a href="mailto:join@acantix.com" class="relative z-10 inline-flex px-8 py-3 rounded-full bg-white text-[#1a1a1a] text-sm font-bold hover:bg-[#f5e642] transition-colors shadow-sm">join@Acantix.com</a>
            </div>
        </div>
    </section>
"""

with open(r'f:\acantix\careers.html', 'w', encoding='utf-8') as f:
    f.write(head_and_nav + careers_body + footer_and_scripts)

print("careers.html created successfully!")
