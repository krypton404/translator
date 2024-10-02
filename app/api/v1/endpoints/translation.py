from fastapi import APIRouter
from pydantic import BaseModel
from app.services.translation_service import translate_text

router = APIRouter()


class TranslationRequest(BaseModel):
    text: str
    source_language: str
    target_language: str


class TranslationResponse(BaseModel):
    translated_text: str


@router.post("/", response_model=TranslationResponse)
def translate(request: TranslationRequest):
    translated_text = translate_text(
        request.text, request.source_language, request.target_language
    )
    return TranslationResponse(translated_text=translated_text)
