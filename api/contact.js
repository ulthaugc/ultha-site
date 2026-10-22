// Contact form ("Let's talk") submissions.
// Every submission is logged (Vercel → Logs) so nothing is lost.
// If RESEND_API_KEY is set, it's also emailed to CONTACT_TO (default ultha@ultha.co),
// with Reply-To set to the founder so you can just hit Reply.
const esc = (s) => String(s || '').replace(/[&<>"]/g, (c) => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;' }[c]));

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false });
  }
  const b = typeof req.body === 'string' ? JSON.parse(req.body || '{}') : (req.body || {});
  if (b.company) return res.json({ ok: true }); // honeypot

  const name = String(b.name || '').trim().slice(0, 100);
  const email = String(b.email || '').trim().toLowerCase().slice(0, 200);
  const website = String(b.website || '').trim().slice(0, 200);
  const stage = String(b.stage || '').slice(0, 40);
  const tier = String(b.tier || '').slice(0, 60);
  const needs = (Array.isArray(b.needs) ? b.needs : []).map((n) => String(n).slice(0, 60)).slice(0, 15);
  const message = String(b.message || '').trim().slice(0, 4000);

  if (!name) return res.status(400).json({ ok: false, error: 'Please add your name.' });
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) return res.status(400).json({ ok: false, error: 'Please enter a valid email.' });

  const lead = { name, email, website, stage, tier, needs, message, at: new Date().toISOString() };
  console.log('contact lead', JSON.stringify(lead));

  const key = process.env.RESEND_API_KEY;
  if (key) {
    const rows = [['Name', name], ['Email', email], ['Website', website], ['Stage', stage], ['Interested in', needs.join(', ')], ['Plan', tier]]
      .filter(([, v]) => v)
      .map(([k, v]) => `<tr><td style="padding:4px 12px 4px 0;color:#5A6B79">${k}</td><td style="padding:4px 0"><b>${esc(v)}</b></td></tr>`).join('');
    const html = `<div style="font-family:Arial,sans-serif;color:#1B2A38"><h2 style="margin:0 0 12px">New lead from ultha.co 🏮</h2><table>${rows}</table>${message ? `<p style="margin-top:16px;padding:12px;background:#EEF1F2;border-radius:8px;white-space:pre-wrap">${esc(message)}</p>` : ''}<p style="color:#5A6B79;font-size:13px">Hit Reply to answer ${esc(name)} directly.</p></div>`;
    try {
      const r = await fetch('https://api.resend.com/emails', {
        method: 'POST',
        headers: { Authorization: `Bearer ${key}`, 'Content-Type': 'application/json' },
        body: JSON.stringify({
          from: process.env.CONTACT_FROM || 'ultha.co <onboarding@resend.dev>',
          to: [process.env.CONTACT_TO || 'ultha@ultha.co'],
          reply_to: email,
          subject: `New lead: ${name}${website ? ' · ' + website : ''}`,
          html,
        }),
      });
      if (!r.ok) console.error('resend error', r.status, await r.text());
    } catch (e) {
      console.error('resend request failed', e);
    }
  }
  return res.json({ ok: true });
}
