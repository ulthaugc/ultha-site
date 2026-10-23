import sys,re
sys.path.insert(0,'/tmp/claude-0/-home-claude/c55b7bce-055d-5cb1-96bf-984be9841218/scratchpad')
from illus import journey_svg, tree_svg
from urllib.parse import quote
S='/tmp/claude-0/-home-claude/c55b7bce-055d-5cb1-96bf-984be9841218/scratchpad/'
s=open('index.html').read()
def sec(t,start):
    a=t.index(start); b=t.index('</section>',a)+10; return a,b
# save pricing for pricing page
a,b=sec(s,'<section id="pricing">'); open(S+'pricing_section.html','w').write(s[a:b])
pa=s.index('<style>/* pricing v2 */'); pb=s.index('</style>',pa)+8; open(S+'pricing_css.html','w').write(s[pa:pb])
# 1 stat
stat='''<section id="whynow" class="wn">
<div class="wn-in st reveal">
<span class="wn-kick">Why this matters now</span>
<p class="st-big"><span class="st-n">83%</span><span class="st-t">of the buying process happens <em>without you</em> in the room.</span></p>
<div class="st-bar" role="img" aria-label="17% of the buying process is spent talking to sales reps, 83% is spent researching without you"><span class="b1"></span><span class="b2"></span></div>
<div class="st-leg"><span><i class="l1"></i>17% talking to sales reps</span><span><i class="l2"></i>83% reading reviews, comparing you, asking AI</span></div>
<p class="st-sub">Buyers spend just 17% of the process talking to sales reps. The rest of the time, they’re reading about you without you.</p>
<cite>Source: Gartner</cite>
</div>
</section>'''
a,b=sec(s,'<section id="whynow"'); s=s[:a]+stat+s[b:]
# 2 how + services replace loop
steps=[('1 · Listen','One customer conversation','15 minutes with a customer who loves you.'),
       ('2 · Capture','Becomes proof','Reviews, testimonials and case studies, approved by them.'),
       ('3 · Show','Proof becomes content','Short videos, posts and carousels for socials and your site.'),
       ('4 · Get found','Shows up where buyers look','Your site, G2, LinkedIn and AI search.')]
lis=''.join(f'<li>{journey_svg(i+1)}<div class="hw-txt"><span class="hw-k">{k}</span><b>{t}</b><span class="hw-d">{d}</span></div></li>' for i,(k,t,d) in enumerate(steps))
how=f'''<section id="how" class="hw">
<div class="hw-in">
<div class="hw-head reveal"><span class="wn-kick">How it works</span><h2>One conversation. Proof everywhere.</h2><p>One customer conversation becomes proof, proof becomes content, and content shows up where buyers and AI search look.</p></div>
<ol class="hw-steps reveal">{lis}</ol>
<!-- When the video is ready, wrap .hw-vid in <a href="..."> or swap in a <video>. -->
<div class="hw-vid reveal"><span class="hw-thumb"><img src="video-poster.jpg" alt=""><span aria-hidden="true">▶</span></span><span class="hw-vt"><b>Watch me explain it in 90 seconds</b><span>Video coming soon</span></span></div>
</div>
</section>

<section id="services" class="sv">
<div class="sv-in">
<div class="sv-head reveal"><span class="wn-kick">What I make</span><h2>Every piece builds trust. <span>Trust grows revenue.</span></h2></div>
<div class="reveal">{tree_svg(False)}{tree_svg(True)}</div>
</div>
</section>'''
a,b=sec(s,'<section id="loop"'); s=s[:a]+how+s[b:]
# 3 agency id
s=s.replace('<section style="background: #22354A">\n<div style="max-width: 980px; margin: 0 auto; padding: 96px 24px;','<section id="agency" style="background: #22354A">\n<div style="max-width: 980px; margin: 0 auto; padding: 72px 24px;',1)
# 4 pricing -> strip
strip='''<section id="plans" class="pl">
<div class="pl-in reveal">
<div><span class="wn-kick">Pricing</span><h2>Three ways to start.</h2><p>Proof Sprint · 90-Day Proof Engine · Keep it running. Clear scope, clear price, no open-ended retainers.</p></div>
<a class="pl-btn" href="/pricing">See pricing →</a>
</div>
</section>'''
a,b=sec(s,'<section id="pricing">'); s=s[:a]+strip+s[b:]
# 5 links
s=s.replace('href="#loop"','href="#how"').replace('href="#pricing"','href="/pricing"')
# 6 closing line
s=s.replace('Tell me about your startup. I’ll show you what search and AI tools say about you, and what’s missing.','Share a bit about your startup. I’ll map out the proof you could have in 30 days.')
# faq padding
s=s.replace('<section id="faq" style="max-width: 820px; margin: 0 auto; padding: 104px 24px;','<section id="faq" style="max-width: 820px; margin: 0 auto; padding: 72px 24px;')
# 7 css
D,M='#111C27','#1B2A38'
def wave(c): return 'url("data:image/svg+xml,'+quote(f"<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 1440 70' preserveAspectRatio='none'><path d='M0 0H1440V30C1200 70 960 10 720 34S240 64 0 26Z' fill='{c}'/></svg>")+'") top/100% 60px no-repeat'
PANEL='margin:20px;border-radius:48px;overflow:hidden;position:relative;border:1px solid rgba(198,211,219,.12);border-top-color:rgba(255,255,255,.22);box-shadow:inset 0 1px 0 rgba(255,255,255,.10),inset 0 40px 80px -40px rgba(198,211,219,.10),0 2px 0 rgba(0,0,0,.4),0 40px 70px -30px rgba(0,0,0,.75)'
arrow='url("data:image/svg+xml,'+quote("<svg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 80 30'><path d='M4 22 C24 2 52 2 70 16' fill='none' stroke='#FFE29A' stroke-width='2.5' stroke-dasharray='5 6' stroke-linecap='round'/><path d='M62 9 l9 8 -11 3' fill='none' stroke='#FFE29A' stroke-width='2.5' stroke-linecap='round' stroke-linejoin='round'/></svg>")+'") center/contain no-repeat'
css=f'''<style>/* v3: tighter page, stat, how, services, plans */
section h2{{font-size:clamp(26px,2.9vw,38px)!important}}
.herohl{{font-size:clamp(34px,3.9vw,54px)}}
#whynow.wn{{background:{wave(M)},{D}!important}}
#whynow .wn-in.st{{max-width:880px;margin:0 auto;padding:104px 24px 72px!important;text-align:center;display:flex;flex-direction:column;align-items:center}}
.st-big{{margin:18px 0 26px;display:flex;flex-direction:column;align-items:center;gap:6px}}
.st-n{{font-family:Figtree,system-ui,sans-serif;font-weight:800;font-size:clamp(92px,12vw,150px);line-height:.95;letter-spacing:-.04em;color:#FFE29A}}
.st-t{{font-family:'Young Serif',serif;font-size:clamp(24px,2.8vw,36px);line-height:1.2;color:#fff;max-width:17em}}
.st-t em{{font-style:normal;color:#FFE29A}}
.st-bar{{display:flex;width:100%;max-width:640px;height:16px;border-radius:999px;overflow:hidden;gap:4px}}
.st-bar .b1{{width:17%;background:#5E7586;border-radius:999px 0 0 999px}}
.st-bar .b2{{flex:1;background:#FFE29A;border-radius:0 999px 999px 0}}
.st-leg{{display:flex;flex-wrap:wrap;justify-content:center;gap:8px 26px;margin:14px 0 22px;font-size:14.5px;color:#C6D3DB}}
.st-leg span{{display:inline-flex;align-items:center;gap:8px}}
.st-leg i{{width:10px;height:10px;border-radius:50%;display:inline-block}}.st-leg .l1{{background:#5E7586}}.st-leg .l2{{background:#FFE29A}}
.st-sub{{margin:0;font-size:17px;line-height:1.55;color:#A9BAC5;max-width:36em}}
.st cite{{margin-top:10px;font-style:normal;font-size:12.5px;color:#6F8494}}
#how{{background:{M};{PANEL}}}
.hw-in{{max-width:1120px;margin:0 auto;padding:72px 32px 56px}}
.hw-head{{text-align:center;max-width:680px;margin:0 auto 36px;display:flex;flex-direction:column;align-items:center;gap:10px}}
.hw-head h2{{margin:0;font-family:'Young Serif',serif;font-weight:400;color:#fff;line-height:1.15}}
.hw-head p{{margin:0;font-size:17px;color:#C6D3DB}}
.hw-steps{{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(4,1fr);gap:34px}}
.hw-steps li{{position:relative;display:flex;flex-direction:column;align-items:center;text-align:center}}
.hw-steps li:not(:last-child)::after{{content:"";position:absolute;top:58px;right:-46px;width:60px;height:24px;background:{arrow};z-index:1}}
.hw-art{{display:block;width:100%;max-width:260px;height:auto}}
.hw-txt{{display:flex;flex-direction:column;gap:4px;margin-top:10px}}
.hw-k{{font-size:12px;font-weight:700;letter-spacing:.12em;text-transform:uppercase;color:#F08A74}}
.hw-txt b{{font-family:'Young Serif',serif;font-weight:400;font-size:20px;line-height:1.25;color:#fff}}
.hw-d{{font-size:14.5px;line-height:1.45;color:#A9BAC5}}
.hw-vid{{display:flex;align-items:center;gap:14px;width:max-content;margin:40px auto 0;background:#22354A;border:1px solid #3A5169;border-radius:999px;padding:8px 24px 8px 8px}}
.hw-thumb{{position:relative;width:60px;height:60px;border-radius:50%;overflow:hidden;flex:none;box-shadow:0 0 0 3px rgba(255,226,154,.7)}}
.hw-thumb img{{width:100%;height:100%;object-fit:cover;object-position:40% 22%;display:block}}
.hw-thumb span{{position:absolute;inset:0;display:flex;align-items:center;justify-content:center;background:rgba(17,28,39,.35);color:#fff;font-size:16px}}
.hw-vt{{display:flex;flex-direction:column;line-height:1.3}}.hw-vt b{{font-family:'Young Serif',serif;font-weight:400;font-size:17px;color:#fff}}.hw-vt span{{font-size:13px;color:#93A6B4}}
#services{{background:{wave(D)},{M}!important}}
.sv-in{{max-width:1180px;margin:0 auto;padding:96px 24px 48px}}
.sv-head{{text-align:center;display:flex;flex-direction:column;align-items:center;gap:10px;margin-bottom:8px}}
.sv-head h2{{margin:0;font-family:'Young Serif',serif;font-weight:400;color:#fff;line-height:1.15}}.sv-head h2 span{{color:#FFE29A}}
.tree-art{{display:block;width:100%;height:auto}}.tree-m{{display:none}}
#agency{{background:{wave(M)},{D}!important}}
#agency>div{{padding-top:96px!important}}
#clients .cp-in{{padding:64px 24px 52px!important}}
#clients .cp h2,#clients h2{{margin-bottom:24px!important}}
#clients .cp-nav{{margin-top:30px!important}}
#clients .sig{{margin-top:22px!important;padding-top:18px!important}}
.pl{{background:{D}}}
.pl-in{{max-width:1060px;margin:0 auto;padding:56px 24px;display:flex;align-items:center;justify-content:space-between;gap:24px 40px;flex-wrap:wrap}}
.pl-in>div{{display:flex;flex-direction:column;gap:8px;align-items:flex-start;max-width:640px}}
.pl-in .wn-kick{{align-self:flex-start!important;margin:0!important}}
.pl h2{{margin:0;font-family:'Young Serif',serif;font-weight:400;color:#fff}}
.pl p{{margin:0;font-size:16px;color:#A9BAC5}}
.pl-btn{{text-decoration:none;background:#FFE29A;color:#1B2A38!important;border-radius:999px;padding:14px 26px;font-weight:600;white-space:nowrap}}
.pl-btn:hover{{background:#fff}}
@media (max-width:900px){{.hw-steps{{grid-template-columns:1fr 1fr;row-gap:30px}}.hw-steps li:nth-child(2)::after{{display:none}}}}
@media (max-width:760px){{
section h2{{font-size:26px!important}}
#whynow .wn-in.st{{padding:72px 20px 52px!important}}
.st-n{{font-size:88px}}.st-t{{font-size:24px}}.st-leg{{flex-direction:column;align-items:center;gap:6px;font-size:14px}}.st-sub{{font-size:15.5px}}
#how{{margin:10px;border-radius:30px}}
.hw-in{{padding:52px 18px 40px}}.hw-head{{margin-bottom:24px}}.hw-head p{{font-size:15.5px}}
.hw-steps{{grid-template-columns:1fr;gap:18px}}
.hw-steps li{{display:grid;grid-template-columns:132px 1fr;align-items:center;text-align:left;gap:14px}}
.hw-steps li::after{{display:none!important}}
.hw-art{{max-width:132px}}.hw-txt{{margin:0}}.hw-txt b{{font-size:18px}}.hw-d{{font-size:14px}}
.hw-vid{{margin-top:28px;padding-right:18px}}.hw-thumb{{width:50px;height:50px}}.hw-vt b{{font-size:15px}}
.sv-in{{padding:72px 14px 32px}}.tree-d{{display:none}}.tree-m{{display:block;max-width:420px;margin:0 auto}}
#agency>div{{padding-top:80px!important;padding-bottom:56px!important}}
#clients .cp-in{{padding:48px 18px 40px!important}}
.pl-in{{padding:44px 20px;flex-direction:column;align-items:flex-start}}
}}
</style>
</head>'''
s=s.replace('</head>',css,1)
open('index.html','w').write(s)
print('ok')
