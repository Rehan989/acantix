import re

with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav = text[:nav_end]
footer_start = text.find('<footer>')
footer_and_scripts = text[footer_start:]

careers_body = """
    <!-- TICKER -->
    <div style="margin-top:68px;" class="ticker-wrap">
        <div class="ticker-track">
            <span>◈ NOW HIRING</span><span>◈ DEEP WORK FIRST</span><span>◈ JOIN ACANTIX</span><span>◈ SHAPE AGENTIC AI</span><span>◈ SYSTEMS NOT SILOS</span>
            <span>◈ NOW HIRING</span><span>◈ DEEP WORK FIRST</span><span>◈ JOIN ACANTIX</span><span>◈ SHAPE AGENTIC AI</span><span>◈ SYSTEMS NOT SILOS</span>
        </div>
    </div>
    
    <!-- ═══ CAREERS HERO ═══ -->
    <section style="padding:120px 0 60px;background:#fff;text-align:center;">
        <div style="max-width:1280px;margin:0 auto;padding:0 28px;">
            <div class="tag tag-sky" style="margin-bottom:22px;">
                Join Acantix
            </div>
            <h1 style="font-size:clamp(2.5rem,4vw,3.8rem);font-weight:800;color:var(--ink2);margin-bottom:20px;">
                We don't just hire.<br/> Careers aren't jobs —<br/>
                <em class="serif shimmer-text" style="font-style:italic;font-weight:400;">they're journeys of building impact.</em>
            </h1>
            <p style="font-size:1.1rem;color:var(--muted);max-width:700px;margin:0 auto 40px;line-height:1.8;">
                At Acantix, we create technologies that think, adapt, and scale. Our products aren't just smart, 
                they're agentic, autonomous and purpose-built for real-world impact. We're building a company for 
                deep thinkers, restless builders and clear communicators.
            </p>
        </div>
    </section>

    <hr class="div" />

    <!-- ═══ CULTURE & VALUES ═══ -->
    <section style="padding:100px 0;background:var(--bg);">
        <div style="max-width:1280px;margin:0 auto;padding:0 28px;">
            <div style="text-align:center;margin-bottom:60px;">
                <h2 style="font-size:2.4rem;font-weight:800;color:var(--ink2);">It's not about the tools.<br/><span style="color:var(--sky);">It's about the people behind them.</span></h2>
                <p style="color:var(--muted);margin-top:20px;">We don't run job ads, We don't chase resume</p>
            </div>
            <div style="display:grid;grid-template-columns:1fr 1fr;gap:30px;">
                <div class="card">
                    <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:12px;color:var(--ink2);">Deep Work First</h3>
                    <p style="color:var(--muted);line-height:1.7;">We respect focus, async thinking, and flow. Our work patterns are designed for clarity and momentum—not noise.</p>
                </div>
                <div class="card">
                    <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:12px;color:var(--ink2);">Growth Without Permission</h3>
                    <p style="color:var(--muted);line-height:1.7;">You don't need a promotion to explore. Team members self-initiate projects, experiments, and ideas. We help shape them into product-grade realities.</p>
                </div>
                <div class="card">
                    <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:12px;color:var(--ink2);">Systems, Not Silos</h3>
                    <p style="color:var(--muted);line-height:1.7;">Engineering works closely with design, product, data, and research. We're small enough to move fast and smart enough to stay aligned.</p>
                </div>
                <div class="card">
                    <h3 style="font-size:1.4rem;font-weight:700;margin-bottom:12px;color:var(--ink2);">Merit wins Culture</h3>
                    <p style="color:var(--muted);line-height:1.7;">Its not about democracy, its Meritocracy. We're hiring for passion not for roles.</p>
                </div>
            </div>
        </div>
    </section>

    <hr class="div" />

    <!-- ═══ OPEN ROLES ═══ -->
    <section style="padding:100px 0;background:#fff;">
        <div style="max-width:1280px;margin:0 auto;padding:0 28px;">
            <div style="margin-bottom:60px;">
                <h2 style="font-size:2.4rem;font-weight:800;color:var(--ink2);">Open Positions</h2>
            </div>
            <div style="display:flex;flex-direction:column;gap:20px;">
                <div class="bp-card" style="display:flex;align-items:center;padding:30px;justify-content:space-between;">
                    <div style="display:flex;align-items:center;gap:30px;">
                        <div class="step-num" style="margin:0;border-color:var(--sky);color:var(--sky);">01</div>
                        <div>
                            <h3 style="font-size:1.5rem;font-weight:700;color:var(--ink2);margin-bottom:8px;">AI Engineer</h3>
                            <p style="color:var(--muted);max-width:600px;">Build and deploy agentic systems for real-time decisions. Work with LLMs, edge-AI, and domain-specific models.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="btn btn-sky" style="white-space:nowrap;">Apply Now</a>
                </div>
                
                <div class="bp-card" style="display:flex;align-items:center;padding:30px;justify-content:space-between;">
                    <div style="display:flex;align-items:center;gap:30px;">
                        <div class="step-num" style="margin:0;border-color:var(--sky);color:var(--sky);">02</div>
                        <div>
                            <h3 style="font-size:1.5rem;font-weight:700;color:var(--ink2);margin-bottom:8px;">Product Designer</h3>
                            <p style="color:var(--muted);max-width:600px;">Shape the feel and function of agent-first tools. Experience in motion, systems thinking, and data UI is a plus.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="btn btn-sky" style="white-space:nowrap;">Apply Now</a>
                </div>

                <div class="bp-card" style="display:flex;align-items:center;padding:30px;justify-content:space-between;">
                    <div style="display:flex;align-items:center;gap:30px;">
                        <div class="step-num" style="margin:0;border-color:var(--sky);color:var(--sky);">03</div>
                        <div>
                            <h3 style="font-size:1.5rem;font-weight:700;color:var(--ink2);margin-bottom:8px;">Platform Engineer</h3>
                            <p style="color:var(--muted);max-width:600px;">Help us scale safely. Secure, observable, resilient infrastructure is your craft.</p>
                        </div>
                    </div>
                    <a href="mailto:join@acantix.com" class="btn btn-sky" style="white-space:nowrap;">Apply Now</a>
                </div>
            </div>
            
            <div style="margin-top:60px;padding:40px;background:var(--ink2);border-radius:20px;text-align:center;color:#fff;">
                <h3 style="font-size:1.8rem;font-weight:700;margin-bottom:16px;">Don't see a perfect fit?</h3>
                <p style="color:rgba(255,255,255,0.7);max-width:500px;margin:0 auto 24px;">Tell us what excites you and where you want to make an impact.</p>
                <a href="mailto:join@acantix.com" class="btn btn-sky">join@Acantix.com</a>
            </div>
        </div>
    </section>
"""

with open(r'f:\acantix\careers.html', 'w', encoding='utf-8') as f:
    f.write(head_and_nav + careers_body + footer_and_scripts)

print("careers.html created successfully!")
