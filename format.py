# -*- coding: utf-8 -*-

s="""
问题一：答案是这些
问题二：答案是这些

问题三：答案是这些
问题四：第一点：答案。第二点：答案
"""

enter_flag = False

for i in s:
	if i == "\n" and not enter_flag:
		enter_flag = True
		not_print = True
	if i != "\n" and enter_flag and not_print:
		not_print = False	
		print("**", end="")	
	print(i, end="")	
	if i == "：" and enter_flag:
		enter_flag = False
		print("**", end="")			