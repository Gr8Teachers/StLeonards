FORM_HTML = '''  <!-- Online enquiry -->
  <section id="enquiry">
    <div class="wrap">
      <div class="enq" id="enqBox">
        <div class="enq-head">
          <div class="icon"><svg viewBox="0 0 24 24"><path d="M2 5h20v14H2zm2 2v.5l8 5 8-5V7l-8 5z"/></svg></div>
          <h2>{{form_h}}</h2>
          <p>{{form_sub}}</p>
        </div>
        <form id="enqForm" action="https://formsubmit.co/esolstleonards@tafensw.edu.au" method="POST">
          <input type="text" name="_honey" class="hp" tabindex="-1" autocomplete="off" aria-hidden="true">
          <div class="fgrid">
            <label class="fld"><span>{{f_name}} <b aria-hidden="true">*</b></span><input name="Name" type="text" required autocomplete="name" maxlength="100"></label>
            <label class="fld"><span>{{f_mobile}} <b aria-hidden="true">*</b></span><input name="Mobile number" type="tel" required autocomplete="tel" inputmode="tel" pattern="[0-9 +()\\-]{8,20}" maxlength="20" dir="ltr" placeholder="04xx xxx xxx"></label>
            <label class="fld"><span>{{f_email}}</span><input name="email" type="email" autocomplete="email" maxlength="120" dir="ltr"></label>
            <label class="fld"><span>{{f_visa}} <b aria-hidden="true">*</b></span><select name="Visa status" required>
              <option value="" selected disabled>{{f_choose}}</option>
              <option value="Australian citizen">{{v_cit}}</option>
              <option value="New Zealand citizen">{{v_nz}}</option>
              <option value="Permanent resident (PR)">{{v_pr}}</option>
              <option value="Temporary resident (TR)">{{v_tr}}</option>
              <option value="Bridging visa">{{v_bv}}</option>
              <option value="Visitor visa">{{v_vis}}</option>
              <option value="Other">{{v_oth}}</option>
            </select></label>
          </div>
          <p class="fnote">{{f_privacy}}</p>
          <button class="btn btn-red" type="submit" id="enqBtn"><svg viewBox="0 0 24 24"><path d="M2 21 23 12 2 3v7l15 2-15 2z"/></svg><span>{{f_send}}</span></button>
          <p class="fstatus" id="enqStatus" role="status" aria-live="polite"></p>
        </form>
        <div class="enq-done" id="enqDone" hidden>
          <div class="tick"><svg viewBox="0 0 24 24"><path d="M9 16.2 4.8 12l-1.4 1.4L9 19 21 7l-1.4-1.4z"/></svg></div>
          <p>{{f_thanks}}</p>
        </div>
      </div>
    </div>
  </section>

'''

FORM_CSS = '''
/* Online enquiry form */
#enquiry{padding-bottom:0}
.enq{display:grid;grid-template-columns:1fr 1.7fr;gap:44px;background:#fff;border:1px solid var(--line);border-top:5px solid var(--red);border-radius:var(--radius);padding:40px;box-shadow:0 12px 40px rgba(20,30,50,.08)}
.enq-head h2{font-size:clamp(1.6rem,3vw,2.2rem);font-weight:700;line-height:1.2}
.enq-head p{color:var(--muted);margin-top:10px;font-size:1.05rem}
.fgrid{display:grid;grid-template-columns:1fr 1fr;gap:18px}
.fld{display:block}
.fld span{display:block;font-family:"Poppins","Open Sans","TAFE Script",sans-serif;font-weight:600;font-size:.98rem;margin-bottom:6px}
.fld b{color:var(--red)}
.fld input,.fld select{width:100%;font:inherit;font-size:1.05rem;color:var(--ink);background:#fff;border:1.5px solid #cbd2d9;border-radius:10px;padding:.75em .9em;min-height:52px;transition:border-color .15s,box-shadow .15s}
.fld select{appearance:none;-webkit-appearance:none;background-image:linear-gradient(45deg,transparent 50%,var(--muted) 50%),linear-gradient(135deg,var(--muted) 50%,transparent 50%);background-position:calc(100% - 20px) 52%,calc(100% - 14px) 52%;background-size:6px 6px;background-repeat:no-repeat;padding-right:2.4em}
[dir="rtl"] .fld select{background-position:14px 52%,20px 52%;padding-right:.9em;padding-left:2.4em}
[dir="rtl"] .fld input[dir="ltr"]{text-align:right}
.fld input:focus,.fld select:focus{outline:none;border-color:var(--red);box-shadow:0 0 0 4px #fbeef2}
.fld input:user-invalid,.fld select:user-invalid{border-color:#d33}
.hp{position:absolute !important;width:1px;height:1px;overflow:hidden;clip:rect(0 0 0 0);clip-path:inset(50%);white-space:nowrap;border:0;padding:0;margin:-1px}
#enqForm{position:relative}
.fnote{color:var(--muted);font-size:.92rem;margin:16px 0}
#enqBtn{font-size:1.05rem;padding:.85em 2em}
#enqBtn[disabled]{opacity:.7;cursor:wait}
.fstatus{margin-top:12px;font-weight:600}
.fstatus.err{color:var(--red)}
.enq-done{display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;gap:14px;padding:20px}
.enq-done[hidden]{display:none}
.enq-done .tick{width:72px;height:72px;border-radius:50%;background:#e6f4ea;display:flex;align-items:center;justify-content:center}
.enq-done .tick svg{width:40px;height:40px;fill:#1d7a3a}
.enq-done p{font-family:"Poppins","Open Sans","TAFE Script",sans-serif;font-weight:600;font-size:1.25rem;max-width:460px}
@media (max-width:900px){.enq{grid-template-columns:1fr;gap:22px;padding:28px}}
@media (max-width:620px){.fgrid{grid-template-columns:1fr}.enq{padding:24px 20px}#enqBtn{width:100%;justify-content:center}}
@media print{#enquiry{display:none !important}}
/* Keep long translated text inside the screen on phones */
[id]{scroll-margin-top:84px}
@media (max-width:380px){.nav .btn{font-size:.78rem}.nav img{height:22px !important}.lang summary{padding:.5em .7em}}
.date-card > *, .contact > *, .enq > *, .fgrid > *{min-width:0}
h1,h2,h3,.pill,.btn{overflow-wrap:break-word}
@media (max-width:620px){
  .pill{white-space:normal;text-align:start;max-width:100%}
  .hero .btn,.date-card .btn,#enqBtn{white-space:normal;text-align:center}
}
'''

FORM_JS = '''
(function(){
  var f=document.getElementById("enqForm"); if(!f) return;
  var btn=document.getElementById("enqBtn"), st=document.getElementById("enqStatus");
  var ENDPOINT="https://formsubmit.co/ajax/esolstleonards@tafensw.edu.au";
  var MSG={sending:{{JS_SENDING}},error:{{JS_ERROR}}};
  f.addEventListener("submit",function(e){
    e.preventDefault();
    if(!f.reportValidity()) return;
    var data={};
    new FormData(f).forEach(function(v,k){ data[k]=String(v).trim(); });
    if(data._honey){ done(); return; }
    delete data._honey;
    data["Page language"]={{JS_LANG}};
    data["Submitted"]=new Date().toLocaleString("en-AU",{timeZone:"Australia/Sydney"});
    data._subject="New English class enquiry – St Leonards ("+{{JS_LANG}}+" page)";
    data._template="table";
    data._captcha="false";
    if(!data.email) delete data.email;
    btn.disabled=true; st.className="fstatus"; st.textContent=MSG.sending;
    fetch(ENDPOINT,{method:"POST",headers:{"Content-Type":"application/json","Accept":"application/json"},body:JSON.stringify(data)})
      .then(function(r){ return r.json().catch(function(){ return {}; }).then(function(j){ return {ok:r.ok,j:j}; }); })
      .then(function(res){
        if(res.ok && String(res.j.success)==="true"){ done(); }
        else { fail(); }
      })
      .catch(fail);
  });
  function done(){
    f.hidden=true; document.getElementById("enqDone").hidden=false;
    document.getElementById("enqBox").scrollIntoView({behavior:"smooth",block:"center"});
  }
  function fail(){ btn.disabled=false; st.className="fstatus err"; st.textContent=MSG.error; }
})();
'''

# ---- Switched to Microsoft Forms (embedded on screen, QR code on print) ----
MSFORM_URL = "https://forms.office.com/r/xY44v3tmUZ"
MSFORM_EMBED = "https://forms.cloud.microsoft/Pages/ResponsePage.aspx?id=InJTGddVgUWE-8LaboNcdI723fir1b5Po48Qf5Q6vgZUQ0lXT1hHWTlUVTFISUZRRFg2Q0hXN1IxSS4u&amp;embed=true"
FORM_HTML = ''   # FormSubmit form removed
FORM_JS = ''
MSFORM_HTML = '''      <div class="qr-box print-qr">
        <img src="{{A}}assets/qr.png" alt="QR code">
        <h3>{{qr_h}}</h3>
        <p>{{qr_p}}</p>
      </div>
      <div class="msform" id="enquiry">
        <div class="msform-head">
          <div class="icon"><svg viewBox="0 0 24 24"><path d="M2 5h20v14H2zm2 2v.5l8 5 8-5V7l-8 5z"/></svg></div>
          <div><h3>{{form_h}}</h3><p>{{form_sub}}</p></div>
        </div>
        <iframe src="''' + MSFORM_EMBED + '''" title="{{form_h}}" loading="lazy" allowfullscreen webkitallowfullscreen mozallowfullscreen msallowfullscreen></iframe>
        <a class="msform-open" href="''' + MSFORM_URL + '''" target="_blank" rel="noopener">{{f_open}} <span aria-hidden="true">&#8599;</span></a>
      </div>'''
MSFORM_CSS = '''
/* Embedded Microsoft Form (screen) / QR code (print) */
.print-qr{display:none}
.contact{grid-template-columns:1fr 1.25fr;align-items:start}
.msform{background:#fff;border:1px solid var(--line);border-top:5px solid var(--red);border-radius:var(--radius);padding:24px;box-shadow:0 12px 40px rgba(20,30,50,.08)}
.msform-head{display:flex;gap:14px;align-items:flex-start;margin-bottom:14px}
.msform-head .icon{margin:0;flex:none}
.msform-head h3{font-size:1.5rem;font-weight:700;line-height:1.2}
.msform-head p{color:var(--muted);margin-top:4px}
.msform iframe{display:block;width:100%;height:1050px;border:0;border-radius:10px;background:var(--bg)}
.msform-open{display:inline-block;margin-top:12px;color:var(--red);font-weight:600;text-decoration:none}
.msform-open:hover{text-decoration:underline}
@media (max-width:900px){.contact{grid-template-columns:1fr}.msform iframe{height:1150px}}
@media (max-width:620px){.msform{padding:16px}.msform iframe{height:1250px}}
@media print{.print-qr{display:flex !important}.msform{display:none !important}}
'''
