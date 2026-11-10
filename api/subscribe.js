// Field Notes newsletter signups (Kit / ConvertKit API v4).
// Requires KIT_API_KEY in Vercel. Optionally KIT_FORM_ID and/or KIT_TAG_ID
// to add the subscriber to a Kit form or tag after create/upsert.
// If KIT_API_KEY is missing, the signup is still logged and we return ok
// so the form does not break while Kit is being set up.
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
  const isPreview = process.env.VERCEL_ENV === 'preview';
  const dbg = [];
  const thanksBase = '/field-notes?welcome=1';
  const thanksUrl = () => isPreview && dbg.length ? `${thanksBase}&kit=${encodeURIComponent(dbg.join(','))}` : thanksBase;
  const failEmail = '/field-notes?error=email';

  if (company) return wantsJson ? res.json({ ok: true, ...(isPreview ? { kit: dbg } : {}) }) : res.redirect(303, thanksUrl()); // honeypot
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email) || email.length > 200) {
    return wantsJson ? res.status(400).json({ ok: false, error: 'Please enter a valid email.' }) : res.redirect(303, failEmail);
  }

  console.log('field-notes signup', JSON.stringify({ email, name, at: new Date().toISOString() }));

  const key = process.env.KIT_API_KEY;
  dbg.push('key:' + (key ? 'yes' : 'no'), 'form:' + (process.env.KIT_FORM_ID ? 'yes' : 'no'));
  if (!key) {
    console.warn('KIT_API_KEY not set; signup logged only');
    return wantsJson ? res.json({ ok: true, ...(isPreview ? { kit: dbg } : {}) }) : res.redirect(303, thanksUrl());
  }

  const headers = {
    'Content-Type': 'application/json',
    Accept: 'application/json',
    'X-Kit-Api-Key': key,
  };

  try {
    const createRes = await fetch('https://api.kit.com/v4/subscribers', {
      method: 'POST',
      headers,
      body: JSON.stringify({
        email_address: email,
        ...(name ? { first_name: name } : {}),
      }),
    });
    const createText = await createRes.text();
    let createJson = null;
    try { createJson = createText ? JSON.parse(createText) : null; } catch (_) {}

    dbg.push('create:' + createRes.status + (createJson && createJson.subscriber ? ':' + createJson.subscriber.state : ''));
    if (createRes.status === 401 && process.env.KIT_FORM_ID) {
      // Key may be an older v3 key: v3 subscribes straight to a form with api_key in the body.
      try {
        const v3 = await fetch(`https://api.convertkit.com/v3/forms/${encodeURIComponent(process.env.KIT_FORM_ID)}/subscribe`, {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify({ api_key: key, email, ...(name ? { first_name: name } : {}) }),
        });
        dbg.push('v3:' + v3.status);
        if (!v3.ok) console.error('kit v3 subscribe error', v3.status, await v3.text());
      } catch (e) {
        console.error('kit v3 subscribe failed', e);
        dbg.push('v3:error');
      }
      return wantsJson ? res.json({ ok: true, ...(isPreview ? { kit: dbg } : {}) }) : res.redirect(303, thanksUrl());
    }
    if (!createRes.ok) {
      console.error('kit create subscriber error', createRes.status, createText);
      // Still return ok so the visitor gets a friendly thanks; signup is logged above.
      return wantsJson ? res.json({ ok: true, ...(isPreview ? { kit: dbg } : {}) }) : res.redirect(303, thanksUrl());
    }

    const subscriberId = createJson && createJson.subscriber && createJson.subscriber.id;
    const referrer = String(req.headers.referer || req.headers.referrer || 'https://ultha.co/field-notes');

    const formId = process.env.KIT_FORM_ID;
    if (formId && subscriberId) {
      try {
        const fr = await fetch(`https://api.kit.com/v4/forms/${encodeURIComponent(formId)}/subscribers/${subscriberId}`, {
          method: 'POST',
          headers,
          body: JSON.stringify({ referrer }),
        });
        dbg.push('addform:' + fr.status);
        if (!fr.ok) console.error('kit add to form error', fr.status, await fr.text());
      } catch (e) {
        console.error('kit add to form failed', e);
      }
    }

    const tagId = process.env.KIT_TAG_ID;
    if (tagId && subscriberId) {
      try {
        const tr = await fetch(`https://api.kit.com/v4/tags/${encodeURIComponent(tagId)}/subscribers/${subscriberId}`, {
          method: 'POST',
          headers,
          body: JSON.stringify({}),
        });
        if (!tr.ok) console.error('kit tag subscriber error', tr.status, await tr.text());
      } catch (e) {
        console.error('kit tag subscriber failed', e);
      }
    }
  } catch (e) {
    console.error('kit request failed', e);
    dbg.push('error:' + String(e && e.message || e).slice(0, 60));
  }

  return wantsJson ? res.json({ ok: true, ...(isPreview ? { kit: dbg } : {}) }) : res.redirect(303, thanksUrl());
}
