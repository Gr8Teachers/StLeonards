import re
t=open('/home/claude/work/template2.html').read()
t=t.replace('<style>\n{{FONTS}}','<link rel="stylesheet" href="{{A}}assets/fonts.css">\n<style>')
t=t.replace('url("data:image/jpeg;base64,{{PHOTO}}")','url("{{A}}assets/photo.jpg")')
t=t.replace('src="data:image/jpeg;base64,{{LOGO}}"','src="{{A}}assets/logo.jpg"')
t=t.replace('src="data:image/png;base64,{{QR}}"','src="{{A}}assets/qr.png"')
assert '{{PHOTO}}' not in t and 'base64' not in t
s=t.index('          <li class="lang-en">'); e=t.index('            </ul>\n            <p class="lang-note">')
t=t[:s]+'{{LANG_ITEMS}}\n'+t[e:]
s=t.index('<script>'); e=t.index('</script>')+len('</script>')
t=t[:s]+'''<script>
(function(){
  var d=document.getElementById("langMenu");
  document.addEventListener("click",function(e){ if(d.open && !d.contains(e.target)) d.open=false; });
  document.addEventListener("keydown",function(e){ if(e.key==="Escape") d.open=false; });
})();
</script>'''+t[e:]
P=[('<html lang="en">','<html lang="{{LANG}}" dir="{{DIR}}">'),
('<title>Free* English Classes | TAFE NSW St Leonards</title>','<title>{{title}}</title>'),
('content="Free* English classes for adults at TAFE NSW St Leonards. Next info day: Wednesday 09/12/2026, 10am – 4pm. Come in and have a free English test."','content="{{meta_desc}}"'),
('aria-label="TAFE NSW home"','aria-label="TAFE NSW"'),
('<li class="link"><a href="#offer">What we offer</a></li>','<li class="link"><a href="#offer">{{nav_offer}}</a></li>'),
('<li class="link"><a href="#info-day">Info day</a></li>','<li class="link"><a href="#info-day">{{nav_info}}</a></li>'),
('<li class="link"><a href="#contact">Contact</a></li>','<li class="link"><a href="#contact">{{nav_contact}}</a></li>'),
('aria-label="Print this flyer"','aria-label="{{print}}"'),
('<span class="hide-sm">Print</span>','<span class="hide-sm">{{print}}</span>'),
('aria-label="Translate this page – choose your language"','aria-label="{{choose_lang}}"'),
('<span>Your language</span></summary>','<span>{{your_lang}}</span></summary>'),
('<p class="lang-title">Choose your language</p>','<p class="lang-title">{{choose_lang}}</p>'),
('<p class="lang-note">Translated by Google Translate. Some words may not be exact.</p>','<p class="lang-note">{{lang_note}}</p>'),
('<h1>Free* English Classes<span>for adults – from beginner to advanced</span></h1>','<h1>{{h1}}<span>{{h1_sub}}</span></h1>'),
('<p class="lead">Learn English to live, work and study in Australia. Come to our info day and have a free English test.</p>','<p class="lead">{{lead}}</p>'),
('href="#info-day">See info day details</a>','href="#info-day">{{btn_info}}</a>'),
('href="#contact">Contact us</a>','href="#contact">{{btn_contact}}</a>'),
('<div class="m">Wed</div><div class="d">09/12</div><div class="y">2026</div>','<div class="m">{{cal_top}}</div><div class="d{{CAL_CLS}}">{{cal_mid}}</div><div class="y">{{cal_bot}}</div>'),
('<div class="dc-eyebrow">Our next Info day</div>','<div class="dc-eyebrow">{{dc_eyebrow}}</div>'),
('<h2>Wednesday 09/12/2026</h2>','<h2>{{date_heading}}</h2>'),
('</svg>10am – 4pm</span>','</svg><bdi>{{time}}</bdi></span>'),
('</svg>Free English test</span>','</svg>{{free_test}}</span>'),
('<p>Building P, Level 4, Room P4.02 · 213 Pacific Hwy, St Leonards</p>','<p>{{dc_where}}</p>'),
('</svg>Get directions</a>','</svg>{{get_dir}}</a>'),
('<h2>What we offer</h2>','<h2>{{offer_h}}</h2>'),
('<p>Flexible English classes for adults, with the support of TAFE NSW teachers, services and facilities.</p>','<p>{{offer_sub}}</p>'),
('<h3>Beginner to Advanced</h3><p>Classes at every level for adult learners.</p>','<h3>{{o1_t}}</h3><p>{{o1_d}}</p>'),
('<h3>Day and Evening classes</h3><p>Choose a timetable that fits around work and family.</p>','<h3>{{o2_t}}</h3><p>{{o2_d}}</p>'),
('<h3>Face-to-face and Online</h3><p>Study on campus or join your class online.</p>','<h3>{{o3_t}}</h3><p>{{o3_d}}</p>'),
('<h3>For a variety of visa holders</h3><p>Classes open to many visa types – ask us about eligibility.</p>','<h3>{{o4_t}}</h3><p>{{o4_d}}</p>'),
('<h3>English to live, work &amp; study</h3><p>Practical English for everyday life, jobs and further study in Australia.</p>','<h3>{{o5_t}}</h3><p>{{o5_d}}</p>'),
('<h3>TAFE services &amp; facilities</h3><p>Access TAFE NSW libraries, resources and student support.</p>','<h3>{{o6_t}}</h3><p>{{o6_d}}</p>'),
('<h2>How to get started</h2>','<h2>{{steps_h}}</h2>'),
("<p>Can't come on the info day? Just contact us or walk in.</p>",'<p>{{steps_sub}}</p>'),
('<h3>Visit or contact us</h3><p>Come to the info day on 09/12/2026, call, email, or walk in to the campus.</p>','<h3>{{s1_t}}</h3><p>{{s1_d}}</p>'),
("<h3>Eligibility check</h3><p>We'll check your visa / residency to confirm your eligibility, and discuss the study options available to you.</p>",'<h3>{{s2_t}}</h3><p>{{s2_d}}</p>'),
("<h3>Take a free English test</h3><p>We'll check your English level so you start in the right class.</p>",'<h3>{{s3_t}}</h3><p>{{s3_d}}</p>'),
('<h3>Start your class</h3><p>Choose day or evening, face-to-face or online, and start learning.</p>','<h3>{{s4_t}}</h3><p>{{s4_d}}</p>'),
("<h2>Can't come on the info day?<br>Just contact us or walk in!</h2>",'<h2>{{c_h1}}<br>{{c_h2}}</h2>'),
('<p>Our team is happy to answer your questions.</p>','<p>{{c_p}}</p>'),
('<small>Phone</small><a href="tel:+61279206475">7920 6475</a>','<small>{{lbl_phone}}</small><a href="tel:+61279206475" dir="ltr">7920 6475</a>'),
('<small>Email</small><a href="mailto:','<small>{{lbl_email}}</small><a dir="ltr" href="mailto:'),
('<small>Address</small><a href=','<small>{{lbl_addr}}</small><a dir="ltr" href='),
('alt="QR code: Free English TAFE NSW St Leonards"','alt="QR code"'),
('<h3>Scan me</h3>','<h3>{{qr_h}}</h3>'),
('<p>Scan with your phone camera for more information.</p>','<p>{{qr_p}}</p>'),
('<p><em>*Cost:</em> This training is subsidised by the NSW Government for permanent residents, Australian citizens and certain temporary visa holders – eligibility criteria apply.</p>','<p><em>{{cost_lbl}}</em> {{cost}}</p>'),
('<p class="print-only">View online: gr8teachers.github.io/StLeonards</p>','<p class="print-only">{{view_online}} <span dir="ltr">gr8teachers.github.io/StLeonards{{PATH}}</span></p>'),
]
for a,b in P:
    assert a in t,a; t=t.replace(a,b)
t=t.replace('body{font-family:"Open Sans",system-ui,sans-serif;','body{font-family:"Open Sans","TAFE Script",system-ui,"Segoe UI","Noto Sans",Tahoma,sans-serif;')
t=t.replace('h1,h2,h3,.btn,.brand-sub,.date-card{font-family:"Poppins",system-ui,sans-serif}','h1,h2,h3,.btn,.brand-sub,.date-card{font-family:"Poppins","Open Sans","TAFE Script",system-ui,"Segoe UI","Noto Sans",Tahoma,sans-serif}')
extra='''
/* Non-English scripts */
html:not([lang="en"]) .eyebrow,html:not([lang="en"]) .dc-eyebrow,html:not([lang="en"]) .cal .m,html:not([lang="en"]) .cal .y,html:not([lang="en"]) .cl small{letter-spacing:0}
html:not([lang="en"]) h1,html:not([lang="en"]) h2,html:not([lang="en"]) h3{letter-spacing:0}
.lang-panel a.current{background:#fbeef2}
.lang-panel a{align-items:flex-start}
html:not([lang="en"]) .date-card h2{white-space:normal}
.cal .d.sm{font-size:2.3rem;line-height:1.15;padding:10px 6px 4px}
@media (max-width:620px){.cal .d.sm{font-size:2rem}}
@media print{.cal .d.sm{font-size:2rem}}
.lang-panel a.current .ln::after{content:" \\2713";color:var(--red)}
/* Right-to-left */
[dir="rtl"] .hero::before{background:linear-gradient(270deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.5) 45%,rgba(0,0,0,.05) 100%)}
[dir="rtl"] .lang-panel{right:auto;left:0}
[dir="rtl"] .cl a[dir="ltr"]{display:block;text-align:right}
[dir="rtl"] body{line-height:1.7}
html[lang="my"] h1,html[lang="my"] h2,html[lang="my"] h3,html[lang="km"] h1,html[lang="km"] h2,html[lang="km"] h3{line-height:1.55}
html[lang="my"] .hero h1 span,html[lang="km"] .hero h1 span{margin-top:.5em}
html[lang="my"] body,html[lang="km"] body{line-height:1.85}
@media (max-width:620px){[dir="rtl"] .lang-panel{left:4vw;right:4vw}}
@media print{[dir="rtl"] .hero::before{background:linear-gradient(270deg,rgba(0,0,0,.72) 0%,rgba(0,0,0,.5) 55%,rgba(0,0,0,.1) 100%)}}
'''
t=t.replace('/* ---------- Print: one-page A4 flyer ---------- */',extra+'\n/* ---------- Print: one-page A4 flyer ---------- */',1)
t=t.replace('  body{zoom:.86}','  body{zoom:{{ZOOM}}}')
assert '@page{size:A4;margin:0}' in t  # keep A4 page size
import sys; sys.path.insert(0,'/home/claude/build'); from form_patch import FORM_HTML, FORM_CSS, FORM_JS, MSFORM_HTML, MSFORM_CSS
assert '  <!-- Contact -->' in t
t=t.replace('  <!-- Contact -->', FORM_HTML+'  <!-- Contact -->')
t=t.replace('<a class="btn btn-ghost" href="#contact">{{btn_contact}}</a>','<a class="btn btn-ghost" href="#enquiry">{{btn_contact}}</a>')
old_qr='''      <div class="qr-box">
        <img src="{{A}}assets/qr.png" alt="QR code">
        <h3>{{qr_h}}</h3>
        <p>{{qr_p}}</p>
      </div>'''
assert old_qr in t
t=t.replace(old_qr, MSFORM_HTML)
t=t.replace('/* ---------- Print: one-page A4 flyer ---------- */', FORM_CSS+MSFORM_CSS+'\n/* ---------- Print: one-page A4 flyer ---------- */',1)
t=t.replace('  document.addEventListener("keydown",function(e){ if(e.key==="Escape") d.open=false; });\n})();','  document.addEventListener("keydown",function(e){ if(e.key==="Escape") d.open=false; });\n})();'+FORM_JS)
t=t.replace('"Poppins",sans-serif','"Poppins","Open Sans","TAFE Script",sans-serif').replace('"Open Sans",sans-serif','"Open Sans","TAFE Script",sans-serif')
open('/home/claude/build/template.html','w').write(t)
body=t[t.index('<body>'):t.index('<script>')]
left=[x.strip() for x in re.findall(r'>([^<>{}]+)<',body) if re.search(r'[A-Za-z]{3,}',x)]
print('untemplated text:',left)
