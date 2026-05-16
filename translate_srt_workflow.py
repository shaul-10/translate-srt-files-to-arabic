#!/usr/bin/env python3
"""
translate_srt_workflow.py
-------------------------
Master script that orchestrates the complete SRT translation workflow:
1. Extracts text from SRT
2. Translates text using OpenAI
3. Reconstructs SRT with translated content

Usage:
    python3 translate_srt_workflow.py input.srt
    
Output:
    input_ar.srt (fully translated SRT file)

Requirements:
    pip install openai
    export OPENAI_API_KEY="sk-..."
"""

import sys
import subprocess
from pathlib import Path


def run_command(script: str, args: list) -> bool:
    """Run a Python script with arguments."""
    try:
        cmd = ['python3', script] + args
        print(f"\n▶ Running: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        print(result.stdout)
        if result.stderr:
            print(result.stderr)
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error running {script}:")
        print(e.stdout)
        print(e.stderr)
        return False
    except FileNotFoundError:
        print(f"✗ Error: {script} not found in current directory")
        return False


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 translate_srt_workflow.py <input.srt>")
        print("\nWorkflow:")
        print("  1. srt_to_txt.py     - Extract text from SRT")
        print("  2. translate_txt.py  - Translate to Arabic")
        print("  3. txt_to_srt.py     - Reconstruct SRT")
        sys.exit(1)
    
    input_file = Path(sys.argv[1])
    
    if not input_file.exists():
        print(f"✗ Error: file '{input_file}' not found.")
        sys.exit(1)
    
    print("=" * 60)
    print("SRT TRANSLATION WORKFLOW")
    print("=" * 60)
    print(f"Input: {input_file}")
    print(f"Output: {input_file.stem}_ar.srt")
    print("=" * 60)
    
    # Step 1: Extract text
    print("\n[1/3] Extracting text from SRT...")
    if not run_command('srt_to_txt.py', [str(input_file)]):
        print("✗ Failed to extract text")
        sys.exit(1)
    
    txt_file = input_file.parent / f"{input_file.stem}.txt"
    
    # Step 2: Translate text
    print("\n[2/3] Translating text to Arabic...")
    if not run_command('translate_txt.py', [str(txt_file)]):
        print("✗ Failed to translate text")
        sys.exit(1)
    
    txt_ar_file = input_file.parent / f"{input_file.stem}_ar.txt"
    
    # Step 3: Reconstruct SRT
    print("\n[3/3] Reconstructing SRT with translated text...")
    if not run_command('txt_to_srt.py', [str(input_file), str(txt_ar_file)]):
        print("✗ Failed to reconstruct SRT")
        sys.exit(1)
    
    # Final output
    output_file = input_file.parent / f"{input_file.stem}_ar.srt"
    
    print("\n" + "=" * 60)
    print("✓ WORKFLOW COMPLETED SUCCESSFULLY!")
    print("=" * 60)
    print(f"\nFinal output: {output_file}")
    print(f"Ready to use: {output_file.name}")
    print("\nTemporary files:")
    print(f"  - {txt_file.name} (can be deleted)")
    print(f"  - {txt_ar_file.name} (can be deleted)")


if __name__ == "__main__":
    main()
