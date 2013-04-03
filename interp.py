#!/usr/bin/env python

def solve(s):
	n = 0
	plusVal = 1
	minusVal = -1
	for c in s:
		if c == '+':
			n += plusVal
		elif c == '-':
			n += minusVal
		elif c == 'x':
			plusVal, minusVal = minusVal, plusVal
	return n

if __name__ == "__main__":
	probStr = "--------------++++++++++-++++----++++++++----x---------------++++-+-+---+++++"
	print(solve(probStr))
