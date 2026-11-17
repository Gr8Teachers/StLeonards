"""St Leonards government-funded programs text -> langs/z_stl_programs.json"""
import json, os
K = ['gp_h', 'gp1', 'gp2', 'gp3']
P = {
"en": ["Government-funded programs available at St Leonards", "Adult Migrant English Program (AMEP)", "Skills for Education and Employment (SEE)", "TAFE Fee-Free Courses"],
"ar": ["برامج ممولة من الحكومة متاحة في St Leonards", "برنامج اللغة الإنجليزية للمهاجرين البالغين (AMEP)", "مهارات التعليم والتوظيف (SEE)", "دورات TAFE المجانية"],
"prs": ["برنامه‌های تمویل‌شده توسط حکومت در St Leonards", "برنامه انگلیسی برای مهاجران بزرگسال (AMEP)", "مهارت‌ها برای تحصیل و استخدام (SEE)", "کورس‌های رایگان TAFE"],
"fa": ["برنامه‌های دولتی موجود در St Leonards", "برنامه زبان انگلیسی مهاجران بزرگسال (AMEP)", "مهارت‌هایی برای تحصیل و اشتغال (SEE)", "دوره‌های رایگان TAFE"],
"ps": ["په St Leonards کې د حکومت لخوا تمویل شوي پروګرامونه", "د لویو کډوالو لپاره د انګلیسي ژبې پروګرام (AMEP)", "د زده کړې او دندې لپاره مهارتونه (SEE)", "د TAFE وړیا کورسونه"],
"ckb": ["بەرنامە پشتگیریکراوەکانی حکومەت لە St Leonards", "بەرنامەی ئینگلیزی بۆ کۆچبەرە گەورەساڵەکان (AMEP)", "تواناکان بۆ خوێندن و کار (SEE)", "خولە بەخۆڕاییەکانی TAFE"],
"ur": ["St Leonards میں دستیاب حکومتی مالی امداد والے پروگرام", "بالغ تارکینِ وطن کے لیے انگریزی پروگرام (AMEP)", "تعلیم اور روزگار کے لیے مہارتیں (SEE)", "TAFE کے فیس فری کورسز"],
"kmr": ["Bernameyên bi fînansa hikûmetê li St Leonards", "Bernameya Îngilîzî ya Koçberên Mezin (AMEP)", "Jêhatîbûn ji bo Perwerde û Kar (SEE)", "Kursên belaş ên TAFE"],
"tr": ["St Leonards'da devlet destekli programlar", "Yetişkin Göçmen İngilizce Programı (AMEP)", "Eğitim ve İstihdam Becerileri (SEE)", "TAFE Ücretsiz Kursları"],
"zh": ["St Leonards 提供的政府资助项目", "成人移民英语项目 (AMEP)", "教育与就业技能项目 (SEE)", "TAFE 免学费课程"],
"ja": ["St Leonardsで受けられる政府助成プログラム", "成人移民英語プログラム（AMEP）", "教育・就労のためのスキルプログラム（SEE）", "TAFE授業料無料コース"],
"ko": ["St Leonards에서 제공하는 정부 지원 프로그램", "성인 이민자 영어 프로그램(AMEP)", "교육 및 취업 기술 프로그램(SEE)", "TAFE 수업료 무료 과정"],
"mn": ["St Leonards-д төрийн санхүүжилттэй хөтөлбөрүүд", "Насанд хүрэгч цагаачдын англи хэлний хөтөлбөр (AMEP)", "Боловсрол ба хөдөлмөр эрхлэлтийн ур чадвар (SEE)", "TAFE-ийн төлбөргүй сургалтууд"],
"my": ["St Leonards တွင် ရရှိနိုင်သော အစိုးရ ထောက်ပံ့သည့် အစီအစဉ်များ", "လူကြီး ရွှေ့ပြောင်းနေထိုင်သူများအတွက် အင်္ဂလိပ်စာ အစီအစဉ် (AMEP)", "ပညာရေးနှင့် အလုပ်အကိုင်အတွက် ကျွမ်းကျင်မှုများ (SEE)", "TAFE အခမဲ့ သင်တန်းများ"],
"km": ["កម្មវិធីដែលរដ្ឋាភិបាលឧបត្ថម្ភ នៅ St Leonards", "កម្មវិធីភាសាអង់គ្លេសសម្រាប់ជនអន្តោប្រវេសន៍ពេញវ័យ (AMEP)", "ជំនាញសម្រាប់ការអប់រំ និងការងារ (SEE)", "វគ្គសិក្សាឥតគិតថ្លៃរបស់ TAFE"],
"th": ["โครงการที่รัฐบาลสนับสนุนที่ St Leonards", "โครงการภาษาอังกฤษสำหรับผู้ย้ายถิ่นวัยผู้ใหญ่ (AMEP)", "ทักษะเพื่อการศึกษาและการทำงาน (SEE)", "หลักสูตรไม่เสียค่าเล่าเรียนของ TAFE"],
"vi": ["Các chương trình do chính phủ tài trợ tại St Leonards", "Chương trình Anh ngữ cho Người Di dân Trưởng thành (AMEP)", "Kỹ năng cho Giáo dục và Việc làm (SEE)", "Các khóa học miễn phí của TAFE"],
"id": ["Program yang didanai pemerintah di St Leonards", "Program Bahasa Inggris untuk Migran Dewasa (AMEP)", "Keterampilan untuk Pendidikan dan Pekerjaan (SEE)", "Kursus Bebas Biaya TAFE"],
"hi": ["St Leonards में उपलब्ध सरकारी वित्तपोषित कार्यक्रम", "वयस्क प्रवासी अंग्रेज़ी कार्यक्रम (AMEP)", "शिक्षा और रोज़गार के लिए कौशल (SEE)", "TAFE शुल्क-मुक्त पाठ्यक्रम"],
"ne": ["St Leonards मा उपलब्ध सरकारी अनुदानित कार्यक्रमहरू", "वयस्क आप्रवासी अंग्रेजी कार्यक्रम (AMEP)", "शिक्षा र रोजगारका लागि सीप (SEE)", "TAFE निःशुल्क कोर्सहरू"],
"pa": ["St Leonards ਵਿੱਚ ਉਪਲਬਧ ਸਰਕਾਰੀ ਫੰਡ ਵਾਲੇ ਪ੍ਰੋਗਰਾਮ", "ਬਾਲਗ ਪ੍ਰਵਾਸੀ ਅੰਗਰੇਜ਼ੀ ਪ੍ਰੋਗਰਾਮ (AMEP)", "ਸਿੱਖਿਆ ਅਤੇ ਰੁਜ਼ਗਾਰ ਲਈ ਹੁਨਰ (SEE)", "TAFE ਫੀਸ-ਮੁਕਤ ਕੋਰਸ"],
"ta": ["St Leonards-இல் கிடைக்கும் அரசு நிதியுதவி திட்டங்கள்", "வயது வந்த குடியேறிகளுக்கான ஆங்கிலத் திட்டம் (AMEP)", "கல்வி மற்றும் வேலைவாய்ப்புக்கான திறன்கள் (SEE)", "TAFE கட்டணமில்லா படிப்புகள்"],
"ru": ["Государственные программы в St Leonards", "Программа английского языка для взрослых мигрантов (AMEP)", "Навыки для образования и трудоустройства (SEE)", "Бесплатные курсы TAFE"],
"uk": ["Державні програми в St Leonards", "Програма англійської мови для дорослих мігрантів (AMEP)", "Навички для освіти та працевлаштування (SEE)", "Безкоштовні курси TAFE"],
"es": ["Programas financiados por el Gobierno en St Leonards", "Programa de Inglés para Migrantes Adultos (AMEP)", "Habilidades para la Educación y el Empleo (SEE)", "Cursos gratuitos de TAFE"],
"pt": ["Programas financiados pelo governo em St Leonards", "Programa de Inglês para Migrantes Adultos (AMEP)", "Habilidades para Educação e Emprego (SEE)", "Cursos gratuitos do TAFE"],
"sw": ["Mipango inayofadhiliwa na Serikali katika St Leonards", "Mpango wa Kiingereza kwa Wahamiaji Watu Wazima (AMEP)", "Ujuzi kwa Elimu na Ajira (SEE)", "Kozi za Bure za TAFE"],
"ti": ["ብመንግስቲ ዝምወሉ መደባት ኣብ St Leonards", "መደብ እንግሊዝኛ ንዓበይቲ ስደተኛታት (AMEP)", "ክእለታት ንትምህርትን ስራሕን (SEE)", "ናጻ ኮርሳት TAFE"],
}
assert len(P) == 28 and all(len(v) == 4 for v in P.values())
ROOT = os.path.dirname(os.path.abspath(__file__))
MORE = {"en":"Find out more about {x}","ar":"اعرف المزيد عن {x}","prs":"درباره {x} بیشتر بدانید","fa":"درباره {x} بیشتر بدانید","ps":"د {x} په اړه نور معلومات","ckb":"زیاتر دەربارەی {x} بزانە","ur":"{x} کے بارے میں مزید جانیں","kmr":"Li ser {x} bêtir fêr bibin","tr":"{x} hakkında daha fazla bilgi","zh":"进一步了解 {x}","ja":"{x}について詳しく見る","ko":"{x}에 대해 자세히 알아보기","mn":"{x}-ийн талаар дэлгэрэнгүй","my":"{x} အကြောင်း ပိုမိုသိရှိရန်","km":"ស្វែងយល់បន្ថែមអំពី {x}","th":"ดูข้อมูลเพิ่มเติมเกี่ยวกับ {x}","vi":"Tìm hiểu thêm về {x}","id":"Pelajari lebih lanjut tentang {x}","hi":"{x} के बारे में और जानें","ne":"{x} बारे थप जान्नुहोस्","pa":"{x} ਬਾਰੇ ਹੋਰ ਜਾਣੋ","ta":"{x} பற்றி மேலும் அறியுங்கள்","ru":"Подробнее о {x}","uk":"Докладніше про {x}","es":"Más información sobre {x}","pt":"Saiba mais sobre {x}","sw":"Pata maelezo zaidi kuhusu {x}","ti":"ብዛዕባ {x} ተወሳኺ ፍለጡ"}
assert set(MORE) == set(P)
XS = ['AMEP', 'SEE', 'TAFE Fee\u2011Free']
for k in P: P[k][0] = P[k][0].replace('St Leonards', '<bdi dir="ltr">St&nbsp;Leonards</bdi>')
out = {k: dict(zip(K, v)) for k, v in P.items()}
for k in out:
    for i, x in enumerate(XS, 1):
        out[k][f'gp{i}_more'] = MORE[k].replace('{x}', '<bdi dir="ltr">' + x.replace(' ', '&nbsp;') + '</bdi>')
json.dump(out, open(os.path.join(ROOT, 'langs', 'z_stl_programs.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
print('ok', len(P))
