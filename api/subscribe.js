// Starter kit signups.
// If MAILERLITE_API_KEY (and optionally MAILERLITE_GROUP_ID) are set in Vercel
// project env vars, subscribers are added to MailerLite. Every signup is also
// logged so nothing is lost while the email tool is being set up.
export default async function handler(req, res) {
  if (req.method !== 'POST') {
    res.setHeader('Allow', 'POST');
    return res.status(405).json({ ok: false });
  }
  const body = typeof req.body === 'string' ? Object.fromEntries(new URLSearchParams(req.body)) : (req.body || {});
  const email = String(body.email || '').trim().toLowerCase();
  const name = String(body.name || '').trim().slice(0, 80);
  const company = String(body.company || '');
  const wantsJson = (req.headers['accept'] || '').includes('application/json');

  if (company) return wantsJson ? res.json({ ok: true }) : res.redirect(303, '/kit?welcome=1'); // honeypot
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 200) {
    return wantsJson ? res.status(400).json({ ok: false, error: 'Please enter a valid email.' }) : res.redirect(303, '/starter-kit?error=email');
  }

  console.log('starter-kit signup', JSON.stringify({ email, name, at: new Date().toISOString() }));

  const key = process.env.MAILERLITE_API_KEY;
  if (key) {
    try {
      const payload = { email, fields: { name } };
      if (process.env.MAILERLITE_GROUP_ID) payload.groups = [process.env.MAILERLITE_GROUP_ID];
      const r = await fetch('https://connect.mailerlite.com/api/subscribers', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', Accept: 'application/json', Authorization: `Bearer ${key}` },
        body: JSON.stringify(payload),
      });
      if (!r.ok) console.error('mailerlite error', r.status, await r.text());
    } catch (e) {
      console.error('mailerlite request failed', e);
    }
  }
  return wantsJson ? res.json({ ok: true }) : res.redirect(303, '/kit?welcome=1');
}
