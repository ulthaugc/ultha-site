"""Light-mode hero illustration: layered translucent hills, shaded cliffs, rounded people. viewBox 140 240 1000 360."""

def person(x, base, body, shade, s=1.0, arm=None, phone=False, op=1):
    w = 9.5*s; r = 7.2*s
    o = f'<g opacity="{op}">'
    o += f'<ellipse cx="{x}" cy="{base+1.5}" rx="{w*1.3:.1f}" ry="{2.4*s:.1f}" fill="{shade}" opacity=".22"/>'
    if arm == 'up':
        o += f'<path d="M{x+w*.55:.1f} {base-16*s:.1f} q{6*s:.1f} -{6*s:.1f} {8*s:.1f} -{16*s:.1f}" stroke="{body}" stroke-width="{4*s:.1f}" stroke-linecap="round" fill="none"/>'
    if arm == 'up2':
        o += f'<path d="M{x-w*.55:.1f} {base-16*s:.1f} q-{6*s:.1f} -{6*s:.1f} -{8*s:.1f} -{16*s:.1f}" stroke="{body}" stroke-width="{4*s:.1f}" stroke-linecap="round" fill="none"/>'
    o += f'<path d="M{x-w:.1f} {base} v-{11*s:.1f} q0 -{9*s:.1f} {w:.1f} -{9*s:.1f} q{w:.1f} 0 {w:.1f} {9*s:.1f} v{11*s:.1f}z" fill="{body}"/>'
    o += f'<path d="M{x+w*.25:.1f} {base} v-{11*s:.1f} q0 -{8*s:.1f} {w*.75:.1f} -{8.5*s:.1f} q{w*.25:.1f} 1 {w*.25:.1f} {8.5*s:.1f} v{11*s:.1f}z" fill="{shade}" opacity=".18"/>'
    if phone:
        o += f'<rect x="{x-2*s:.1f}" y="{base-17*s:.1f}" width="{5*s:.1f}" height="{7.5*s:.1f}" rx="1.3" fill="#FFE7A3"/>'
    o += f'<circle cx="{x}" cy="{base-27*s:.1f}" r="{r:.1f}" fill="{body}"/>'
    o += f'<circle cx="{x-2.2*s:.1f}" cy="{base-29.2*s:.1f}" r="{r*.36:.1f}" fill="#FFFFFF" opacity=".3"/>'
    return o + '</g>'

def heart(x, y, s=1.4, d=0):
    return f'<g transform="translate({x} {y}) scale({s})"><path class="heart" style="--d:{d}s" d="M0 0c-6-4-6-9-2-10 2 0 2 1 2 2 0-1 0-2 2-2 4 1 4 6-2 10z" fill="#E9604B"/></g>'

def hero_svg(P):
    deep, mid, light, wash, ink = P['deep'], P['mid'], P['light'], P['wash'], P['ink']
    g = f'''<svg class="herosvg" viewBox="140 240 1000 360" preserveAspectRatio="xMidYMax slice" style="position:relative;z-index:0;display:block;width:100%;height:clamp(280px,32vw,460px);margin-top:clamp(-40px,-2vw,-10px)" aria-hidden="true">
<defs>
<linearGradient id="hl1" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{light}" stop-opacity=".75"/><stop offset="1" stop-color="{light}" stop-opacity="0"/></linearGradient>
<linearGradient id="hl2" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{mid}" stop-opacity=".45"/><stop offset="1" stop-color="{light}" stop-opacity=".05"/></linearGradient>
<linearGradient id="cl" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{mid}" stop-opacity=".9"/><stop offset=".55" stop-color="{light}" stop-opacity=".9"/><stop offset="1" stop-color="{wash}" stop-opacity="0"/></linearGradient>
<linearGradient id="cs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{deep}" stop-opacity=".55"/><stop offset="1" stop-color="{mid}" stop-opacity="0"/></linearGradient>
<linearGradient id="gap" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#FFFFFF" stop-opacity="0"/><stop offset="1" stop-color="#FFFFFF" stop-opacity=".95"/></linearGradient>
<radialGradient id="sun"><stop offset="0" stop-color="#FFD66B" stop-opacity=".55"/><stop offset="1" stop-color="#FFD66B" stop-opacity="0"/></radialGradient>
<filter id="soft" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur stdDeviation="6"/></filter>
</defs>
<circle class="hl-sun" cx="600" cy="372" r="80" fill="url(#sun)" opacity=".8"/>
<path class="hl-back1" d="M140 372 C260 330 360 318 470 336 C600 356 700 300 820 306 C940 312 1040 340 1140 324 V600 H140Z" fill="url(#hl1)"/>
<path class="hl-back2" d="M140 400 C250 362 360 350 460 362 C580 376 690 340 800 344 C920 348 1030 372 1140 360 V600 H140Z" fill="url(#hl2)"/>
<!-- left cliff -->
<path d="M140 412 C230 398 330 396 420 402 L468 416 L446 600 H140Z" fill="url(#cl)"/>
<path d="M468 416 L446 600 H412 L436 428Z" fill="url(#cs)"/>
<path d="M140 412 C230 398 330 396 420 402 L468 416" fill="none" stroke="{deep}" stroke-width="2" stroke-linecap="round" opacity=".7"/>
<path d="M170 432 C230 424 300 424 360 428" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".3" fill="none"/>
<!-- right cliff -->
<path d="M1140 414 C1060 402 960 400 870 406 L824 418 L846 600 H1140Z" fill="url(#cl)"/>
<path d="M824 418 L846 600 H880 L856 430Z" fill="url(#cs)"/>
<path d="M1140 414 C1060 402 960 400 870 406 L824 418" fill="none" stroke="{deep}" stroke-width="2" stroke-linecap="round" opacity=".7"/>
<path d="M920 434 C980 428 1050 428 1110 432" stroke="#FFFFFF" stroke-width="5" stroke-linecap="round" opacity=".3" fill="none"/>
<!-- valley mist -->
<rect x="440" y="440" width="420" height="160" fill="url(#gap)"/>
<ellipse cx="645" cy="560" rx="300" ry="40" fill="#FFFFFF" opacity=".8" filter="url(#soft)"/>
<!-- bridge -->
<path d="M452 396 Q645 452 840 398" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>
'''
    import math
    planks = ''
    for i in range(22):
        t = (i+.5)/22
        x = 452 + (840-452)*t
        y = (1-t)**2*418 + 2*(1-t)*t*474 + t**2*420
        dy = 2*(1-t)*(474-418) + 2*t*(420-474)
        ang = math.degrees(math.atan2(dy, 840-452))
        planks += f'<g transform="translate({x:.1f} {y:.1f}) rotate({ang:.1f})"><g class="plank" style="--d:{.35+i*.07:.2f}s"><rect x="-7" y="-1" width="14" height="6" rx="1.5" fill="#B88A3E" opacity=".35"/><rect x="-7" y="-3.5" width="14" height="6" rx="1.5" fill="#FFC94D"/></g></g>'
    hangers = ''
    for i in range(1, 11):
        t = i/11
        x = 452 + (840-452)*t
        y1 = (1-t)**2*396 + 2*(1-t)*t*452 + t**2*398
        y2 = (1-t)**2*418 + 2*(1-t)*t*474 + t**2*420
        hangers += f'<path d="M{x:.1f} {y1:.1f} V{y2-3:.1f}" stroke="{ink}" stroke-width="1.2" opacity=".6"/>'
    g += hangers + planks
    g += f'<path d="M452 418 Q645 474 840 420" fill="none" stroke="{ink}" stroke-width="2" stroke-linecap="round"/>'
    g += f'<path d="M452 422 V392 M840 424 V394" stroke="{ink}" stroke-width="3.5" stroke-linecap="round"/>'
    # customers
    g += '<g class="hl-cust">'
    cust = [(246, 'up2'), (280, None), (314, 'up'), (348, None)]
    for x, a in cust:
        g += person(x, 404, deep, ink, 1.0, a)
    g += heart(266, 352, d=0) + heart(298, 346, d=1.2) + heart(330, 352, d=2.4)
    g += f'<text x="296" y="316" text-anchor="middle" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{ink}">your customers</text></g><g class="hl-pros">'
    # prospects
    pros = [(930, False), (962, True), (994, False), (1026, True), (1058, False)]
    for x, ph in pros:
        if x == 994:
            g += '<g class="hs-gone">' + person(x, 408, mid, ink, .95, None, ph, .75) + '</g>'
            continue
        g += person(x, 408, mid, ink, .95, None, ph, .75)
    g += f'<g class="ghost" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{mid}" text-anchor="middle"><text x="946" y="352">?</text><text x="1010" y="344">?</text><text x="1060" y="352">?</text></g>'
    g += f'<text x="994" y="316" text-anchor="middle" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{ink}">your prospects, searching</text></g>'
    g += (f'<g class="hs-walker" aria-hidden="true" opacity="0"><set attributeName="opacity" to="1" begin="3.2s" fill="freeze"/>'
          '<animateMotion begin="3.2s" dur="4.6s" fill="freeze" calcMode="spline" keyPoints="0;1" keyTimes="0;1" keySplines=".45 0 .55 1" path="M994 408 L846 416 Q645 470 446 414 L386 404"/>'
          '<g class="hs-bob"><g><animate attributeName="opacity" to="0" begin="6.4s" dur=".7s" fill="freeze"/>' + person(0, 0, mid, ink, .95) + '</g>'
          '<g opacity="0"><animate attributeName="opacity" to="1" begin="6.4s" dur=".7s" fill="freeze"/>' + person(0, 0, deep, ink, 1.0) + '</g></g>'
          '<g transform="translate(0 -46) scale(1.4)"><path class="hs-heart" d="M0 0c-6-4-6-9-2-10 2 0 2 1 2 2 0-1 0-2 2-2 4 1 4 6-2 10z" fill="#E9604B" opacity="0"><set attributeName="opacity" to="1" begin="7.6s" fill="freeze"/></path></g></g>')
    g += f'<g class="svgcap" font-family="Caveat, cursive" font-size="20" fill="{deep}" text-anchor="middle"><text x="645" y="504">↑</text><text x="645" y="526">Your customers trust you. Your prospects don’t, yet.</text><text x="645" y="548">I build the bridge.</text></g>'
    g += '</svg>'
    return g

PALETTES = {
    'cobalt':  dict(deep='#1F4FD8', mid='#7C9CF0', light='#C9D7FB', wash='#EEF3FF', ink='#14213D'),
    'ocean':   dict(deep='#0E5A8A', mid='#5FA3C8', light='#C2DDEC', wash='#EEF6FA', ink='#0F2A3D'),
    'indigo':  dict(deep='#3B3FB6', mid='#8D8FE0', light='#D4D5F6', wash='#F2F2FD', ink='#1C1D4A'),
    'navysky': dict(deep='#1E3A6E', mid='#6A9BD8', light='#CFE0F5', wash='#F2F7FD', ink='#132238'),
}
