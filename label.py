# -*- coding: utf-8 -*-

import csv
import sys
import os
from os import listdir
from os.path import isfile, join
import argparse
from bs4 import BeautifulSoup

hedge_dictionary = {}


def processFile(filename):
    soup = BeautifulSoup(open(filename))
    paragraph = soup.get_text()
    print paragraph.encode('utf-8').decode('utf-8','ignore')
    sentences = paragraph.split("\n")
        #with open(filename, 'rU') as input_file:
    count = {'HREL':0,'HPROP':0}
    wordcount = 0
    print filename, ",",
    lines = []
    print wordcount
    for line in sentences:
        if len(line) > 1:
        #for line in input_file:
            dash = u"\u4E00"
            line = line.replace(dash, "")
            line = line.replace("\,", "")
            line = line.replace("<", "")
            line = line.replace(">", "")
            line = line.replace("\"\"", "")
            line = line.replace("\"", "")
            line = line.replace("=", "")
            line = line.replace(".", "")
            line = line.replace("!", "")
            line = line.replace("?" ,"")
            dot = u"\u3002"
            line = line.replace(dot, "")
            print line
            line = line.trim()
            wds = line.split()
            wordcount += len(wds)
            for hedge in hedge_dictionary:
                print hedge
                print line
                if unicode(hedge) in line:
                    line = line.replace(hedge, "<"+hedge_dictionary[hedge]+">"+hedge+"</"+hedge_dictionary[hedge]+">")
                    count[hedge_dictionary[hedge]] += 1
            lines.append(line)

        print count['HREL'], ",", count['HPROP'],",", count['HREL'] + count['HPROP'], ",", wordcount, ",", float(count['HREL'] + count['HPROP'])/float(wordcount)

    with open(filename + ".anno.txt", 'w') as out_file:
        for item in lines:
            out_file.write(item)


def readInDictionary(filename):
    with open(filename, 'rU') as input_file:
        reader = csv.reader(input_file)
        next(reader, None)
        
        for line1 in reader:
            hedge_dictionary[line1[0]] = line1[3]
    


def main():
    #parser = argparse.ArgumentParser(description='Label hedges in file(s).')
    #parser.add_argument('-l', '--lang', help='Input language: ch for Chinese or sp for Spanish.')
    #parser.add_argument('-d', '--folder', help='Label all files in a folder.')
    #parser.add_argument('-f', '--file', help='Label a single file.')
    #args = parser.parse_args()
    lang = sys.argv[1]
    dir = sys.argv[2]
    fil = sys.argv[3]
    #if args.lang == "sp":
    if lang == "sp":
        readInDictionary('spanish_hedges.csv')
    elif lang == "ch":
        readInDictionary('chinese_hedges.csv')
    else:
        print "Error: Please specify the language of the files you wish to label - ch for Chinese or sp for Spanish."
    
    print dir
    if "false" not in dir:
#if args.folder:
        if os.path.exists(dir):
            print "Labeling all files in: ", dir
            onlyfiles = [ f for f in listdir(dir) if (isfile(join(dir,f)) and "anno" not in f and ".DS_Store" not in f) ]
                #and ".cmp.txt.seg.txt" in f) ]
            print "Filename,hRel,hProp,Total,Total Words,% Hedges"
            for file in onlyfiles:
                #print "Labeling file: ", join(args.folder, file)
                processFile(join(dir, file))

        else:
            print "Please enter a valid folder path."
    
    elif fil is not "false":
        if os.path.exists(fil):
                print "Labeling file: ", fil
                processFile(fil)
        else:
            print "Please enter a valid file path."

    else:
        print "Error: Please specify EITHER a valid folder path or a valid file path."



if __name__ == "__main__":
    main()

