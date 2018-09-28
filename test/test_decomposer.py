#!/usr/bin/env python
# -*- coding: utf-8 -*-

from decomposer import *
import unittest

class TestDecomposer(unittest.TestCase):

    def test_word_decompose(self):
    	decomp = decompose_word("한국어")
        self.assertEqual(decomp, ["ㅎ", "ㅏ", "ㄴ", "ㄱ", "ㅜ", "ㄱ", "ㅇ", "ㅓ"])

    def test_word_decompose_def_rem(self):
    	decomp = decompose_word("한국a어")
        self.assertEqual(decomp, ["ㅎ", "ㅏ", "ㄴ", "ㄱ", "ㅜ", "ㄱ", "a", "ㅇ", "ㅓ"])

    def test_word_decompose_rem(self):
    	decomp = decompose_word("한국a어", discard_non_korean=True)
        self.assertEqual(decomp, ["ㅎ", "ㅏ", "ㄴ", "ㄱ", "ㅜ", "ㄱ", "ㅇ", "ㅓ"])

   	def test_sentence_decompose(self):
   		pass

   	def test_sentence_decompose_def_rem(self):
   		pass

   	def test_sentence_decompose_rem(self):
   		pass

if __name__ == '__main__':
    unittest.main()