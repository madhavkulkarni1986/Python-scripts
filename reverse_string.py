'''----------------------------------------
Script to reverse a string.
This script takes exactly one argument, the string to be reversed.
Usage:
	reverse_string.py <STRING>
	
	Example: 
	python3 reverse_string "Sample string"
	Output: gnirts elpmaS

----------------------------------------'''

import sys

def usage():
	print("Usage:",sys.argv[0],"<string>")

def reverse_str(string):
	slen = len(string) - 1
	rev_str=[]
	while slen >=0:
	    rev_str.append(string[slen])
	    slen=slen-1
	return rev_str

if(len(sys.argv) == 2):
    string=sys.argv[1]
    rev=reverse_str(string)
    print(''.join(rev))
else:
    print("Wrong number of arguments passed")
    usage()
