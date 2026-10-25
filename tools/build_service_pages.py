# Builds the three service pages (voice-of-customer, customer-stories, ai-search)
# from the shell of testimonial-videos.html: head, sticky header and footer stay shared.
import json, re
R = '/Users/milan.moktan/Claude/ultha-site/'
shell = open(R + 'tools/service_shell.html').read()

a = shell.index('<section class="tv-wrap">')
b = shell.index('<footer')
top, bottom = shell[:a], shell[b:]
top = top.replace('.mockflag{', '.mockflag-x{')

extra = '''<style>
.sv-card,.sv-stat{box-sizing:border-box}
.sv-card{background:#fff;border:1px solid #D5DFF8;border-radius:22px;padding:22px 24px;box-shadow:0 30px 60px -30px rgba(31,79,216,.45);width:100%;max-width:420px;font-size:14.5px}
.sv-card h3{margin:0 0 2px;font-family:'Young Serif',serif;font-weight:400;font-size:20px;color:#14213D}
.sv-card .sv-ex{font-size:12px;color:#586A7C;margin:0 0 14px}
.sv-row{display:grid;grid-template-columns:1fr auto;gap:10px;align-items:center;padding:9px 0;border-top:1px solid #EDF1FA}
.sv-row b{font-weight:600;color:#14213D}.sv-row small{display:block;color:#586A7C;font-size:12.5px}
.sv-tag{font-size:11.5px;font-weight:800;border-radius:6px;padding:3px 8px;white-space:nowrap}
.sv-fix{background:#FFF4D9;color:#8F6200}.sv-keep{background:#E8EFFD;color:#1F4FD8}.sv-build{background:#E9F7EF;color:#1D7A46}
.sv-steps{max-width:900px;margin:0 auto;display:grid;grid-template-columns:repeat(3,1fr);gap:18px;counter-reset:s}
.sv-steps div{position:relative;padding:20px 20px 20px 62px;background:#fff;border:1px solid #D5DFF8;border-radius:18px}
.sv-steps div::before{counter-increment:s;content:counter(s);position:absolute;left:18px;top:18px;width:32px;height:32px;border-radius:50%;background:#1F4FD8;color:#fff;font-weight:800;display:flex;align-items:center;justify-content:center}
.sv-steps b{display:block;font-family:'Young Serif',serif;font-weight:400;font-size:18px;color:#14213D;margin-bottom:4px}
.sv-steps p{margin:0;font-size:14.5px;line-height:1.5;color:#424A5E}
.sv-list{max-width:760px;margin:0 auto;display:grid;grid-template-columns:1fr 1fr;gap:12px 28px;padding:0;list-style:none}
.sv-list li{position:relative;padding-left:28px;font-size:15.5px;line-height:1.5;color:#14213D}
.sv-list li::before{content:"✓";position:absolute;left:0;top:0;color:#1F4FD8;font-weight:800}
.sv-list li small{display:block;color:#586A7C;font-size:13.5px}
.sv-faq{max-width:760px;margin:0 auto;display:grid;gap:10px}
.sv-faq details{background:#fff;border:1px solid #D5DFF8;border-radius:16px;padding:16px 20px}
.sv-faq summary{cursor:pointer;font-family:'Young Serif',serif;font-size:17px;color:#14213D}
.sv-faq p{margin:10px 0 0;font-size:15px;line-height:1.6;color:#424A5E}
.sv-stat{background:linear-gradient(150deg,#1F4FD8,#3D6BE6);color:#fff;border-radius:24px;padding:26px 28px;width:100%;max-width:420px;box-shadow:0 30px 60px -28px rgba(31,79,216,.6)}
.sv-stat b{display:block;font-size:44px;line-height:1.05;font-weight:800;letter-spacing:-.01em}
.sv-stat p{margin:6px 0 18px;color:#DCE6FC;font-size:15px}
.sv-stat p:last-child{margin-bottom:0}
.sv-stat small{display:block;color:#B9CBF6;font-size:12px;margin-top:-12px;margin-bottom:18px}
.sv-note{text-align:center;font-size:15px;color:#424A5E;margin:18px auto 0;max-width:640px}
.sv-note a{color:#1F4FD8;font-weight:600}
.tv-grid.c3{grid-template-columns:repeat(3,1fr)}
@media (max-width:900px){.sv-steps,.sv-list{grid-template-columns:1fr}.tv-grid.c3{grid-template-columns:1fr 1fr}.sv-card,.sv-stat{max-width:none}}
@media (max-width:560px){.tv-grid,.tv-grid.c3{grid-template-columns:1fr}}
</style>
'''

def grid(items, cls=''):
    return f'<div class="tv-grid {cls}">' + ''.join(f'<div><i>{i}</i><b>{t}</b><p>{d}</p></div>' for i, t, d in items) + '</div>'

def faq(items):
    return '<div class="sv-faq">' + ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in items) + '</div>'

def faq_ld(items):
    return '<script type="application/ld+json">' + json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": re.sub('<[^>]+>', '', q), "acceptedAnswer": {"@type": "Answer", "text": re.sub('<[^>]+>', '', a)}} for q, a in items]}, ensure_ascii=False) + '</script>'

def sec(kick, h2, body):
    return f'<section class="tv-sec"><span class="tv-k" style="display:table;margin:0 auto">{kick}</span><h2>{h2}</h2>{body}</section>'

def hero(kick, h1, p, right, b1='Let’s talk →'):
    return f'''<section class="tv-wrap"><div class="tv-hero">
<div><span class="tv-k">{kick}</span>
<h1>{h1}</h1>
<p>{p}</p>
<div class="tv-btns"><a class="tv-b1" href="/contact">{b1}</a><a class="tv-b2" href="/pricing">See pricing</a></div></div>
<div>{right}</div></div></section>'''

def cta(t, p):
    return f'<div class="tv-cta"><div><b>{t}</b><p>{p}</p></div><a href="/contact">Let’s talk →</a></div>'

def page(slug, title, desc, body, faqs):
    h = top
    h = re.sub(r'<title>.*?</title>', f'<title>{title}</title>', h, count=1, flags=re.S)
    h = re.sub(r'<meta name="description" content="[^"]*">', f'<meta name="description" content="{desc}">', h, count=1)
    h = re.sub(r'<meta property="og:title" content="[^"]*">', f'<meta property="og:title" content="{title}">', h, count=1)
    h = re.sub(r'<meta property="og:description" content="[^"]*">', f'<meta property="og:description" content="{desc}">', h, count=1)
    h = h.replace('https://ultha.co/customer-stories', f'https://ultha.co/{slug}')
    h = h.replace('</head>', faq_ld(faqs) + '\n</head>', 1)
    open(R + slug + '.html', 'w').write(h + extra + body + sec('Questions', 'Good to know', faq(faqs)) + '\n' + bottom)

# ---------- Voice of customer ----------
brief = '''<div class="sv-card"><h3>Insights brief</h3><p class="sv-ex">Example · 6 customer calls · 1 page</p>
<div class="sv-row"><span><b>Reporting is slow to set up</b><small>4 of 6 customers · admins on Growth plan</small></span><span class="sv-tag sv-fix">Fix first</span></div>
<div class="sv-row"><span><b>Onboarding feels fast</b><small>5 of 6 customers · mentioned unprompted</small></span><span class="sv-tag sv-keep">Keep</span></div>
<div class="sv-row"><span><b>Want a Slack integration</b><small>3 of 6 customers · teams over 20 people</small></span><span class="sv-tag sv-build">Build next</span></div>
<div class="sv-row"><span><b>Pricing page is confusing</b><small>2 of 6 customers · came close to choosing a competitor</small></span><span class="sv-tag sv-fix">Fix</span></div>
</div>'''
voc_faq = [
 ('Will customers really be honest with you?', 'More honest than with you. A neutral person isn’t the team that built the product, so customers say what they’d hold back on a call with the founder or their account manager.'),
 ('Is what they say kept private?', 'Yes. Criticism goes into your Insights brief and never into anything public. Only quotes a customer approves are ever used as testimonials.'),
 ('Who reads the Insights brief?', 'Your product and engineering team. It’s one page: the top issues, how many customers raised each one, who it affects and what to fix, keep or build next. Each issue is written so it can go straight into Jira or Linear.'),
 ('Can the same calls give us testimonials too?', 'Yes. That’s the point of every plan. What customers love becomes testimonials, case studies and content. What they’d change becomes the brief.'),
 ('What’s the difference between win-loss and churn interviews?', 'Win-loss calls are with buyers who recently chose you or a competitor, to learn why. Churn interviews are with customers who left, to learn who you should stop attracting and what to fix.'),
]
voc = hero('Voice of customer research for SaaS', 'Hear what customers won’t tell you. <span>Know what to fix next.</span>',
 'I run 30-minute calls with your customers as a neutral third party. You get a one-page Insights brief your product and engineering team can act on.', brief)
voc += sec('Why a third party', 'Customers tell me what they won’t tell you.',
 '<div class="tv-vs"><div><b>When the founder asks</b>“It’s great, we love it.” Polite answers, small complaints left out, and the real reason a deal almost fell through never comes up.</div><div><b>When I ask</b>The honest version: what’s slow, what’s missing, why they nearly chose someone else, and what would make them stay.</div></div>')
voc += sec('What you can book', 'Four ways to hear from customers.', grid([
 ('📞', 'Customer calls', '30-minute remote calls with your current customers. No prep for them.'),
 ('🧭', 'Insights brief', 'One page for product and engineering: what to fix, keep and build next.'),
 ('🏆', 'Win-loss study', 'Calls with buyers who chose you, and buyers who chose a competitor.'),
 ('🚪', 'Churn interviews', 'Calls with customers who left, so you know who to stop attracting.'),
]))
voc += sec('What’s in the brief', 'One page your team can act on.', '<ul class="sv-list">'
 '<li>Top issues, ranked<small>by how many customers raised them</small></li>'
 '<li>Who it affects<small>plan, role and team size</small></li>'
 '<li>The problem in their words<small>short quotes, kept private</small></li>'
 '<li>What to fix, keep or build next<small>written like a ticket for Jira or Linear</small></li>'
 '<li>What customers love<small>so nobody breaks it</small></li>'
 '<li>A 30-minute readout<small>I walk your team through it</small></li></ul>')
voc += sec('How it works', 'From intros to a brief in two weeks.', '<div class="sv-steps">'
 '<div><b>You send intros</b><p>5 to 10 customers, plus a few lost deals or churned accounts if you want win-loss or churn calls.</p></div>'
 '<div><b>I run the calls</b><p>30 minutes each, remote, friendly. No scripts and no prep on their end.</p></div>'
 '<div><b>You get the brief</b><p>One page, patterns across every call, and a readout with your team.</p></div></div>'
 '<p class="sv-note">The same calls also become testimonials and case studies. <a href="/customer-stories">See customer stories →</a></p>')
voc += cta('Find out what your customers really think.', 'Included in every plan, or book customer calls and a brief on their own.')
page('voice-of-customer', 'Voice of customer research for SaaS · Ultha',
 'Voice of customer research for SaaS startups: 30-minute calls with your customers, run by a neutral third party, turned into a one-page Insights brief your product team can act on. Win-loss and churn interviews too.',
 voc, voc_faq)

# ---------- Customer stories ----------
phones = '''<div class="tv-phones">
<div class="tv-ph"><img src="img/video-poster-me.jpg" alt="Ultha"><em>▶ 60s</em><span><b>What I ask your customers</b>The questions that turn “it’s great” into a real story.</span></div>
<div class="tv-ph"><img src="img/ask-me.jpg" alt="Ultha holding a microphone"><em>▶ 45s</em><span><b>One call, many pieces</b>How a 30-minute chat becomes a month of content.</span></div>
<div class="tv-ph"><img src="img/me-smile.jpg" alt="Ultha smiling"><em>▶ 30s</em><span><b>Your customer’s OK</b>How approval works before anything goes live.</span></div>
</div><p class="tv-phnote">Short videos from me about how it works. Your customers star in theirs.</p>'''
cs_faq = [
 ('Do my customers have to be on camera?', 'No. Every call becomes written testimonials and stories first. Video is only for customers who want it.'),
 ('Is this a video production company?', 'No film crew and no studio. Customer story videos are recorded remotely and edited by me. UGC-style and tutorial videos are made by me.'),
 ('Who approves what goes live?', 'Your customer approves every quote, story and video before it’s used. Nothing goes live without a yes.'),
 ('Where do we use the content?', 'Your website, sales decks and follow-up emails, LinkedIn, and pages AI search tools read when buyers ask for recommendations.'),
]
cs = hero('Customer stories for SaaS', 'Real customers. <span>Stories buyers trust.</span>',
 'Testimonials, case studies and customer story videos, all from 30-minute remote calls with your customers. Approved by them before anything goes live.', phones)
cs += sec('What you get', 'One customer call. A month of content.', grid([
 ('💬', 'Testimonials', 'Quotes in your customers’ own words, approved by them.'),
 ('📄', 'Case studies', 'Before, after and real numbers your sales team can send.'),
 ('🎬', 'Customer story videos', 'Recorded remotely and edited for your site and sales decks.'),
 ('📱', 'UGC & tutorial videos', 'Short videos I make that show your product in use.'),
 ('🗂️', 'Posts & carousels', 'Ready for LinkedIn and your website, every month.'),
 ('🧰', 'A proof bank for sales', 'Every great quote, sorted by the objection it answers.'),
], 'c3'))
cs += sec('Why it’s different', 'Real customers. No film crew.',
 '<div class="tv-vs"><div><b>Typical testimonial video company</b>$3k–15k per video, a film crew, weeks of scheduling, one video at a time.</div><div><b>With me</b>Remote calls, written and video stories from the same conversation, and honest feedback for your product team too.</div></div>'
 '<p class="sv-note">What customers would change goes into a private brief for your team. <a href="/voice-of-customer">See voice of customer insights →</a></p>')
cs += cta('Want your first customer stories this month?', 'Included in every plan. Case studies and videos can also be booked on their own.')
page('customer-stories', 'Customer stories, case studies & testimonial videos for SaaS · Ultha',
 'Customer stories for SaaS: testimonials, case studies and customer story videos from 30-minute remote calls with your customers. No film crew. Approved by your customers before anything goes live.',
 cs, cs_faq)

# ---------- AI search ----------
stat = '''<div class="sv-stat"><b>29% → 51%</b><p>of software buyers now start research in an AI chatbot</p><small>G2 buyer surveys, 2025 vs 2026</small>
<b>69%</b><p>switched vendors because AI recommended someone else</p><small>G2 Answer Economy report, 2026</small></div>'''
ai_faq = [
 ('Is this the same as generative engine optimization?', 'Yes. You’ll also see it called GEO, answer engine optimization (AEO) or LLM SEO. They all mean helping AI tools find, trust and recommend you.'),
 ('Why does customer proof matter for AI search?', 'AI tools lean on what real customers say: case studies, stories and reviews on many sites. Your own claims count for less than your customers’ words.'),
 ('Can’t I just use AI to write this?', 'AI can write copy. It can’t call your customers. The proof AI tools trust has to come from real people.'),
 ('How long until we show up?', 'Your first stories and pages go live in the first month. Visibility in AI answers builds over the months after.'),
]
ai = hero('AI search optimization for SaaS', 'When buyers ask AI, <span>make sure it names you.</span>',
 'AI tools recommend software based on what real customers say. I turn your customer calls into proof AI can find, then set up your site so it gets cited.', stat)
ai += sec('What AI looks at', 'Three things decide if AI recommends you.', grid([
 ('🗣️', 'What customers say', 'Real stories and results in your customers’ own words.'),
 ('🌐', 'Proof beyond your site', 'Mentions and stories on sites you don’t own.'),
 ('❓', 'Clear answers on your site', 'Pages that answer the questions buyers ask AI.'),
], 'c3'))
ai += sec('What I set up', 'Proof first, then pages AI can read.', '<ul class="sv-list">'
 '<li>Case studies and customer stories<small>from real customer calls</small></li>'
 '<li>Comparison pages<small>you vs the tools buyers compare you with</small></li>'
 '<li>Clear answer sections<small>for the questions buyers type into AI</small></li>'
 '<li>Structured page data<small>so AI tools can read your pages</small></li>'
 '<li>A monthly AI search check<small>is AI naming you yet?</small></li>'
 '<li>Proof your sales team can send<small>the same stories, reused</small></li></ul>'
 '<p class="sv-note">Why this matters now: <a href="/case-studies/the-year-buyers-stopped-googling">The year buyers stopped Googling software first →</a></p>')
ai += cta('Find out if AI recommends you today.', 'AI search setup is part of every plan.')
page('ai-search', 'AI search optimization for SaaS · Ultha',
 'AI search optimization for SaaS startups: turn real customer calls into proof AI tools trust, then set up your site so ChatGPT and Google’s AI answers cite you. Also known as generative engine optimization.',
 ai, ai_faq)
print('built')
