#!/bin/bash
lflag=false
dflag=false
fflag=false
DIR="false"
FILE="false"
while getopts ":l:d:f:" opt; do
case $opt in
    l)
        echo "-l was triggered, Parameter: $OPTARG" >&2
        lflag=true;
        LANG=$OPTARG;;
    d)
        echo "-d was triggered, Parameter: $OPTARG" >&2
        dflag=true;
        end="*";
        DIR=$OPTARG;;

    f)
        echo "-f was triggered, Parameter: $OPTARG" >&2
        fflag=true;
        FILE=$OPTARG;;
    \?)
        echo "Invalid option: -$OPTARG" >&2
        exit 1;;
    :)
        echo "Option -$OPTARG requires an argument." >&2
        exit 1;;
esac
done


if ! $lflag
then
    echo "Please specify the target language using the -l flag" >&2
exit 1
fi

if ! [[ $dflag || $fflag ]]
then
    echo "Please include either a directory (-d) or a file (-f) to process" >&2
exit 1
fi

if [ "$LANG" == "ch" ];
then
    CHDIR=$DIR$end
    bash ./segment_ch.sh $CHDIR
fi

python label.py $LANG $DIR $FILE
