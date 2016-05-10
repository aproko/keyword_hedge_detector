The label.py script tags hedge words in Spanish and Chinese. Two types of hedges are recognized - relational (tagged with <HREL>) and propositional (tagged with <HPROP>). The former has to do with the speaker (or the subject's) relation to what is being said (eg. words like 'think', 'maybe', 'guess', etc); the latter has to do with imprecision in the content of the sentence itself (eg. words like 'sort of', 'approximately', 'some', etc).

The input should be in plain text format, with one sentence per line. The output will be the same sentences in the same order, with the hedge words surrounded by tags, with the same filename and the extension '.anno.txt'.

Eg. I think John was a little tired after his exams.
    I <HREL>think</HREL> John was <HPROP>a little</HPROP> tired after his exams.

The script takes the following flags:

-l: specify the language of the files you wish to label (ch for Chinese or sp for Spanish). REQUIRED.
-d: specify the path to a folder in which all the files you wish to label are located.
-f: specify the path to a single file that you wish to label.

An example command is the following:
    python label.py -l sp -f /path/to/my/file.txt
    
The files containing the dictionaries of hedge words in Spanish and Chinese are located in spanish_hedges.csv and chinese_hedges.csv. DO NOT open these in Microsoft Word, as it messes up the encoding and will create errors with regard to special accented characters. Always open as a plain text file.