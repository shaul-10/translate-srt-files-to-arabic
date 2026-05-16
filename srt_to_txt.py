#!/usr/bin/env python3
"""
srt_to_txt.py
--------------
Extracts text from SRT file, preserving line structure.
Removes: index, timecode, and empty lines
Keeps: subtitle text content only

Usage:
    python3 srt_to_txt.py input.srt
    
Output:
    input.txt (subtitle text only, one subtitle per line)
"""

import sys
from pathlib import Path


def parse_srt_file(file_path: str) -> list:
    """Parse SRT file and extract subtitle texts."""
    with open(file_path, 'r', encoding='utf-8-sig', newline='') as f:
        content = f.read()
    
    # Normalize line endings
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
            # Skip index (lines[0]) and timecode (lines[1])
            # Keep text from lines[2] onwards
            text_lines = lines[2:]
            subtitle_text = '\n'.join(text_lines)
            
            subtitles.append(subtitle_text)
        except (ValueError, IndexError):
            continue
    
    return subtitles


def save_txt_file(file_path: str, subtitles: list):
    """Save extracted text to file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        for subtitle in subtitles:
            f.write(subtitle)
            f.write('\n\n')  # Double newline between subtitles for readability


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 srt_to_txt.py <input.srt>")
        print("Output: <input>.txt")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"Error: file '{input_file}' not found.")
        sys.exit(1)
    
    print(f"Extracting text from: {input_file.name}")
    subtitles = parse_srt_file(str(input_file))
    
    if not subtitles:
        print("Error: no subtitles found in file.")
        sys.exit(1)
    
    # Generate output filename
    output_file = input_file.parent / f"{input_file.stem}.txt"
    
    print(f"Found {len(subtitles)} subtitles")
    print(f"Saving text to: {output_file.name}")
    
    save_txt_file(str(output_file), subtitles)
    
    print(f"✓ Done!")
    print(f"  Input:  {input_file}")
    print(f"  Output: {output_file}")


if __name__ == "__main__":
    main()
