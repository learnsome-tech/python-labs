# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

outFile = open('sample2.txt', 'w')
outFile.write('My second output file!')
#   22
outFile.write('Write some more.')
#   16
outFile.close()
print(open('sample2.txt').read())
#   My second output file!Write some more.
