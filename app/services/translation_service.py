from typing import Dict
from app.models.translation_model import translate


def translate_text(
    text: str, source_language: str, target_language: str
) -> Dict[str, str]:
    translated_text = translate(
        text, src_lang_code=source_language, trg_lang_code=target_language
    )
    return {source_language: text, target_language: translated_text}
