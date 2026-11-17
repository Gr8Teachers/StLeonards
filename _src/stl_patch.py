"""St Leonards-only additions to template.html (run after make_template.py)."""
p = '/home/claude/build/template.html'
t = open(p, encoding='utf-8').read()
PROGS = [
    ("https://www.tafensw.edu.au/programs/adult-migrant-english-program", "gp1", "Adult Migrant English Program (AMEP)",
     "https://immi.homeaffairs.gov.au/settling-in-australia/amep/about-the-program"),
    ("https://www.tafensw.edu.au/programs/skills-for-education-and-employment", "gp2", "Skills for Education and Employment (SEE)",
     "https://www.dewr.gov.au/skills-education-and-employment"),
    ("https://www.tafensw.edu.au/course-areas/foundation-skills-english-language-and-auslan", "gp3", "TAFE Fee-Free Courses",
     "https://www.tafensw.edu.au/fee-free"),
]
items = ''.join(
    f'''        <div class="prog"><span class="pn">{i}</span><div class="pt"><a class="pl" href="{url}" target="_blank" rel="noopener"><strong>{{{{{key}}}}}</strong> <span aria-hidden="true">&#8599;</span></a><small lang="en" dir="ltr">{en}</small><a class="pm" href="{more}" target="_blank" rel="noopener">{{{{{key}_more}}}} <span aria-hidden="true">&#8599;</span></a></div></div>\n'''
    for i, (url, key, en, more) in enumerate(PROGS, 1))
SECTION = f'''  <!-- Government-funded programs -->
  <section id="programs">
    <div class="wrap">
      <div class="sec-head"><h2>{{{{gp_h}}}}</h2></div>
      <div class="prog-grid">
{items}      </div>
    </div>
  </section>

'''
anchor = '  <!-- How to get started -->'
if anchor not in t:
    anchor = '  <!-- How to start -->'
assert anchor in t, 'steps anchor missing'
t = t.replace(anchor, SECTION + anchor, 1)
CSS = '''
/* Government-funded programs (St Leonards) */
#programs{padding-top:0}
.prog-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
.prog-grid > *{min-width:0}
.prog .pt strong,.prog .pt small{overflow-wrap:break-word}
@media (max-width:420px){.prog{padding:18px 14px;gap:12px}}
.prog{display:flex;align-items:flex-start;gap:16px;background:#fff;border:1px solid var(--line);border-left:5px solid var(--red);border-radius:var(--radius);padding:22px 20px;color:var(--ink)}
.prog .pn{flex:none;width:40px;height:40px;border-radius:50%;background:var(--red);color:#fff;display:flex;align-items:center;justify-content:center;font-family:"Poppins","Open Sans","TAFE Script",sans-serif;font-weight:700}
.prog .pt{min-width:0;display:flex;flex-direction:column;align-items:flex-start}
.prog .pt strong{display:inline;font-family:"Poppins","Open Sans","TAFE Script",sans-serif;font-weight:600;font-size:1.08rem;line-height:1.35;color:var(--red);text-decoration:underline;text-underline-offset:3px;text-decoration-thickness:1px}
.prog .pl{color:var(--red);text-decoration:none;font-family:"Poppins","Open Sans","TAFE Script",sans-serif;font-weight:600}
.prog .pl:hover strong{text-decoration-thickness:2px}
.prog .pm{display:inline-block;margin-top:12px;padding-top:10px;border-top:1px dashed var(--line);color:var(--ink);font-weight:600;font-size:.95rem;text-decoration:underline;text-underline-offset:3px;text-decoration-color:var(--red)}
.prog .pm:hover{color:var(--red)}
.prog .pt small{display:block;color:var(--muted);font-size:.85rem;margin-top:4px}
html[lang="en"] .prog .pt small{display:none}
[dir="rtl"] .prog{border-left:1px solid var(--line);border-right:5px solid var(--red)}
[dir="rtl"] .prog .pt small{text-align:right}
@media (max-width:900px){.prog-grid{grid-template-columns:1fr}}
@media print{#programs{display:none !important}}
'''
t = t.replace('</style>', CSS + '</style>', 1)
open(p, 'w', encoding='utf-8').write(t)
print('St Leonards programs section added')

# St Leonards: remove the two "find out more" buttons (covered by the programs section)
import re as _re
t = open(p, encoding='utf-8').read()
t2 = _re.sub(r'      <p class="more">\n.*?      </p>\n', '', t, count=1, flags=_re.S)
assert t2 != t, 'more buttons not found'
open(p, 'w', encoding='utf-8').write(t2)
print('find-out-more buttons removed')

# St Leonards print: bigger QR code, less white space around it
t = open(p, encoding='utf-8').read()
QR_CSS = '''
@media print{
  .qr-box{padding:8px 10px !important;justify-content:center}
  .qr-box img{width:100% !important;max-width:{{QRW}}px}
  .qr-box h3{margin-top:4px !important;font-size:1.3rem}
  .qr-box p{font-size:1.05rem !important;line-height:1.3;margin:0}
}
'''
t = t.replace('</style>', QR_CSS.replace('{{QRW}}', '230') + '</style>', 1)
open(p, 'w', encoding='utf-8').write(t)
print('print QR enlarged')
