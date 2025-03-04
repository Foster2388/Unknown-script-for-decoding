import os
import urllib.request
from urllib import request
from collections import OrderedDict


remote_url1 = 'https://raw.githubusercontent.com/ngosang/trackerslist/master/trackers_all.txt'
remote_url2 = 'https://cf.trackerslist.com/all.txt'


file1 = 'NEW_TRACKERS1.txt'
file2 = 'NEW_TRACKERS2.txt'

request.urlretrieve(remote_url1, file1)

opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'MyApp/1.0')]
urllib.request.install_opener(opener)
urllib.request.urlretrieve(remote_url2, file2)



def appendData(file1Path, file2Path, file3Path):

    with open(file1Path, 'r') as file1:
        lines1 = list(line.strip() for line in file1)

    with open(file2Path, 'r') as file2:
        lines2 = list(line.strip() for line in file2)
        
    with open(file3Path, 'r') as file3:
        lines3 = list(line.strip() for line in file3)

    res = list(OrderedDict.fromkeys(lines1 + lines2 + lines3))

    with open(file3Path, 'w') as resultFile:
        resultFile.write('\n'.join(res))

# replace with your file paths
file1Path = 'NEW_TRACKERS1.txt'
file2Path = 'NEW_TRACKERS2.txt'
file3Path = 'TRACKERS.txt'

appendData(file1Path, file2Path, file3Path)

  

with open('TRACKERS.txt') as f:
    seen = set()  # keep track of the lines already seen
    deduped = []
    for line in f:
        line = line.rstrip()
        if line not in seen:  # if not seen already, write the lines to result
            deduped.append(line)
        seen.add(line)

with open('TRACKERS.txt', 'w') as f:
    f.writelines([l + '\n' for l in deduped])

os.remove(file1Path)
os.remove(file2Path)
