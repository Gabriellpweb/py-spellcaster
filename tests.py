# -*- coding: utf-8 -*-
import unittest
from spellcaster import SpellCaster


class TestSpellCheck(unittest.TestCase):

    def test_suggest(self):
        term = 'soa paulo test'
        result = 'São Paulo test'
        spell_caster = SpellCaster('pt_br')
        payload = spell_caster.cast_suggest_spell(term)
        self.assertEquals(payload['replacement'], result)


if __name__ == "__main__":
    unittest.main()
