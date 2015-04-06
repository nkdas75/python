'''
this is a google code jam problem.
Given a list of space separated words, reverse the order of the words.
Each line of text contains L letters and W words. A line will only
consist of letters and space characters. There will be exactly one
space character between each pair of consecutive words.
Input file is something like this -
5 # this indicates number of lines in the file to process
this is a test
foobar
all your base
class
pony along
'''

def readandreverse(file):
    with open(file) as f:
        firstline = f.readline()
        num = int(firstline)
        for line in range(num) :
            oneline = f.readline()
            listofwords=oneline.rsplit()
            listofwords.reverse()
            print(" ".join(listofwords))
        f.close()

readandreverse("B-small-practice.in")
