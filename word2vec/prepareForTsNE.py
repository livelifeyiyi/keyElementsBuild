#!/usr/bin/env python

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals
import argparse

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

if __name__ == "__main__":
    parser = argparse.ArgumentParser()

    parser.add_argument('-e', action='store', dest='embedFile', required=True,
                        help='Path of embed results')

    parser.add_argument('-l', action='store', dest='outputLabel', required=True,
                        help='Path of output lable file')

    parser.add_argument('-x', action='store', dest='outputEmbedding',
                        required=True,
                        help='Path of output vector results for sample words')

    r = parser.parse_args()

    with open(r.embedFile, "r") as fInput:
        with open(r.outputLabel, "w") as fOutputLabel:
            with open(r.outputEmbedding, "w") as fOutputEmbed:
                lineCount, dimension = [int(x) for x in next(fInput).split()]

                wordDict = dict((k, v.strip()) for k, v in (l.split(' ', 1) for l in fInput))
                '''f = open('wordDict.txt', 'w')
                f.write(str(wordDict))'''
                for key in wordDict:
                    fOutputLabel.write("%s\n" % key)
                    fOutputEmbed.write("%s\n" % wordDict[key])
