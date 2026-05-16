#!/usr/bin/env python3
"""
translate_srt.py
----------------
Translates SRT subtitle files from Hebrew to Arabic using OpenAI API.
Preserves:
- UTF-8 with BOM encoding
- CRLF line endings
- RTL/LTR directional marks and HTML tags
- Timing information
- Numeric and English text

Usage:
    python3 translate_srt.py input.srt [--glossary glossary.csv]

Requirements:
    pip install openai

Set API Key:
    export OPENAI_API_KEY="sk-..."

Glossary Format (CSV):
    hebrew,arabic
    לולאת while,حلقة while
    שיטה סטטית,دالة ساكنة
"""

import sys
import os
import csv
from pathlib import Path
from openai import OpenAI

# ─── API Key ─────────────────────────────────────────────────────
API_KEY = os.environ.get("OPENAI_API_KEY", "")
# ─────────────────────────────────────────────────────────────────

MODEL = "gpt-4o"

# ─── Technical Terms (preserved as-is) ──────────────────────────
PRESERVE_TERMS = {
    "BlueJ", "Java", "main", "println", "print", "while", 
    "public", "static", "void", "int", "String", "for", "if",
    "return", "class", "new", "extends", "implements"
}

# ─── RTL/LTR Control Characters ───────────────────────────────
RLE = '\u202A'  # Right-to-Left Embedding
LRE = '\u202B'  # Left-to-Right Embedding
PDF = '\u202C'  # Pop Directional Formatting
RLM = '\u200F'  # Right-to-Left Mark
LRM = '\u200E'  # Left-to-Right Mark

# ─── Global Glossary ──────────────────────────────────────────
GLOSSARY = {}


def load_glossary_csv(csv_path: str) -> dict:
    """
    Load glossary from CSV file.
    Expected format:
        hebrew,arabic
        עברית,عربي
        ...
    
    Returns dict: {hebrew_term: arabic_term}
    """
    glossary = {}
    
    try:
        with open(csv_path, 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            
            # Check if header exists
            if reader.fieldnames is None or 'hebrew' not in reader.fieldnames or 'arabic' not in reader.fieldnames:
                print(f"Error: CSV must have 'hebrew' and 'arabic' columns")
                return glossary
            
            for row in reader:
                hebrew = row.get('hebrew', '').strip()
                arabic = row.get('arabic', '').strip()
                
                if hebrew and arabic:
                    glossary[hebrew] = arabic
        
        print(f"✓ Loaded {len(glossary)} terms from glossary")
        return glossary
    
    except FileNotFoundError:
        print(f"Error: Glossary file not found: {csv_path}")
        sys.exit(1)
    except Exception as e:
        print(f"Error reading glossary: {e}")
        sys.exit(1)


def detect_language(text: str) -> str:
    """Detect if text is Hebrew, English, or mixed."""
    hebrew_chars = sum(1 for c in text if '\u0590' <= c <= '\u05FF')
    english_chars = sum(1 for c in text if c.isascii() and c.isalpha())
    
    if hebrew_chars > english_chars:
        return "hebrew"
    elif english_chars > hebrew_chars:
        return "english"
    else:
        return "mixed"


def format_glossary_for_prompt(glossary: dict) -> str:
    """Format glossary for inclusion in the prompt."""
    if not glossary:
        return ""
    
    lines = ["Glossary (Hebrew → Arabic):"]
    for hebrew, arabic in list(glossary.items())[:20]:  # Limit to 20 for token count
        lines.append(f"  {hebrew} → {arabic}")
    
    if len(glossary) > 20:
        lines.append(f"  ... and {len(glossary) - 20} more terms")
    
    return "\n".join(lines)


def translate_subtitle_text(client, text: str, glossary: dict = None) -> str:
    """Translate a subtitle line, preserving RTL/LTR markers."""
    
    # Detect language
    lang = detect_language(text)
    
    # If it's pure English, don't translate
    if lang == "english":
        return text
    
    # Build glossary section
    glossary_text = ""
    if glossary:
        glossary_text = f"\n\nUSE THIS GLOSSARY FOR CONSISTENT TRANSLATION:\n{format_glossary_for_prompt(glossary)}"
    
    # Build prompt for translation
    prompt = f"""You are a professional translator from Hebrew to Arabic,
specializing in educational content about programming.

IMPORTANT RULES:
1. Translate Hebrew text to Arabic
2. Keep English words and numbers EXACTLY as they are
3. Preserve all formatting marks like:
   - <rtl>, </rtl>, <ltr>, </ltr> tags
   - Unicode directional characters (‮, ‬, ‫, etc.)
4. Keep variable names, function names, and technical terms unchanged
5. Return ONLY the translated text with original formatting{glossary_text}

TEXT TO TRANSLATE:
{text}

Remember:
- Do NOT modify English technical terms
- Do NOT change formatting marks
- Translate only Hebrew content
- If a term appears in the glossary, use that translation"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )

    translated = response.choices[0].message.content.strip()
    return translated


def parse_srt_file(file_path: str) -> list:
    """
    Parse SRT file with UTF-8 BOM encoding and CRLF line endings.
    Returns list of subtitle blocks: [index, timecode, text_lines]
    """
    # Read with UTF-8-sig to handle BOM automatically
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        content = f.read()
    
    # Normalize line endings to \n for parsing (but remember we had CRLF)
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Split by double newlines to get subtitle blocks
    blocks = content.split('\n\n')
    
    subtitles = []
    for block in blocks:
        if not block.strip():
            continue
        
        lines = block.strip().split('\n')
        if len(lines) < 3:
            continue
        
        # SRT format: index, timecode, text (can be multiple lines)
        try:
            index = int(lines[0])
            timecode = lines[1]
            text_lines = lines[2:]
            
            subtitles.append({
                'index': index,
                'timecode': timecode,
                'text': '\n'.join(text_lines)
            })
        except (ValueError, IndexError):
            # Skip malformed blocks
            continue
    
    return subtitles


def save_srt_file(file_path: str, subtitles: list):
    """
    Save SRT file with UTF-8 BOM encoding and CRLF line endings.
    Preserves RTL/LTR directional marks.
    """
    output_lines = []
    
    for sub in subtitles:
        output_lines.append(str(sub['index']))
        output_lines.append(sub['timecode'])
        output_lines.append(sub['text'])
        output_lines.append('')  # Empty line between subtitles
    
    content = '\n'.join(output_lines)
    
    # Write with UTF-8-sig (includes BOM) and CRLF line endings
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
        # Convert \n to \r\n for CRLF
        content = content.replace('\n', '\r\n')
        f.write(content)


def translate_srt(input_path: str, glossary_path: str = None, client: OpenAI = None) -> str:
    """Main translation function."""
    
    input_file = Path(input_path)
    if not input_file.exists():
        print(f"Error: file '{input_path}' not found.")
        sys.exit(1)
    
    # Load glossary if provided
    glossary = {}
    if glossary_path:
        glossary = load_glossary_csv(glossary_path)
    
    print(f"Loading SRT file: {input_file.name}")
    subtitles = parse_srt_file(input_path)
    
    if not subtitles:
        print("Error: no subtitles found in file.")
        sys.exit(1)
    
    print(f"Found {len(subtitles)} subtitles")
    
    translated_subtitles = []
    
    for i, sub in enumerate(subtitles, 1):
        print(f"Translating subtitle {i}/{len(subtitles)}...", end=" ", flush=True)
        try:
            translated_text = translate_subtitle_text(client, sub['text'], glossary)
            
            translated_subtitles.append({
                'index': sub['index'],
                'timecode': sub['timecode'],
                'text': translated_text
            })
            print("✓")
        except Exception as e:
            print(f"✗ Error: {e}")
            sys.exit(1)
    
    # Generate output file name
    output_path = input_file.parent / f"{input_file.stem}_ar.srt"
    
    print(f"\nSaving Arabic subtitles...")
    save_srt_file(str(output_path), translated_subtitles)
    
    print(f"✓ Done!")
    print(f"  Input:  {input_file}")
    if glossary_path:
        print(f"  Glossary: {glossary_path}")
    print(f"  Output: {output_path}")
    
    return str(output_path)


def print_help():
    print("""
translate_srt.py — Hebrew to Arabic SRT Translator
===================================================

USAGE:
    python3 translate_srt.py <srt_file> [--glossary <glossary.csv>]

ARGUMENTS:
    <srt_file>          Path to an SRT subtitle file
    --glossary FILE     (Optional) Path to CSV glossary file

OUTPUT:
    <name>_ar.srt       Arabic subtitles with:
                        - UTF-8 with BOM encoding
                        - CRLF line endings
                        - RTL/LTR marks preserved
                        - English and technical terms unchanged
                        - Glossary terms applied consistently

GLOSSARY CSV FORMAT:
    The CSV must have two columns: 'hebrew' and 'arabic'
    
    Example glossary.csv:
    ───────────────────────────────────────────
    hebrew,arabic
    לולאת while,حلقة while
    שיטה סטטית,دالة ساكنة
    מספר שלם,عدد صحيح
    ספרה,رقم
    סכום,مجموع
    ───────────────────────────────────────────

SETUP (one time only):
    1. Install OpenAI library:
           pip install openai
    2. Set your OpenAI API key:
           export OPENAI_API_KEY="sk-..."

EXAMPLES:
    # Simple translation (no glossary)
    python3 translate_srt.py demo_video.srt

    # Translation with glossary
    python3 translate_srt.py demo_video.srt --glossary glossary.csv

    # Different directory
    python3 translate_srt.py subtitles/hebrew_subs.srt --glossary terms/tech_glossary.csv

FEATURES:
    ✓ Automatic language detection
    ✓ Preserves RTL/LTR directional marks and HTML tags
    ✓ Keeps English text and technical terms unchanged
    ✓ UTF-8 with BOM encoding
    ✓ CRLF line endings (Windows-compatible)
    ✓ Optional CSV glossary for consistent terminology
    ✓ Low temperature (0.1) for consistent translation

OPTIONS:
    -h, --help, -?      Show this help message
""")


def main():
    if len(sys.argv) < 2 or sys.argv[1] in ("-h", "--help", "-?"):
        print_help()
        sys.exit(0)
    
    if not API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        print("Run: export OPENAI_API_KEY='sk-...'")
        sys.exit(1)
    
    input_file = sys.argv[1]
    glossary_file = None
    
    # Parse optional glossary argument
    if len(sys.argv) >= 4 and sys.argv[2] in ("--glossary", "-g"):
        glossary_file = sys.argv[3]
    
    client = OpenAI(api_key=API_KEY)
    translate_srt(input_file, glossary_file, client)


if __name__ == "__main__":
    main()
