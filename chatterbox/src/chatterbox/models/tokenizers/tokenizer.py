import logging

import torch
from tokenizers import Tokenizer


# Special tokens
SOT = "[START]"
EOT = "[STOP]"
UNK = "[UNK]"
SPACE = "[SPACE]"
SPECIAL_TOKENS = [SOT, EOT, UNK, SPACE, "[PAD]", "[SEP]", "[CLS]", "[MASK]"]

logger = logging.getLogger(__name__)

class EnTokenizer:
    def __init__(self, vocab_file_path):
        self.tokenizer: Tokenizer = Tokenizer.from_file(vocab_file_path)
        self.check_vocabset_sot_eot()

    def check_vocabset_sot_eot(self):
        voc = self.tokenizer.get_vocab()
        assert SOT in voc
        assert EOT in voc

    def text_to_tokens(self, text: str, language_id: str = None):
        text_tokens = self.encode(text, language_id=language_id)
        text_tokens = torch.IntTensor(text_tokens).unsqueeze(0)
        return text_tokens

    def encode(self, txt: str, language_id: str = None, verbose=False):
        """
        clean_text > (append `lang_id`) > replace SPACE > encode text using Tokenizer
        """
        txt = txt.replace(' ', SPACE)
        code = self.tokenizer.encode(txt)
        ids = code.ids
        return ids

    def decode(self, seq):
        if isinstance(seq, torch.Tensor):
            seq = seq.cpu().numpy()

        txt: str = self.tokenizer.decode(seq,
        skip_special_tokens=False)
        txt = txt.replace(' ', '')
        txt = txt.replace(SPACE, ' ')
        txt = txt.replace(EOT, '')
        txt = txt.replace(UNK, '')
        return txt


class MultilingualTokenizer(EnTokenizer):
    """
    Multilingual tokenizer that prepends language ID tokens to text.
    Supports common language codes used in multilingual TTS.
    """
    
    # Language ID to token mapping
    LANG_TOKENS = {
        "en": "[EN]",
        "de": "[DE]",
        "fr": "[FR]",
        "es": "[ES]",
        "it": "[IT]",
        "pt": "[PT]",
        "pl": "[PL]",
        "tr": "[TR]",
        "ru": "[RU]",
        "nl": "[NL]",
        "cs": "[CS]",
        "ar": "[AR]",
        "zh": "[ZH]",
        "ja": "[JA]",
        "hu": "[HU]",
        "ko": "[KO]",
        "hi": "[HI]",
    }
    
    def __init__(self, vocab_file_path):
        super().__init__(vocab_file_path)
        self.check_language_tokens()
    
    def check_language_tokens(self):
        """Check if language tokens exist in vocabulary"""
        voc = self.tokenizer.get_vocab()
        available_langs = []
        for lang_code, lang_token in self.LANG_TOKENS.items():
            if lang_token in voc:
                available_langs.append(lang_code)
        
        if available_langs:
            logger.info(f"Multilingual tokenizer initialized. Available languages: {', '.join(available_langs)}")
        else:
            logger.warning("No language tokens found in vocabulary. Multilingual support may not work.")
    
    def encode(self, txt: str, language_id: str = None, verbose=False):
        """
        Encode text with optional language ID prepended.
        
        Args:
            txt: Input text to encode
            language_id: Language code (e.g., 'en', 'de', 'fr')
            verbose: Enable verbose logging
        
        Returns:
            List of token IDs
        """
        # Prepend language token if specified
        if language_id is not None:
            lang_token = self.LANG_TOKENS.get(language_id.lower())
            if lang_token:
                # Add language token at the beginning
                txt = lang_token + txt
                if verbose:
                    logger.info(f"Prepended language token: {lang_token}")
            else:
                logger.warning(f"Language '{language_id}' not supported. Available: {list(self.LANG_TOKENS.keys())}")
        
        # Replace spaces and encode
        txt = txt.replace(' ', SPACE)
        code = self.tokenizer.encode(txt)
        ids = code.ids
        return ids
