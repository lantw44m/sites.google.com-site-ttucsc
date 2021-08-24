#!/usr/bin/env python
# -*- encoding: utf-8 -*-

import sys

def BMI(height, weight):
	return ( weight / ( height / 100.0) ** 2)

if len(sys.argv) != 3:
	pass
else:
	print sys.argv
	print sys.argv[1:]
	print map(int, sys.argv[1:])
	print BMI(*map(int, sys.argv[1:]))


