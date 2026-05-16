# 🚀 QUICK START - התחלה מהירה

## בדקה אחת: הכל מה שצריך לדעת

---

## 1️⃣ **הגדרה (פעם אחת בלבד)**

```bash
# התקנת ספריה
pip install openai

# הגדרת API Key
export OPENAI_API_KEY="sk-..."
```

✅ **סיים!** עכשיו אתה מוכן.

---

## 2️⃣ **הרץ את התרגום**

```bash
python3 translate_srt_workflow.py demo.srt
```

**זהו!** הקובץ `demo_ar.srt` מוכן! ✓

---

## 3️⃣ **דוגמה אמיתית (כמו שלך):**

```bash
python3 translate_srt_workflow.py "/mnt/c/Users/user/Documents/openUniversity/11203 מדמח בתיכון/סרטונים/הדגמה לשאלות קוד/הדגמת שאלות קוד באתר BOM.srt"
```

**תוצאה:** 
```
הדגמת שאלות קוד באתר BOM_ar.srt ✓
```

---

## 📊 **זה כל הסיפור!**

| שלב | פקודה | תוצאה |
|-----|--------|--------|
| **1** | `pip install openai` | ספריה מותקנת |
| **2** | `export OPENAI_API_KEY="sk-..."` | API מוגדר |
| **3** | `python3 translate_srt_workflow.py input.srt` | `input_ar.srt` ✓ |

---

## 💡 **אפשרויות נוספות:**

### **שמור את קבצי העזר (.txt):**
```bash
python3 translate_srt_workflow.py demo.srt --keep-temp
```

### **תרגום ישיר (מהר יותר):**
```bash
python3 translate_srt.py demo.srt
```

---

## ⏱️ **כמה זמן?**

- 🔧 הגדרה: 1 דקה
- ⏳ תרגום: 2-5 דקות (תלוי במספר כתוביות)
- 📦 סה"כ: 5 דקות בשטח!

---

## 💰 **עלות:**

- 46 כתוביות (כמו בדוגמה) ≈ **$0.04**
- 100 כתוביות ≈ **$0.09**
- 300 כתוביות ≈ **$0.28**

---

## ✅ **בדיקה:**

```bash
# הרץ את הדוגמה
python3 translate_srt_workflow.py demo.srt

# בדוק את הקובץ
cat demo_ar.srt
```

✓ **אם אתה רואה ערבית** - עבד!

---

## 📚 **למידע יותר:**

- **README.md** - הוראות מלאות
- **README_WORKFLOW.md** - פרטים על ה-Workflow
- **README_COMPLETE.md** - תרגום ישיר

---

## 🎯 **זה הכל!**

**שלוש שורות:**
```bash
pip install openai
export OPENAI_API_KEY="sk-..."
python3 translate_srt_workflow.py demo.srt
```

**וסיים!** 🎉

---

**גרסה:** 2.1  
**עדכון אחרון:** May 2026
