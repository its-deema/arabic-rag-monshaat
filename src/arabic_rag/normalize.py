"""Light Arabic normalization.

Deliberately small: each step is a flag, so "raw vs normalized" can be
measured as an experiment instead of assumed to help.
"""
import re

# Harakat + Quranic marks (U+064B..U+065F, U+0670) — short vowels, shadda, sukun.
DIACRITICS = re.compile(r"[ً-ٰٟ]")
TATWEEL = "ـ"  # ـ  the stretching character, purely visual
ALEF_VARIANTS = re.compile(r"[آأإٱ]")  # آ أ إ ٱ -> ا
# Arabic-Indic digits ٠١٢٣٤٥٦٧٨٩ -> 0-9 so "المادة ٥" matches "المادة 5"
ARABIC_DIGITS = str.maketrans("٠١٢٣٤٥٦٧٨٩", "0123456789")


def normalize(
    text: str,
    *,
    diacritics: bool = True,
    tatweel: bool = True,
    alef: bool = True,
    digits: bool = True,
    teh_marbuta: bool = False,  # ة -> ه : off by default, it can change meaning
    alef_maqsura: bool = False,  # ى -> ي : off by default, same reason
) -> str:
    if diacritics:
        text = DIACRITICS.sub("", text)
    if tatweel:
        text = text.replace(TATWEEL, "")
    if alef:
        text = ALEF_VARIANTS.sub("ا", text)
    if digits:
        text = text.translate(ARABIC_DIGITS)
    if teh_marbuta:
        text = text.replace("ة", "ه")
    if alef_maqsura:
        text = text.replace("ى", "ي")
    return re.sub(r"\s+", " ", text).strip()
