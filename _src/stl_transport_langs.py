"""St Leonards transport lines -> langs/z_stl_transport.json"""
import json, os
# walk format ({n} minutes, {p} = station name kept in English), bus line
F = {
"en": ["{n}-minute walk from {p} Station", "All bus services on <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ar": ["على بُعد {n} دقائق سيرًا على الأقدام من محطة {p}", "جميع خطوط الحافلات على <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"prs": ["{n} دقیقه پیاده‌روی از ایستگاه {p}", "همه خطوط بس در <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"fa": ["{n} دقیقه پیاده‌روی از ایستگاه {p}", "همه خطوط اتوبوس در <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ps": ["د {p} سټېشن څخه {n} دقیقې پلې لار", "د <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> ټولې بس کرښې"],
"ckb": ["{n} خولەک بە پێ لە وێستگەی {p}", "هەموو هێڵەکانی پاس لە <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ur": ["{p} اسٹیشن سے {n} منٹ کی پیدل مسافت", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> پر تمام بس سروسز"],
"kmr": ["{n} deqîqe meş ji Stasyona {p}", "Hemû xetên otobûsê li ser <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"tr": ["{p} İstasyonu'na {n} dakika yürüme mesafesinde", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> üzerindeki tüm otobüs hatları"],
"zh": ["距 {p} 站步行 {n} 分钟", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> 上所有公交线路"],
"ja": ["{p}駅から徒歩{n}分", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>を通るすべてのバス"],
"ko": ["{p} 역에서 도보 {n}분", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>의 모든 버스 노선"],
"mn": ["{p} буудлаас явганаар {n} минут", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> дээрх бүх автобусны чиглэл"],
"my": ["{p} ဘူတာမှ လမ်းလျှောက် {n} မိနစ်", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> ပေါ်ရှိ ဘတ်စ်ကားလိုင်းအားလုံး"],
"km": ["ដើរ {n} នាទីពីស្ថានីយ {p}", "ខ្សែឡានក្រុងទាំងអស់នៅលើ <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"th": ["เดิน {n} นาทีจากสถานี {p}", "รถเมล์ทุกสายบน <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"vi": ["Cách ga {p} {n} phút đi bộ", "Tất cả các tuyến xe buýt trên <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"id": ["{n} menit berjalan kaki dari Stasiun {p}", "Semua layanan bus di <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"hi": ["{p} स्टेशन से {n} मिनट की पैदल दूरी", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> पर सभी बस सेवाएँ"],
"ne": ["{p} स्टेसनबाट {n} मिनेट पैदल", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> मा सबै बस सेवा"],
"pa": ["{p} ਸਟੇਸ਼ਨ ਤੋਂ {n} ਮਿੰਟ ਦੀ ਪੈਦਲ ਦੂਰੀ", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi> 'ਤੇ ਸਾਰੀਆਂ ਬੱਸ ਸੇਵਾਵਾਂ"],
"ta": ["{p} நிலையத்திலிருந்து {n} நிமிட நடை", "<bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>-இல் அனைத்து பேருந்து சேவைகளும்"],
"ru": ["{n} минут пешком от станции {p}", "Все автобусы по <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"uk": ["{n} хвилин пішки від станції {p}", "Усі автобуси по <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"es": ["A {n} minutos a pie de la estación {p}", "Todos los autobuses de <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"pt": ["A {n} minutos a pé da estação {p}", "Todas as linhas de ônibus da <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"sw": ["Dakika {n} kwa miguu kutoka Kituo cha {p}", "Huduma zote za basi kwenye <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
"ti": ["ካብ መዕረፊ {p} {n} ደቒቕ ብእግሪ", "ኩሎም ኣውቶቡሳት ኣብ <bdi dir=\"ltr\">Pacific&nbsp;Hwy</bdi>"],
}
assert len(F) == 28
def P(x): return '<bdi dir="ltr">' + x.replace(' ', '&nbsp;') + '</bdi>'
out = {}
for k, (w, bus) in F.items():
    t1 = w.replace('{n}', '5').replace('{p}', P('St Leonards'))
    t2 = w.replace('{n}', '8').replace('{p}', P('Crows Nest Metro'))
    if k == 'en':
        t1 = '5-minute walk from St Leonards Train Station'; t2 = '8-minute walk from Crows Nest Metro Station'
    if k == 'ru': t1 = t1.replace('5 минут', '5 минут'); t2 = t2.replace('8 минут', '8 минут')
    out[k] = {'tr1': t1, 'tr2': t2, 'tr3': bus}
ROOT = os.path.dirname(os.path.abspath(__file__))
json.dump(out, open(os.path.join(ROOT, 'langs', 'z_stl_transport.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('ok', len(out))
