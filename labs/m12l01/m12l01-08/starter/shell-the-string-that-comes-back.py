# Shell session from the video, as a file you can run.
# Each line below was typed at the >>> prompt; the commented lines are
# what Python answered. Run it with:  python3 -i thisfile.py

outFile = open('sample3.txt', 'w')
outFile.write('A revised output file!\n')
#   23
outFile.write('Write some more.\n')
#   17
outFile.close()
inFile = open('sample3.txt', 'r')
contents = inFile.read()
contents
#   'A revised output file!\nWrite some more.\n'
print(contents)
#   A revised output file!
#   Write some more.
