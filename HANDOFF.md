# Handoff: ultha.co site work (paused Oct 22, 2026)

Repo: ulthaugc/ultha-site. Vercel auto-deploys `main` to ultha.co.
Owner: Ultha. Preferences: short punchy copy, casual human tone, options side by side, no corporate words
("aesthetic", "happy", "willing", "awareness", "conversions"), say "AI search" not just ChatGPT,
dark navy theme with white cards for readability, illustrations in the homepage-hero style (navy, light figures,
yellow #FFE29A accents, dotted ground, Caveat handwriting), no fog in new illustrations.
She now says: push straight to main, no preview needed — but render and check desktop (1440) + mobile (390) first.

## Branch with work in progress: `site-v3-wip`
Contains (not yet on main):
- Mobile collapsible menu (`menu.js`, loaded on index, about, guides)
- All Calendly links replaced with /contact ("Let's talk")
- Closing line: "Share a bit about your startup. I'll map out the proof you could have in 30 days."
- Homepage v3 (built by `tools/build_home.py`, already applied to index.html):
  - Stat section: one bold "83% of the buying process happens without you in the room" + 17/83 bar (Gartner)
  - New #how section: 4 illustrated steps (tools/illus.py scenes) + "Watch me explain it" video pill (video coming)
  - Old #loop "How it all works together" section removed
  - New #services tree illustration (roots = services, trunk = trust, fruit = revenue)
  - Pricing moved off homepage → slim #plans strip linking to /pricing
  - Tighter spacing, smaller section H2s, nav "How it works" → #how, "Pricing" → /pricing

## Still to do (her feedback list)
1. Fix tree illustration: G2 chip yellow dot overlaps text; soil band has hard rectangular edges at left/right;
   "grown from real customer conversations" label collides with roots (move it below chips or above soil).
   Check mobile tree (`.tree-m`).
2. Create /pricing page (pricing.html): use tools/pricing_section.html + tools/pricing_css.html, same header/footer
   as about.html, add menu.js, plus a "Good to know" details block under the table (interviews are 15 min,
   customers approve everything, Keep it running only after the 90-Day Engine, content for socials or website,
   custom/one-off work available). Add /pricing to sitemap.xml. Fix about.html nav "/#pricing" → "/pricing", "/#loop" → "/#how".
3. Testimonials section on homepage: keep as is but shorter vertically (partly done via CSS in v3 block).
4. About page: add all 6 testimonials as a visible grid of boxes (no slider). Quotes are in index.html #clients .cp-card.
5. FAQ + footer stay the same.
6. Contact form email via Google Workspace: switch api/contact.js to SMTP (nodemailer, smtp.gmail.com:465)
   using Vercel env vars GMAIL_USER and GMAIL_APP_PASSWORD (she sets these herself in Vercel; needs a Google
   app password, which requires 2-Step Verification). Keep Resend as fallback. Add nodemailer to package.json.
7. Render-check all pages desktop + mobile, then merge to main and confirm the Vercel deploy.

## Pricing (live on main inside index.html today)
Proof Sprint $5,000 one-time, 30 days · 90-Day Proof Engine $6,000/mo · Keep it running $3,500/mo (only after Engine).
Add-ons (no prices): customer interviews, case studies, short-form videos, website optimization for AI search,
webinar or panel cut into shorts. Custom box: "Need something custom? Let's build it around you."
