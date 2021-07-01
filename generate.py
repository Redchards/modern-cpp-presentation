import os
import sys

os.system(f"pandoc -t revealjs -V revealjs-url=./ --slide-level={sys.argv[1]} -s presentation.md -o index.html")