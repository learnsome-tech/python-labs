import argparse
import os
import subprocess
import sys

parser = argparse.ArgumentParser(prog='shout')
parser.add_argument('word')
parser.add_argument('--times', type=int, default=1)
args = parser.parse_args(['hi', '--times', '3'])
print(args.word * args.times)

child = subprocess.run([sys.executable, '-c', 'print(1 + 1)'],
                       capture_output=True, text=True)
print(child.returncode, child.stdout.strip())

print(os.path.basename('/home/ada/notes.txt'))
print(sys.version_info.major)
