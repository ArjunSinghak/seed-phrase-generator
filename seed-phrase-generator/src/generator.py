import secrets
from mnemonic import Mnemonic

class SeedPhraseGenerator:
    """Generates BIP39 seed phrases with configurable strength."""

    def __init__(self, language: str = "english"):
        self.mnemo = Mnemonic(language)

    def generate(self, strength: int = 128) -> str:
        """Generate a seed phrase. strength must be multiple of 32 (128-256)."""
        if strength % 32 != 0 or strength < 128 or strength > 256:
            raise ValueError("Strength must be 128, 160, 192, 224, or 256")
        entropy = secrets.token_bytes(strength // 8)
        return self.mnemo.to_mnemonic(entropy)

def generate_seed_phrase(strength: int = 128, language: str = "english") -> str:
    """Convenience function to generate a seed phrase."""
    generator = SeedPhraseGenerator(language)
    return generator.generate(strength)