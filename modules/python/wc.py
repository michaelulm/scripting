#!/usr/bin/env python3

# read all lines
f = open("demo.txt", "r")

# init variables
counter_lines = 0
counter_chars = 0
counter_words = 0

# iterate through file -> line by line
for x in f:
#  print(x)
  counter_lines = counter_lines + 1
  # iterate each character of each line
  for y in x:
    counter_chars = counter_chars + 1

  # split current line and iterare through each words
  for z in x.split(" "):
    counter_words = counter_words + 1

# final output like bash command wc
print("Lines: {}".format(counter_lines))
print("Chars: {}".format(counter_chars))
print("Words: {}".format(counter_words))

# don't forget to close file
f.close()
