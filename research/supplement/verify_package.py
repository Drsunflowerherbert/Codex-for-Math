#!/usr/bin/env python3
"""Check the sanitized public snapshot. Original archive receipts are historical."""
import subprocess,sys
from pathlib import Path
if __name__=='__main__':
    checker=Path(__file__).resolve().parents[2]/'publication/verify.py'
    raise SystemExit(subprocess.run([sys.executable,str(checker)]).returncode)
