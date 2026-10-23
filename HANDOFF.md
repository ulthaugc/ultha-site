# Handoff: ultha.co site work (paused Oct 22, 2026)

Repo: ulthaugc/ultha-site. Vercel auto-deploys `main` to ultha.co.
Owner: Ultha. Preferences: short punchy copy, casual human tone, options side by side, no corporate words
("aesthetic", "happy", "willing", "awareness", "conversions"), say "AI search" not just ChatGPT,
dark navy theme with white cards for readability, illustrations in the homepage-hero style (navy, light figures,
yellow #FFE29A accents, dotted ground, Caveat handwriting), no fog in new illustrations.
She now says: push straight to main, no preview needed — but render and check desktop (1440) + mobile (390) first.

## Status (Oct 22, 2026, later): site v3 is LIVE on main
Everything from `site-v3-wip` was merged to main and deployed:
- Mobile collapsible menu (`menu.js`; panel now hidden on desktop, it used to leak as raw links at the page bottom)
- All Calendly links → /contact; closing line "Share a bit about your startup. I'll map out the proof you could have in 30 days." (also on About)
- Homepage v3: 83% stat, #how 4-step journey + video pill, #services tree (dot/soil/label fixed), slim #plans strip → /pricing
- Testimonials: compact on phones (avatar row, left-aligned quote, tighter signature)
- New /pricing page (pricing.html, generated from tools/pricing_section.html + tools/pricing_css.html) with
  "Good to know" cards and Offer JSON-LD. Added to sitemap.xml and llms.txt.
- About: all 6 testimonials as boxes (#reviews), nav → /#how and /pricing, CTA now "Ask me a question →" + playbook link
- api/contact.js sends via Google Workspace SMTP (nodemailer) when GMAIL_USER + GMAIL_APP_PASSWORD are set, else Resend.

## Round 2 (on site-v3-wip, awaiting her OK to merge)
- Stat section compact (83% beside the text, ~half a screen); #services merged into #how under the title
  "Every piece builds trust. Trust grows revenue." with a Caveat bridge line into the tree
- About testimonial boxes and all pricing / Good to know cards switched from white to navy (#22354A); Engine card keeps yellow outline
- impact.com removed from About timeline; starter kit reframed as "Get the playbook I use, free." (kit, contact, footers, llms.txt)
- pricing.html is now regenerated with dark-card overrides (build script lives in the session scratchpad; edit pricing.html directly if needed)

## Still open
1. Ultha: in Vercel → ultha-site → Settings → Environment Variables add GMAIL_USER=ultha@ultha.co and
   GMAIL_APP_PASSWORD=<Google app password> (myaccount.google.com/apppasswords, needs 2-Step Verification), redeploy,
   then send a test from ultha.co/contact. Until then leads only land in Vercel logs.
3. Swap in the real video for the "Watch me explain it" pill when recorded.

## Pricing (live at /pricing)
Proof Sprint $5,000 one-time, 30 days · 90-Day Proof Engine $6,000/mo · Keep it running $3,500/mo (only after Engine).
Add-ons (no prices): customer interviews, case studies, short-form videos, website optimization for AI search,
webinar or panel cut into shorts. Custom box: "Need something custom? Let's build it around you."
