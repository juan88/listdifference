# -*- coding: utf-8 -*-
#!/usr/bin/python
#

import os
import argparse
from pathlib import Path

class ListDifference(object):

    def __init__(self, inputFile, differenceFile, outputFile):
        self.inputList = self.loadFileContentsToList(inputFile)
        self.output = outputFile
        self.differenceList = self.loadFileContentsToList(differenceFile)

    def loadFileContentsToList(self, filename):
        with open(filename) as f:
            return list(set(f.read().splitlines()))


    def difference(self, input, difference):
        return [item for item in input if item not in difference]

    def generateDifference(self):
        diff = self.difference(self.inputList, self.differenceList)
        file = open(self.output, 'w')
        for item in diff:
            file.write("%s\n" % item)
        file.close()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("inputList", help="The input file with items to be filtered")
    parser.add_argument("differenceList", help="The list of values that are to be excluded from the first list")
    parser.add_argument("outputList", help="The filename where to save the difference between the two lists")
    args = parser.parse_args()
    print(args.inputList)
    print(args.differenceList)
    print(args.outputList)

    ld = ListDifference(args.inputList, args.differenceList, args.outputList)
    ld.generateDifference()


if __name__ == "__main__":
    # execute only if run as a script
    main()