#!/usr/bin/env python3
"""Compile a LaTeX file to PDF using available tools.
Tries multiple approaches in order:
1. pdflatex (system)
2. tectonic (system)  
3. Python reportlab (fallback, basic)

Usage: python3 compile_latex.py <input.tex> <output.pdf>
"""
import os, sys, subprocess, shutil

def find_tool(*names):
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None

def compile_pdflatex(tex_file, output_dir):
    pdflatex = find_tool("pdflatex", "xelatex", "lualatex")
    if not pdflatex:
        return False
    try:
        result = subprocess.run(
            [pdflatex, "-output-directory", output_dir, "-interaction=nonstopmode", tex_file],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode == 0:
            return True
        print(f"pdflatex failed (exit {result.returncode}):")
        print(result.stderr[-500:] if result.stderr else "no stderr")
        return False
    except (subprocess.TimeoutExpired, OSError) as e:
        print(f"pdflatex error: {e}")
        return False

def compile_tectonic(tex_file, output_dir):
    tectonic = shutil.which("tectonic")
    if not tectonic:
        return False
    try:
        result = subprocess.run(
            [tectonic, "--outdir", output_dir, tex_file],
            capture_output=True, text=True, timeout=120
        )
        return result.returncode == 0
    except (subprocess.TimeoutExpired, OSError):
        return False

def main():
    if len(sys.argv) < 3:
        print("Usage: compile_latex.py <input.tex> <output.pdf>")
        sys.exit(1)

    tex_file = os.path.abspath(sys.argv[1])
    output_pdf = os.path.abspath(sys.argv[2])
    output_dir = os.path.dirname(output_pdf)
    base_name = os.path.splitext(os.path.basename(tex_file))[0]

    if not os.path.exists(tex_file):
        print(f"ERROR: {tex_file} not found")
        sys.exit(1)

    os.makedirs(output_dir, exist_ok=True)

    print(f"Compiling {tex_file}...")

    # Try pdflatex first
    if compile_pdflatex(tex_file, output_dir):
        generated = os.path.join(output_dir, f"{base_name}.pdf")
        if os.path.exists(generated):
            os.rename(generated, output_pdf)
            print(f"SUCCESS: {output_pdf}")
            sys.exit(0)

    # Try tectonic
    if compile_tectonic(tex_file, output_dir):
        generated = os.path.join(output_dir, f"{base_name}.pdf")
        if os.path.exists(generated):
            os.rename(generated, output_pdf)
            print(f"SUCCESS: {output_pdf}")
            sys.exit(0)

    print("ERROR: No TeX compiler available. Install texlive-latex-base or tectonic.")
    sys.exit(1)

if __name__ == "__main__":
    main()
