"""PDF text extraction plus a quick quality check.

Government PDFs often extract badly: letters come out reversed (visual
order) or as "presentation forms" (U+FB50..U+FEFF) instead of normal
Arabic letters. Run `check_quality` on a sample before trusting a file.
"""
from dataclasses import dataclass
import re

ARABIC = re.compile(r"[؀-ۿ]")
PRESENTATION_FORMS = re.compile(r"[ﭐ-﷿ﹰ-﻿]")
# Very common words; if their reversed spelling shows up more often,
# the PDF probably stores text in visual (reversed) order.
COMMON = ["في", "من", "على", "إلى", "التي", "الذي", "المنشآت"]


@dataclass
class PageText:
    doc: str
    page: int  # 1-based, matches what people cite
    text: str


def extract_pages(pdf_path: str) -> list[PageText]:
    import fitz  # PyMuPDF; imported here so the rest works without it

    with fitz.open(pdf_path) as pdf:
        return [
            PageText(doc=pdf_path, page=i + 1, text=page.get_text("text"))
            for i, page in enumerate(pdf)
        ]


def check_quality(text: str) -> dict:
    """Return simple signals; a human still looks at the sample."""
    chars = [c for c in text if not c.isspace()]
    n = len(chars) or 1
    words = text.split()
    forward = sum(words.count(w) for w in COMMON)
    reversed_ = sum(words.count(w[::-1]) for w in COMMON)
    return {
        "arabic_ratio": round(sum(bool(ARABIC.match(c)) for c in chars) / n, 3),
        "presentation_form_ratio": round(len(PRESENTATION_FORMS.findall(text)) / n, 3),
        "common_words_forward": forward,
        "common_words_reversed": reversed_,
        "looks_reversed": reversed_ > forward,
        "likely_scanned": len(chars) < 50,  # almost no text layer -> needs OCR
    }
