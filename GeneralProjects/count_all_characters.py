# This programs executes on any .txt file
# then counts all the characters in the file
# (including spaces and tabs, excluding new
# lines) and prints out the resulting total
# number of characters
#
# Copyright 2019 Wei Liao
import sys

filename = sys.argv[1]
to_count = open(filename)
count = 0
for line in to_count:
	for character in line:
		if character != "\n":
			count += 1
to_count.close()
print("Total character count (including space/tab) is", count)
