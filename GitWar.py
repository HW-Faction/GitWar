import time
import os
from tqdm import tqdm
import sys
import subprocess


def progressbar(it, prefix="", size=60, file=sys.stdout):
    count = len(it)

    def show(j):
        x = int(size*j/count)
        file.write("%s[%s%s] %i/%i\r" %
                   (prefix, "#"*x, "."*(size-x), j, count))
        file.flush()
    show(0)
    for i, item in enumerate(it):
        yield item
        show(i+1)
    file.write("\n")
    file.flush()


with open('./Source1.py', 'r') as source1:
    with open('Source2.py', 'a') as source2:
        linelist = source1.readlines()
        countOfLines = len(linelist)
        for i in range(1):
            print('saving line ', i)
            source2.write('' + linelist[i])
            print('committing to github...')
            os.system("git commit -m 'v4.0' .")
            for i in progressbar(range(15), "Computing: ", 40):
                time.sleep(0.1)
            print('pushing to master...')

            for i in tqdm(range(int(9e6))):
                pass
            os.system('git push origin master')
            for i in progressbar(range(15), "Computing: ", 40):
                time.sleep(0.1)
            for i in tqdm(range(int(9e6))):
                pass
            print('\n' + '#'*20 + ' ---DONE--- ' + '#'*20)
