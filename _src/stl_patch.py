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

# St Leonards: transport lines in a right-hand column above "Get directions" (web);
# on print the same column shows address + transport (button hidden)
t = open(p, encoding='utf-8').read()
TRAIN = '<svg viewBox="0 0 24 24"><path d="M12 2c-4 0-8 .5-8 4v9.5A3.5 3.5 0 0 0 7.5 19L6 20.5v.5h12v-.5L16.5 19a3.5 3.5 0 0 0 3.5-3.5V6c0-3.5-4-4-8-4zM7.5 17a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm3.5-7H6V6h5zm2 0V6h5v4zm3.5 7a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/></svg>'
BUS = '<svg viewBox="0 0 24 24"><path d="M4 16c0 .9.4 1.7 1 2.2V20a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1h8v1a1 1 0 0 0 1 1h1a1 1 0 0 0 1-1v-1.8c.6-.5 1-1.3 1-2.2V6c0-3.5-3.6-4-8-4s-8 .5-8 4zm3.5 1a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zm9 0a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM18 11H6V6h12z"/></svg>'
assert '<p>{{dc_where}}</p>' in t
t = t.replace('<p>{{dc_where}}</p>', '<p class="dc-where">{{dc_where}}</p>', 1)
import re as _re2
m = _re2.search(r'\n      <a class="btn btn-white" href="https://www\.google\.com/maps[^"]*" target="_blank" rel="noopener">\n.*?\{\{get_dir\}\}</a>', t, _re2.S)
assert m, 'directions button not found'
btn = m.group(0)
side = ('\n      <div class="dc-side"><div class="dc-loc"><p class="print-where">{{dc_where}}</p>'
        + f'\n        <p class="walk">{TRAIN}<span>{{{{tr1}}}}</span></p>'
        + f'\n        <p class="walk">{TRAIN}<span>{{{{tr2}}}}</span></p>'
        + f'\n        <p class="walk">{BUS}<span>{{{{tr3}}}}</span></p></div>'
        + btn.replace('\n      <a', '\n        <a') + '\n      </div>')
t = t.replace(btn, side, 1)
CSS2 = """
/* St Leonards info-day card: smaller text, transport column on the right */
.date-card h2{font-size:clamp(1.5rem,3.2vw,2.3rem)}
.dc-eyebrow{font-size:.9rem}
.date-card .pill{font-size:clamp(1rem,1.7vw,1.2rem)}
.date-card .pill-y{font-size:clamp(.95rem,1.5vw,1.08rem)}
.date-card .dc-where{font-size:.98rem}
.dc-side{display:flex;flex-direction:column;align-items:flex-start;gap:16px;min-width:0}
.dc-loc .print-where{display:none}
.date-card p.walk{display:flex;align-items:center;gap:.5em;margin:0 0 6px;font-weight:600;color:#fff;font-size:1rem;white-space:nowrap}
.date-card p.walk svg{width:1.1em;height:1.1em;fill:currentColor;flex:none}
@media (max-width:1100px){
  .dc-side{grid-column:1/-1;flex-direction:row;flex-wrap:wrap;align-items:center;justify-content:space-between}
  .dc-side .btn{grid-column:auto !important}
}
@media (max-width:620px){
  .dc-side{flex-direction:column;align-items:center}
  .date-card p.walk{white-space:normal;display:block;text-align:center}
  .date-card p.walk svg{display:inline-block;vertical-align:-.15em;margin-inline-end:.4em}
  .dc-side .btn{width:100%;justify-content:center}
}
@media print{
  .date-card{grid-template-columns:auto auto 1fr !important;column-gap:20px !important}
  .date-card h2{font-size:1.75rem !important}
  .dc-eyebrow{font-size:.85rem !important}
  .pill{font-size:1.05rem !important;padding:.35em .8em !important}
  .pill-y{font-size:.95rem !important}
  .dc-row{gap:8px !important;margin:10px 0 0 !important}
  .date-card .dc-where{display:none}
  .dc-side{grid-column:auto !important;border-inline-start:1.5px solid rgba(255,255,255,.35);padding-inline-start:20px;align-self:stretch;justify-content:center;display:flex !important;flex-direction:column !important}
  .dc-loc .print-where{display:block;font-size:1.2rem;line-height:1.35;color:#fff;margin-bottom:4px}
  .dc-loc p.walk{font-size:1.1rem !important;margin:6px 0 0}
  html[lang="ps"] .dc-loc p.walk,html[lang="ta"] .dc-loc p.walk{white-space:normal;overflow-wrap:anywhere}
  html[lang="ta"] .dc-side{min-width:0;max-width:260px}
}
"""
t = t.replace('</style>', CSS2 + '</style>', 1)
open(p, 'w', encoding='utf-8').write(t)
print('transport column added')
