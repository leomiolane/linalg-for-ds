#!/bin/bash
lecture_path(){
	if [ $1 -lt 10 ]; then
		echo lectures/lecture_0$1/lecture_0$1.pdf
	else
		echo lectures/lecture_$1/lecture_$1.pdf
	fi
}
if [ -f "notes.zip" ]; then
	rm notes.zip
fi

let "i = 1"
myzip="zip -j notes.zip outline.pdf"
while [ -f `lecture_path $i` ]; do
	lpath=`lecture_path $i`
	myzip="$myzip $lpath"
	let "i=i+1"
done

echo `$myzip`
