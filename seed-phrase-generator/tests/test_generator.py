import unittest
from src.generator import generate_seed_phrase, SeedPhraseGenerator
from src.validator import validate_seed_phrase

class TestSeedPhraseGenerator(unittest.TestCase):

    def test_generate_default(self):
        phrase = generate_seed_phrase()
        self.assertEqual(len(phrase.split()), 12)
        self.assertTrue(validate_seed_phrase(phrase))

    def test_generate_256(self):
        phrase = generate_seed_phrase(strength=256)
        self.assertEqual(len(phrase.split()), 24)
        self.assertTrue(validate_seed_phrase(phrase))

    def test_invalid_strength(self):
        with self.assertRaises(ValueError):
            generate_seed_phrase(strength=100)

    def test_generator_class(self):
        gen = SeedPhraseGenerator("english")
        phrase = gen.generate(128)
        self.assertTrue(validate_seed_phrase(phrase))

if __name__ == "__main__":
    unittest.main()