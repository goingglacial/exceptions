import os.path
import sys

while True: 
    try:
        filename = raw_input("Please enter a valid filename. \n< ")
        count = 0
        with open(filename, 'r') as f:
            for line in f:
                count += 1
        print "There are",count, "lines in your file."
        break
    except IOError:
        print "Apologies! There was an error with your file."
        sys.exit()




