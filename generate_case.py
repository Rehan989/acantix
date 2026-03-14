import re

with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav = text[:nav_end]
footer_start = text.find('<footer>')
footer_and_scripts = text[footer_start:]

case_studies_body = """
    <!-- TICKER -->
    <div style="margin-top:68px;" class="ticker-wrap">
        <div class="ticker-track">
            <span>◈ CLIENT SUCCESS</span><span>◈ PROVEN RESULTS</span><span>◈ IMPACT DELIVERED</span><span>◈ TRANSFORMING INDUSTRIES</span><span>◈ REAL PROJECTS</span>
            <span>◈ CLIENT SUCCESS</span><span>◈ PROVEN RESULTS</span><span>◈ IMPACT DELIVERED</span><span>◈ TRANSFORMING INDUSTRIES</span><span>◈ REAL PROJECTS</span>
        </div>
    </div>
    
    <!-- ═══ CASE HERO ═══ -->
    <section style="padding:120px 0 60px;background:#fff;text-align:center;">
        <div style="max-width:1280px;margin:0 auto;padding:0 28px;">
            <div class="tag tag-sky" style="margin-bottom:22px;">
                Client Success Stories
            </div>
            <h1 style="font-size:clamp(2.5rem,4vw,3.8rem);font-weight:800;color:var(--ink2);margin-bottom:20px;">
                Transforming <em class="serif shimmer-text" style="font-style:italic;font-weight:400;">Industries</em>
            </h1>
            <p style="font-size:1.1rem;color:var(--muted);max-width:700px;margin:0 auto 40px;line-height:1.8;">
                From startups to enterprises, we've partnered with organizations across industries to deliver measurable results through intelligent solutions. Real projects. Real impact. Real testimonials.
            </p>
            
            <div style="display:flex;justify-content:center;gap:40px;margin-top:40px;">
                <div>
                    <div style="font-size:2rem;font-weight:800;color:var(--sky);">50+</div>
                    <div class="mono" style="font-size:0.6rem;color:var(--muted);letter-spacing:0.1em;">PROJECTS DELIVERED</div>
                </div>
                <div>
                    <div style="font-size:2rem;font-weight:800;color:var(--sky);">5</div>
                    <div class="mono" style="font-size:0.6rem;color:var(--muted);letter-spacing:0.1em;">INDUSTRIES</div>
                </div>
                <div>
                    <div style="font-size:2rem;font-weight:800;color:var(--sky);">100%</div>
                    <div class="mono" style="font-size:0.6rem;color:var(--muted);letter-spacing:0.1em;">SUCCESS RATE</div>
                </div>
            </div>
        </div>
    </section>

    <hr class="div" />

    <!-- ═══ PORTFOLIO ═══ -->
    <section style="padding:100px 0;background:var(--bg);">
        <div style="max-width:1280px;margin:0 auto;padding:0 28px;">
            <div style="text-align:center;margin-bottom:60px;">
                <h2 style="font-size:2.4rem;font-weight:800;color:var(--ink2);margin-bottom:30px;">Project Portfolio</h2>
                
                <div style="display:inline-flex;background:#fff;padding:8px;border-radius:50px;box-shadow:0 4px 12px rgba(0,0,0,0.05);flex-wrap:wrap;justify-content:center;gap:10px;">
                    <button class="btn" style="background:var(--ink2);color:#fff;padding:8px 20px;font-size:0.85rem;">All Projects <span style="background:rgba(255,255,255,0.2);padding:2px 6px;border-radius:10px;font-size:0.7rem;margin-left:6px;">5</span></button>
                    <button class="btn" style="background:transparent;color:var(--muted);padding:8px 20px;font-size:0.85rem;">Mobile Apps</button>
                    <button class="btn" style="background:transparent;color:var(--muted);padding:8px 20px;font-size:0.85rem;">AI Bots</button>
                    <button class="btn" style="background:transparent;color:var(--muted);padding:8px 20px;font-size:0.85rem;">Manufacturing</button>
                    <button class="btn" style="background:transparent;color:var(--muted);padding:8px 20px;font-size:0.85rem;">Automation</button>
                </div>
            </div>
            
            <div style="display:grid;grid-template-columns:repeat(auto-fill, minmax(380px, 1fr));gap:30px;">
                
                <!-- Healthcare -->
                <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
                    <div style="height:200px;background:linear-gradient(135deg, #0ea5e9, #0284c7);display:flex;align-items:center;justify-content:center;color:#fff;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none"><path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10z" stroke="white" stroke-width="2"/><path d="M12 8v8M8 12h8" stroke="white" stroke-width="2" stroke-linecap="round"/></svg>
                    </div>
                    <div style="padding:30px;flex:1;display:flex;flex-direction:column;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;">
                            <span class="mono" style="font-size:0.6rem;color:var(--sky);letter-spacing:0.1em;font-weight:700;">HEALTHCARE</span>
                            <span class="tag">Mobile Apps</span>
                        </div>
                        <h3 style="font-size:1.4rem;font-weight:700;color:var(--ink2);margin-bottom:12px;">HealthTrack Mobile App</h3>
                        <p style="color:var(--muted);line-height:1.6;font-size:0.95rem;margin-bottom:20px;">Remote patient monitoring and medication adherence tracking for chronic disease management.</p>
                        <div style="background:var(--bg2);padding:15px;border-radius:10px;margin-bottom:20px;border-left:3px solid var(--sky);">
                            <div style="font-weight:700;color:var(--sky3);font-size:1.2rem;">85%</div>
                            <div style="font-size:0.8rem;color:var(--muted);">improvement in patient medication adherence</div>
                        </div>
                        <div style="margin-top:auto;">
                            <a href="#" style="display:inline-flex;align-items:center;gap:6px;color:var(--sky2);font-weight:600;text-decoration:none;font-size:0.9rem;">View Full Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Retail -->
                <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
                    <div style="height:200px;background:linear-gradient(135deg, #8b5cf6, #6d28d9);display:flex;align-items:center;justify-content:center;color:#fff;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none"><path d="M21 16V8a2 2 0 00-1-1.73l-7-4a2 2 0 00-2 0l-7 4A2 2 0 003 8v8a2 2 0 001 1.73l7 4a2 2 0 002 0l7-4A2 2 0 0021 16z" stroke="white" stroke-width="2"/><path d="M12 22V12" stroke="white" stroke-width="2"/><path d="M3.27 6.96L12 12l8.73-5.04" stroke="white" stroke-width="2"/></svg>
                    </div>
                    <div style="padding:30px;flex:1;display:flex;flex-direction:column;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;">
                            <span class="mono" style="font-size:0.6rem;color:var(--sky);letter-spacing:0.1em;font-weight:700;">RETAIL & E-COMMERCE</span>
                            <span class="tag">AI Bots</span>
                        </div>
                        <h3 style="font-size:1.4rem;font-weight:700;color:var(--ink2);margin-bottom:12px;">RetailBot Assistant</h3>
                        <p style="color:var(--muted);line-height:1.6;font-size:0.95rem;margin-bottom:20px;">24/7 customer support automation and personalised product recommendations to increase sales conversion.</p>
                        <div style="background:var(--bg2);padding:15px;border-radius:10px;margin-bottom:20px;border-left:3px solid var(--sky);">
                            <div style="font-weight:700;color:var(--sky3);font-size:1.2rem;">300%</div>
                            <div style="font-size:0.8rem;color:var(--muted);">increase in customer engagement</div>
                        </div>
                        <div style="margin-top:auto;">
                            <a href="#" style="display:inline-flex;align-items:center;gap:6px;color:var(--sky2);font-weight:600;text-decoration:none;font-size:0.9rem;">View Full Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Manufacturing -->
                <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
                    <div style="height:200px;background:linear-gradient(135deg, #10b981, #047857);display:flex;align-items:center;justify-content:center;color:#fff;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none"><path d="M12 6V4m0 2a2 2 0 100 4m0-4a2 2 0 110 4m-6 8a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4m6 6v10m6-2a2 2 0 100-4m0 4a2 2 0 110-4m0 4v2m0-6V4" stroke="white" stroke-width="2" stroke-linecap="round"/></svg>
                    </div>
                    <div style="padding:30px;flex:1;display:flex;flex-direction:column;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;">
                            <span class="mono" style="font-size:0.6rem;color:var(--sky);letter-spacing:0.1em;font-weight:700;">MANUFACTURING</span>
                            <span class="tag">Manufacturing</span>
                        </div>
                        <h3 style="font-size:1.4rem;font-weight:700;color:var(--ink2);margin-bottom:12px;">SmartFactory Automation</h3>
                        <p style="color:var(--muted);line-height:1.6;font-size:0.95rem;margin-bottom:20px;">Streamline production workflows, reduce manual errors, and optimise equipment maintenance scheduling.</p>
                        <div style="background:var(--bg2);padding:15px;border-radius:10px;margin-bottom:20px;border-left:3px solid var(--sky);">
                            <div style="font-weight:700;color:var(--sky3);font-size:1.2rem;">50%</div>
                            <div style="font-size:0.8rem;color:var(--muted);">reduction in production downtime</div>
                        </div>
                        <div style="margin-top:auto;">
                            <a href="#" style="display:inline-flex;align-items:center;gap:6px;color:var(--sky2);font-weight:600;text-decoration:none;font-size:0.9rem;">View Full Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Financial Services -->
                <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
                    <div style="height:200px;background:linear-gradient(135deg, #f59e0b, #b45309);display:flex;align-items:center;justify-content:center;color:#fff;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none"><path d="M3 10h18M7 15h1m4 0h1m-7 4h12a3 3 0 003-3V8a3 3 0 00-3-3H6a3 3 0 00-3 3v8a3 3 0 003 3z" stroke="white" stroke-width="2" stroke-linecap="round"/></svg>
                    </div>
                    <div style="padding:30px;flex:1;display:flex;flex-direction:column;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;">
                            <span class="mono" style="font-size:0.6rem;color:var(--sky);letter-spacing:0.1em;font-weight:700;">FINANCIAL SERVICES</span>
                            <span class="tag">Mobile Apps</span>
                        </div>
                        <h3 style="font-size:1.4rem;font-weight:700;color:var(--ink2);margin-bottom:12px;">FinanceFlow Mobile Suite</h3>
                        <p style="color:var(--muted);line-height:1.6;font-size:0.95rem;margin-bottom:20px;">Modernize legacy banking systems with secure mobile banking and automated compliance reporting.</p>
                        <div style="background:var(--bg2);padding:15px;border-radius:10px;margin-bottom:20px;border-left:3px solid var(--sky);">
                            <div style="font-weight:700;color:var(--sky3);font-size:1.2rem;">90%</div>
                            <div style="font-size:0.8rem;color:var(--muted);">faster transaction processing</div>
                        </div>
                        <div style="margin-top:auto;">
                            <a href="#" style="display:inline-flex;align-items:center;gap:6px;color:var(--sky2);font-weight:600;text-decoration:none;font-size:0.9rem;">View Full Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

                <!-- Education -->
                <div class="card" style="padding:0;overflow:hidden;display:flex;flex-direction:column;">
                    <div style="height:200px;background:linear-gradient(135deg, #ec4899, #be185d);display:flex;align-items:center;justify-content:center;color:#fff;">
                        <svg width="64" height="64" viewBox="0 0 24 24" fill="none"><path d="M12 14l9-5-9-5-9 5 9 5z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0012 20.055a11.952 11.952 0 00-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/><path d="M12 14v7" stroke="white" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                    </div>
                    <div style="padding:30px;flex:1;display:flex;flex-direction:column;">
                        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:15px;">
                            <span class="mono" style="font-size:0.6rem;color:var(--sky);letter-spacing:0.1em;font-weight:700;">EDUCATION TECHNOLOGY</span>
                            <span class="tag">Automation</span>
                        </div>
                        <h3 style="font-size:1.4rem;font-weight:700;color:var(--ink2);margin-bottom:12px;">EduAdapt Learning Platform</h3>
                        <p style="color:var(--muted);line-height:1.6;font-size:0.95rem;margin-bottom:20px;">Personalised learning experiences that adapt to individual student progress and learning styles.</p>
                        <div style="background:var(--bg2);padding:15px;border-radius:10px;margin-bottom:20px;border-left:3px solid var(--sky);">
                            <div style="font-weight:700;color:var(--sky3);font-size:1.2rem;">70%</div>
                            <div style="font-size:0.8rem;color:var(--muted);">improvement in student engagement</div>
                        </div>
                        <div style="margin-top:auto;">
                            <a href="#" style="display:inline-flex;align-items:center;gap:6px;color:var(--sky2);font-weight:600;text-decoration:none;font-size:0.9rem;">View Full Case Study <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M5 12h14M12 5l7 7-7 7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg></a>
                        </div>
                    </div>
                </div>

            </div>

             <div style="margin-top:60px;padding:40px;background:var(--ink2);border-radius:20px;text-align:center;color:#fff;">
                <h3 style="font-size:1.8rem;font-weight:700;margin-bottom:16px;">Ready to Join Our Success Stories?</h3>
                <p style="color:rgba(255,255,255,0.7);max-width:600px;margin:0 auto 24px;line-height:1.7;">Whether you're looking to streamline operations, enhance customer experience, or drive innovation, we're here to transform your vision into measurable results.</p>
                <a href="index.html#contact" class="btn btn-sky">Start Your Success Story</a>
            </div>
            
        </div>
    </section>
"""

with open(r'f:\acantix\case-studies.html', 'w', encoding='utf-8') as f:
    f.write(head_and_nav + case_studies_body + footer_and_scripts)

print("case-studies.html created successfully!")
