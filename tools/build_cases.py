"""Builds the case study pages in /case-studies from the content below.
Run from the repo root: python3 tools/build_cases.py
Every number here is from the source linked on its page. Keep it that way."""
import html, json

HUB = 'Case studies &amp; guides'

def page(slug, title, meta, dek, kicker, read, hero, body, faq, sources, nxt):
    url = f'https://ultha.co/case-studies/{slug}'
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "Article", "headline": html.unescape(title), "description": meta, "datePublished": "2026-10-23", "dateModified": "2026-10-23",
         "image": "https://ultha.co/og.jpg", "mainEntityOfPage": url,
         "author": {"@type": "Person", "name": "Ultha Niraula", "url": "https://ultha.co/about"},
         "publisher": {"@type": "Person", "name": "Ultha Niraula", "url": "https://ultha.co"}},
        {"@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}]}
    faq_html = ''.join(f'<details><summary>{q}</summary><p>{a}</p></details>' for q, a in faq)
    src_html = ''.join(f'<li><a href="{u}">{t}</a>{d}</li>' for t, u, d in sources)
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Case studies · Ultha</title>
<meta name="description" content="{meta}">
<meta property="og:type" content="article">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{meta}">
<meta property="og:image" content="https://ultha.co/og.jpg">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Young+Serif&amp;family=Figtree:wght@400;500;600;700;800&amp;family=Caveat:wght@600&amp;display=swap">
<link rel="stylesheet" href="/guides/guide.css">
<link rel="stylesheet" href="/case-studies/case.css">
<script type="application/ld+json">{json.dumps(ld, ensure_ascii=False)}</script>
<link rel="stylesheet" href="/scale.css">
<link rel="stylesheet" href="/theme.css">
<link rel="stylesheet" href="/guides/article.css">
<link rel="stylesheet" href="/site-chrome.css">
</head>
<body>
<div class="progress" aria-hidden="true"></div>
<div class="stickybar"><header class="topbar" style="position: relative; z-index: 2; max-width: 1180px; margin: 0 auto; box-sizing: border-box; padding: 22px 24px; display: flex; flex-wrap: wrap; align-items: center; justify-content: space-between; gap: 12px">
<a href="/" style="text-decoration:none;color:inherit;font-family: 'Young Serif', serif; font-size: 22px; letter-spacing: 0.02em; display: inline-flex; align-items: center; gap: 10px"><img src="/ultha-mark.svg" alt="" width="34" height="18">ULTHA</a>
<nav style="display: flex; flex-wrap: wrap; align-items: center; gap: 26px; font-size: 15px">
<a href="/#how" style="text-decoration: none">How it works</a>
<a href="/about" style="text-decoration: none">About</a>
<a href="/pricing" style="text-decoration: none">Pricing</a>
<a href="/guides" style="text-decoration: none">Case studies &amp; guides</a>
<a href="/contact" style="text-decoration: none; background: #1F4FD8; color: #EEF2F6; border-radius: 999px; padding: 9px 18px">Let’s talk</a>
</nav>
</header></div>

<main>
<div class="wrap">
<a class="kicker" href="/guides#case-studies">Case study · {kicker}</a>
<h1>{title}</h1>
<p class="dek">{dek}</p>
<div class="byline"><img src="/img/face.jpg" alt="Ultha Niraula"><span><b>Ultha Niraula</b> · Oct 2026 · {read} min read</span></div>
</div>

<div class="hero" aria-hidden="true">{hero}</div>

<div class="wrap">
{body}

<div class="endcta">
<div>
<b>Want this running for your startup?</b>
<span>I talk to your customers and turn what they say into reviews, stories and videos buyers (and AI search) trust. Or start on your own with the free playbook.</span>
</div>
<div class="btns">
<a class="b1" href="/contact">Let's talk</a>
<a class="b2" href="/starter-kit">Get the free playbook</a>
</div>
</div>

<a class="nextl" href="{nxt[0]}"><span>Next case study</span>{nxt[1]} →</a>

<section class="faq">
<h2>Quick answers</h2>
{faq_html}
</section>

<div class="author">
<img src="/img/face.jpg" alt="Ultha Niraula">
<p><b>Written by Ultha Niraula</b><br>Former product manager and co-founder of a marketing agency that worked with 40+ brands, before going solo. I help startups turn what their customers already say into proof buyers and AI search trust.</p>
</div>

<div class="sources"><b>Sources</b>
<ol>{src_html}</ol>
<p style="margin-top:8px">I didn't work on the companies named here. Company results are as reported in the published case studies linked above.</p></div>
</div>
</main>
<footer style="background: #F9F9FA; color: #14213D">
<div style="max-width: 1180px; margin: 0 auto; padding: 72px 24px 32px; display: flex; flex-direction: column; gap: 48px">
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 24px">
<div class="ft-note"><div style="display: flex; flex-direction: column; gap: 8px; max-width: 520px">
<h2 style="margin: 0; font-family: 'Young Serif', serif; font-weight: 400; font-size: clamp(26px, 3vw, 36px); color: #14213D">Curious where you stand?</h2>
<p style="margin: 0">Share a bit about your startup. I’ll map out the proof you could have in 30 days.</p><span class="ft-sig">— Ultha</span>
</div></div>
<div style="display: flex; flex-direction: column; align-items: flex-start; gap: 10px"><a href="/contact" style="text-decoration: none; background: #1F4FD8; color: #EEF2F6; border-radius: 999px; padding: 14px 26px; font-weight: 500">Let’s talk</a><a href="/starter-kit" style="color: #14213D; font-size: 15px; text-underline-offset: 4px">or get the free playbook →</a></div>
</div>
<div style="display: flex; flex-wrap: wrap; justify-content: space-between; align-items: center; gap: 16px; border-top: 1px solid #99A5C3; padding-top: 24px; font-size: 15px">
<span style="font-family: 'Young Serif', serif; font-size: 20px; color: #14213D; display: inline-flex; align-items: center; gap: 10px"><img src="/ultha-mark-white.svg" alt="" width="30" height="16">ULTHA</span>
<nav style="display: flex; flex-wrap: wrap; gap: 22px"><a href="/#how" style="color: #14213D; text-decoration: none">How it works</a><a href="/about" style="color: #14213D; text-decoration: none">About</a><a href="/pricing" style="color: #14213D; text-decoration: none">Pricing</a><a href="/testimonial-videos" style="color: #14213D; text-decoration: none">Testimonial videos</a><a href="/#faq" style="color: #14213D; text-decoration: none">FAQ</a><a href="/starter-kit" style="color: #14213D; text-decoration: none">Free playbook</a><a href="/guides" style="color: #14213D; text-decoration: none">Case studies &amp; guides</a><a href="/contact" style="color: #14213D; text-decoration: none">Let’s talk</a></nav>
<span>© 2026 Ultha · Santa Barbara, CA</span>
</div>
</div>
</footer>
<script src="/guides/guide.js"></script>
<script>(function(){{var b=document.querySelector(".stickybar");if(!b)return;var f=function(){{b.classList.toggle("scrolled",scrollY>8)}};addEventListener("scroll",f,{{passive:true}});f()}})();</script>
<script src="/menu.js" defer></script>
</body>
</html>
'''

G2_2026 = ('G2, "In the Answer Economy, Don\'t Win the Click, Win the Answer"', 'https://company.g2.com/news/g2-research-the-answer-economy', ', survey of 1,076 B2B software buyers, March 2026 (published April 15, 2026).')
G2_2025 = ('G2, 2025 Buyer Behavior Report, "Proving Value in the Age of AI"', 'https://research.g2.com/cmos-2025-buyer-behavior-report-research-g2', ', 1,100 B2B decision-makers.')
SALESLOFT = ('G2, "How Salesloft drives pipeline with G2"', 'https://sell.g2.com/case-studies/case-study-salesloft-drives-pipeline', ', July 20, 2022.')
MEMORYBLUE = ('G2, "How memoryBlue generated $800K in influenced pipeline in one month"', 'https://sell.g2.com/case-studies/how-memoryblue-generated-800k-in-influenced-pipeline-in-one-month', '.')
GARTNER_26 = ('Gartner, "Gartner Sales Survey Finds 67% of B2B Buyers Prefer a Rep-Free Experience"', 'https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience', ', survey of 646 B2B buyers, Aug to Sept 2025 (published March 9, 2026).')
GARTNER_25 = ('Gartner, "Gartner Sales Survey Finds 61% of B2B Buyers Prefer a Rep-Free Buying Experience"', 'https://www.gartner.com/en/newsroom/press-releases/2025-06-25-gartner-sales-survey-finds-61-percent-of-b2b-buyers-prefer-a-rep-free-buying-experience', ', survey of 632 B2B buyers, Aug to Sept 2024 (published June 25, 2025).')
GARTNER_17 = ('Gartner, "The B2B Buying Journey"', 'https://www.gartner.com/en/sales/insights/b2b-buying-journey', '.')
FORRESTER = ('Forrester, "B2B Buyer Adoption Of Generative AI"', 'https://www.forrester.com/report/b2b-buyer-adoption-of-generative-ai/RES181769', ', from Forrester\'s Buyers\' Journey Survey, 2024.')

# ---------- shared hero art (light guide style) ----------
def hero_reviews():
    return '''<svg viewBox="0 0 900 360">
<defs><filter id="b"><feGaussianBlur stdDeviation="18"/></filter></defs>
<path d="M0 290 Q220 250 450 280 T900 270 V360 H0Z" fill="#A9B5D2"/>
<ellipse cx="450" cy="290" rx="380" ry="40" fill="#14213D" filter="url(#b)" opacity=".12"/>
<g font-family="Figtree,sans-serif">
<g transform="translate(80 60)"><rect width="250" height="76" rx="16" fill="#F5F5F5" stroke="#99A5C3" stroke-width="1.5"/><text x="18" y="30" font-size="15" fill="#FFC94D">★★★★★</text><g stroke="#99A5C3" stroke-width="5" stroke-linecap="round"><line x1="18" y1="48" x2="220" y2="48"/><line x1="18" y1="62" x2="170" y2="62"/></g></g>
<g transform="translate(110 152)"><rect width="250" height="76" rx="16" fill="#F5F5F5" stroke="#99A5C3" stroke-width="1.5"/><text x="18" y="30" font-size="15" fill="#FFC94D">★★★★★</text><g stroke="#99A5C3" stroke-width="5" stroke-linecap="round"><line x1="18" y1="48" x2="210" y2="48"/><line x1="18" y1="62" x2="150" y2="62"/></g></g>
<path d="M390 150 C450 130 480 130 530 140" fill="none" stroke="#1F4FD8" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round"/><path d="M522 130 l12 10 l-14 6" fill="none" stroke="#1F4FD8" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
<g transform="translate(560 50)"><rect width="270" height="200" rx="18" fill="#14213D"/><text x="22" y="36" font-size="12" letter-spacing="2" fill="#A9B5D2">PIPELINE</text>
<rect x="22" y="150" width="34" height="30" rx="5" fill="#2E4170"/><rect x="70" y="128" width="34" height="52" rx="5" fill="#2E4170"/><rect x="118" y="104" width="34" height="76" rx="5" fill="#3D5AA8"/><rect x="166" y="76" width="34" height="104" rx="5" fill="#1F4FD8"/><rect x="214" y="52" width="34" height="128" rx="5" fill="#FFC94D"/></g>
</g>
<text x="80" y="270" font-family="Caveat,cursive" font-size="26" fill="#E9604B">customers talking…</text>
<text x="640" y="290" font-family="Caveat,cursive" font-size="26" fill="#14213D">…deals moving</text>
</svg>'''

def hero_ai():
    return '''<svg viewBox="0 0 900 360">
<defs><filter id="b"><feGaussianBlur stdDeviation="18"/></filter></defs>
<path d="M0 290 Q220 250 450 280 T900 270 V360 H0Z" fill="#A9B5D2"/>
<ellipse cx="450" cy="290" rx="380" ry="40" fill="#14213D" filter="url(#b)" opacity=".12"/>
<g font-family="Figtree,sans-serif">
<g transform="translate(90 70)" opacity=".55"><rect width="260" height="44" rx="22" fill="#F5F5F5" stroke="#99A5C3" stroke-width="1.5"/><text x="20" y="28" font-size="15" fill="#424A5E">🔍 best tool for my team</text><g stroke="#99A5C3" stroke-width="5" stroke-linecap="round"><line x1="10" y1="70" x2="230" y2="70"/><line x1="10" y1="90" x2="200" y2="90"/><line x1="10" y1="110" x2="220" y2="110"/></g><text x="10" y="150" font-family="Caveat,cursive" font-size="24" fill="#E9604B">2025: start here</text></g>
<g transform="translate(470 40)"><rect width="340" height="220" rx="20" fill="#14213D"/><rect x="20" y="20" width="230" height="40" rx="20" fill="#2E4170"/><text x="38" y="45" font-size="14" fill="#EEF2F6">Which tool should we buy?</text>
<rect x="70" y="76" width="250" height="122" rx="18" fill="#1F4FD8"/><text x="90" y="104" font-size="13" fill="#EEF2F6">Top picks, based on reviews:</text>
<g font-size="14" fill="#fff"><text x="90" y="130">1. Vendor A ★ 4.8</text><text x="90" y="152">2. Vendor B ★ 4.7</text><text x="90" y="174" fill="#FFC94D">3. You? ?</text></g></g>
</g>
<text x="560" y="300" font-family="Caveat,cursive" font-size="26" fill="#14213D">2026: start here</text>
</svg>'''

def hero_habit():
    cells = ''
    for i in range(8):
        x = 70 + i * 96
        h = 40 + i * 22
        cells += f'<rect x="{x}" y="{250-h}" width="62" height="{h}" rx="8" fill="{"#FFC94D" if i==7 else ("#1F4FD8" if i>3 else "#99A5C3")}"/><text x="{x+31}" y="276" text-anchor="middle" font-family="Figtree,sans-serif" font-size="13" fill="#424A5E">Q{i+1}</text>'
    return f'''<svg viewBox="0 0 900 360">
<path d="M0 300 Q220 270 450 292 T900 284 V360 H0Z" fill="#A9B5D2"/>
{cells}
<path d="M90 190 C300 160 520 110 820 40" fill="none" stroke="#E9604B" stroke-width="3" stroke-dasharray="6 8" stroke-linecap="round"/>
<text x="560" y="70" font-family="Caveat,cursive" font-size="28" fill="#E9604B">reviews keep stacking</text>
<text x="70" y="326" font-family="Caveat,cursive" font-size="24" fill="#14213D">8 quarters in a row, one small ask at a time</text>
</svg>'''

def nums(items):
    return '<div class="nums">' + ''.join(f'<div><span class="n">{n}</span><span>{t}</span><small>{s}</small></div>' for n, t, s in items) + '</div>'

def table(head, rows, hi_col=None):
    th = ''.join(f'<th>{h}</th>' for h in head)
    tr = ''
    for r in rows:
        hi = ' class="hi"'
        cells = f'<th scope="row">{r[0]}</th>' + ''.join(f'<td data-h="{head[i + 1]}"{hi if hi_col == i + 1 else ""}>{c}</td>' for i, c in enumerate(r[1:]))
        tr += f'<tr>{cells}</tr>'
    return f'<div class="cmpw"><table class="cmp"><thead><tr>{th}</tr></thead><tbody>{tr}</tbody></table></div>'

# ---------- 1. Salesloft ----------
CS1_BODY = f'''<p class="note">I didn't work with Salesloft. This is a breakdown of their published case study, so you can see what happens when someone treats customer proof like a system instead of a one-off ask.</p>

<div class="tldr">
<b class="t">The short version</b>
<ul>
<li>Salesloft had been on G2 since 2014, but nobody owned reviews until 2018.</li>
<li>They started asking on a schedule, thanked every reviewer, answered every review and put the best quotes in their sales team's hands.</li>
<li>Reported result: <b>$1.82M in pipeline</b> and <b>$781K in revenue</b> tied to G2, with an <b>85% response rate</b> on review asks.</li>
</ul>
</div>

<h2>Happy customers, quiet proof</h2>
<p>Salesloft makes sales software and had plenty of users who liked it. They'd had a G2 profile for years. What they didn't have was a plan. Reviews came in when they came in.</p>
<p>That changed in 2018, when Alexandria Snow joined as product marketing director and decided customer voice should be part of how they sell, not just a badge on the website.</p>

<h2>What they did</h2>
<ol class="steps">
<li><b>Asked on a schedule</b><p>They picked customers likely to review, and G2 sent a planned series of emails linking to Salesloft's review page. Snow added personal emails on top.</p></li>
<li><b>Thanked everyone, whatever they said</b><p>Reviewers got a gift card as a thank-you, no matter what they wrote. That keeps reviews honest, which is exactly why buyers trust them.</p></li>
<li><b>Put reviews in sales' hands</b><p>They turned reviews into a "Customer Story Flipbook," used them in sales decks and featured them on their website. Snow called the flipbook one of their most popular sales tools.</p></li>
<li><b>Answered every review, even the bad ones</b><p>The team replied to reviews and worked directly with unhappy customers to fix problems. A good reply to a bad review can do more than another 5-star one.</p></li>
</ol>

<h2>The numbers</h2>
{nums([("85%", "response rate on their review requests", "G2 case study, 2022"),
       ("$1.82M", "in pipeline driven by G2", "G2 case study, 2022"),
       ("$781K", "in revenue directly influenced by G2", "G2 case study, 2022"),
       ("2,600+", "reviews, with a 4.8 out of 5 rating", "G2 case study, 2022")])}
<p>And Snow said those numbers undersell it, because G2 had a touchpoint in essentially every deal. Reviews weren't a marketing side project. They showed up in sales conversations everywhere.</p>

<div class="now">
<span class="t">Why this matters more now</span>
<h3>In 2022, reviews helped buyers who visited G2. In 2026, AI reads them for everyone.</h3>
<ul>
<li><b>51%</b> of software buyers now start research in an AI chatbot more often than Google. A year earlier it was <b>29%</b>.</li>
<li>Buyers say citations from review sites are their <b>top trust signal</b> when AI recommends a vendor.</li>
<li>AI tools lean on <b>recent</b> reviews. A pile of reviews from years ago fades, so the reviews you collect this quarter are the ones AI reads next quarter.</li>
</ul>
<small>Source: G2, survey of 1,076 B2B software buyers, March 2026.</small>
</div>

<h2>What this looks like for a startup</h2>
<p>You don't need 2,600 reviews or a product marketing team. You need the same four habits, sized for a team where the founder still answers support tickets.</p>
{table(["", "What Salesloft did", "The startup version"], [
    ["Who asks", "Product marketing director, plus a G2 email campaign", "One owner (you, or me), with a short list of happy customers"],
    ["How", "Scheduled emails and personal notes", "Short customer calls first, then an easy review link"],
    ["Where proof goes", "Sales flipbook, decks, website", "A proof bank your sales team can grab from, plus your homepage and G2"],
    ["Bad reviews", "Answered and fixed with the customer", "Answered within a week, in a human voice"],
    ["What it led to", "$1.82M pipeline, $781K revenue (reported)", "Proof that shows up when buyers and AI search look"],
], hi_col=2)}
'''
CS1_FAQ = [
    ("Did Salesloft pay for reviews?", "They gave reviewers a gift card as a thank-you, and it was given no matter what the review said. That's different from paying for positive reviews, which review sites don't allow."),
    ("How many reviews does a startup need?", "There's no magic number. Start with your happiest customers and keep reviews coming every month. Recent, detailed reviews count for more than a big old pile."),
    ("Why do reviews matter for AI search?", "AI tools pull from sites that aren't yours, like review sites, when they answer 'what's the best tool for X?' In G2's 2026 survey, buyers named review-site citations as their top trust signal in AI answers."),
]

# ---------- 2. AI shortlist ----------
CS2_BODY = f'''<p class="note">This one is a market case study. Instead of one company, it follows what happened to software buying in a single year, using big buyer surveys from G2, Gartner and Forrester.</p>

<div class="tldr">
<b class="t">The short version</b>
<ul>
<li>In March 2026, <b>51%</b> of software buyers started research in an AI chatbot more often than Google. A year earlier it was <b>29%</b>.</li>
<li><b>69%</b> ended up picking a different vendor than they planned because of a chatbot's answer. <b>1 in 3</b> bought from a vendor they'd never heard of.</li>
<li>AI answers lean on reviews and real customer stories. If yours are thin, you're less likely to be named, and you may never know you lost the deal.</li>
</ul>
</div>

<h2>What changed in one year</h2>
<p>Most buying shifts take a decade. This one took about twelve months. Here's the same question asked a year apart.</p>
{table(["", "Before", "Now", "Source"], [
    ["Start research in an AI chatbot more often than Google", "29%", "<span class='up'>51%</span>", "G2, 2025 vs 2026 surveys"],
    ["Prefer buying with no sales rep at all", "61%", "<span class='up'>67%</span>", "Gartner, surveyed 2024 vs 2025"],
    ["Say AI research is more productive than Google", "36%", "<span class='up'>53%</span>", "G2, seven months apart"],
], hi_col=2)}
<p>And it isn't a niche habit. In Forrester's 2024 survey, <b>89%</b> of B2B buyers had already used generative AI in at least one part of their buying process.</p>

<h2>The deals you never hear about</h2>
<p>Here's the part that should worry any founder. When buyers ask AI for recommendations, they act on the answer.</p>
{nums([("69%", "chose a different vendor than they first planned because it showed up in a chatbot's recommendation", "G2, March 2026"),
       ("1 in 3", "bought from a vendor they had never heard of before", "G2, March 2026"),
       ("85%", "think more highly of a vendor when AI includes it in an answer", "G2, March 2026"),
       ("#1", "AI chatbots became the top source shaping vendor shortlists, just ahead of review sites", "G2, 2025 Buyer Behavior Report")])}
<p>Put that next to Gartner's finding that buyers spend only <b>17%</b> of their buying time talking to vendors at all. The shortlist gets written in the other 83%, and more and more of that is a conversation with AI. If you're not in the answer, you're often out before anyone books a call.</p>

<h2>Where AI gets its answers</h2>
<p>AI tools don't take your word for it. They look for what other people say about you.</p>
<ul class="plain">
<li><b>Review sites carry weight.</b> Buyers say citations from software review sites are their top trust signal in AI answers.</li>
<li><b>Thin proof makes AI hesitate.</b> A weak review presence makes AI less confident, and less likely to recommend you.</li>
<li><b>Fresh beats old.</b> Marketers are now prioritizing review recency and volume, because models increasingly favor recent reviews.</li>
<li><b>Consistency builds trust.</b> Buyers see it as a good sign when ChatGPT, Gemini and Claude all describe a vendor the same way.</li>
</ul>

<div class="now">
<span class="t">Why waiting is expensive</span>
<h3>The shift happened during this buying cycle, not some future one.</h3>
<ul>
<li>Buyers who start in a chatbot form a shortlist <b>before</b> they ever visit your site.</li>
<li>Proof takes time to build up. Every quarter you wait is a quarter of reviews and stories your competitors collect and you don't.</li>
<li>With <b>1 in 3</b> buyers picking a vendor they'd never heard of, being unknown isn't safe anymore. Someone else is happy to be the name AI suggests.</li>
</ul>
<small>Sources: G2 (March 2026), Gartner, Forrester.</small>
</div>

<h2>What buyers do now, and what they need to find</h2>
{table(["What the buyer does", "What they find if you've built proof", "What they find if you haven't"], [
    ["Asks a chatbot for the best tool", "Your name, with reviews behind it", "Your competitors"],
    ["Checks review sites", "Recent, detailed reviews from people like them", "A few old reviews, or none"],
    ["Visits your site", "Customer stories with real numbers", "Claims only you are making"],
    ["Brings it to their team", "Quotes and videos they can forward", "Nothing to share"],
], hi_col=1)}
'''
CS2_FAQ = [
    ("Is Google still worth it for B2B software?", "Yes. In G2's 2026 survey, 61% of buyers used AI search alongside Google. The point isn't to drop Google. It's to make sure that when buyers ask AI, you're part of the answer too."),
    ("How do I get my startup mentioned by ChatGPT?", "Give it real things to read about you on sites you don't own: recent reviews, customer stories and comparisons. AI tools trust what customers say about you more than what you say about yourself."),
    ("Do these numbers apply to startups or just big companies?", "The surveys cover B2B software buyers across company sizes. The habit of asking AI first applies no matter who you're selling to, and smaller vendors gain the most when buyers are open to names they've never heard of."),
]

# ---------- 3. memoryBlue ----------
CS3_BODY = f'''<p class="note">I didn't work with memoryBlue. This breakdown comes from their published G2 case study. It's a good example of the slow, steady version of customer proof, the kind you can't rush later.</p>

<div class="tldr">
<b class="t">The short version</b>
<ul>
<li>memoryBlue, a B2B sales development firm, asks for reviews at customer milestones and alongside its quarterly customer survey.</li>
<li>It always has a review campaign running, and its delivery teams compete on a leaderboard.</li>
<li>Reported result: <b>300+ verified reviews</b>, Leader status in two categories for <b>8 quarters in a row</b>, and <b>$800K in influenced pipeline</b> tracked in a single month.</li>
</ul>
</div>

<h2>Not one big push</h2>
<p>A lot of companies treat reviews like spring cleaning: one big burst, then nothing for a year. memoryBlue went the other way. They built small asks into moments that were already happening.</p>

<h2>The habit, in four parts</h2>
<ol class="steps">
<li><b>Ask at the happy moments</b><p>Review requests go out at customer milestones, when results are fresh and the customer is most likely to say yes.</p></li>
<li><b>Ride along with the survey</b><p>Asks are synced with the quarterly customer satisfaction survey, so customers who just gave a high score get an easy next step.</p></li>
<li><b>Make it a team sport</b><p>Delivery teams compete on a review leaderboard. The people closest to customers own the ask, not just marketing.</p></li>
<li><b>Never switch it off</b><p>At least one review campaign is always running, and G2 is connected to their CRM so they can see which deals reviews touched.</p></li>
</ol>

<h2>The numbers</h2>
{nums([("$800K", "in influenced pipeline, tracked in one month", "G2 case study"),
       ("300+", "verified reviews to date", "G2 case study"),
       ("8 quarters", "in a row as a Leader in two core categories", "G2 case study"),
       ("5", "G2 categories where they show up", "G2 case study")])}

<div class="pull">Eight quarters in a row is two years of steady asking. That's the part you can't buy in a month.<small>My take on memoryBlue's results</small></div>

<div class="now">
<span class="t">Why the timing matters</span>
<h3>Proof compounds. The clock starts the day you start.</h3>
<ul>
<li>Buyers spend only <b>17%</b> of their buying time talking to vendors. The rest is research, and that's where reviews and stories do the selling.</li>
<li>For enterprise buyers, review sites are the <b>#1 research source (56%)</b>, just ahead of AI search (55%).</li>
<li>AI tools increasingly favor <b>recent</b> reviews. A steady habit keeps you fresh. A one-time push goes stale.</li>
</ul>
<small>Sources: Gartner; G2 2025 Buyer Behavior Report; G2, March 2026.</small>
</div>

<h2>Start now, or start next year</h2>
<p>Same company, same customers. The only difference is when the habit starts.</p>
{table(["", "Start this quarter", "Start next year"], [
    ["Reviews", "A year of fresh reviews AI can read", "Starting from zero while competitors have a year's head start"],
    ["Customer stories", "Stories your sales team uses in every deal", "Sales still telling buyers to 'trust us'"],
    ["Category rankings", "Consecutive quarters adding up", "The streak hasn't started"],
    ["AI answers", "A real chance to be the name AI suggests", "Hoping buyers find you some other way"],
], hi_col=1)}
'''
CS3_FAQ = [
    ("When is the best time to ask a customer for a review?", "Right after a win: a milestone, a great support moment, or a high score on your satisfaction survey. That's when results are fresh and saying yes feels easy."),
    ("Should sales or marketing own reviews?", "Whoever is closest to the customer. memoryBlue gave the ask to its delivery teams and made it a friendly competition, which kept reviews coming without a big campaign."),
    ("How do I know if reviews are helping sales?", "Connect your review platform to your CRM if you can, and ask new customers what they read before buying. memoryBlue tracked $800K in influenced pipeline in one month this way."),
]

PAGES = [
    ('salesloft-reviews-pipeline', 'How Salesloft turned customer reviews into $1.8M in pipeline',
     'Salesloft started asking customers for reviews on a schedule and gave the best ones to its sales team. Reported result: $1.82M in pipeline and $781K in revenue. Here is what they did and why it matters more in 2026.',
     'They had thousands of users who liked the product. Things changed when they started asking them on purpose, and handed the answers to sales.',
     'Reviews', 6, hero_reviews(), CS1_BODY, CS1_FAQ, [SALESLOFT, G2_2026],
     ('/case-studies/the-year-buyers-stopped-googling', 'The year buyers stopped Googling software first')),
    ('the-year-buyers-stopped-googling', 'The year buyers stopped Googling software first',
     'In one year, the share of software buyers who start research in an AI chatbot jumped from 29% to 51%. 69% switched vendors because of a chatbot answer. What changed, and why waiting is risky.',
     'In twelve months, software buyers moved their research from Google to AI chatbots. Here is what changed, and what it means if AI doesn\'t know your name.',
     'AI search', 6, hero_ai(), CS2_BODY, CS2_FAQ, [G2_2026, G2_2025, GARTNER_26, GARTNER_25, FORRESTER, GARTNER_17],
     ('/case-studies/memoryblue-always-on-reviews', 'memoryBlue: $800K in pipeline from a steady review habit')),
    ('memoryblue-always-on-reviews', 'memoryBlue: $800K in pipeline from a steady review habit',
     'memoryBlue asks for reviews at customer milestones, keeps a campaign always running and tracked $800K in influenced pipeline in one month. Why steady proof beats one big push.',
     'Not one big push. Small, steady asks at the moments customers were already happy, kept up quarter after quarter.',
     'Review habit', 5, hero_habit(), CS3_BODY, CS3_FAQ, [MEMORYBLUE, GARTNER_17, G2_2025, G2_2026],
     ('/case-studies/salesloft-reviews-pipeline', 'How Salesloft turned customer reviews into $1.8M in pipeline')),
]

if __name__ == '__main__':
    for p in PAGES:
        open(f'case-studies/{p[0]}.html', 'w').write(page(*p))
        print('wrote', p[0])
