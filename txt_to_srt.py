#!/usr/bin/env python3
"""
txt_to_srt.py
--------------
Reconstructs SRT file from original and translated text.
Matches translated text back to original SRT structure.

Usage:
    python3 txt_to_srt.py original.srt translated.txt
    
Output:
    original_ar.srt (SRT with translated text)
"""

import sys
from pathlib import Path


def parse_srt_file(file_path: str) -> list:
    """Parse SRT file and extract all components."""
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        content = f.read()
    
    # Normalize line endings
    content = content.replace('\r\n', '\n').replace('\r', '\n')
    
    # Split by double newlines
    blocks = content.split('\n\n')
    
    subtitles = []
    for block in blocks:
        if not block.strip():
            continue
        
        lines = block.strip().split('\n')
        if len(lines) < 3:
            continue
        
        try:
            index = int(lines[0])
            timecode = lines[1]
            
            subtitles.append({
                'index': index,
                'timecode': timecode,
                'text': None  # Will be filled with translated text
            })
        except (ValueError, IndexError):
            continue
    
    return subtitles


def load_translated_text(file_path: str) -> list:
    """Load translated text file."""
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Split by double newlines (matching the structure from srt_to_txt)
    text_blocks = content.split('\n\n')
    
    # Remove empty blocks
    text_blocks = [block.strip() for block in text_blocks if block.strip()]
    
    return text_blocks


def save_srt_file(file_path: str, subtitles: list):
    """Save reconstructed SRT file."""
    output_lines = []
    
    for sub in subtitles:
        output_lines.append(str(sub['index']))
        output_lines.append(sub['timecode'])
        output_lines.append(sub['text'])
        output_lines.append('')  # Empty line between subtitles
    
    content = '\n'.join(output_lines)
    
    # Write with UTF-8 BOM and CRLF line endings (matching original SRT format)
    with open(file_path, 'w', encoding='utf-8-sig', newline='') as f:
        content = content.replace('\n', '\r\n')
        f.write(content)


def main():
    if len(sys.argv) < 3:
        print("Usage: python3 txt_to_srt.py <original.srt> <translated.txt>")
        print("Output: <original>_ar.srt")
        sys.exit(1)
    
    original_srt = Path(sys.argv[1])
    translated_txt = Path(sys.argv[2])
    
    if not original_srt.exists():
        print(f"Error: file '{original_srt}' not found.")
        sys.exit(1)
    
    if not translated_txt.exists():
        print(f"Error: file '{translated_txt}' not found.")
        sys.exit(1)
    
    print(f"Loading original SRT: {original_srt.name}")
    subtitles = parse_srt_file(str(original_srt))
    
    print(f"Loading translated text: {translated_txt.name}")
    translated_texts = load_translated_text(str(translated_txt))
    
    if len(subtitles) != len(translated_texts):
        print(f"Warning: Subtitle count mismatch!")
        print(f"  Original: {len(subtitles)} subtitles")
        print(f"  Translated: {len(translated_texts)} blocks")
        print(f"  Using minimum: {min(len(subtitles), len(translated_texts))}")
    
    # Match translated text to subtitles
    for i, sub in enumerate(subtitles):
        if i < len(translated_texts):
            sub['text'] = translated_texts[i]
        else:
            sub['text'] = ""  # Empty if translation is missing
    
    # Generate output filename
    output_file = original_srt.parent / f"{original_srt.stem}_ar.srt"
    
    print(f"Saving reconstructed SRT: {output_file.name}")
    save_srt_file(str(output_file), subtitles)
    
    print(f"✓ Done!")
    print(f"  Original SRT: {original_srt}")
    print(f"  Translated:   {translated_txt}")
    print(f"  Output:       {output_file}")


if __name__ == "__main__":
    main()
