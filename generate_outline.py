import os
import re


N = 0
look_for_next_lecture = True

while (look_for_next_lecture):
    N += 1
    if N < 10:
        nb = '0' + str(N)
    else:
        nb = str(N)
    # folder name
    folder_name = 'lecture_' + nb
    # Check if lecture folder exists
    folder_exists = os.path.isdir(folder_name)
    print folder_exists
    look_for_next_lecture = folder_exists

    # Read Titlek
    tex_file = open(folder_name + '/' + folder_name + '.tex').read()
    # print tex_file.readline()
    search = 'Lecture ' + str(N) + ': ' + '(.*?)\}'
    title = re.findall(search, tex_file, re.S)
    print title
print N
