/* Mobile menu: adds a menu button to the header on small screens. */
(function () {
  var nav = document.querySelector('.topbar nav, header .nav');
  if (!nav) return;
  var header = nav.closest('header');
  var root = document.documentElement;

  var css =
    '.mnav-btn,.mnav-panel,.mnav-shade{display:none}' +
    '@media (max-width:760px){' +
    'header nav,header .nav{margin-left:auto}' +
    '.mnav-btn{display:inline-flex;align-items:center;justify-content:center;flex:none;width:44px;height:44px;margin-left:10px;border-radius:999px;border:1px solid rgba(198,211,219,.32);background:transparent;cursor:pointer;padding:0;position:relative;z-index:61}' +
    '.mnav-btn span,.mnav-btn span::before,.mnav-btn span::after{display:block;width:18px;height:2px;background:#EEF1F2;border-radius:2px;transition:transform .25s,background .25s,top .25s}' +
    '.mnav-btn span{position:relative}' +
    '.mnav-btn span::before,.mnav-btn span::after{content:"";position:absolute;left:0}' +
    '.mnav-btn span::before{top:-6px}.mnav-btn span::after{top:6px}' +
    '.mnav-open .mnav-btn span{background:transparent}' +
    '.mnav-open .mnav-btn span::before{top:0;transform:rotate(45deg)}' +
    '.mnav-open .mnav-btn span::after{top:0;transform:rotate(-45deg)}' +
    '.mnav-panel{display:block;position:fixed;left:10px;right:10px;z-index:60;background:#111C27;border:1px solid rgba(198,211,219,.16);border-radius:22px;padding:8px;box-shadow:0 24px 50px rgba(0,0,0,.55);opacity:0;transform:translateY(-8px);pointer-events:none;transition:opacity .2s,transform .2s}' +
    '.mnav-open .mnav-panel{opacity:1;transform:none;pointer-events:auto}' +
    '.mnav-panel a{display:flex;justify-content:space-between;align-items:center;padding:14px 16px;font:500 17px Figtree,system-ui,sans-serif;color:#EEF1F2!important;text-decoration:none;border-radius:14px}' +
    '.mnav-panel a:active,.mnav-panel a:hover{background:#1B2A38}' +
    '.mnav-panel a::after{content:"\\2192";color:#FFE29A}' +
    '.mnav-panel a+a{border-top:1px solid rgba(198,211,219,.08)}' +
    '.mnav-panel a.mnav-cta{margin-top:8px;border-top:0;background:#FFE29A;color:#1B2A38!important;justify-content:center;font-weight:600}' +
    '.mnav-panel a.mnav-cta::after{content:""}' +
    '.mnav-shade{display:block;position:fixed;inset:0;z-index:59;background:rgba(8,13,19,.5);opacity:0;pointer-events:none;transition:opacity .2s}' +
    '.mnav-open .mnav-shade{opacity:1;pointer-events:auto}' +
    '}';
  var st = document.createElement('style');
  st.textContent = css;
  document.head.appendChild(st);

  var links = [].slice.call(nav.querySelectorAll('a'));
  var cta = links[links.length - 1];
  var items = links.slice(0, -1).map(function (a) { return { href: a.getAttribute('href'), text: a.textContent.trim() }; });
  if (!items.some(function (i) { return /starter-kit/.test(i.href); })) items.push({ href: '/starter-kit', text: 'Free playbook' });
  if (!items.some(function (i) { return /guides/.test(i.href); })) items.push({ href: '/guides', text: 'Guides' });

  var panel = document.createElement('nav');
  panel.className = 'mnav-panel';
  panel.id = 'mnav-panel';
  panel.setAttribute('aria-label', 'Menu');
  items.forEach(function (i) {
    var a = document.createElement('a');
    a.href = i.href; a.textContent = i.text;
    panel.appendChild(a);
  });
  var c = document.createElement('a');
  c.href = cta.getAttribute('href'); c.textContent = cta.textContent.trim(); c.className = 'mnav-cta';
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
  header.appendChild(btn);
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
