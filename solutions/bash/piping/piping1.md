# Piping Exercises Part 1

Exercises based on Manfred Pamsl, Linux I

[country.txt](../../../exercises/bash/piping/country.txt)

## Display just the name and the first language of the countries.
```console
$ cut -d"," -f1,9 country.txt
```

## Display the name and the capital of the countries, sort by the capital.
```console
$ cut -d"," -f1,3 country.txt | sort -t"," -k2
```

## Display the top 5 countries (name) with their population, sort by the population of their capital. Display just the top 5
```console
$ sort -t"," -k4 -nr country.txt | cut -d"," -f-2 | head -5
```

## Display all Latin American countries (name) and their first language, reverse sort by the country
```console
$ grep "Latin America" country.txt | cut -d"," -f1,9 | sort -t"," -k1 -r
```

## Optional with REGEX
### Display all European countries (name,population) that have a greater population than 10 million.
```console
$ grep Europe country.txt |  cut -d"," -f-2 | egrep ",[1-9][0-9]{7,}$"
```
```console
$ egrep "^[^,]*,[1-9][0-9]{7,},.*Europe" country.txt | cut -d"," -f-2
```