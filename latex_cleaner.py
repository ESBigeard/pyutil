#!/usr/bin/python
# -*- coding:utf-8 -*-
""" deletes temporary files generated by pdflatex in the folder this script is launched from"""

import os

for fname in os.listdir(os.getcwd()):
	if fname[-4:] in [".aux",".log",".blg",".bbl",".toc",".lof",".lot",".out"]:
		os.remove(fname)
