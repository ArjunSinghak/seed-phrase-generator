from mnemonic import Mnemonic

def validate_seed_phrase(phrase: str, language: str = "english") -> bool:
    """Check if a BIP39 seed phrase is valid."""
    mnemo = Mnemonic(language)
    return mnemo.check(phrase)