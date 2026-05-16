# SRT Translation Workflow

## 📋 תיאור כללי

**תהליך תרגום חדש ומשופר** המתרגם קובצי SRT מעברית לערבית עם הקשר מלא.

### **האיך זה עובד:**

```
demo.srt (עברית)
    ↓
[srt_to_txt.py] → חלץ טקסט
    ↓
demo.txt (טקסט בלבד)
    ↓
[translate_txt.py] → תרגם עם OpenAI
    ↓
demo_ar.txt (ערבית)
    ↓
[txt_to_srt.py] → החזר מבנה SRT
    ↓
demo_ar.srt ✓
```

---

## 🚀 **שימוש מהיר:**

### **דרך 1: Master Script (מומלץ - הכל בפעם אחת)**

```bash
python3 translate_srt_workflow.py demo.srt
```

✓ עושה את כל 3 השלבים אוטומטית
✓ תוצאה: `demo_ar.srt`

---

### **דרך 2: שלב אחר שלב (לביקורת)**

```bash
# שלב 1: חלץ טקסט
python3 srt_to_txt.py demo.srt
# Output: demo.txt

# בדוק את demo.txt אם צריך...

# שלב 2: תרגם
python3 translate_txt.py demo.txt
# Output: demo_ar.txt

# בדוק את demo_ar.txt אם צריך...

# שלב 3: החזר SRT
python3 txt_to_srt.py demo.srt demo_ar.txt
# Output: demo_ar.srt
```

---

## 📁 **הסקריפטים:**

### **1. `srt_to_txt.py`** - חלץ טקסט

```bash
python3 srt_to_txt.py <input.srt>
```

**מה זה עושה:**
- ✓ קורא את קובץ ה-SRT
- ✓ מוציא את הטקסט בלבד (ללא index/timecode)
- ✓ שומר את מבנה השורות (כל subtitle בשורה נפרדת)
- ✓ שומר ל-TXT

**Output:** `input.txt`

---

### **2. `translate_txt.py`** - תרגם עם OpenAI

```bash
python3 translate_txt.py <input.txt>
```

**מה זה עושה:**
- ✓ קורא את קובץ ה-TXT
- ✓ **שולח את כל הטקסט ל-OpenAI כ-context אחד**
- ✓ מתרגם עברית לערבית
- ✓ שומר את מבנה השורות בדיוק
- ✓ שומר ל-TXT ערבי

**Output:** `input_ar.txt`

**יתרונות:**
- ✓ API רואה את **כל הטקסט ביחד** (הקשר מלא)
- ✓ תרגום טבעי יותר
- ✓ ללא צורך ב-fallback dictionary

---

### **3. `txt_to_srt.py`** - החזר מבנה SRT

```bash
python3 txt_to_srt.py <original.srt> <translated.txt>
```

**מה זה עושה:**
- ✓ קורא את ה-SRT המקורי (עבור index/timecode)
- ✓ קורא את הטקסט המתורגם
- ✓ משלב אותם חזרה
- ✓ שומר ל-SRT ערבי שלם

**Input:**
- `original.srt` - עם index וtimecode
- `translated.txt` - הטקסט המתורגם

**Output:** `original_ar.srt`

**תכונות:**
- ✓ UTF-8 with BOM
- ✓ CRLF line endings
- ✓ מבנה SRT תקין

---

### **4. `translate_srt_workflow.py`** - Master

```bash
python3 translate_srt_workflow.py <input.srt>
```

**מה זה עושה:**
- ✓ הרץ את כל 3 הסקריפטים בסדר
- ✓ מנהל את הקבצים הביניים
- ✓ מראה progress
- ✓ טיפול בשגיאות

**Output:** `input_ar.srt`

---

## ⚙️ **הגדרה:**

### **1. התקנת תלויות:**

```bash
pip install openai
```

### **2. הגדרת OpenAI API Key:**

```bash
export OPENAI_API_KEY="sk-..."
```

---

## 💡 **יתרונות הוויז הזה:**

✅ **הקשר מלא** - API תורגם הכל בקשר אחד
✅ **שומר מבנה** - אותו מספר שורות
✅ **קל לתקן** - אפשר לבדוק ב-TXT אם צריך
✅ **אין fallback** - API תורגם כל עברית
✅ **ברור** - כל שלב עושה משהו אחד

---

## 📊 **דוגמה מלאה:**

```bash
# הרץ את workflow
python3 translate_srt_workflow.py סרטון.srt

# תוצאה:
# סרטון.txt (טקסט בלבד)
# סרטון_ar.txt (תרגום ערבי)
# סרטון_ar.srt ✓ (קובץ SRT ערבי סופי)
```

---

## ❓ **שאלות נפוצות:**

**ש: האם צריך כל 4 הסקריפטים?**
ת: לא, רק `translate_srt_workflow.py` אם אתה משתמש בדרך קלה.
   בדרך ידנית - צריך את 3 + master.

**ש: מה לעשות אם התרגום לא טוב?**
ת: בדוק את `.txt` קודם שליחה ל-API. ממש קל לראות את הבעיה.

**ש: האם זה שומר את UTF-8 BOM ו-CRLF?**
ת: כן! בדיוק כמו בקובץ המקורי.

**ש: כמה זמן זה לוקח?**
ת: ~2-3 שניות לכל subtitle = 100 subtitles ≈ 3-5 דקות.

---

## 🎯 **מה הבא:**

1. ✓ הרץ את הworkflow
2. ✓ בדוק את התוצאה
3. ✓ השתמש ב-SRT הערבי בסרטון שלך!

---

**בהצלחה!** 🚀✨
