#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math

jlt = "ㄱ|ㄲ|ㄴ|ㄷ|ㄸ|ㄹ|ㅁ|ㅂ|ㅃ|ㅅ|ㅆ|ㅇ|ㅈ|ㅉ|ㅊ|ㅋ|ㅌ|ㅍ|ㅎ".split("|")
jtt = "|ㄱ|ㄲ|ㄱㅅ|ㄴ|ㄴㅈ|ㄴㅎ|ㄷ|ㄹ|ㄹㄱ|ㄹㅁ|ㄹㅂ|ㄹㅅ|ㄹㅌ|ㄹㅍ|ㄹㅎ|ㅁ|ㅂ|ㅂㅅ|ㅅ|ㅆ|ㅇ|ㅈ|ㅊ|ㅋ|ㅌ|ㅍ|ㅎ".split("|")
jvt = "ㅏ|ㅐ|ㅑ|ㅒ|ㅓ|ㅔ|ㅕ|ㅖ|ㅗ|ㅘ|ㅙ|ㅚ|ㅛ|ㅜ|ㅝ|ㅞ|ㅟ|ㅠ|ㅡ|ㅢ|ㅣ".split("|")
utf_base = 0xAC00
total = 11172
t = 28
n = 588

def decompose_sentance(sent):
	pass

def decompose_word(word, discard_non_korean=False):
	'''
	'''
	utf8_word = word.decode("utf-8")
	vals = []
	for c in utf8_word:
		index = ord(c) - utf_base
		if index < 0 or index >= total:
			if not discard_non_korean: 
				vals.append(c)
		else:
			l_index = int(math.floor(index / n))
  			v_index = int(math.floor((index % n) / t))
  			t_index = int(index % t)
  			if jlt[l_index] is not "": vals.append(jlt[l_index])
  			if jvt[v_index] is not "": vals.append(jvt[v_index])
  			if jtt[t_index] is not "": vals.append(jtt[t_index])
  	return vals