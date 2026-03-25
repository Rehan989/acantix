import os
import re

cases = [
    {
        "id": "healthcare",
        "title": "HealthTrack Mobile App",
        "description": "Remote patient monitoring and medication adherence tracking for chronic disease management",
        "tags": ["Mobile Apps", "Healthcare"],
        "challenges": [
            "Patients struggling with medication compliance",
            "Limited visibility into patient health between visits",
            "High hospital readmission rates for chronic conditions",
            "Need for 24/7 monitoring without overwhelming medical staff"
        ],
        "solution": "AI-powered mobile health platform with predictive analytics and automated alert systems",
        "components": [
            "Developed AI-powered medication reminder system with smart notifications",
            "Implemented real-time vital signs monitoring through IoT integration",
            "Created predictive analytics to identify at-risk patients early",
            "Built an intuitive mobile interface for patients and healthcare providers"
        ],
        "tech": ["React Native", "TensorFlow Lite", "Node.js", "PostgreSQL", "AWS IoT", "Machine Learning APIs"],
        "results": [
            "85% improvement in patient medication adherence",
            "40% reduction in hospital readmissions",
            "50,000+ patients actively using the platform",
            "92% patient satisfaction rate",
            "60% reduction in emergency department visits"
        ],
        "testimonial": {
            "quote": "Acantix transformed our patient care delivery. The AI-driven insights have revolutionised how we monitor and support our chronic disease patients.",
            "author": "Dr. Sarah Johnson, Chief Medical Officer",
            "industry": "Healthcare"
        }
    },
    {
        "id": "retail",
        "title": "RetailBot Assistant",
        "description": "24/7 customer support automation and personalised product recommendations to increase sales conversion",
        "tags": ["AI Bots", "Retail & E-commerce"],
        "challenges": [
            "High volume of repetitive customer inquiries",
            "Limited customer support hours affecting sales",
            "Difficulty providing personalised shopping experiences at scale",
            "Low conversion rates from browsing to purchase"
        ],
        "solution": "Intelligent conversational AI bot with natural language processing and recommendation engine integration",
        "components": [
            "Built an intelligent chatbot with natural language understanding",
            "Integrated machine learning for personalised product recommendations",
            "Implemented sentiment analysis for better customer interaction",
            "Created seamless handoff system to human agents when needed"
        ],
        "tech": ["Python", "OpenAI GPT", "Dialogflow", "React", "MongoDB", "Redis", "Stripe API", "Analytics Dashboard"],
        "results": [
            "300% increase in customer engagement",
            "65% reduction in support tickets",
            "45% boost in average order value",
            "24/7 customer support availability",
            "88% customer satisfaction with bot interactions"
        ],
        "testimonial": {
            "quote": "Our customers love the instant, personalised support. The bot handles complex queries beautifully and has significantly improved our sales metrics.",
            "author": "Michael Chen, VP of Customer Experience",
            "industry": "Retail & E-commerce"
        }
    },
    {
        "id": "manufacturing",
        "title": "SmartFactory Automation",
        "description": "Streamline production workflows, reduce manual errors, and optimize equipment maintenance scheduling",
        "tags": ["Manufacturing", "Manufacturing"],
        "challenges": [
            "Frequent unexpected equipment failures causing downtime",
            "Inconsistent product quality due to manual processes",
            "Inefficient resource allocation and workflow management",
            "High maintenance costs from reactive repairs"
        ],
        "solution": "End-to-end workflow automation system with predictive maintenance and quality control AI",
        "components": [
            "Implemented predictive maintenance using IoT sensors and ML",
            "Deployed computer vision for automated quality control",
            "Created intelligent workflow orchestration system",
            "Built real-time monitoring dashboard for operations team"
        ],
        "tech": ["Python", "Apache Airflow", "Docker", "Kubernetes", "Industrial IoT sensors", "Computer Vision", "PostgreSQL"],
        "results": [
            "50% reduction in production downtime",
            "30% decrease in manufacturing defects",
            "25% cost savings annually",
            "95% accuracy in predicting equipment failures",
            "40% improvement in overall equipment effectiveness (OEE)"
        ],
        "testimonial": {
            "quote": "The automation platform has transformed our manufacturing efficiency. We now predict equipment failures before they happen and maintain consistent quality.",
            "author": "Jennifer Rodriguez, Operations Director",
            "industry": "Manufacturing"
        }
    },
    {
        "id": "finance",
        "title": "FinanceFlow Mobile Suite",
        "description": "Modernize legacy banking systems with secure mobile banking and automated compliance reporting",
        "tags": ["Mobile Apps", "Financial Services"],
        "challenges": [
            "Outdated legacy systems causing slow transaction processing",
            "Increasing fraud attempts requiring better security measures",
            "Complex regulatory compliance requirements",
            "Poor mobile user experience affecting customer satisfaction"
        ],
        "solution": "AI-native fintech platform with biometric security, automated fraud detection, and regulatory compliance",
        "components": [
            "Built modern mobile-first banking platform with Flutter",
            "Implemented AI-powered fraud detection system",
            "Integrated biometric authentication for enhanced security",
            "Automated compliance reporting and regulatory adherence"
        ],
        "tech": ["Flutter", "Node.js", "Blockchain", "AI/ML APIs", "Biometric Authentication", "AWS Security", "Compliance APIs"],
        "results": [
            "90% faster transaction processing",
            "99.8% fraud detection accuracy",
            "Full regulatory compliance achieved",
            "95% customer satisfaction with mobile app",
            "70% reduction in security incidents"
        ],
        "testimonial": {
            "quote": "Acantix delivered a banking solution that exceeds industry security standards while providing an exceptional user experience.",
            "author": "Robert Kim, Chief Technology Officer",
            "industry": "Financial Services"
        }
    },
    {
        "id": "education",
        "title": "EduAdapt Learning Platform",
        "description": "Personalized learning experiences that adapt to individual student progress and learning styles",
        "tags": ["Automation", "Education Technology"],
        "challenges": [
            "One-size-fits-all learning approach not meeting individual needs",
            "Difficulty tracking and measuring student progress effectively",
            "Low student engagement with traditional learning methods",
            "Teachers overwhelmed with personalizing content for each student"
        ],
        "solution": "Adaptive AI tutoring system with real-time progress tracking and personalised curriculum generation",
        "components": [
            "Developed AI algorithms to adapt content to learning styles",
            "Created real-time progress tracking and analytics dashboard",
            "Built intelligent content recommendation system",
            "Implemented gamification elements to boost engagement"
        ],
        "tech": ["React", "Python", "TensorFlow", "Natural Language Processing", "Learning Analytics", "Cloud Infrastructure"],
        "results": [
            "70% improvement in student engagement",
            "55% faster learning progression",
            "95% student satisfaction rate",
            "80% reduction in teacher workload for content personalization",
            "60% improvement in learning outcomes"
        ],
        "testimonial": {
            "quote": "The platform has revolutionised how our students learn. Each student now gets a truly personalised education experience that adapts to their needs.",
            "author": "Dr. Amanda Foster, Head of Digital Learning",
            "industry": "Education Technology"
        }
    }
]

with open(r'f:\acantix\index.html', 'r', encoding='utf-8') as f:
    text = f.read()

nav_end = text.find('</nav>') + len('</nav>')
head_and_nav_base = text[:nav_end]
head_and_nav = head_and_nav_base.replace('href="dist/', 'href="/dist/').replace('src="icon.svg"', 'src="/icon.svg"').replace('href="case-studies.html"', 'href="/case-studies.html"').replace('href="careers.html"', 'href="/careers.html"').replace('href="#', 'href="/#')
head_and_nav = head_and_nav.replace('href="/icon.svg"', 'href="/icon.svg"')

footer_start = text.find('<!-- ══ CONTACT ══ -->')
footer_and_scripts_base = text[footer_start:]
footer_and_scripts = footer_and_scripts_base.replace('src="icon.svg"', 'src="/icon.svg"').replace('href="case-studies.html"', 'href="/case-studies.html"').replace('href="careers.html"', 'href="/careers.html"').replace('href="#', 'href="/#')

for case in cases:
    html = f'''
    <!-- TICKER -->
    <div class="bg-[#1a1a1a] py-1.5 mt-[60px] overflow-hidden">
        <div class="ticker-track flex whitespace-nowrap">
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> CLIENT SUCCESS <span class="text-white/15">◈</span> CASE STUDY <span class="text-white/15">◈</span> {case['title'].upper()}</span>
            <span class="inline-flex items-center gap-4 mx-8 font-mono text-[10px] tracking-[.18em] text-white/40"><span class="text-white/15">◈</span> CLIENT SUCCESS <span class="text-white/15">◈</span> CASE STUDY <span class="text-white/15">◈</span> {case['title'].upper()}</span>
        </div>
    </div>
    
    <!-- ═══ BREADCRUMBS ═══ -->
    <div class="bg-[#fafafa] py-4 border-b border-[#e5e5e5]">
        <div class="max-w-[1000px] mx-auto px-7 flex items-center gap-2">
            <a href="/case-studies.html" class="text-sm text-[#6b6b6b] hover:text-[#1a1a1a] font-medium flex items-center gap-1.5 transition-colors">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none"><path d="M19 12H5M12 19l-7-7 7-7" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>
                Back to Clients
            </a>
        </div>
    </div>

    <!-- ═══ CASE HERO ═══ -->
    <section class="py-20 md:py-28 bg-white border-b border-[#e5e5e5]">
        <div class="max-w-[1000px] mx-auto px-7">
            <div class="flex flex-wrap gap-2 mb-6">
                <span class="bg-[#1a1a1a] text-white px-3 py-1.5 rounded textxs font-bold uppercase tracking-wider">Case Study</span>
                <span class="bg-[#f0f0f0] text-[#1a1a1a] px-3 py-1.5 rounded text-xs font-bold uppercase tracking-wider">{case['tags'][1]}</span>
            </div>
            <h1 class="font-serif font-bold text-[#1a1a1a] text-[clamp(2.5rem,4vw,3.8rem)] leading-[1.15] mb-6">
                {case['title']}
            </h1>
            <p class="text-[#6b6b6b] text-xl md:text-2xl leading-relaxed max-w-[800px] mb-12">
                {case['description']}
            </p>
            
            <div class="flex flex-wrap gap-3">
                <span class="border border-[#e5e5e5] text-[#6b6b6b] px-4 py-2 rounded-full text-sm font-medium">{case['tags'][0]}</span>
                <span class="border border-[#e5e5e5] text-[#6b6b6b] px-4 py-2 rounded-full text-sm font-medium">{case['tags'][1]}</span>
            </div>
        </div>
    </section>

    <!-- ═══ CONTENT ═══ -->
    <section class="py-20 md:py-28 bg-[#fafafa]">
        <div class="max-w-[1000px] mx-auto px-7 grid grid-cols-1 lg:grid-cols-3 gap-16">
            
            <!-- Left Column: Main Content -->
            <div class="lg:col-span-2 space-y-16">
                <!-- The Challenge -->
                <div>
                    <h2 class="font-serif text-3xl font-bold text-[#1a1a1a] mb-6">The Challenge</h2>
                    <p class="text-[#6b6b6b] text-lg leading-relaxed mb-6">{case['description']}</p>
                    <h3 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-4">Key Challenges:</h3>
                    <ul class="space-y-3">
                        {''.join([f'<li class="flex gap-3 text-[#6b6b6b]"><svg class="w-6 h-6 text-[#f5e642] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z"/></svg> <span class="leading-relaxed">{{c}}</span></li>'.format(c=c) for c in case['challenges']])}
                    </ul>
                </div>

                <!-- Our Solution -->
                <div>
                    <h2 class="font-serif text-3xl font-bold text-[#1a1a1a] mb-6">Our Solution</h2>
                    <p class="text-[#6b6b6b] text-lg leading-relaxed mb-6">{case['solution']}</p>
                    <h3 class="text-sm font-bold text-[#1a1a1a] uppercase tracking-wider mb-4">Solution Components:</h3>
                    <ul class="space-y-3">
                        {''.join([f'<li class="flex gap-3 text-[#6b6b6b]"><svg class="w-6 h-6 text-[#22c55e] shrink-0" fill="none" viewBox="0 0 24 24" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg> <span class="leading-relaxed">{{c}}</span></li>'.format(c=c) for c in case['components']])}
                    </ul>
                </div>
                
                <!-- Testimonial -->
                <div class="bg-white border border-[#e5e5e5] p-10 rounded-2xl relative shadow-sm mt-10">
                    <svg class="w-12 h-12 text-[#e5e5e5] absolute top-8 left-8" fill="currentColor" viewBox="0 0 32 32"><path d="M9.333 13.333c0-3.68 3.013-6.667 6.667-6.667v-4c-5.893 0-10.667 4.773-10.667 10.667v13.333h10.667v-10.667h-6.667v-2.667zm16 0c0-3.68 3.013-6.667 6.667-6.667v-4c-5.893 0-10.667 4.773-10.667 10.667v13.333h10.667v-10.667h-6.667v-2.667z"/></svg>
                    <div class="relative z-10 pl-4">
                        <p class="text-xl md:text-2xl text-[#1a1a1a] leading-relaxed italic mb-8">"{case['testimonial']['quote']}"</p>
                        <div>
                            <div class="font-bold text-[#1a1a1a] text-lg">{case['testimonial']['author']}</div>
                            <div class="text-[#6b6b6b] text-sm uppercase tracking-wider font-bold mt-1">{case['testimonial']['industry']}</div>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Right Column: Sidebar -->
            <div class="space-y-8">
                <!-- Results & Impact -->
                <div class="bg-white border border-[#e5e5e5] rounded-2xl p-8 shadow-sm">
                    <h2 class="font-serif text-2xl font-bold text-[#1a1a1a] mb-6">Results & Impact</h2>
                    <h3 class="text-[10px] font-mono font-bold text-[#6b6b6b] uppercase tracking-[0.2em] mb-4">Measurable Outcomes:</h3>
                    
                    <div class="space-y-6">
                        {''.join([f'<div class="flex items-start gap-4"><div class="shrink-0 w-2 h-2 rounded-full bg-[#1a1a1a] mt-2"></div><p class="text-[#1a1a1a] font-medium leading-relaxed">{{r}}</p></div>'.format(r=r) for r in case['results']])}
                    </div>
                </div>

                <!-- Tech Stack -->
                <div class="bg-[#1a1a1a] rounded-2xl p-8 shadow-md">
                    <h2 class="font-serif text-2xl font-bold text-white mb-6">Technology Stack</h2>
                    <div class="flex flex-wrap gap-2">
                        {''.join([f'<span class="bg-white/10 text-white border border-white/20 px-3 py-1.5 rounded-lg text-sm font-medium">{{t}}</span>'.format(t=t) for t in case['tech']])}
                    </div>
                </div>
            </div>
            
        </div>
    </section>

    <!-- ═══ CALL TO ACTION ═══ -->
    <section class="py-24 bg-white border-t border-[#e5e5e5] text-center px-7">
        <div class="max-w-[700px] mx-auto">
            <h2 class="font-serif font-bold text-4xl text-[#1a1a1a] mb-6">Ready for Similar Results?</h2>
            <p class="text-xl text-[#6b6b6b] leading-relaxed mb-10">Let's discuss how we can create a custom solution for your business challenges and drive measurable impact in your industry.</p>
            <a href="/index.html#contact" class="inline-flex px-8 py-4 rounded-full bg-[#1a1a1a] text-white font-bold hover:bg-[#333] transition-all hover:shadow-lg hover:-translate-y-1 text-lg">Start Your Project</a>
        </div>
    </section>
    '''
    
    dir_path = rf'f:\acantix\clients\case-study\{case["id"]}'
    os.makedirs(dir_path, exist_ok=True)
    with open(os.path.join(dir_path, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(head_and_nav + html + footer_and_scripts)

with open(r'f:\acantix\case-studies.html', 'r', encoding='utf-8') as f:
    cs_html = f.read()

cs_html = re.sub(r'(<h3[^>]*>HealthTrack Mobile App</h3>.*?<a href=)"#"', r'\1"/clients/case-study/healthcare/"', cs_html, flags=re.DOTALL)
cs_html = re.sub(r'(<h3[^>]*>RetailBot Assistant</h3>.*?<a href=)"#"', r'\1"/clients/case-study/retail/"', cs_html, flags=re.DOTALL)
cs_html = re.sub(r'(<h3[^>]*>SmartFactory Automation</h3>.*?<a href=)"#"', r'\1"/clients/case-study/manufacturing/"', cs_html, flags=re.DOTALL)
cs_html = re.sub(r'(<h3[^>]*>FinanceFlow Mobile Suite</h3>.*?<a href=)"#"', r'\1"/clients/case-study/finance/"', cs_html, flags=re.DOTALL)
cs_html = re.sub(r'(<h3[^>]*>EduAdapt Learning Platform</h3>.*?<a href=)"#"', r'\1"/clients/case-study/education/"', cs_html, flags=re.DOTALL)

with open(r'f:\acantix\case-studies.html', 'w', encoding='utf-8') as f:
    f.write(cs_html)

print("SUCCESS")
