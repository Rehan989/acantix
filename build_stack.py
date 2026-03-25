import os
import glob

# Generate stack.html
with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav_base = text[:nav_end]
head_and_nav = head_and_nav_base.replace('href="dist/', 'href="/dist/').replace('src="icon.svg"', 'src="/icon.svg"').replace('href="case-studies.html"', 'href="/case-studies.html"').replace('href="careers.html"', 'href="/careers.html"').replace('href="#', 'href="/#')
head_and_nav = head_and_nav.replace('href="/icon.svg"', 'href="/icon.svg"')
head_and_nav = head_and_nav.replace('href="#', 'href="/#')

footer_start = text.find('<!-- ══ CONTACT ══ -->')
footer_and_scripts_base = text[footer_start:]
footer_and_scripts = footer_and_scripts_base.replace('src="icon.svg"', 'src="/icon.svg"').replace('href="case-studies.html"', 'href="/case-studies.html"').replace('href="careers.html"', 'href="/careers.html"').replace('href="#', 'href="/#')

stack_content = f'''
    <!-- TICKER -->
    <div class="bg-[#1a1a1a] py-1.5 mt-[60px] overflow-hidden">
        <div class="ticker-track flex whitespace-nowrap">
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white font-bold"><span class="text-white/15">◈</span> OUR FOUNDATION <span class="text-white/15">◈</span> ACANTIX STACK <span class="text-white/15">◈</span> THE DNA OF INTELLIGENT TRANSFORMATION</span>
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white font-bold"><span class="text-white/15">◈</span> OUR FOUNDATION <span class="text-white/15">◈</span> ACANTIX STACK <span class="text-white/15">◈</span> THE DNA OF INTELLIGENT TRANSFORMATION</span>
        </div>
    </div>
    
    <!-- ═══ STACK HERO ═══ -->
    <section class="py-24 md:py-32 bg-[#fafafa] text-center border-b border-[#e5e5e5]">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="inline-block font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-5">
                Our Foundation
            </div>
            <h1 class="font-serif font-normal leading-[1.12] tracking-tight mb-5 text-[clamp(2.5rem,4vw,3.8rem)] text-[#1a1a1a]">
                Acantix <em class="bg-[#f5e642] px-1.5 italic font-normal">Stack</em>
            </h1>
            <p class="text-[#6b6b6b] text-[1.05rem] md:text-[1.1rem] max-w-[700px] mx-auto mb-10 leading-[1.85]">
                More than technology. More than process. A complete foundation for building systems that think. The DNA of intelligent transformation.
            </p>
            
            <div class="flex flex-wrap justify-center gap-10 md:gap-16 mt-12">
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">3</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">CORE LAYERS</div>
                </div>
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">∞</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">POSSIBILITIES</div>
                </div>
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">1</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">FOUNDATION</div>
                </div>
            </div>
        </div>
    </section>

    <!-- ═══ THE COMPLETE FOUNDATION ═══ -->
    <section class="py-24 bg-white border-b border-[#e5e5e5] relative overflow-hidden">
        <div class="max-w-[900px] mx-auto px-7 relative z-10 text-center">
            <h2 class="font-serif text-[clamp(2rem,3.5vw,3.2rem)] font-bold text-[#1a1a1a] mb-6">The Complete Foundation</h2>
            <p class="text-[#6b6b6b] text-lg leading-relaxed mb-6">
                At Acantix, we don't just build products. We go by strong values, principles that build systems that think. Behind every system, there is a foundation of a stack that makes it all possible.
            </p>
            <p class="text-[#6b6b6b] text-lg leading-relaxed mb-6 font-bold text-[#1a1a1a]">
                Our stack isn't just technical. It's the complete DNA of how we think, work, and deliver impact.
            </p>
            <p class="text-[#6b6b6b] text-lg leading-relaxed">
                The Acantix Stack is built on three interconnected layers: <strong>Purpose</strong> (why we exist), <strong>Strategy</strong> (how we deliver), and <strong>Culture</strong> (the values that drive us). Together, they form the foundation for everything we create.
            </p>
        </div>
        
        <!-- Decoration -->
        <div class="absolute right-[-100px] top-1/2 -translate-y-1/2 opacity-[0.03] pointer-events-none">
            <svg width="400" height="400" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="0.5"><path d="M12 2L2 7l10 5 10-5-10-5zM2 17l10 5 10-5M2 12l10 5 10-5" stroke-linejoin="round" stroke-linecap="round"/></svg>
        </div>
    </section>

    <!-- ═══ CORE PRINCIPLES ═══ -->
    <section class="py-24 bg-[#fafafa]">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="text-center mb-16">
                <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-4 block">Acantix Way</span>
                <h2 class="font-serif text-[clamp(2rem,3.5vw,3.2rem)] font-bold text-[#1a1a1a]">Core Principles</h2>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Principle 1 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-[#1a1a1a] transition-all group">
                    <div class="w-12 h-12 bg-[#fafafa] border border-[#e5e5e5] rounded-xl flex items-center justify-center mb-6 group-hover:bg-[#f5e642] group-hover:border-[#f5e642] transition-colors">
                        <svg class="w-6 h-6 text-[#1a1a1a]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M19 21V5a2 2 0 00-2-2H7a2 2 0 00-2 2v16m14 0h2m-2 0h-5m-9 0H3m2 0h5M9 7h1m-1 4h1m4-4h1m-1 4h1m-5 10v-5a1 1 0 011-1h2a1 1 0 011 1v5m-4 0h4"/></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">Foundation First</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">A solid foundation is not just the start—it's the strength that carries growth long term.</p>
                </div>
                
                <!-- Principle 2 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-[#1a1a1a] transition-all group">
                    <div class="w-12 h-12 bg-[#fafafa] border border-[#e5e5e5] rounded-xl flex items-center justify-center mb-6 group-hover:bg-[#22c55e] group-hover:border-[#22c55e] transition-colors">
                        <svg class="w-6 h-6 text-[#1a1a1a]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">Efficiencies Next</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">Once the foundation is set, efficiency becomes the driver that accelerates progress and performance.</p>
                </div>
                
                <!-- Principle 3 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-[#1a1a1a] transition-all group">
                    <div class="w-12 h-12 bg-[#fafafa] border border-[#e5e5e5] rounded-xl flex items-center justify-center mb-6 group-hover:bg-[#1a1a1a] group-hover:border-[#1a1a1a] transition-colors">
                        <svg class="w-6 h-6 text-[#1a1a1a] group-hover:text-white transition-colors" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z"/></svg>
                    </div>
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">Innovation Always</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">Innovation is woven into our culture, driving us to reimagine possibilities and shape the future.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ═══ THE STACK LAYERS ═══ -->
    <section class="py-24 bg-white border-y border-[#e5e5e5]">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="text-center mb-16 max-w-[800px] mx-auto">
                <h2 class="font-serif text-[clamp(2rem,3.5vw,3.2rem)] font-bold text-[#1a1a1a] mb-6">The Stack Layers</h2>
                <p class="text-[#6b6b6b] text-lg leading-relaxed">
                    Each layer of our stack serves a specific function, but they work together as an integrated whole. Purpose defines our direction, Strategy guides our execution, and Culture ensures we stay true to our values as we scale.
                </p>
            </div>
            
            <div class="space-y-6 max-w-[900px] mx-auto">
                
                <!-- Purpose -->
                <div class="border border-[#e5e5e5] rounded-3xl p-8 md:p-12 relative overflow-hidden flex flex-col md:flex-row gap-8 items-start hover:shadow-lg transition-all group bg-[#fafafa]">
                    <div class="absolute -right-10 -top-10 opacity-5 group-hover:opacity-10 transition-opacity">
                        <div class="text-[180px] font-serif font-black leading-none">P</div>
                    </div>
                    <div class="shrink-0 w-16 h-16 rounded-2xl bg-white border border-[#e5e5e5] flex items-center justify-center group-hover:-translate-y-1 transition-transform">
                        <svg class="w-8 h-8 text-[#1a1a1a]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M5 3v4M3 5h4M6 17v4m-2-2h4m5-16l2.286 6.857L21 12l-5.714 2.143L13 21l-2.286-6.857L5 12l5.714-2.143L13 3z"/></svg>
                    </div>
                    <div class="flex-1 relative z-10 w-full">
                        <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] mb-2 uppercase">Why & What For We Exist</div>
                        <h3 class="text-2xl md:text-3xl font-bold text-[#1a1a1a] mb-6 font-serif">Purpose Stack</h3>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-2 gap-6">
                            <div>
                                <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2">Vision</h4>
                                <p class="text-[#6b6b6b] text-sm leading-relaxed">A world where every decision enriches human experience.</p>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2">Mission</h4>
                                <p class="text-[#6b6b6b] text-sm leading-relaxed">Empower businesses to transform data into decisive intelligence.</p>
                            </div>
                        </div>
                        <div class="mt-6 pt-6 border-t border-[#e5e5e5]">
                            <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2">Brand Promise</h4>
                            <p class="text-[#1a1a1a] font-serif italic text-lg text-[#f5e642] group-hover:text-[#1a1a1a] transition-all"><span class="bg-[#1a1a1a] text-white group-hover:bg-[#f5e642] px-2 py-0.5 rounded">Data to Decisions — Intelligently.</span></p>
                        </div>
                    </div>
                </div>

                <!-- Strategy -->
                <div class="border border-[#e5e5e5] rounded-3xl p-8 md:p-12 relative overflow-hidden flex flex-col md:flex-row gap-8 items-start hover:shadow-lg transition-all group bg-[#fafafa]">
                    <div class="absolute -right-10 -top-10 opacity-5 group-hover:opacity-10 transition-opacity">
                        <div class="text-[180px] font-serif font-black leading-none">S</div>
                    </div>
                    <div class="shrink-0 w-16 h-16 rounded-2xl bg-white border border-[#e5e5e5] flex items-center justify-center group-hover:-translate-y-1 transition-transform">
                        <svg class="w-8 h-8 text-[#1a1a1a]" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z"/></svg>
                    </div>
                    <div class="flex-1 relative z-10 w-full">
                        <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] mb-2 uppercase">How We Deliver Results</div>
                        <h3 class="text-2xl md:text-3xl font-bold text-[#1a1a1a] mb-6 font-serif">Strategy Stack</h3>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
                            <div>
                                <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2 text-[#22c55e]">People</h4>
                                <p class="text-[#6b6b6b] text-sm leading-relaxed font-mono tracking-tight">Visionaries<br>Leaders<br>Executors</p>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2 text-[#22c55e]">Process</h4>
                                <p class="text-[#6b6b6b] text-sm leading-relaxed font-mono tracking-tight">Repeatable<br>Reliable<br>Measurable</p>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-2 text-[#22c55e]">Technology</h4>
                                <p class="text-[#6b6b6b] text-sm leading-relaxed font-mono tracking-tight">Future-Ready<br>Innovative</p>
                            </div>
                        </div>
                    </div>
                </div>

                <!-- Culture -->
                <div class="border border-[#e5e5e5] rounded-3xl p-8 md:p-12 relative overflow-hidden flex flex-col md:flex-row gap-8 items-start hover:shadow-lg transition-all group bg-[#1a1a1a]">
                    <div class="absolute -right-10 -top-10 opacity-5 group-hover:opacity-[0.08] transition-opacity">
                        <div class="text-[180px] font-serif font-black leading-none text-white">C</div>
                    </div>
                    <div class="shrink-0 w-16 h-16 rounded-2xl bg-white/10 border border-white/10 flex items-center justify-center group-hover:-translate-y-1 transition-transform">
                        <svg class="w-8 h-8 text-white" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="1.5" d="M14 10h4.764a2 2 0 011.789 2.894l-3.5 7A2 2 0 0115.263 21h-4.017c-.163 0-.326-.02-.485-.06L7 20m7-10V5a2 2 0 00-2-2h-.095c-.5 0-.905.405-.905.905 0 .714-.211 1.412-.608 2.006L7 11v9m7-10h-2M7 20H5a2 2 0 01-2-2v-6a2 2 0 012-2h2.5"/></svg>
                    </div>
                    <div class="flex-1 relative z-10 w-full">
                        <div class="font-mono text-[10px] text-white/50 tracking-[.25em] mb-2 uppercase">Values That Drive Us</div>
                        <h3 class="text-2xl md:text-3xl font-bold text-white mb-6 font-serif">Culture Stack</h3>
                        
                        <div class="grid grid-cols-1 sm:grid-cols-3 gap-6">
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-2">Mindset First</h4>
                                <p class="text-white/60 text-sm leading-relaxed">Well-Being · Merit that wins</p>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-2">Integrity Always</h4>
                                <p class="text-white/60 text-sm leading-relaxed">Transparent and Explainable</p>
                            </div>
                            <div>
                                <h4 class="text-sm font-bold text-white uppercase tracking-wider mb-2">Impact Forever</h4>
                                <p class="text-white/60 text-sm leading-relaxed">Being a change agent</p>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        </div>
    </section>

    <!-- ═══ HOW WE APPLY ═══ -->
    <section class="py-24 bg-[#fafafa]">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="text-center mb-16 max-w-[800px] mx-auto">
                <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-4 block">Stack in Action</span>
                <h2 class="font-serif text-[clamp(2rem,3.5vw,3.2rem)] font-bold text-[#1a1a1a] mb-6">How We Apply Our Stack</h2>
                <p class="text-[#6b6b6b] text-lg leading-relaxed">
                    The Acantix Stack isn't just theory—it's how we operate every day. From product decisions to team dynamics, every aspect of our work is guided by these three foundational layers.
                </p>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-3 gap-8">
                <!-- Apply 1 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-black transition-all">
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">In Product Development</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">Every feature aligns with our mission to transform data into decisive intelligence.</p>
                </div>
                
                <!-- Apply 2 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-black transition-all">
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">In Team Collaboration</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">Cross-functional teams work with shared processes and clear accountability.</p>
                </div>
                
                <!-- Apply 3 -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl hover:border-black transition-all">
                    <h3 class="text-xl font-bold text-[#1a1a1a] mb-4">In Client Relationships</h3>
                    <p class="text-[#6b6b6b] leading-relaxed">Integrity and transparency guide every interaction and delivery.</p>
                </div>
            </div>
        </div>
    </section>

    <!-- ═══ CALL TO ACTION ═══ -->
    <section class="py-24 bg-white border-y border-[#e5e5e5] text-center px-7 relative overflow-hidden">
        <div class="absolute inset-0 bg-gradient-to-b from-white to-[#fafafa] -z-10"></div>
        <div class="max-w-[700px] mx-auto">
            <h2 class="font-serif font-bold text-4xl text-[#1a1a1a] mb-6">Ready to Build on Our Stack?</h2>
            <p class="text-xl text-[#6b6b6b] leading-relaxed mb-10">Whether you're looking to join our team or partner with us on your next intelligent system, our stack provides the foundation for exceptional outcomes.</p>
            <div class="flex flex-wrap justify-center gap-4">
                <a href="/careers.html" class="inline-flex px-8 py-4 rounded-full bg-white border border-[#1a1a1a] text-[#1a1a1a] font-bold hover:bg-[#fafafa] transition-all hover:shadow-sm text-sm">Explore Careers</a>
                <a href="/index.html#contact" class="inline-flex px-8 py-4 rounded-full bg-[#1a1a1a] border border-[#1a1a1a] text-white font-bold hover:bg-[#333] transition-all hover:shadow-lg hover:-translate-y-1 text-sm">Start a Project</a>
            </div>
        </div>
    </section>
'''

with open(r'f:\acantix\stack.html', 'w', encoding='utf-8') as f:
    f.write(head_and_nav + stack_content + footer_and_scripts)

# Next: Patch all navbars across HTML files
for file_path in glob.glob(r'f:\acantix\**\*.html', recursive=True):
    # Ignore node_modules, chatbot
    if 'node_modules' in file_path or 'chatbot' in file_path:
        continue
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Nav
    patched = content.replace(
        '<a href="case-studies.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Case Studies</a>',
        '<a href="/stack.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Stack</a>\n            <a href="case-studies.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Case Studies</a>'
    )
    patched = patched.replace(
        '<a href="/case-studies.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Case Studies</a>',
        '<a href="/stack.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Stack</a>\n            <a href="/case-studies.html"\n                class="text-[#6b6b6b] text-sm font-medium hover:text-[#1a1a1a] transition-colors">Case Studies</a>'
    )

    # Footer Nav (Company)
    patched = patched.replace(
        '<li><a href="case-studies.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Case Studies</a>',
        '<li><a href="/stack.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Stack</a>\n                    </li>\n                    <li><a href="case-studies.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Case Studies</a>'
    )
    patched = patched.replace(
        '<li><a href="/case-studies.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Case Studies</a>',
        '<li><a href="/stack.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Stack</a>\n                    </li>\n                    <li><a href="/case-studies.html"\n                            class="text-[#6b6b6b] text-sm hover:text-[#1a1a1a] transition-colors no-underline">Case Studies</a>'
    )

    if patched != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(patched)

print('Done')
