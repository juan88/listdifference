# -*- coding: utf-8 -*-
#!/usr/bin/python

import unittest
import os
from listdifference import *

from sys import argv, exit


class ListDifferenceTest(unittest.TestCase):
    
    def testLoadLists(self):
        """ Open the list files and load the contents of them as lists """
        ld = ListDifference("testdirs/01/in01.txt", "testdirs/01/diff01.txt", "testdirs/01/out01.txt")
        ld.inputList.sort()
        ld.differenceList.sort()
        self.assertEqual(ld.inputList, ["goodbye", "hello", "joe", "john", "karl"])
        self.assertEqual(ld.differenceList, ["john","mike"])


    def testLoadListsWithoutRepetitions(self):
        """ Open the list files and load the contents of them as lists but without repetitions """
        ld = ListDifference("testdirs/01/in02.txt", "testdirs/01/diff02.txt", "testdirs/01/out02.txt")
        ld.inputList.sort()
        ld.differenceList.sort()
        self.assertEqual(ld.inputList, ["goodbye", "hello", "joe", "john", "karl"])
        self.assertEqual(ld.differenceList, ["john","mike"])    

    def fileList(self):
        currentPath = Path(self.input)
        l = [pathitem.name for pathitem in currentPath.iterdir() if not(pathitem.is_dir())]
        return l

    def testDiffList1(self):
        """ Compute the difference between the two lists """
        ld = ListDifference("testdirs/01/in01.txt", "testdirs/01/diff01.txt", "testdirs/01/out01.txt")
        diff = ld.difference(ld.inputList, ld.differenceList)
        diff.sort()
        self.assertEqual(diff, ["goodbye", "hello", "joe", "karl"])

    def testDiffList2(self):
        """ Compute the difference between the two lists (test2) """
        ld = ListDifference("testdirs/01/in02.txt", "testdirs/01/diff02.txt", "testdirs/01/out02.txt")
        diff = ld.difference(ld.inputList, ld.differenceList)
        diff.sort()
        self.assertEqual(diff, ["goodbye", "hello", "joe", "karl"])

    def testDiffList3(self):
        """ Compute the difference between the two lists (test3) """
        ld = ListDifference("testdirs/01/in02.txt", "testdirs/01/diff02.txt", "testdirs/01/out02.txt")
        l0 = ([0]*50000)
        l1 = ([1]*50000)
        l01 = l0 + l1

        self.assertEqual(len(l0)+len(l1), len(l01))
        self.assertEqual(50000, len(ld.difference(l01, l1)))
        self.assertEqual(50000, len(ld.difference(l01, l0)))
        self.assertEqual(0, len(ld.difference(l01, l01)))

    def testGenerateDifferenceToFile(self):
        """ Open the list files and load the contents of them as lists """
        output = "testdirs/01/out01.txt"
        ld = ListDifference("testdirs/01/in01.txt", "testdirs/01/diff01.txt", output)
        ld.generateDifference()

        expected = ["goodbye", "hello", "joe", "karl"]        
        result = ld.loadFileContentsToList(output)
        result.sort()

        self.assertEqual(expected, result)

    def testGenerateDifferenceToFile2(self):
        """ Open the list files and load the contents of them as lists (test2) """
        output = "testdirs/01/out02.txt"
        ld = ListDifference("testdirs/01/in02.txt", "testdirs/01/diff02.txt", output)
        ld.generateDifference()

        expected = ["goodbye", "hello", "joe", "karl"]
        result = ld.loadFileContentsToList(output)
        result.sort()

        self.assertEqual(expected, result)

    def readFile(self, ruta):
        if not os.path.exists(ruta):
            sys.exit("El archivo '%s' no existe." % ruta)
        elif not os.path.isfile(ruta):
            sys.exit("El archivo '%s' es invalido." % ruta)

        archivo = open(ruta, "r")
        return archivo.read()



def main():
    unittest.main()

if __name__ == '__main__':
    main()