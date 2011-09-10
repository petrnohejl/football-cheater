#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Football cheater version 1.0

Copyright (C)2008 Petr Nohejl, jestrab.net

This program is free software; you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, write to the Free Software
Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.

This program comes with ABSOLUTELY NO WARRANTY!
"""

### IMPORT #####################################################################

import sys		# argv
import os		# prace s adresari a soubory
import string	# prace s retezci



### KONSTANTY ##################################################################

CONST_DICT_DIR = "dict"			# adresar se slovnikama
CONST_SHOW_UNFILTERED = False	# vypis nalezenych slov bez osetreni opakovatelnosti pismenek
CONST_SHOW_FILTERED = True		# vypis nalezenych slov s osetrenim opakovatelnosti pismenek



### ERRORS A HELP ##############################################################

def ErrorArg():
	print "Error: Incorrect arguments!\nTo show help, run program with parameter -h."
	return
	
def ErrorDict():
	print "Error: Cannot load dictionary!"
	return
	
def Help():
	print "Football cheater version 1.0"
	print ""
	print "Copyright (c)2008 Petr Nohejl, jestrab.net"
	print ""
	print "Program search all corresponding words, which contain chars from input."
	print "Words are got from wordlists saved in directory /" + CONST_DICT_DIR + "."
	print "Optional switch -s sort found words from longest to shortest."
	print ""
	print "Usage: football [-s] chars"
	print "       football -h"
	return
	
	
	
### SORT #######################################################################

def Sort(list):
	result = []
	cur = 0
	max = 0
	
	# zjisteni maxima
	for x in range(len(list)):
		cur = len(list[x])
		if(cur > max):
			max = cur
		
	# pruchod jednotlivymi delkami slova
	for x in range(max, 0, -1):
		# pruchod seznamem
		for y in range(len(list)):
			if(len(list[y]) == x):
				result.append(list[y])
		
	return result



### FOOTBALL ###################################################################

def Football():
	
	# parametr: football -h
	if(len(sys.argv) == 2 and sys.argv[1] == "-h"):
		Help()
		
	
	
	# parametry: football "chars", football -s "chars"
	elif((len(sys.argv) == 2 and sys.argv[1] != "-s") or (len(sys.argv) == 3 and sys.argv[1] == "-s")):
		
		arg = sys.argv[-1]	# vstupni pismenka
		result = []			# vysledny seznam slov
		resultFiltered = []	# vysledny odfiltrovany seznam slov
		
		# nacteni slovniku
		try:
			os.chdir(CONST_DICT_DIR)
			dicts = os.listdir(os.curdir)
		except:
			ErrorDict()
			return
		
		# zobrazeni vypisu unfiltered
		if(CONST_SHOW_UNFILTERED == True):
			print "------------------------------------"
			print "|         UNFILTERED WORDS         |"
			print "------------------------------------"
		
		# pruchod slovniky
		for y in range(len(dicts)):
		
			# otevreni slovniku
			try:
				if(not os.path.isdir(dicts[y])):
					file = open(dicts[y], "r")
			except:
				ErrorDict()
				continue
				
			# pruchod slovnikem
			while(1):
				line = file.readline()	# nacteni radku
				
				# ukoncovaci podminka
				if(line == ""):
					break
					
				line = string.strip(line)	# odstraneni bilych znaku
				state = True
				chars = arg
			
				# pruchod slovem ve slovniku
				for x in range(len(line)):
					if(line[x] not in chars):
						state = False
						
				# slovo ze slovniku lze utvorit z danych pismenek
				if(state == True):
					# zobrazeni vypisu unfiltered
					if(CONST_SHOW_UNFILTERED == True):
						print line
						
					result.append(line)	# pridani slova do seznamu
			
			file.close	# uzavreni slovniku
		
		
		
		# zobrazeni vyslednych odfiltrovanych slov
		if(CONST_SHOW_FILTERED == True):
			print "------------------------------------"
			print "|          FILTERED WORDS          |"
			print "------------------------------------"
		
			# pruchod nalezenymi slovy a osetreni neopakovatelnosti vstupnich pismenek	
			for x in range(len(result)):
			
				line = result[x]
				state = True
				chars = arg
			
				# pruchod slovem ve slovniku
				for x in range(len(line)):
					if(line[x] not in chars):
						state = False
					
					# osetreni neopakovatelnosti vstupnich pismenek	
					index = string.find(chars, line[x])
					chars = chars[:index] + chars[index+1:]
						
				# slovo ze slovniku lze utvorit z danych pismenek
				if(state == True):
					# osetreni neopakovatelnosti slov
					if(line not in resultFiltered):
						resultFiltered.append(line)
		
			# serazeni seznamu od nejdelsich slov
			if(len(sys.argv) == 3 and sys.argv[1] == "-s"):
				resultFiltered = Sort(resultFiltered)
		
			# vypis odfiltrovanych slov
			for x in range(len(resultFiltered)):
				print resultFiltered[x]
		
		return
		
		
		
	# neplatne parametry
	else:
		ErrorArg()
		return
		
	return
	


### MAIN #######################################################################

if (__name__=="__main__"):
	Football()
