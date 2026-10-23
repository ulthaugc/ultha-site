import re, colorsys, sys
sys.path.insert(0,'/tmp/claude-0/-home-claude/c55b7bce-055d-5cb1-96bf-984be9841218/scratchpad')
import hero_light, tree_navy_light as T
COB='#1F4FD8'; INK='#14213D'; SUN='#FFC94D'; CORAL='#E9604B'
SLATE='#586A7C'   # tree navy, one shade lighter
def hx(c):
    c=c.lstrip('#'); 
    if len(c)==3: c=''.join(x*2 for x in c)
    return tuple(int(c[i:i+2],16)/255 for i in (0,2,4))
def tohex(r,g,b): return '#%02X%02X%02X'%tuple(max(0,min(255,round(v*255))) for v in (r,g,b))
def is_navy(r,g,b):
    h,l,s=colorsys.rgb_to_hls(r,g,b); return (0.48<h<0.64 and s<0.45) or (s<0.06 and l>.9)
Y_MAIN={'#FFE29A','#FFF6D6','#FFF6DD','#FFFBEF'}; Y_WARM={'#F2B33D','#D99A1E','#C9A24A','#8A6410'}; CO={'#E36F5A','#F08A74','#B8452F'}
def m(r,g,b):
    H=tohex(r,g,b)
    if H in Y_MAIN: return hx(COB)
    if H in Y_WARM: return hx(SUN)
    if H in CO: return hx(CORAL)
    if not is_navy(r,g,b): return (r,g,b)
    h,l,sa=colorsys.rgb_to_hls(r,g,b)
    l=.05+(1-l)*.93
    if l<.3: return hx(INK)
    if l>.75: sa*=.1; l=.955+(l-.75)*.18
    return colorsys.hls_to_rgb(.62,l,min(1,sa*.9))
def transform(s):
    s=re.sub(r'#[0-9A-Fa-f]{6}\b|#[0-9A-Fa-f]{3}\b(?![0-9A-Fa-f])',lambda x:tohex(*m(*hx(x.group(0)))),s)
    def rg(x):
        r,g,b=(int(x.group(i))/255 for i in (1,2,3)); nr,ng,nb=m(r,g,b)
        return f'rgba({round(nr*255)},{round(ng*255)},{round(nb*255)}'
    s=re.sub(r'rgba?\(\s*(\d+),\s*(\d+),\s*(\d+)',rg,s)
    s=re.sub(r'(?<=[:\s])white\b',tohex(*m(1,1,1)),s)
    return s
if __name__=='__main__':
    import glob
    root='/home/claude/ultha-site/'
    orig_index=open(root+'index.html').read()
    for f in ['index.html','about.html','contact.html','starter-kit.html','kit.html','pricing.html','scale.css','guides/guide.css']+[x[len(root):] for x in glob.glob(root+'guides/*.html')]:
        s=open(root+f).read(); s=transform(s); open(root+f,'w').write(s)
    s=open(root+'index.html').read()
    N=hero_light.PALETTES['navysky']
    a=s.index('<svg class="herosvg"'); b=s.index('</svg>',a)+6
    s=s[:a]+hero_light.hero_svg(N).replace('font-size="20" fill="'+N['deep']+'"','font-size="20" fill="'+COB+'"')+s[b:]
    s=s.replace('<div aria-hidden="true" class="hn-sky">','<div aria-hidden="true" class="hn-sky" style="display:none">')
    a,b=T.blk(s); s=s[:a]+T.tree_block(orig_index)+s[b:]
    open(root+'index.html','w').write(s)
    print('done')
