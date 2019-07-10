import os
import re

def correct_ref(section):
    if '\\ref{' in section:
        return section + '}'
    else:
        return section

def title_item_tex(title):
    return item_tex('\\textsc{' + title + '}')

def item_tex(title):
    return '\\item ' + title + '\n'


N = 0
folder_exists = True

# Latex outline
outline_tex = open('outline_content.tex', 'w')
outline_tex.write('\\begin{enumerate}[label=\\textbf{\\arabic*.}]\n')

readme = open('README.md', 'w')
readme.write('# Optimization and Computational Linear Algebra for Data Science\n')
readme.write('\n')
readme.write('This repository contains some notes for the course, as well as the homeworks.\n')
readme.write('')
readme.write('**These materials are not meant to be proper lecture notes.**\n')
readme.write('They only contain the main results from the course. Examples, figures, and many proofs are missing.\n')

readme.write('\n')
readme.write('You can download all the notes [here](https://github.com/leomiolane/linalg-for-ds/raw/master/notes.zip) in *.zip* format.\n')
readme.write('\n')
readme.write('## Outline\n')

while (folder_exists):
    N += 1
    if N < 10:
        nb = '0' + str(N)
    else:
        nb = str(N)
    # folder name
    folder_name = 'lecture_' + nb
    # Check if lecture folder exists
    folder_exists = os.path.isdir(folder_name)
    if folder_exists:
        # Read Titlek
        tex_file = open(folder_name + '/' + folder_name + '.tex').read()
        # print tex_file.readline()
        search = 'Lecture ' + str(N) + ': ' + '(.*?)\}'
        title = re.findall(search, tex_file, re.S)

        search = r'\\section{(.*?)}'
        sections = re.findall(search, tex_file, re.S)
        url_github = 'https://github.com/leomiolane/linalg-for-ds/raw/master/'
        readme.write(str(N)+ '. [' + title[0] + '](' + url_github + folder_name + '/' + folder_name +'.pdf)' + '\n')
        outline_tex.write(title_item_tex(title[0]))
        outline_tex.write('\\vspace{-0.2cm}\n')
        outline_tex.write('\\begin{enumerate}[label=\\arabic*.,noitemsep]\n')

        for i in range(len(sections)):
            sections[i] = correct_ref(sections[i])
            outline_tex.write(item_tex(sections[i]))
        outline_tex.write('\\end{enumerate}\n')
         
        # print sections
        # print title

outline_tex.write('\\end{enumerate}\n')
print 'Done!'
