# translate_srt.py — תרגום קובצי SRT מעברית לערבית

## 📋 תיאור כללי

סקריפט Python שמתרגם קובצי כתוביות (SRT) מעברית לערבית באמצעות OpenAI API.

**תכונות עיקריות:**
- ✅ UTF-8 with BOM encoding
- ✅ CRLF line endings (תואם Windows)
- ✅ שמירת RTL/LTR directional marks
- ✅ שמירת מונחים באנגלית ללא שינוי
- ✅ תמיכה ב-CSV glossary לתרגום עקבי

---

## 🚀 התקנה והגדרה

### 1. התקנת ספריות נדרשות
```bash
pip install openai
```

### 2. הגדרת OpenAI API Key

בחר אחת מהאפשרויות:

**אפשרות א - Environment Variable (מומלץ):**
```bash
export OPENAI_API_KEY="sk-..."
```

**אפשרות ב - Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="sk-..."
```

---

## 📖 דוגמאות שימוש

### דוגמה 1: תרגום פשוט (ללא glossary)
```bash
python3 translate_srt.py הדגמת_שאלות_קוד_באתר_BOM.srt
```
**תוצאה:**
```
הדגמת_שאלות_קוד_באתר_BOM_ar.srt
```

### דוגמה 2: תרגום עם CSV glossary
```bash
python3 translate_srt.py הדגמת_שאלות_קוד_באתר_BOM.srt --glossary glossary.csv
```

### דוגמה 3: קבצים בתיקיות שונות
```bash
python3 translate_srt.py subtitles/video.srt --glossary terms/glossary.csv
```

### דוגמה 4: קבלת עזרה
```bash
python3 translate_srt.py --help
```

---

## 📝 פורמט CSV Glossary

### מבנה הקובץ
```csv
hebrew,arabic
לולאת while,حلقة while
שיטה סטטית,دالة ساكنة
מספר שלם,عدد صحيح
```

### כללים חשובים:
1. **Headers חובה:** `hebrew` ו-`arabic` בשורה הראשונה
2. **Encoding:** UTF-8 (ללא BOM)
3. **Separator:** פסיק (`,`)
4. **סדר:** עברית בעמודה ראשונה, ערבית בשנייה

### דוגמת קובץ מלא:
```csv
hebrew,arabic
לולאת while,حلقة while
שיטה סטטית,دالة ساكنة
מספר שלם,عدد صحيح
ספרה,رقم
סכום,مجموع
הדפסה,طباعة
מחזיר,يُرجع
מקבל,يستقبل
אלגוריתם,خوارزمية
BlueJ,BlueJ
Java,Java
```

---

## 🔄 כיצד הסקריפט עובד

### תהליך התרגום:

1. **קריאה:** קורא את קובץ ה-SRT עם BOM ו-CRLF
2. **פיצול:** מפצל לתיקיות (index, timecode, text)
3. **זיהוי שפה:** מזהה אם טקסט הוא עברית או אנגלית
4. **העברה ל-API:** שולח טקסט עברי בלבד לתרגום
5. **שמירה:** כותב קובץ ערבי עם אותן הגדרות כמו המקור

### דוגמה של טקסט שמתורגם:

**קלט (עברית):**
```
בסרטון זה, אדגים תרגול של תרגילי הכתיבה שנמצאים
באתר הקורס. נשתמש בסביבת העבודה BlueJ, אבל ניתן
```

**פלט (ערבית):**
```
في هذا الفيديو، سأوضح الممارسة من تمارين الكتابة الموجودة
على موقع الدورة. سنستخدم بيئة العمل BlueJ، لكن يمكن
```

---

## 📊 ארכיטקטורה

```
translate_srt.py
│
├─ parse_srt_file()
│  └─ קורא .srt וחוזר subtitles list
│
├─ load_glossary_csv()
│  └─ טוען מונחים מקובץ CSV
│
├─ detect_language()
│  └─ מזהה עברית/אנגלית/מעורבב
│
├─ translate_subtitle_text()
│  └─ שולח לOpenAI עם glossary
│
└─ save_srt_file()
   └─ כותב .srt עם BOM + CRLF
```

---

## 🔧 הגדרות ופרמטרים

### Model
```python
MODEL = "gpt-4o-mini"
```
ניתן לשנות ל-`gpt-4o` לתרגום מדויק יותר (כמו שעלות גבוהה יותר)

### Temperature
```python
temperature=0.1
```
**0.1** = תרגום עקבי ודטרמיניסטי (מומלץ לטקסט טכני)
- **0.0-0.2:** תרגום עקבי ודיוק גבוה
- **0.3-0.5:** איזון בין דיוק לגיוון
- **0.7+:** יצירתי אך פחות עקבי

---

## 🛠️ פתרון בעיות

### שגיאה: "OPENAI_API_KEY is not set"
```bash
# בדוק שה-key הוגדר:
echo $OPENAI_API_KEY

# אם לא, הגדר אותו:
export OPENAI_API_KEY="sk-..."
```

### שגיאה: "file not found"
```bash
# בדוק שהנתיב נכון:
ls הדגמת_שאלות_קוד_באתר_BOM.srt

# או תן את הנתיב המלא:
python3 translate_srt.py /full/path/to/file.srt
```

### שגיאה: "CSV must have 'hebrew' and 'arabic' columns"
```bash
# בדוק את headers בקובץ CSV:
head -1 glossary.csv
# צריך להראות: hebrew,arabic
```

### התרגום לא מדויק
```bash
# נסה להוסיף/לעדכן glossary:
python3 translate_srt.py input.srt --glossary glossary.csv

# או שנה את ה-model:
# עדכן את שורה 47 ל: MODEL = "gpt-4o"
```

---

## 📤 פלט הסקריפט

### קבצים שנוצרים:
1. **`{input}_ar.srt`** - קובץ הכתוביות הערבי
   - UTF-8 with BOM
   - CRLF line endings
   - RTL/LTR marks משמורים
   - מונחים באנגלית ללא שינוי

### דוגמה של פלט:
```
1
00:00:00,010 --> 00:00:04,170
في هذا الفيديو، سأوضح الممارسة من تمارين الكتابة الموجودة

2
00:00:04,170 --> 00:00:09,090
‫على موقع الدورة. سنستخدم بيئة العمل BlueJ، لكن يمكن
```

---

## 💡 טיפים וכללים

### ✅ עדיפויות טובות:
- השתמש ב-glossary עבור מונחים קבועים
- בדוק תרגום דוגמה לפני הרצה מלאה
- שמור את קובץ ה-glossary שלך לשימוש חוזר

### ❌ תחמוקים נפוצים:
- אל תשנה את encoding של ה-SRT
- אל תבחור ב-temperature גדולה מ-0.3
- אל תשכח להגדיר את OpenAI API key

---

## 📚 מידע נוסף

### קבצים משלימים:
- `glossary_example.csv` - דוגמה של מילון

### קישורים שימושיים:
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [SRT Format Specification](https://en.wikipedia.org/wiki/SubRip)
- [UTF-8 BOM Information](https://unicode.org/reports/tr3/)

---

## 📞 תמיכה

אם יש בעיות:
1. בדוק את ה-error message בזהירות
2. וודא שקובץ ה-input קיים
3. בדוק ש-API key תקין
4. נסה עם דוגמה קטנה קודם

---

**גרסה:** 1.0  
**עדכון אחרון:** May 2026  
**ממוצע זמן תרגום:** ~2-3 שניות ל-subtitle
