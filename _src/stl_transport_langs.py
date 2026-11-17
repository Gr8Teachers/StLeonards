"""St Leonards transport lines -> langs/z_stl_transport.json"""
import json, os
# walk format ({n} minutes, {p} = station name kept in English), bus line
F = {
"en": ["{n}-minute walk from {p}", "All bus services on <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ar": ["{n} دقائق سيرًا من {p}", "جميع خطوط الحافلات على <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"prs": ["{n} دقیقه پیاده تا {p}", "همه خطوط بس در <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"fa": ["{n} دقیقه پیاده تا {p}", "همه خطوط اتوبوس در <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ps": ["له {p} څخه {n} دقیقې پلې", "د <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> ټولې بس کرښې"],
"ckb": ["{n} خولەک بە پێ لە {p}", "هەموو پاسەکانی <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ur": ["{p} سے {n} منٹ پیدل", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> پر تمام بسیں"],
"kmr": ["{n} deqîqe meş ji {p}", "Hemû otobûsên <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"tr": ["{p}'e {n} dakika yürüme", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> üzerindeki tüm otobüsler"],
"zh": ["距 {p} 步行 {n} 分钟", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> 上所有公交线路"],
"ja": ["{p}から徒歩{n}分", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>のすべてのバス"],
"ko": ["{p}에서 도보 {n}분", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>의 모든 버스"],
"mn": ["{p}-аас явганаар {n} минут", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>-ийн бүх автобус"],
"my": ["{p} မှ လမ်းလျှောက် {n} မိနစ်", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> ဘတ်စ်ကားအားလုံး"],
"km": ["ដើរ {n} នាទីពី {p}", "ឡានក្រុងទាំងអស់នៅ <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"th": ["เดิน {n} นาทีจาก {p}", "รถเมล์ทุกสายบน <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"vi": ["{n} phút đi bộ từ {p}", "Mọi tuyến xe buýt trên <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"id": ["{n} menit jalan kaki dari {p}", "Semua bus di <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"hi": ["{p} से {n} मिनट पैदल", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> पर सभी बसें"],
"ne": ["{p} बाट {n} मिनेट पैदल", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> मा सबै बस"],
"pa": ["{p} ਤੋਂ {n} ਮਿੰਟ ਪੈਦਲ", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> 'ਤੇ ਸਾਰੀਆਂ ਬੱਸਾਂ"],
"ta": ["{p}-இலிருந்து {n} நிமிட நடை", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> பேருந்துகள் அனைத்தும்"],
"ru": ["{n} мин пешком от {p}", "Все автобусы по <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"uk": ["{n} хв пішки від {p}", "Усі автобуси по <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"es": ["A {n} minutos a pie de {p}", "Todos los autobuses de <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"pt": ["A {n} minutos a pé de {p}", "Todos os ônibus da <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"sw": ["Dakika {n} kwa miguu kutoka {p}", "Mabasi yote ya <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ti": ["ካብ {p} {n} ደቒቕ ብእግሪ", "ኩሎም ኣውቶቡሳት ኣብ <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
}
assert len(F) == 28
def P(x): return '<bdi dir="ltr">' + x.replace(' ', '&nbsp;') + '</bdi>'
out = {}
for k, (w, bus) in F.items():
    t1 = w.replace('{n}', '5').replace('{p}', P('St Leonards Train'))
    t2 = w.replace('{n}', '8').replace('{p}', P('Crows Nest Metro'))
    if k == 'en':
        t1 = '5 min walk from St Leonards Train'; t2 = '8 min walk from Crows Nest Metro'
    if k == 'ru': t1 = t1.replace('5 минут', '5 минут'); t2 = t2.replace('8 минут', '8 минут')
    out[k] = {'tr1': t1, 'tr2': t2, 'tr3': bus}
ROOT = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(ROOT, 'langs', 'z_stl_transport.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('ok', len(out))
