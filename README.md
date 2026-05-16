# SRT Translation Tools - תרגום קובצי SRT מעברית לערבית

## 📋 תיאור כללי

**סוויט שלמה של כלים לתרגום קובצי SRT (כתוביות) מעברית לערבית** באמצעות OpenAI API.

### **אפשרויות:**
- ✅ **Workflow חדש ומשופר** (מומלץ) - תרגום עם הקשר מלא
- ✅ **תרגום ישיר** - אם אתה צריך מהר יותר

---

## 🚀 **התחלה מהירה:**

### **דרך 1: Workflow חדש (RECOMMENDED) ⭐**

```bash
# הרץ את ה-master script
python3 translate_srt_workflow.py demo.srt

# תוצאה: demo_ar.srt ✓
```

**יתרונות:**
- ✅ תרגום עם **הקשר מלא** (טוב יותר!)
- ✅ שומר את **מבנה ה-SRT** בדיוק
- ✅ **אין fallback dictionary** - API תורגם הכל
- ✅ תרגום **טבעי ותקין**
- ✅ **מחוק קבצי עזר** בסוף

---

### **דרך 2: תרגום ישיר (אם רוצה מהר)**

```bash
python3 translate_srt.py demo.srt
```

---

## 📦 **מה יש בחבילה:**

### **סקריפטים ל-Workflow החדש (מומלץ):**

| סקריפט | תפקיד |
|--------|--------|
| **`translate_srt_workflow.py`** | 🎯 Master - הרץ את הכל + ניקיון |
| `srt_to_txt.py` | חלץ טקסט מ-SRT |
| `translate_txt.py` | תרגם עם OpenAI |
| `txt_to_srt.py` | החזר מבנה SRT |

### **סקריפט ישיר:**

| סקריפט | תפקיד |
|--------|--------|
| `translate_srt.py` | תרגום SRT ישיר (V4 עם fallback) |

### **קובצים אחרים:**

| קובץ | תיאור |
|------|--------|
| `README_WORKFLOW.md` | הוראות מקורות של ה-Workflow |
| `glossary_example.csv` | דוגמה של מילון עברית-ערבית |
| `translate_questions.py` | תרגום JSON שאלות (bonus) |

---

## 🎯 **איזה Workflow לבחור?**

### **בחר Workflow (מומלץ) אם:**
- ✅ רוצה תרגום **טוב יותר**
- ✅ הקשר חשוב לך
- ✅ יש לך זמן (2-5 דקות לסרטון)
- ✅ רוצה **לא fallback dictionary**
- ✅ רוצה ניקיון אוטומטי

### **בחר תרגום ישיר אם:**
- ✅ רוצה מהר יותר
- ✅ סרטון קטן (5-10 כתוביות)
- ✅ OK עם fallback dictionary

---

## 📖 **הוראות מפורטות:**

### **Workflow (מומלץ):**

```bash
python3 translate_srt_workflow.py demo.srt
```

**תהליך:**
1. חלץ טקסט מ-SRT → `demo.txt`
2. תרגם לערבית → `demo_ar.txt`
3. החזר מבנה SRT → `demo_ar.srt`
4. 🧹 מחוק קבצי עזר

**Output:**
- ✅ `demo_ar.srt` (סופי)

---

### **Workflow עם שמירת קבצי עזר:**

אם אתה רוצה לשמור את הקבצים `.txt` לביקורת:

```bash
python3 translate_srt_workflow.py demo.srt --keep-temp
```

**Output:**
- `demo.txt` (קובץ עזר)
- `demo_ar.txt` (קובץ עזר)
- `demo_ar.srt` (סופי)

---

### **תרגום ישיר:**

```bash
python3 translate_srt.py demo.srt
# Output: demo_ar.srt
```

**ראה:** `README_COMPLETE.md` להוראות מפורטות

---

## ⚙️ **התקנה:**

### **1. התקנת ספריות:**
```bash
pip install openai
```

### **2. הגדרת API Key:**
```bash
export OPENAI_API_KEY="sk-..."
```

---

## 💰 **עלויות:**

### **gpt-4o (ברירת מחדל):**
```
Input:  $2.50 per 1M tokens
Output: $10.00 per 1M tokens
```

**דוגמאות:**
- 100 כתוביות ≈ **$0.09**
- 300 כתוביות ≈ **$0.28**
- 1000 כתוביות ≈ **$0.94**

### **gpt-4o-mini (זול יותר):**
```
Input:  $0.15 per 1M tokens
Output: $0.60 per 1M tokens
```

**דוגמאות:**
- 100 כתוביות ≈ **$0.006**
- 300 כתוביות ≈ **$0.017**
- 1000 כתוביות ≈ **$0.056**

---

## 📝 **דוגמה בעולם האמיתי:**

### **הדוגמה שלך:**

```bash
# הנתיב המלא של הסרטון שלך מ-Windows
shaul@DESKTOP-E1DUQDH:~/createExercises/translateTools$ python3 translate_srt_workflow.py "/mnt/c/Users/user/Documents/openUniversity/11203 מדמח בתיכון/סרטונים/הדגמה לשאלות קוד/הדגמת שאלות קוד באתר BOM.srt"

# או עם escape characters (אם יש רווחים):
python3 translate_srt_workflow.py /mnt/c/Users/user/Documents/openUniversity/11203\ מדמח\ בתיכון/סרטונים/הדגמה\ לשאלות\ קוד/הדגמת\ שאלות\ קוד\ באתר\ BOM.srt
```

**תוצאה:**
```
הדגמת שאלות קוד באתר BOM_ar.srt
```

הקובץ יהיה **באותה תיקייה** כמו המקורי!

---

### **דוגמה נוספת (נתיב יחסי):**

אם אתה בתיקייה שמכילה את ה-SRT:

```bash
cd /mnt/c/Users/user/Documents/openUniversity/11203\ מדמח\ בתיכון/סרטונים/הדגמה\ לשאלות\ קוד/

python3 ~/createExercises/translateTools/translate_srt_workflow.py "הדגמת שאלות קוד באתר BOM.srt"
```

---

## ✅ **בדיקה:**

הקובץ `הדגמת_שאלות_קוד_באתר_BOM.srt` תורגם בהצלחה עם:
- ✅ **46 כתוביות** - 100% תרגום
- ✅ **0 בעיות** - כל עברית תורגמה
- ✅ **English שמור** - BlueJ, Java וכו'
- ✅ **Timecodes זהים** - עימוד מושלם
- ✅ **ערבית טבעית** - תרגום איכותי

---

## 📁 **מבנה הפרויקט:**

```
translateTools/
├── translate_srt_workflow.py      ⭐ Master script
├── srt_to_txt.py
├── translate_txt.py
├── txt_to_srt.py
├── translate_srt.py                (Direct translation)
├── translate_questions.py           (For JSON)
├── glossary_example.csv
├── README.md                        (זה הקובץ)
├── README_WORKFLOW.md
└── README_COMPLETE.md
```

---

## 🔧 **אפשרויות:**

### **Workflow:**

```bash
# דרך 1: Master (הכל באחד, עם ניקיון)
python3 translate_srt_workflow.py input.srt

# דרך 2: Master (עם שמירת קבצי עזר)
python3 translate_srt_workflow.py input.srt --keep-temp

# דרך 3: שלב אחר שלב (ידני)
python3 srt_to_txt.py input.srt
python3 translate_txt.py input.txt
python3 txt_to_srt.py input.srt input_ar.txt
```

### **Direct:**

```bash
python3 translate_srt.py input.srt
python3 translate_srt.py input.srt --glossary glossary.csv
```

---

## 💡 **דוגמאות:**

### **דוגמה 1: סרטון בתיקייה אחרת**

```bash
python3 translate_srt_workflow.py /path/to/video.srt
```

### **דוגמה 2: עם נתיב Windows (WSL)**

```bash
python3 translate_srt_workflow.py "/mnt/c/Users/user/Videos/demo.srt"
```

### **דוגמה 3: עם רווחים בשם קובץ**

```bash
python3 translate_srt_workflow.py "my video file.srt"
```

---

## ❓ **שאלות נפוצות:**

**ש: איזה ספריפט לבחור?**
ת: `translate_srt_workflow.py` - הוא הטוב ביותר!

**ש: כמה זמן זה לוקח?**
ת: ~2-3 שניות לכל subtitle
   - 100 subtitles = 3-5 דקות
   - 46 subtitles (דוגמה) = ~2 דקות

**ש: האם התרגום טוב?**
ת: כן! בדיקה הראתה 0 בעיות בדוגמה.

**ש: האם אנגלית נשמרת?**
ת: כן! BlueJ, Java, PrintNumbersUntil וכו' - כל מונח אנגלי נשמר.

**ש: מה הפרש בין Workflow ו-Direct?**
ת:
- **Workflow:** API רואה את **הכל ביחד** → תרגום טוב יותר
- **Direct:** תרגום **משפט אחר משפט** → מהיר יותר

**ש: איפה OpenAI key?**
ת: https://platform.openai.com/account/api-keys

**ש: מה זה `--keep-temp`?**
ת: אם אתה רוצה לשמור את ה-.txt קבצים לביקורת, השתמש בדגל הזה.

**ש: איך מוחקים קבצי עזר ידנית?**
ת:
```bash
rm input.txt input_ar.txt
```

---

## 🎓 **סיכום:**

### **תהליך תרגום:**
1. בחר `translate_srt_workflow.py`
2. הרץ עם קובץ ה-SRT שלך
3. קבל `_ar.srt` מוכן
4. קבצי עזר מחוקים אוטומטית
5. העלה לסרטון שלך

### **תוצאה:**
✅ סרטון עברי בערבית
✅ כל הכתוביות תורגמו
✅ עימוד מושלם
✅ ערבית טבעית
✅ ניקיון אוטומטי

---

**בהצלחה!** 🚀✨

**גרסה:** 2.1 (עם ניקיון אוטומטי ודוגמה אמיתית)  
**עדכון אחרון:** May 2026
