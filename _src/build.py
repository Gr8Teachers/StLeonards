import json, os, re, glob, html, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, 'site')

# folder, html lang, dir, native name, English name
LANGS = [
    ('',    'en',      'ltr', 'English',            'Original'),
    ('ar',  'ar',      'rtl', 'العربية',             'Arabic'),
    ('my',  'my',      'ltr', 'မြန်မာ',              'Burmese'),
    ('prs', 'fa-AF',   'rtl', 'دری',                 'Dari'),
    ('fa',  'fa',      'rtl', 'فارسی',               'Farsi'),
    ('hi',  'hi',      'ltr', 'हिन्दी',               'Hindi'),
    ('id',  'id',      'ltr', 'Bahasa Indonesia',   'Indonesian'),
    ('ja',  'ja',      'ltr', '日本語',               'Japanese'),
    ('km',  'km',      'ltr', 'ខ្មែរ',                'Khmer'),
    ('ko',  'ko',      'ltr', '한국어',               'Korean'),
    ('kmr', 'ku',      'ltr', 'Kurmancî',           'Kurdish (Kurmanji)'),
    ('ckb', 'ckb',     'rtl', 'کوردی سۆرانی',        'Kurdish (Sorani)'),
    ('mn',  'mn',      'ltr', 'Монгол',             'Mongolian'),
    ('ne',  'ne',      'ltr', 'नेपाली',               'Nepali'),
    ('ps',  'ps',      'rtl', 'پښتو',                'Pashto'),
    ('pt',  'pt',      'ltr', 'Português',          'Portuguese'),
    ('pa',  'pa',      'ltr', 'ਪੰਜਾਬੀ',               'Punjabi'),
    ('ru',  'ru',      'ltr', 'Русский',            'Russian'),
    ('zh',  'zh-Hans', 'ltr', '简体中文',             'Simplified Chinese'),
    ('es',  'es',      'ltr', 'Español',            'Spanish'),
    ('sw',  'sw',      'ltr', 'Kiswahili',          'Swahili'),
    ('ta',  'ta',      'ltr', 'தமிழ்',               'Tamil'),
    ('th',  'th',      'ltr', 'ภาษาไทย',             'Thai'),
    ('ti',  'ti',      'ltr', 'ትግርኛ',               'Tigrinya'),
    ('tr',  'tr',      'ltr', 'Türkçe',             'Turkish'),
    ('uk',  'uk',      'ltr', 'Українська',         'Ukrainian'),
    ('ur',  'ur',      'rtl', 'اردو',                'Urdu'),
    ('vi',  'vi',      'ltr', 'Tiếng Việt',         'Vietnamese'),
]

tpl = open(os.path.join(ROOT, 'template.html'), encoding='utf-8').read()
en = json.load(open(os.path.join(ROOT, 'langs', 'en.json'), encoding='utf-8'))
trans = {}
for f in glob.glob(os.path.join(ROOT, 'langs', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    if os.path.basename(f) == 'en.json':
        continue
    for lk, lv in d.items():
        trans.setdefault(lk, {}).update(lv)

zoom = json.load(open(os.path.join(ROOT, 'zoom.json'))) if os.path.exists(os.path.join(ROOT, 'zoom.json')) else {}
only = os.environ.get('ONLY')

def lang_items(cur):
    out = []
    for folder, code, d, native, eng in LANGS:
        if folder not in ('',) and folder not in trans:
            continue
        here = '' if cur == '' else '../'
        href = here + (folder + '/' if folder else '')
        if href == '':
            href = './'
        cls = ' class="current" aria-current="page"' if folder == cur else ''
        li = ' class="lang-en"' if folder == '' else ''
        out.append(f'          <li{li}><a href="{href}" hreflang="{code}"{cls}><span class="ln" lang="{code}" dir="{d}">{native}</span><span class="le">{eng}</span></a></li>')
    return '\n'.join(out)

built = []
for folder, code, d, native, eng in LANGS:
    if folder and folder not in trans:
        continue
    if only and folder not in only.split(','):
        continue
    s = dict(en)
    if folder:
        missing = [k for k in en if k not in trans[folder] and k not in ('dc_where','cal_mid','cal_bot')]
        if missing:
            print('MISSING', folder, missing)
        s.update(trans[folder])
    if d == 'rtl':
        for k, v in s.items():
            s[k] = re.sub(r'(?<![\d/])(\d{1,2}[/.]\d{1,2}(?:[/.]\d{4})?)(?![\d/])', r'<bdi dir="ltr">\1</bdi>', v)
    page = tpl
    page = page.replace('{{LANG}}', code).replace('{{DIR}}', d)
    page = page.replace('{{A}}', '' if not folder else '../')
    page = page.replace('{{PATH}}', '' if not folder else '/' + folder)
    zv = zoom.get(folder or 'en', 0.86)
    page = page.replace('{{ZOOM}}', str(zv))
    page = page.replace('{{LANG_ITEMS}}', lang_items(folder))
    page = page.replace('{{JS_LANG}}', json.dumps(eng if folder else 'English')).replace('{{JS_SENDING}}', json.dumps(html.unescape(s['f_sending']))).replace('{{JS_ERROR}}', json.dumps(html.unescape(s['f_error'])))
    page = page.replace('{{CAL_CLS}}', ' sm' if s.get('cal_sm') else '')
    for k, v in s.items():
        val = v
        if k in ('title', 'meta_desc'):
            val = html.escape(re.sub('<[^>]+>', '', html.unescape(v)), quote=True)
        page = page.replace('{{' + k + '}}', val)
    left = re.findall(r'\{\{[^}]+\}\}', page)
    if left:
        print('UNFILLED', folder, set(left))
    dest = os.path.join(OUT, folder) if folder else OUT
    os.makedirs(dest, exist_ok=True)
    open(os.path.join(dest, 'index.html'), 'w', encoding='utf-8').write(page)
    built.append(folder or 'en')

import shutil
if os.path.exists(os.path.join(OUT, 'assets')):
    shutil.rmtree(os.path.join(OUT, 'assets'))
shutil.copytree(os.path.join(ROOT, 'assets'), os.path.join(OUT, 'assets'))
print('built', len(built), ' '.join(built))
