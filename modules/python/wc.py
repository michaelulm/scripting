#!/usr/bin/env python3

filename = "demo.txt"

# read all lines
f = open(filename, "r")

# init variables
counter_lines = 0
counter_chars = 0
counter_words = 0

# iterate through file -> line by line
for line in f:
#  print(x)
  counter_lines += 1
  # iterate each character of each line
  #for c in line:
  #  counter_chars = counter_chars + 1
  
  # just use len of current line -> more efficient
  counter_chars += len(line)

  # split current line and iterare through each words
  #for w in line.split(" "):
  #  counter_words = counter_words + 1
  counter_words += len(line.split(" "))

# extended output like bash command wc
print("Lines: {}".format(counter_lines))
print("Words: {}".format(counter_words))
print("Chars: {}".format(counter_chars))

# same output like wc
print("{} {} {} {}".format(counter_lines, counter_words, counter_chars, filename))

# don't forget to close file
f.close()
