from arabic_rag.normalize import normalize
from arabic_rag.extract import check_quality


def test_alef_variants_unified():
    assert normalize("أنشطة إدارة آليات") == "انشطة ادارة اليات"


def test_diacritics_and_tatweel_removed():
    assert normalize("المُنْشَـــآت") == "المنشات"


def test_digits():
    assert normalize("المادة ١٢") == "المادة 12"


def test_meaning_changing_steps_off_by_default():
    assert normalize("مدرسة على") == "مدرسة على"
    assert normalize("مدرسة", teh_marbuta=True) == "مدرسه"


def test_reversed_text_detected():
    good = "يقدم البرنامج الدعم في مجال التمويل من الهيئة"
    bad = " ".join(w[::-1] for w in good.split())
    assert not check_quality(good)["looks_reversed"]
    assert check_quality(bad)["looks_reversed"]
