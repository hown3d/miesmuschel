from logging import log, warning
from typing import Optional

import lingua
from lingua import Language, LanguageDetectorBuilder

LINGUA_LANGS = [Language.ENGLISH, Language.FRENCH, Language.GERMAN, Language.SPANISH]


def detect_language(text: str) -> Optional[lingua.Language]:
    detector = LanguageDetectorBuilder.from_languages(*LINGUA_LANGS).with_preloaded_language_models().build()
    lang = detector.detect_language_of(text)
    if lang is None:
        warning("could not detect language for text")
    # gtts expect IETF language tag in lower case
    return lang
