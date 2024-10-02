from transformers import MBartForConditionalGeneration, MBart50TokenizerFast

model = MBartForConditionalGeneration.from_pretrained(
    "facebook/mbart-large-50-many-to-many-mmt"
)
tokenizer = MBart50TokenizerFast.from_pretrained(
    "facebook/mbart-large-50-many-to-many-mmt"
)


lang_dict = {
    "ar": "ar_AR",  # Arabic
    "cs": "cs_CZ",  # Czech
    "de": "de_DE",  # German
    "en": "en_XX",  # English
    "es": "es_XX",  # Spanish
    "et": "et_EE",  # Estonian
    "fi": "fi_FI",  # Finnish
    "fr": "fr_XX",  # French
    "gu": "gu_IN",  # Gujarati
    "hi": "hi_IN",  # Hindi
    "it": "it_IT",  # Italian
    "ja": "ja_XX",  # Japanese
    "kk": "kk_KZ",  # Kazakh
    "ko": "ko_KR",  # Korean
    "lt": "lt_LT",  # Lithuanian
    "lv": "lv_LV",  # Latvian
    "my": "my_MM",  # Burmese
    "ne": "ne_NP",  # Nepali
    "nl": "nl_XX",  # Dutch
    "ro": "ro_RO",  # Romanian
    "ru": "ru_RU",  # Russian
    "si": "si_LK",  # Sinhala
    "tr": "tr_TR",  # Turkish
    "vi": "vi_VN",  # Vietnamese
    "zh": "zh_CN",  # Chinese
    "af": "af_ZA",  # Afrikaans
    "az": "az_AZ",  # Azerbaijani
    "bn": "bn_IN",  # Bengali
    "fa": "fa_IR",  # Persian
    "he": "he_IL",  # Hebrew
    "hr": "hr_HR",  # Croatian
    "id": "id_ID",  # Indonesian
    "ka": "ka_GE",  # Georgian
    "km": "km_KH",  # Khmer
    "mk": "mk_MK",  # Macedonian
    "ml": "ml_IN",  # Malayalam
    "mn": "mn_MN",  # Mongolian
    "mr": "mr_IN",  # Marathi
    "pl": "pl_PL",  # Polish
    "ps": "ps_AF",  # Pashto
    "pt": "pt_XX",  # Portuguese
    "sv": "sv_SE",  # Swedish
    "sw": "sw_KE",  # Swahili
    "ta": "ta_IN",  # Tamil
    "te": "te_IN",  # Telugu
    "th": "th_TH",  # Thai
    "tl": "tl_XX",  # Tagalog
    "uk": "uk_UA",  # Ukrainian
    "ur": "ur_PK",  # Urdu
    "xh": "xh_ZA",  # Xhosa
    "gl": "gl_ES",  # Galician
    "sl": "sl_SI",  # Slovene
}


def translate(text, src_lang_code="en", trg_lang_code="hi"):
    src_lang = lang_dict[src_lang_code]
    trg_lang = lang_dict[trg_lang_code]
    tokenizer.src_lang = src_lang
    encoded = tokenizer(text, return_tensors="pt")
    generated_tokens = model.generate(
        **encoded, forced_bos_token_id=tokenizer.lang_code_to_id[trg_lang]
    )
    return tokenizer.batch_decode(generated_tokens, skip_special_tokens=True)
