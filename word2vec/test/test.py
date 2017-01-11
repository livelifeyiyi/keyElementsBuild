import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-s', action='store', dest='sampleFile', required=True,
                        help='Path of sample file to visualize by t-SNE')

    r = parser.parse_args()

    wordCount = {}  # Counter() is not availabe in Python 2.6.6

    with open(r.sampleFile, "r") as wordFile:
        for line in wordFile:
            for w in line.split():
                wordCount[w] = wordCount.get(w, 0) + 1
    f = open('wordCount.txt', 'w')
    f.write(str(wordCount))
    #print wordCount