#!/bin/bash
folder=./

for file in `ls $folder`; do
    file1=$file.tab
    sed 's/\t/    /g' $file > $file1
    mv $file1 $file
done
exit
