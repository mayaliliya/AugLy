#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.

from augly.text.composition import Compose, OneOf

from augly.text.functional import (
    apply_lambda,
    get_baseline,
    insert_punctuation_chars,
    insert_whitespace_chars,
    insert_zero_width_chars,
    replace_bidirectional,
    replace_fun_fonts,
    replace_similar_chars,
    replace_similar_unicode_chars,
    replace_upside_down,
    simulate_typos,
    split_words,
)

from augly.text.intensity import (
    apply_lambda_intensity,
    get_baseline_intensity,
    insert_punctuation_chars_intensity,
    insert_whitespace_chars_intensity,
    insert_zero_width_chars_intensity,
    replace_bidirectional_intensity,
    replace_fun_fonts_intensity,
    replace_similar_chars_intensity,
    replace_similar_unicode_chars_intensity,
    replace_upside_down_intensity,
    simulate_typos_intensity,
    split_words_intensity,
)

from augly.text.transforms import (
    ApplyLambda,
    GetBaseline,
    InsertPunctuationChars,
    InsertWhitespaceChars,
    InsertZeroWidthChars,
    ReplaceBidirectional,
    ReplaceFunFonts,
    ReplaceSimilarChars,
    ReplaceSimilarUnicodeChars,
    ReplaceUpsideDown,
    SimulateTypos,
    SplitWords,
)

__all__ = [
    "Compose",
    "OneOf",
    "ApplyLambda",
    "GetBaseline",
    "InsertPunctuationChars",
    "InsertWhitespaceChars",
    "InsertZeroWidthChars",
    "ReplaceBidirectional",
    "ReplaceFunFonts",
    "ReplaceSimilarChars",
    "ReplaceSimilarUnicodeChars",
    "ReplaceUpsideDown",
    "SimulateTypos",
    "SplitWords",
    "apply_lambda",
    "get_baseline",
    "insert_punctuation_chars",
    "insert_whitespace_chars",
    "insert_zero_width_chars",
    "replace_bidirectional",
    "replace_fun_fonts",
    "replace_similar_chars",
    "replace_similar_unicode_chars",
    "replace_upside_down",
    "simulate_typos",
    "split_words",
    "apply_lambda_intensity",
    "get_baseline_intensity",
    "insert_punctuation_chars_intensity",
    "insert_whitespace_chars_intensity",
    "insert_zero_width_chars_intensity",
    "replace_bidirectional_intensity",
    "replace_fun_fonts_intensity",
    "replace_similar_chars_intensity",
    "replace_similar_unicode_chars_intensity",
    "replace_upside_down_intensity",
    "simulate_typos_intensity",
    "split_words_intensity",
]
