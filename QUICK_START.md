# 🚀 התחלה מהירה

## 3 צעדים פשוטים:

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

## 📁 קבצים שקיבלת:

| קובץ | תיאור |
|------|-------|
| `translate_srt.py` | סקריפט התרגום הראשי |
| `glossary_example.csv` | דוגמה של מילון עברית-ערבית |
| `README.md` | דוקומנטציה מלאה |
| `QUICK_START.md` | קובץ זה |

---

## ✨ מה הסקריפט עושה:

```
input.srt (עברית)
       ↓
[זיהוי שפה]
       ↓
[שלח לOpenAI]
       ↓
[טעינת glossary אם קיים]
       ↓
input_ar.srt (ערבית ✓)
```

---

## 🎯 דוגמה מסיימת:

```bash
# הרץ עם glossary לתרגום עקבי
python3 translate_srt.py demo.srt --glossary my_glossary.csv

# תראה:
# ✓ Loaded 30 terms from glossary
# Found 100 subtitles
# Translating subtitle 1/100... ✓
# ... (עוד 99 כתוביות)
# ✓ Done!
#   Input:  demo.srt
#   Glossary: my_glossary.csv
#   Output: demo_ar.srt
```

---

## 📝 יצירת Glossary שלך:

1. פתח Excel או Text Editor
2. כתוב שתי עמודות:
   ```
   hebrew,arabic
   מונח עברי,مصطلح عربي
   ```
3. שמור כ-CSV (UTF-8, ללא BOM)
4. השתמש עם `--glossary`

---

## ❓ שאלות נפוצות:

**ש: האם אצטרך glossary?**
ת: לא, הוא אופציונלי. ללא glossary זה עדיין עובד טוב.

**ש: כמה זמן זה לוקח?**
ת: ~2-3 שניות לכל כתובית. 100 כתוביות ≈ 3-5 דקות.

**ש: איפה מקבלים OpenAI key?**
ת: https://platform.openai.com/account/api-keys

**ש: יכול להרוץ ללא אינטרנט?**
ת: לא, צריך חיבור ל-OpenAI API.

---

## 🔗 הצעות הבאות:

1. קרא את `README.md` לפרטים מלאים
2. תרגל עם קובץ קטן קודם
3. בנה glossary בהדרגה כשאתה משתמש

---

**מוכן להתחיל?** בהצלחה! 🎬✨
