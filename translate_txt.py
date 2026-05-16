#!/usr/bin/env python3
"""
translate_txt.py
----------------
Translates text file from Hebrew to Arabic using OpenAI API.
Preserves line structure - same number of lines in output.

Usage:
    python3 translate_txt.py input.txt
    
Output:
    input_ar.txt (Arabic translation)

Requirements:
    pip install openai
    export OPENAI_API_KEY="sk-..."
"""

import sys
import os
from pathlib import Path
from openai import OpenAI

# ─── API Key ─────────────────────────────────────────────────────
API_KEY = os.environ.get("OPENAI_API_KEY", "")
# ─────────────────────────────────────────────────────────────────

MODEL = "gpt-4o"


def load_text_file(file_path: str) -> str:
    """Load text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def translate_text(client, text: str) -> str:
    """
    Translate Hebrew text to Arabic.
    Preserves the structure of the text.
    """
    prompt = f"""You are a professional translator from Hebrew to Arabic,
specializing in educational content about programming.

Translate the following Hebrew text to Arabic.

CRITICAL RULES:
1. Translate ALL Hebrew text to Arabic
2. Keep English words and numbers EXACTLY as they are
3. Preserve the exact structure of the text
4. Keep the same number of paragraphs and line breaks
5. Return ONLY the translated text, nothing else

TEXT TO TRANSLATE:
{text}

IMPORTANT:
- Translate every Hebrew word
- Do NOT add or remove any line breaks
- Keep English technical terms unchanged
- Make sure the Arabic text is natural and correct"""

    response = client.chat.completions.create(
        model=MODEL,
        messages=[{"role": "user", "content": prompt}],
        temperature=0.1,
    )

    translated = response.choices[0].message.content.strip()
    return translated


def save_text_file(file_path: str, text: str):
    """Save translated text to file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(text)


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate_txt.py <input.txt>")
        print("Output: <input>_ar.txt")
        sys.exit(1)
    
    if not API_KEY:
        print("Error: OPENAI_API_KEY is not set.")
        print("Run: export OPENAI_API_KEY='sk-...'")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: file '{input_file}' not found.")
        sys.exit(1)
    
    print(f"Loading text from: {input_file.name}")
    text = load_text_file(str(input_file))
    
    print(f"Translating to Arabic...")
    
    client = OpenAI(api_key=API_KEY)
    translated_text = translate_text(client, text)
    
    # Generate output filename
    output_file = input_file.parent / f"{input_file.stem}_ar.txt"
    
    print(f"Saving translation to: {output_file.name}")
    save_text_file(str(output_file), translated_text)
    
    print(f"✓ Done!")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")


if __name__ == "__main__":
    main()
