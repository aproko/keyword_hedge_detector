#!bin/bash

DIR="/Users/aproko/Desktop/Chinese_Data/chinese/LDC2015E78_DEFT_Rich_ERE_Chinese_and_English_Parallel_Annotation_V1/data/cmn/source/*.cmp.txt"

for f in $DIR;
do
    /Users/aproko/Downloads/stanford-segmenter-2015-12-09/segment.sh ctb $f UTF-8 0 >> $f.seg.txt
done


