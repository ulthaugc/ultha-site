/* Mobile menu: adds a menu button to the header on small screens. */
(function () {
  // Prefer a real <nav> of links. Avoid matching homepage .wrap.nav (which also wraps the brand).
  var nav = document.querySelector('.topbar nav, header.site .nav-links, header nav.nav-links, header .nav-links');
  if (!nav) nav = document.querySelector('header .nav');
  if (!nav) return;
  var header = nav.closest('header');
  if (!header) return;
  var root = document.documentElement;
  var isSiteHeader = header.classList.contains('site');

  var css =
    '.mnav-btn,.mnav-panel,.mnav-shade{display:none}' +
    '@media (max-width:760px){' +
    '.mnav-btn{display:inline-flex;align-items:center;justify-content:center;flex:none;width:44px;height:44px;margin-left:8px;border-radius:999px;border:1px solid #D5DFF8;background:#fff;cursor:pointer;padding:0;position:relative;z-index:61}' +
    // Phone: Free review leaves the header bar; it stays as the menu CTA only
    '.mnav-src-cta{display:none!important}' +
    '.mnav-btn span,.mnav-btn span::before,.mnav-btn span::after{display:block;width:18px;height:2px;background:#14213D;border-radius:2px;transition:transform .25s,background .25s,top .25s}' +
    '.mnav-btn span{position:relative}' +
    '.mnav-btn span::before,.mnav-btn span::after{content:"";position:absolute;left:0}' +
    '.mnav-btn span::before{top:-6px}.mnav-btn span::after{top:6px}' +
    '.mnav-open .mnav-btn span{background:transparent}' +
    '.mnav-open .mnav-btn span::before{top:0;transform:rotate(45deg)}' +
    '.mnav-open .mnav-btn span::after{top:0;transform:rotate(-45deg)}' +
    '.mnav-panel{display:block;position:fixed;left:10px;right:10px;z-index:60;background:#FFFFFF;border:1px solid #D5DFF8;border-radius:18px;padding:8px;box-shadow:0 22px 44px -26px rgba(31,79,216,.38);opacity:0;transform:translateY(-8px);pointer-events:none;transition:opacity .2s,transform .2s}' +
    '.mnav-open .mnav-panel{opacity:1;transform:none;pointer-events:auto}' +
    '.mnav-panel a{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;font:500 16px Inter,system-ui,sans-serif;color:#14213D!important;text-decoration:none;border-radius:12px}' +
    '.mnav-panel a:active,.mnav-panel a:hover{background:#EEF3FE}' +
    '.mnav-panel a::after{content:"\\2192";color:#1F4FD8}' +
    '.mnav-panel a+a{border-top:1px solid #D5DFF8}' +
    '.mnav-panel a.mnav-cta{margin-top:8px;border-top:0;background:#1F4FD8;color:#FFFFFF!important;justify-content:center;font-weight:600}' +
    '.mnav-panel a.mnav-cta::after{content:""}' +
    '.mnav-shade{display:block;position:fixed;inset:0;z-index:59;background:rgba(238,243,254,.55);opacity:0;pointer-events:none;transition:opacity .2s}' +
    '.mnav-open .mnav-shade{opacity:1;pointer-events:auto}' +
    '}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  // Only count nav links, not the brand mark inside a wrapping .nav
  var links = [].slice.call(nav.querySelectorAll('a')).filter(function (a) {
    return !a.classList.contains('brand') && !a.closest('.brand');
  });
  if (!links.length) return;
  var cta = links[links.length - 1];
  cta.classList.add('mnav-src-cta');
  var items = links.slice(0, -1).map(function (a) {
    return { href: a.getAttribute('href'), text: a.textContent.trim() };
  });
  // Older topbar pages still surface playbook/guides; homepage (.site) sticks to its desktop nav.
  if (!isSiteHeader) {
    if (!items.some(function (i) { return /starter-kit/.test(i.href || ''); })) {
      items.push({ href: '/starter-kit', text: 'Free playbook' });
    }
    if (!items.some(function (i) { return /guides/.test(i.href || ''); })) {
      items.push({ href: '/guides', text: 'Case studies & guides' });
    }
  }

  var panel = document.createElement('nav');
  panel.className = 'mnav-panel';
  panel.id = 'mnav-panel';
  panel.setAttribute('aria-label', 'Menu');
  items.forEach(function (i) {
    var a = document.createElement('a');
    a.href = i.href;
    a.textContent = i.text;
    panel.appendChild(a);
  });
  var c = document.createElement('a');
  c.href = cta.getAttribute('href');
  c.textContent = cta.textContent.trim();
  c.className = 'mnav-cta';
  panel.appendChild(c);

  var shade = document.createElement('div');
  shade.className = 'mnav-shade';

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'mnav-btn';
  btn.setAttribute('aria-label', 'Open menu');
  btn.setAttribute('aria-expanded', 'false');
  btn.setAttribute('aria-controls', 'mnav-panel');
  btn.innerHTML = '<span></span>';

  // Sit beside the Free review / last CTA inside the nav row
  nav.appendChild(btn);
  document.body.appendChild(shade);
  document.body.appendChild(panel);

  function set(open) {
    if (open) panel.style.top = header.getBoundingClientRect().bottom + 8 + 'px';
    root.classList.toggle('mnav-open', open);
    btn.setAttribute('aria-expanded', String(open));
    btn.setAttribute('aria-label', open ? 'Close menu' : 'Open menu');
  }
  btn.addEventListener('click', function () { set(!root.classList.contains('mnav-open')); });
  shade.addEventListener('click', function () { set(false); });
  panel.addEventListener('click', function (e) { if (e.target.tagName === 'A') set(false); });
  document.addEventListener('keydown', function (e) { if (e.key === 'Escape') set(false); });
  window.addEventListener('resize', function () { if (window.innerWidth > 760) set(false); });
})();
