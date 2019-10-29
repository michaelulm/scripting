#!/bin/bash

DIR=file-structure/$(date +%Y)
mkdir -p $DIR

for((i=1;i<=12;i++))
do
  if [ $i -lt 10 ] 
  then
	mkdir $DIR/0$i
  else
	mkdir $DIR/$i
  fi
done
