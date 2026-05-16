# translate_srt.py — תרגום קובצי SRT מעברית לערבית

📍 **Repository:** GitHub

---

## 🚀 התחלה מהירה (3 צעדים)

### 1️⃣ הגדר API Key
```bash
export OPENAI_API_KEY="sk-..."
```

### 2️⃣ הרץ ללא glossary
```bash
python3 translate_srt.py הדגמת_שאלות_קוד_באתר_BOM.srt
```

### 3️⃣ (אופציונלי) הרץ עם glossary
```bash
python3 translate_srt.py הדגמת_שאלות_קוד_באתר_BOM.srt --glossary glossary.csv
```

---

## 📋 תיאור כללי

סקריפט Python שמתרגם קובצי כתוביות (SRT) מעברית לערבית באמצעות OpenAI API.

**תכונות עיקריות:**
- ✅ UTF-8 with BOM encoding
- ✅ CRLF line endings (תואם Windows)
- ✅ שמירת RTL/LTR directional marks
- ✅ שמירת מונחים באנגלית ללא שינוי
- ✅ תמיכה ב-CSV glossary לתרגום עקבי
- ✅ תרגום את כל המילים העבריות בהקשר המלא של המשפט

---

## 🛠️ התקנה והגדרה

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
מקبל,يستقبل
אלגוריתם,خوارزمية
BlueJ,BlueJ
Java,Java
```

---

## 🔄 כיצד הסקריפט עובד

### תהליך התרגום:

1. **קריאה:** קורא את קובץ ה-SRT עם BOM ו-CRLF
2. **פיצול:** מפצל לתיקיות (index, timecode, text)
3. **זיהוי שפה:** בודק אם יש אפילו תו עברי אחד
4. **העברה ל-API:** שולח **את כל המשפט** (עם הקשר!) ל-OpenAI
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
│  └─ בודק אם יש עברית (אפילו תו אחד)
│
├─ translate_subtitle_text()
│  └─ שולח את כל המשפט ל-OpenAI עם הקשר
│
└─ save_srt_file()
   └─ כותב .srt עם BOM + CRLF
```

---

## 🔧 הגדרות ופרמטרים

### Model (שורה 38)
```python
MODEL = "gpt-4o"
```

**אפשרויות:**
- `"gpt-4o"` - דיוק גבוה (יקר יותר) ⭐ **ברירת מחדל כרגע**
- `"gpt-4o-mini"` - דיוק טוב, זול יותר

**איך לשנות:**
פתח את `translate_srt.py` **בשורה 38** וערוך:
```python
# לדיוק גבוה (יקר):
MODEL = "gpt-4o"

# לחיסכון (זול):
MODEL = "gpt-4o-mini"
```

---

### Temperature (שורה 170)
```python
temperature=0.1
```
**0.1** = תרגום עקבי ודטרמיניסטי (מומלץ לטקסט טכני)

**אפשרויות:**
- **0.0-0.2:** תרגום עקבי ודיוק גבוה ✓
- **0.3-0.5:** איזון בין דיוק לגיוון
- **0.7+:** יצירתי אך פחות עקבי

**איך לשנות:**
פתח את `translate_srt.py` **בשורה 170** וערוך:
```python
# לדיוק גבוה:
temperature=0.1

# לגיוון יותר:
temperature=0.3
```

---

## 💰 עלויות API

### gpt-4o (המודל הנוכחי - שורה 38):
```
Input:  $2.50 per 1M tokens
Output: $10.00 per 1M tokens
```

**דוגמאות עלויות:**
- 100 כתוביות (≈7,500 tokens) ≈ **$0.09**
- 300 כתוביות (≈22,500 tokens) ≈ **$0.28**
- 1000 כתוביות (≈75,000 tokens) ≈ **$0.94**

### gpt-4o-mini (אפשרות חיסכוני - שורה 38):
```
Input:  $0.15 per 1M tokens
Output: $0.60 per 1M tokens
```

**דוגמאות עלויות:**
- 100 כתוביות ≈ **$0.006**
- 300 כתוביות ≈ **$0.017**
- 1000 כתוביות ≈ **$0.056**

### בחירת Model:

| Model | דיוק | עלות | אופן שימוש |
|-------|------|------|-----------|
| **gpt-4o** (שורה 38) | גבוה ⭐ | יקר | דיוק קריטי, תרגומים חשובים |
| gpt-4o-mini (שורה 38) | טוב | זול ✓ | תרגומים רבים, בדיקות |

### איך להחליף:

**בשורה 38 של `translate_srt.py`:**
```python
# עבור דיוק גבוה (יקר):
MODEL = "gpt-4o"

# עבור חיסכון (יותר זול):
MODEL = "gpt-4o-mini"
```

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

# או שנה את ה-model בשורה 38:
MODEL = "gpt-4o"  # לדיוק גבוה יותר
```

---

## 📤 פלט הסקריפט

### קבצים שנוצרים:
1. **`{input}_ar.srt`** - קובץ הכתוביות הערבי
   - UTF-8 with BOM
   - CRLF line endings
   - RTL/LTR marks משמורים
   - מונחים באנגלית ללא שינוי
   - **משפטים שלמים תורגמו בהקשר**

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
- כל משפט תורגם **בשלמותו עם הקשר מלא**

### ❌ תחמוקים נפוצים:
- אל תשנה את encoding של ה-SRT
- אל תבחור ב-temperature גדולה מ-0.3 (אלא אם אתה צריך גיוון)
- אל תשכח להגדיר את OpenAI API key

---

## ❓ שאלות נפוצות

**ש: האם אצטרך glossary?**
ת: לא, הוא אופציונלי. ללא glossary זה עדיין עובד טוב.

**ש: כמה זמן זה לוקח?**
ת: ~2-3 שניות לכל כתובית. 100 כתוביות ≈ 3-5 דקות.

**ש: איפה מקבלים OpenAI key?**
ת: https://platform.openai.com/account/api-keys

**ש: יכול להרוץ ללא אינטרנט?**
ת: לא, צריך חיבור ל-OpenAI API.

**ש: יכול להפעיל בלי glossary?**
ת: כן, בהחלט! הוא אופציונלי ומשפר דיוק בלבד.

**ש: האם תורגם כל מילה בנפרד?**
ת: לא! משפט שלם נשלח ל-OpenAI עם הקשר מלא, ככה התרגום טבעי ותקין.

**ש: מה עלות התרגום?**
ת: תלוי בmodel (שורה 38):
   - gpt-4o: ≈ $0.09 ל-100 כתוביות
   - gpt-4o-mini: ≈ $0.006 ל-100 כתוביות

---

## 🎓 סיכום כללי

### קבצים במכולה זו:

| קובץ | תיאור |
|------|-------|
| `translate_srt.py` | סקריפט התרגום הראשי |
| `translate_questions.py` | סקריפט לתרגום JSON שאלות |
| `glossary_example.csv` | דוגמה של מילון עברית-ערבית |

### זרימת עבודה מומלצת:

1. **שלב 1 - בדיקה:**
   ```bash
   python3 translate_srt.py test.srt
   ```

2. **שלב 2 - בדיקת איכות:**
   - בדוק את הפלט בעברית/ערבית
   - אם צריך, צור glossary

3. **שלב 3 - תרגום מלא:**
   ```bash
   python3 translate_srt.py full_file.srt --glossary glossary.csv
   ```

4. **שלב 4 - שימוש בקובץ:**
   - העלה את `_ar.srt` לסרטון ב-YouTube/Moodle

---

## 📚 מידע נוסף

### קישורים שימושיים:
- [OpenAI API Documentation](https://platform.openai.com/docs)
- [SRT Format Specification](https://en.wikipedia.org/wiki/SubRip)
- [UTF-8 BOM Information](https://unicode.org/reports/tr3/)

### קבצים משלימים:
- `glossary_example.csv` - דוגמה של מילון

---

## 📞 תמיכה

אם יש בעיות:
1. בדוק את ה-error message בזהירות
2. וודא שקובץ ה-input קיים
3. בדוק ש-API key תקין
4. נסה עם דוגמה קטנה קודם

---

**גרסה:** 1.1 (gpt-4o model, עם מספרי שורות מדויקים)  
**עדכון אחרון:** May 2026  
**ממוצע זמן תרגום:** ~2-3 שניות ל-subtitle

**מוכן להתחיל?** בהצלחה! 🎬✨
