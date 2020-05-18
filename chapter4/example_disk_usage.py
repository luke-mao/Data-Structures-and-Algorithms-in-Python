# calculate the disk usage, given the path

import os

def disk_usage(path):
    total = os.path.getsize(path) # get the size of current path
    
    if os.path.isdir(path):         # if current path is a directory
        for filename in os.listdir(path):
            childpath = os.path.join(path, filename)
            total += disk_usage(childpath)
    
    print('{0:<7}'.format(total), path)
    return total


if __name__ == '__main__':
    # probably only works on the linux, not windows
    disk_usage("/usr/rt/courses")