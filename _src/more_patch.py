# Adds "find out more" buttons under the "What we offer" cards (TAFE NSW AMEP page + Home Affairs AMEP page).
# Applied to template.html by make_template.py (both St Leonards and Campsie builds).
MORE_URL = "https://www.tafensw.edu.au/programs/adult-migrant-english-program"
AMEP_URL = "https://immi.homeaffairs.gov.au/settling-in-australia/amep/about-the-program"
def apply_more(path):
    t = open(path, encoding='utf-8').read()
    anchor = '<h3>{{o6_t}}</h3><p>{{o6_d}}</p></div>\n      </div>\n'
    assert anchor in t
    t = t.replace(anchor, anchor +
        '      <p class="more">\n'
        '        <a class="btn btn-outline" href="' + MORE_URL + '" target="_blank" rel="noopener">{{more_link}} <span aria-hidden="true">&#8599;</span></a>\n'
        '        <a class="btn btn-outline" href="' + AMEP_URL + '" target="_blank" rel="noopener">{{amep_link}} <span aria-hidden="true">&#8599;</span></a>\n'
        '      </p>\n', 1)
    css = '''
/* Find out more links */
.more{display:flex;flex-wrap:wrap;justify-content:center;gap:14px;margin-top:36px}
.more .btn{font-size:1.02rem;padding:.8em 1.6em;white-space:normal;text-align:center;justify-content:center;max-width:100%}
@media (max-width:620px){.more .btn{width:100%}}
@media print{.more{display:none !important}}
'''
    t = t.replace('</style>', css + '</style>', 1)
    open(path, 'w', encoding='utf-8').write(t)
