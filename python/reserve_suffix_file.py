# coding=utf-8
import os

root_folder = './'
suffix_name = '.h'

def DeleteSuffixFile(folder):
    for item in os.listdir(folder):
        if os.path.isdir(os.path.join(folder, item)):
            DeleteSuffixFile(os.path.join(folder, item))
        elif item.endswith(suffix_name):
            print('reserved file: ' + os.path.join(folder, item))
        else:
            os.remove(os.path.join(folder, item))
            
def DeleteEmptyDir(folder):
    if os.path.isdir(folder):
        for item in os.listdir(folder):
            DeleteEmptyDir(os.path.join(folder, item))
        if not os.listdir(folder):
            os.rmdir(folder)
            print("delete empty dir: " + folder)

def main():
    DeleteSuffixFile(os.path.abspath(root_folder))
    DeleteEmptyDir(os.path.abspath(root_folder))

if __name__ == '__main__':
    main()