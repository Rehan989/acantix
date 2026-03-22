import re

with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav = text[:nav_end]
footer_start = text.find('<!-- ══ CONTACT ══ -->')
footer_and_scripts = text[footer_start:]

case_studies_body = """
    <!-- TICKER -->
    <div class="bg-[#1a1a1a] py-1.5 mt-[60px] overflow-hidden">
        <div class="ticker-track flex whitespace-nowrap">
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> CLIENT SUCCESS <span class="text-white/15">◈</span> PROVEN RESULTS <span class="text-white/15">◈</span> IMPACT DELIVERED <span class="text-white/15">◈</span> TRANSFORMING INDUSTRIES <span class="text-white/15">◈</span> REAL PROJECTS</span>
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> CLIENT SUCCESS <span class="text-white/15">◈</span> PROVEN RESULTS <span class="text-white/15">◈</span> IMPACT DELIVERED <span class="text-white/15">◈</span> TRANSFORMING INDUSTRIES <span class="text-white/15">◈</span> REAL PROJECTS</span>
        </div>
    </div>
    
    <!-- ═══ CASE HERO ═══ -->
    <section class="py-24 md:py-32 bg-[#fafafa] text-center">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="inline-block font-mono text-[10px] text-[#6b6b6b] tracking-[.25em] uppercase mb-5">
                Client Success Stories
            </div>
            <h1 class="font-serif font-normal leading-[1.12] tracking-tight mb-5 text-[clamp(2.5rem,4vw,3.8rem)] text-[#1a1a1a]">
                Transforming <em class="bg-[#f5e642] px-1.5 italic font-normal">Industries</em>
            </h1>
            <p class="text-[#6b6b6b] text-[1.05rem] md:text-[1.1rem] max-w-[700px] mx-auto mb-10 leading-[1.85]">
                From startups to enterprises, we've partnered with organizations across industries to deliver measurable results through intelligent solutions. Real projects. Real impact. Real testimonials.
            </p>
            
            <div class="flex flex-wrap justify-center gap-10 md:gap-16 mt-12">
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">50+</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">PROJECTS DELIVERED</div>
                </div>
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">5</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">INDUSTRIES</div>
                </div>
                <div>
                    <div class="text-3xl md:text-4xl font-black text-[#1a1a1a] leading-none mb-2">100%</div>
                    <div class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em]">SUCCESS RATE</div>
                </div>
            </div>
        </div>
    </section>

    <hr class="border-[#e5e5e5]" />

    <!-- ═══ PORTFOLIO ═══ -->
    <section class="py-24 md:py-32 bg-white">
        <div class="max-w-[1280px] mx-auto px-7">
            <div class="text-center mb-16">
                <h2 class="font-serif font-bold text-[#1a1a1a] text-[clamp(2rem,3.5vw,3.2rem)] mb-8">Project Portfolio</h2>
                
                <div class="inline-flex flex-wrap justify-center gap-2 p-1.5 bg-[#fafafa] border border-[#e5e5e5] rounded-full shadow-sm">
                    <button class="bg-[#1a1a1a] text-white px-5 py-2 rounded-full text-sm font-semibold transition-all flex items-center gap-2 pointer-events-none hover:bg-[#1a1a1a]">All Projects <span class="bg-white/20 px-1.5 py-0.5 rounded text-[10px] font-mono leading-none">5</span></button>
                    <button class="hover:bg-[#f0f0f0] text-[#6b6b6b] hover:text-[#1a1a1a] px-5 py-2 rounded-full text-sm font-medium transition-all">Mobile Apps</button>
                    <button class="hover:bg-[#f0f0f0] text-[#6b6b6b] hover:text-[#1a1a1a] px-5 py-2 rounded-full text-sm font-medium transition-all">AI Bots</button>
                    <button class="hover:bg-[#f0f0f0] text-[#6b6b6b] hover:text-[#1a1a1a] px-5 py-2 rounded-full text-sm font-medium transition-all">Manufacturing</button>
                    <button class="hover:bg-[#f0f0f0] text-[#6b6b6b] hover:text-[#1a1a1a] px-5 py-2 rounded-full text-sm font-medium transition-all">Automation</button>
                </div>
            </div>
            
            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                
                <!-- Healthcare -->
                <div class="border border-[#e5e5e5] rounded-2xl bg-white overflow-hidden flex flex-col hover:border-[#bbb] hover:shadow-lg transition-all group">
                    <div class="h-[220px] bg-[#1a1a1a] flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#1a1a1a] to-[#333] opacity-80 group-hover:scale-105 transition-transform duration-700"></div>
                        <svg class="relative z-10 w-14 h-14 text-white/90" viewBox="0 0 24 24" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="currentColor" stroke-width="1.5"/><path d="M12 8v8M8 12h8" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <div class="flex flex-wrap justify-between items-center mb-5 gap-2">
                            <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em] font-bold uppercase">Healthcare</span>
                            <span class="bg-[#f0f0f0] text-[#1a1a1a] px-2.5 py-1 rounded text-[10px] font-bold uppercase tracking-wider">Mobile Apps</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3 leading-tight group-hover:text-[#22c55e] transition-colors">HealthTrack Mobile App</h3>
                        <p class="text-[#6b6b6b] leading-relaxed text-sm mb-6">Remote patient monitoring and medication adherence tracking for chronic disease management.</p>
                        
                        <div class="bg-[#fafafa] border border-[#e5e5e5] border-l-4 border-l-[#22c55e] p-4 rounded-lg mb-8">
                            <div class="font-black text-2xl text-[#1a1a1a] mb-0.5">85%</div>
                            <div class="text-xs text-[#6b6b6b] leading-relaxed">improvement in patient medication adherence</div>
                        </div>
                        
                        <div class="mt-auto">
                            <a href="#" class="inline-flex items-center gap-2 text-[#1a1a1a] font-bold text-sm group/link">View Full Case Study <svg class="w-4 h-4 group-hover/link:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Retail -->
                <div class="border border-[#e5e5e5] rounded-2xl bg-white overflow-hidden flex flex-col hover:border-[#bbb] hover:shadow-lg transition-all group">
                    <div class="h-[220px] bg-[#1a1a1a] flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#1a1a1a] to-[#333] opacity-80 group-hover:scale-105 transition-transform duration-700"></div>
                        <svg class="relative z-10 w-14 h-14 text-white/90" viewBox="0 0 24 24" fill="none"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="currentColor" stroke-width="1.5"/><path d="M12 22V12" stroke="currentColor" stroke-width="1.5"/><path d="M3.27 6.96L12 12l8.73-5.04" stroke="currentColor" stroke-width="1.5"/></svg>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <div class="flex flex-wrap justify-between items-center mb-5 gap-2">
                            <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em] font-bold uppercase">Retail & E-Commerce</span>
                            <span class="bg-[#f0f0f0] text-[#1a1a1a] px-2.5 py-1 rounded text-[10px] font-bold uppercase tracking-wider">AI Bots</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3 leading-tight group-hover:text-[#f5e642] transition-colors">RetailBot Assistant</h3>
                        <p class="text-[#6b6b6b] leading-relaxed text-sm mb-6">24/7 customer support automation and personalised product recommendations to increase sales conversion.</p>
                        
                        <div class="bg-[#fafafa] border border-[#e5e5e5] border-l-4 border-l-[#f5e642] p-4 rounded-lg mb-8">
                            <div class="font-black text-2xl text-[#1a1a1a] mb-0.5">300%</div>
                            <div class="text-xs text-[#6b6b6b] leading-relaxed">increase in customer engagement</div>
                        </div>
                        
                        <div class="mt-auto">
                            <a href="#" class="inline-flex items-center gap-2 text-[#1a1a1a] font-bold text-sm group/link">View Full Case Study <svg class="w-4 h-4 group-hover/link:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Manufacturing -->
                <div class="border border-[#e5e5e5] rounded-2xl bg-white overflow-hidden flex flex-col hover:border-[#bbb] hover:shadow-lg transition-all group">
                    <div class="h-[220px] bg-[#1a1a1a] flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#1a1a1a] to-[#333] opacity-80 group-hover:scale-105 transition-transform duration-700"></div>
                        <svg class="relative z-10 w-14 h-14 text-white/90" viewBox="0 0 24 24" fill="none"><path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <div class="flex flex-wrap justify-between items-center mb-5 gap-2">
                            <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em] font-bold uppercase">Manufacturing</span>
                            <span class="bg-[#f0f0f0] text-[#1a1a1a] px-2.5 py-1 rounded text-[10px] font-bold uppercase tracking-wider">Automation</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3 leading-tight group-hover:text-[#22c55e] transition-colors">SmartFactory Automation</h3>
                        <p class="text-[#6b6b6b] leading-relaxed text-sm mb-6">Streamline production workflows, reduce manual errors, and optimise equipment maintenance scheduling.</p>
                        
                        <div class="bg-[#fafafa] border border-[#e5e5e5] border-l-4 border-l-[#22c55e] p-4 rounded-lg mb-8">
                            <div class="font-black text-2xl text-[#1a1a1a] mb-0.5">50%</div>
                            <div class="text-xs text-[#6b6b6b] leading-relaxed">reduction in production downtime</div>
                        </div>
                        
                        <div class="mt-auto">
                            <a href="#" class="inline-flex items-center gap-2 text-[#1a1a1a] font-bold text-sm group/link">View Full Case Study <svg class="w-4 h-4 group-hover/link:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Financial Services -->
                <div class="border border-[#e5e5e5] rounded-2xl bg-white overflow-hidden flex flex-col hover:border-[#bbb] hover:shadow-lg transition-all group">
                    <div class="h-[220px] bg-[#1a1a1a] flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#1a1a1a] to-[#333] opacity-80 group-hover:scale-105 transition-transform duration-700"></div>
                        <svg class="relative z-10 w-14 h-14 text-white/90" viewBox="0 0 24 24" fill="none"><path d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round"/></svg>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <div class="flex flex-wrap justify-between items-center mb-5 gap-2">
                            <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em] font-bold uppercase">Financial Services</span>
                            <span class="bg-[#f0f0f0] text-[#1a1a1a] px-2.5 py-1 rounded text-[10px] font-bold uppercase tracking-wider">Mobile Apps</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3 leading-tight group-hover:text-[#f5e642] transition-colors">FinanceFlow Mobile Suite</h3>
                        <p class="text-[#6b6b6b] leading-relaxed text-sm mb-6">Modernize legacy banking systems with secure mobile banking and automated compliance reporting.</p>
                        
                        <div class="bg-[#fafafa] border border-[#e5e5e5] border-l-4 border-l-[#f5e642] p-4 rounded-lg mb-8">
                            <div class="font-black text-2xl text-[#1a1a1a] mb-0.5">90%</div>
                            <div class="text-xs text-[#6b6b6b] leading-relaxed">faster transaction processing</div>
                        </div>
                        
                        <div class="mt-auto">
                            <a href="#" class="inline-flex items-center gap-2 text-[#1a1a1a] font-bold text-sm group/link">View Full Case Study <svg class="w-4 h-4 group-hover/link:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Education -->
                <div class="border border-[#e5e5e5] rounded-2xl bg-white overflow-hidden flex flex-col hover:border-[#bbb] hover:shadow-lg transition-all group">
                    <div class="h-[220px] bg-[#1a1a1a] flex items-center justify-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#1a1a1a] to-[#333] opacity-80 group-hover:scale-105 transition-transform duration-700"></div>
                        <svg class="relative z-10 w-14 h-14 text-white/90" viewBox="0 0 24 24" fill="none"><path d="M12 14l9-5-9-5-9 5 9 5z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 14v7" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </div>
                    <div class="p-8 flex-1 flex flex-col">
                        <div class="flex flex-wrap justify-between items-center mb-5 gap-2">
                            <span class="font-mono text-[10px] text-[#6b6b6b] tracking-[.15em] font-bold uppercase">Education Technology</span>
                            <span class="bg-[#f0f0f0] text-[#1a1a1a] px-2.5 py-1 rounded text-[10px] font-bold uppercase tracking-wider">Automation</span>
                        </div>
                        <h3 class="text-xl font-bold text-[#1a1a1a] mb-3 leading-tight group-hover:text-[#22c55e] transition-colors">EduAdapt Learning Platform</h3>
                        <p class="text-[#6b6b6b] leading-relaxed text-sm mb-6">Personalised learning experiences that adapt to individual student progress and learning styles.</p>
                        
                        <div class="bg-[#fafafa] border border-[#e5e5e5] border-l-4 border-l-[#22c55e] p-4 rounded-lg mb-8">
                            <div class="font-black text-2xl text-[#1a1a1a] mb-0.5">70%</div>
                            <div class="text-xs text-[#6b6b6b] leading-relaxed">improvement in student engagement</div>
                        </div>
                        
                        <div class="mt-auto">
                            <a href="#" class="inline-flex items-center gap-2 text-[#1a1a1a] font-bold text-sm group/link">View Full Case Study <svg class="w-4 h-4 group-hover/link:translate-x-1 transition-transform" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

            </div>

             <div class="mt-20 p-12 bg-[#fafafa] border border-[#e5e5e5] rounded-3xl text-center shadow-sm relative overflow-hidden">
                <div class="absolute inset-0 border-[8px] border-white pointer-events-none rounded-3xl"></div>
                <h3 class="text-3xl font-bold mb-4 relative z-10 text-[#1a1a1a]">Ready to Join Our Success Stories?</h3>
                <p class="text-[#6b6b6b] max-w-[600px] mx-auto mb-8 relative z-10 leading-[1.7] text-lg">Whether you're looking to streamline operations, enhance customer experience, or drive innovation, we're here to transform your vision into measurable results.</p>
                <a href="index.html#contact" class="relative z-10 inline-flex px-8 py-3 rounded-full bg-[#1a1a1a] text-white text-sm font-bold hover:bg-[#333] transition-all hover:shadow-lg hover:-translate-y-1">Start Your Success Story</a>
            </div>
            
        </div>
    </section>
"""

with open(r'f:\acantix\case-studies.html', 'w', encoding='utf-8') as f:
    f.write(head_and_nav + case_studies_body + footer_and_scripts)

print("case-studies.html created successfully!")
