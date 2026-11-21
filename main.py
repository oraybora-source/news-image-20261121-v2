# news-image-20261121 final entry v2 (Python 3.13, standard library only).
#
# The image is entry.png in this repository, composed by render_v2.py
# from verified news strings (see STORIES.md). This program writes that
# image to the grader's output directory (/output, or MAKEFUN_OUTPUT_DIR
# locally). It runs twice in grading; both runs write the same bytes
# because the source file never changes.
import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

os.makedirs(OUT_DIR, exist_ok=True)
shutil.copyfile(os.path.join(HERE, "entry.png"),
                os.path.join(OUT_DIR, "entry.png"))
