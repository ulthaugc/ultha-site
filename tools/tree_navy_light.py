"""Navy tree for the white site: one shade lighter, white chips, readable labels. tree_block(index_html) -> new hw-tree block."""
import re
NAVY={'#22354A','#263B52','#2A4057','#2E445B','#33495F','#344B62','#3A5169','#3B526A','#2C4157','#2A3E54','#4F6880','#5E7891','#6E87A0','#4A627A','#34495F','#1B2A38'}
def lighten(h,k=.18):
    r,g,b=(int(h[i:i+2],16) for i in (1,3,5))
    return '#%02X%02X%02X'%tuple(round(c+(255-c)*k) for c in (r,g,b))
def blk(t):
    a=t.index('<div class="hw-tree tv">'); b=t.index('</svg>',t.index('tv-art tv-m',a))+6; return a,b
def tree_block(o):
    a,b=blk(o); t=o[a:b]
    t=re.sub(r'(<text[^>]*Caveat[^>]*font-size="27"[^>]*fill=")#FFE29A"',r'\1#1F4FD8"',t)
    t=t.replace('fill="none" stroke="#FFE29A" stroke-width="2" stroke-linecap="round"','fill="none" stroke="#1F4FD8" stroke-width="2" stroke-linecap="round"')
    t=re.sub(r'(<text[^>]*Caveat[^>]*fill=")#C6D3DB"',r'\1#14213D"',t)
    t=t.replace('stroke="#C6D3DB" stroke-width="1.8"','stroke="#14213D" stroke-width="1.8"')
    t=t.replace('fill="#FFFFFF" opacity="0.24"','fill="#1B2A38" opacity="0.32"')
    t=re.sub(r'(<rect[^>]*rx="21\.0"[^>]*fill=")#1B2A38"([^>]*stroke=")rgba\(198,211,219,\.38\)"',r'\1#FFFFFF"\2#C9D7FB"',t)
    t=re.sub(r'(<text[^>]*font-size="1[34](?:\.5)?"[^>]*fill=")#EEF1F2"',r'\1#14213D"',t)
    t=t.replace('class="tv-dot"','class="tv-dot" style="fill:#1F4FD8"')
    t=re.sub(r'<text x="320" y="322" ([^>]*)fill="#EEF1F2">trust',r'<text x="354" y="322" text-anchor="start" font-family="Caveat, cursive" font-size="26" font-weight="600" fill="#14213D">trust',t)
    t=re.sub(r'#[0-9A-Fa-f]{6}\b',lambda m: lighten(m.group(0).upper()) if m.group(0).upper() in NAVY else m.group(0),t)
    return t
