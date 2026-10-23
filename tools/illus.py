"""Illustrations for ultha.co: journey scenes + services tree. Hero-style: navy, light figures, yellow accents, dotted ground."""
import math, random

NAVY='#1B2A38'; DEEP='#111C27'; G1='#22354A'; G2='#2A4057'; G3='#3A5169'
LIGHT='#EEF1F2'; MIST='#C6D3DB'; SLATE='#8FA3B1'; SUN='#FFE29A'; AMBER='#F2B33D'; CORAL='#E36F5A'; CARD='#F7F9FA'

def dots(pid, op=.32):
    return f'<pattern id="{pid}" width="9" height="9" patternUnits="userSpaceOnUse"><circle cx="2" cy="2" r="1.2" fill="#FFFFFF" opacity="{op}"/></pattern>'

def person(x, base, col, s=1.0):
    h = 9*s
    return (f'<circle cx="{x}" cy="{base-42*s:.1f}" r="{h:.1f}" fill="{col}"/>'
            f'<path d="M{x-13*s:.1f} {base} v-{16*s:.1f} c0-{14*s:.1f} {26*s:.1f}-{14*s:.1f} {26*s:.1f} 0 v{16*s:.1f}Z" fill="{col}"/>')

def heart(x, y, s=1.0, col=CORAL):
    return f'<path transform="translate({x} {y}) scale({s})" d="M0 0c-6-4-6-9-2-10 2 0 2 1 2 2 0-1 0-2 2-2 4 1 4 6-2 10z" fill="{col}"/>'

def star(x, y, r=5, col=AMBER):
    pts=[]
    for i in range(10):
        a=-math.pi/2+i*math.pi/5; rr=r if i%2==0 else r*.45
        pts.append(f'{x+rr*math.cos(a):.1f},{y+rr*math.sin(a):.1f}')
    return f'<polygon points="{" ".join(pts)}" fill="{col}"/>'

def mound(pid):
    d='M0 220 V176 C50 160 110 150 150 151 C200 152 250 160 300 176 V220Z'
    return f'<path d="{d}" fill="{G1}"/><path d="{d}" fill="url(#{pid})"/><path d="M0 176 C50 160 110 150 150 151 C200 152 250 160 300 176" fill="none" stroke="{G3}" stroke-width="2"/>'

def scene(n, pid):
    p=f'<defs>{dots(pid)}</defs>'
    if n==1:  # one conversation
        body=(mound(pid)+person(108,154,LIGHT)+person(196,154,MIST,.95)
              +f'<g><path d="M44 30 h104 a14 14 0 0 1 14 14 v26 a14 14 0 0 1 -14 14 h-56 l-14 14 v-14 h-34 a14 14 0 0 1 -14 -14 v-26 a14 14 0 0 1 14 -14z" fill="{CARD}"/>'
              f'<rect x="46" y="46" width="70" height="6" rx="3" fill="{SLATE}"/><rect x="46" y="60" width="50" height="6" rx="3" fill="{SLATE}" opacity=".7"/>'+heart(136,64,1.5)+'</g>'
              +f'<g><path d="M178 58 h52 a12 12 0 0 1 12 12 v10 a12 12 0 0 1 -12 12 h-22 v12 l-12 -12 h-18 a12 12 0 0 1 -12 -12 v-10 a12 12 0 0 1 12 -12z" fill="{SUN}"/>'
              f'<text x="204" y="83" text-anchor="middle" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{NAVY}">why?</text></g>')
    elif n==2:  # becomes proof
        body=(mound(pid)
              +f'<g transform="rotate(7 205 95)"><rect x="160" y="36" width="96" height="118" rx="10" fill="{MIST}"/>'
              f'<rect x="174" y="52" width="50" height="7" rx="3.5" fill="{NAVY}" opacity=".7"/><rect x="174" y="70" width="66" height="5" rx="2.5" fill="{SLATE}"/><rect x="174" y="82" width="58" height="5" rx="2.5" fill="{SLATE}"/><rect x="174" y="94" width="64" height="5" rx="2.5" fill="{SLATE}"/>'
              f'<rect x="174" y="112" width="40" height="22" rx="4" fill="{SLATE}" opacity=".6"/></g>'
              +f'<g transform="rotate(-5 120 100)"><rect x="46" y="50" width="150" height="100" rx="14" fill="{CARD}"/>'
              f'<circle cx="72" cy="76" r="11" fill="{SUN}"/><rect x="90" y="70" width="56" height="6" rx="3" fill="{NAVY}" opacity=".75"/><rect x="90" y="81" width="36" height="5" rx="2.5" fill="{SLATE}"/>'
              +''.join(star(66+i*14,104,6) for i in range(5))
              +f'<rect x="60" y="118" width="120" height="5" rx="2.5" fill="{SLATE}"/><rect x="60" y="129" width="92" height="5" rx="2.5" fill="{SLATE}"/></g>'
              +f'<circle cx="196" cy="54" r="15" fill="{SUN}" stroke="{NAVY}" stroke-width="2"/><path d="M189 54 l5 5 l9 -10" fill="none" stroke="{NAVY}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>')
    elif n==3:  # becomes content
        car=''
        for i,(c,dx) in enumerate([(SLATE,16),(MIST,8),(CARD,0)]):
            car+=f'<rect x="{50+dx}" y="{64-dx}" width="72" height="72" rx="10" fill="{c}"/>'
        car+=(f'<path d="M58 124 l18 -22 l12 13 l8 -9 l18 18z" fill="{G3}"/><circle cx="104" cy="82" r="7" fill="{AMBER}"/>'
              f'<circle cx="76" cy="148" r="3" fill="{SUN}"/><circle cx="87" cy="148" r="3" fill="{SLATE}"/><circle cx="98" cy="148" r="3" fill="{SLATE}"/>')
        phone=(f'<rect x="160" y="26" width="78" height="132" rx="16" fill="{DEEP}" stroke="{LIGHT}" stroke-width="2.5"/>'
               f'<rect x="168" y="38" width="62" height="100" rx="8" fill="{G3}"/>'
               f'<circle cx="199" cy="86" r="17" fill="{SUN}"/><path d="M193 77 v18 l15 -9z" fill="{NAVY}"/>'
               f'<rect x="176" y="120" width="34" height="4" rx="2" fill="{MIST}" opacity=".8"/><rect x="176" y="128" width="22" height="4" rx="2" fill="{MIST}" opacity=".5"/>'
               +heart(240,52,1.4))
        body=mound(pid)+car+phone
    else:  # shows up where buyers look
        body=(mound(pid)
              +f'<rect x="34" y="30" width="214" height="40" rx="20" fill="{CARD}"/>'
              f'<circle cx="57" cy="49" r="7" fill="none" stroke="{NAVY}" stroke-width="2.5"/><path d="M62 54 l6 6" stroke="{NAVY}" stroke-width="2.5" stroke-linecap="round"/>'
              f'<text x="76" y="55" font-family="Figtree, sans-serif" font-size="14" fill="#5E7586">best tool for my team?</text>'
              f'<path d="M262 20 l3.5 9 9 3.5 -9 3.5 -3.5 9 -3.5 -9 -9 -3.5 9 -3.5z" fill="{SUN}"/>'
              f'<path d="M282 46 l2 5 5 2 -5 2 -2 5 -2 -5 -5 -2 5 -2z" fill="{SUN}" opacity=".7"/>'
              +person(108,154,'#D7E1E7',.9)+person(150,154,'#D7E1E7',.9)+person(192,154,'#D7E1E7',.9)
              +heart(108,96,1.3)+heart(150,92,1.3)+heart(192,96,1.3))
    return p+body

def journey_svg(n):
    return f'<svg class="hw-art" viewBox="0 0 300 200" aria-hidden="true">{scene(n, f"hwd{n}")}</svg>'

# ---------------- services tree ----------------
SERVICES=['Testimonials','Case studies','G2 &amp; Capterra reviews','Short videos &amp; UGC','Posts &amp; carousels','AI search pages']

def crown(cx, cy, R, rnd, n=34):
    out=[]
    cols=[G2,G3,'#4A627A',G3,G2]
    for i in range(n):
        a=rnd.uniform(0,2*math.pi); d=R*math.sqrt(rnd.uniform(0,1))
        x=cx+d*math.cos(a)*1.25; y=cy+d*math.sin(a)*.78
        r=rnd.uniform(R*.26,R*.42)
        out.append((y,f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r:.1f}" fill="{rnd.choice(cols)}"/>'))
    out.sort()
    hi=''.join(f'<circle cx="{cx+R*rnd.uniform(-1,1)*1.0:.1f}" cy="{cy+R*rnd.uniform(-.9,.2)*.7:.1f}" r="{rnd.uniform(R*.1,R*.18):.1f}" fill="#5E7586" opacity=".55"/>' for _ in range(9))
    return ''.join(s for _,s in out)+hi

def fruits(cx, cy, R, rnd, n=9):
    s=''
    for i in range(n):
        a=rnd.uniform(0,2*math.pi); d=R*rnd.uniform(.25,.95)
        x=cx+d*math.cos(a)*1.2; y=cy+d*math.sin(a)*.7
        s+=f'<circle cx="{x:.1f}" cy="{y:.1f}" r="9" fill="{SUN}"/><circle cx="{x-3:.1f}" cy="{y-3:.1f}" r="3" fill="#FFF6D6"/>'
    return s

def tree_svg(mobile=False):
    rnd=random.Random(7)
    if not mobile:
        W,H=1200,640; tx=600; ground=380; ccx,ccy,R=600,170,150
        chip_w,chip_h,fs=196,46,16
        xs=[110,305,500,700,895,1090]; ys=[560,520,580,580,520,560]
        chips=list(zip(xs,ys))
    else:
        W,H=390,700; tx=195; ground=290; ccx,ccy,R=195,140,92
        chip_w,chip_h,fs=168,44,14
        chips=[(95,410),(295,410),(95,505),(295,505),(95,600),(295,600)]
    pid='trd'+('m' if mobile else 'd')
    s=[f'<svg class="tree-art {"tree-m" if mobile else "tree-d"}" viewBox="0 0 {W} {H}" role="img" aria-label="A tree: services as roots, trust as the trunk, revenue as the fruit">',
       f'<defs>{dots(pid,.28)}<linearGradient id="{pid}s" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="{G1}"/><stop offset="1" stop-color="{DEEP}"/></linearGradient></defs>']
    # soil
    gp=f'M0 {ground+18} C{W*.2} {ground-6} {W*.4} {ground+4} {W*.5} {ground} C{W*.62} {ground-4} {W*.82} {ground+8} {W} {ground+14} V{H} H0Z'
    s.append(f'<path d="{gp}" fill="url(#{pid}s)"/>')
    s.append(f'<path d="M0 {ground+18} C{W*.2} {ground-6} {W*.4} {ground+4} {W*.5} {ground} C{W*.62} {ground-4} {W*.82} {ground+8} {W} {ground+14} V{ground+60} H0Z" fill="url(#{pid})"/>')
    s.append(f'<path d="M0 {ground+18} C{W*.2} {ground-6} {W*.4} {ground+4} {W*.5} {ground} C{W*.62} {ground-4} {W*.82} {ground+8} {W} {ground+14}" fill="none" stroke="{G3}" stroke-width="2"/>')
    # roots to chips
    for (x,y) in chips:
        top=y-chip_h/2
        mid=(ground+top)/2
        s.append(f'<path d="M{tx} {ground+6} C{tx} {mid} {x} {mid-10} {x} {top}" fill="none" stroke="#7A6450" stroke-width="{6 if not mobile else 4}" stroke-linecap="round" opacity=".9"/>')
        s.append(f'<path d="M{tx} {ground+6} C{tx} {mid} {x} {mid-10} {x} {top}" fill="none" stroke="#C9A27A" stroke-width="{2.2 if not mobile else 1.6}" stroke-linecap="round" opacity=".55"/>')
    # trunk + branches
    tw=34 if not mobile else 22
    s.append(f'<path d="M{tx-tw*1.4} {ground+8} C{tx-tw*.7} {ground-30} {tx-tw*.55} {ccy+70} {tx-tw*.5} {ccy+30} L{tx+tw*.5} {ccy+30} C{tx+tw*.55} {ccy+70} {tx+tw*.7} {ground-30} {tx+tw*1.4} {ground+8}Z" fill="#9C7B5E"/>')
    s.append(f'<path d="M{tx-tw*.1} {ground} C{tx-tw*.2} {ground-60} {tx-tw*.05} {ccy+80} {tx-tw*.15} {ccy+40}" stroke="#7A6450" stroke-width="3" fill="none" opacity=".7"/>')
    br=R*.9
    for dx,dy in [(-br*.9,-R*.25),(br*.9,-R*.3),(-br*.45,-R*.6),(br*.4,-R*.65)]:
        s.append(f'<path d="M{tx} {ccy+50} Q{tx+dx*.4} {ccy+20} {tx+dx} {ccy+dy}" stroke="#9C7B5E" stroke-width="{12 if not mobile else 8}" fill="none" stroke-linecap="round"/>')
    s.append(crown(ccx,ccy,R,rnd))
    s.append(fruits(ccx,ccy,R,rnd, 10 if not mobile else 7))
    # labels
    if not mobile:
        s.append(f'<text x="{tx}" y="{ground-40}" text-anchor="middle" font-family="Caveat, cursive" font-size="30" font-weight="600" fill="{LIGHT}">trust</text>')
        s.append(f'<text x="{ccx+R*1.5}" y="{ccy-60}" font-family="Caveat, cursive" font-size="34" font-weight="600" fill="{SUN}">more revenue</text>')
        s.append(f'<path d="M{ccx+R*1.5+20} {ccy-50} C{ccx+R*1.45} {ccy-20} {ccx+R*1.3} {ccy-10} {ccx+R*1.12} {ccy-14}" fill="none" stroke="{SUN}" stroke-width="2.5" stroke-linecap="round"/><path d="M{ccx+R*1.12+10} {ccy-22} l-10 8 l12 4" fill="none" stroke="{SUN}" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"/>')
        s.append(f'<text x="{ccx-R*1.55}" y="{ground-34}" text-anchor="end" font-family="Caveat, cursive" font-size="26" font-weight="600" fill="{MIST}">deals close faster</text>')
        s.append(f'<path d="M{ccx-R*1.55+6} {ground-44} C{ccx-R*1.2} {ground-60} {tx-tw*2.2} {ground-60} {tx-tw*1.1} {ground-70}" fill="none" stroke="{MIST}" stroke-width="2" stroke-linecap="round"/>')
        s.append(f'<text x="{tx}" y="{ground+52}" text-anchor="middle" font-family="Caveat, cursive" font-size="24" font-weight="600" fill="{SLATE}">grown from real customer conversations</text>')
    else:
        s.append(f'<text x="{tx}" y="{ground-24}" text-anchor="middle" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{LIGHT}">trust</text>')
        s.append(f'<text x="{W-12}" y="{ccy-R*.9}" text-anchor="end" font-family="Caveat, cursive" font-size="22" font-weight="600" fill="{SUN}">more revenue</text>')
        s.append(f'<text x="{tx}" y="{ground+44}" text-anchor="middle" font-family="Caveat, cursive" font-size="18" font-weight="600" fill="{SLATE}">grown from real customer conversations</text>')
    for (x,y),lab in zip(chips,SERVICES):
        s.append(f'<rect x="{x-chip_w/2}" y="{y-chip_h/2}" width="{chip_w}" height="{chip_h}" rx="{chip_h/2}" fill="{CARD}"/>')
        s.append(f'<circle cx="{x-chip_w/2+20}" cy="{y}" r="5" fill="{AMBER}"/>')
        s.append(f'<text x="{x+8}" y="{y+fs*.36:.1f}" text-anchor="middle" font-family="Figtree, sans-serif" font-size="{fs}" font-weight="600" fill="{NAVY}">{lab}</text>')
    s.append('</svg>')
    return ''.join(s)
