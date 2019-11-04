#!/usr/bin/env python3

filename_original = "countries.txt"
delimiter = "|"
field_nr = 1

# prefix for new lists
list_prefix = "country"

# prepare lists
for letter in range(97, (97+26)):
  filename = "{}_{}.txt".format(list_prefix, str(chr(letter)))
  print(filename)
  f = open(filename, "w")
  f.close()

# read all lines
f = open(filename_original, "r")

for x in f:
  datafield = x.split(delimiter)[field_nr]
  print(datafield)
  first_letter = datafield[0].lower()
  f = open("{}_{}.txt".format(list_prefix, first_letter), "a")
  f.write(datafield)
  f.close()
