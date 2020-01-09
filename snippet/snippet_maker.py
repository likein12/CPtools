# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 16:43:00 2019

@author: likein12
"""

"""
listfile format

FILENAME_INDEX = 0
PREFIX_INDEX = 1
DESCRIPTION_INDEX = 2
"""

def create_snippet(file):
    filename, prefix, description = file
    try:
        code =["\t\t\t" + '"' + line[:-1] + '"' + "\n" for line in open(filename, "r")]
    except:
        print("something wrong with "+filename)
        return None
    code = ["\t\t\t"] + code + ["\n"]
    code = ",\n\t\t\t".join(code)
    snippet = "\t" + '"' + filename + '"' + " : {\n" \
    + "\t\t" + '"' + "prefix" + '"' + " : " + '"' + prefix + '"' + "\n\n" \
    + "\t\t" + '"' + "body" + '"' + " : [\n" + code + "\t\t" + "]" + "\n\n" \
    + "\t\t" + '"' + "description" + '"' + " : " + '"' + description + '"' + "\n\n" \
    + "\t" + "}"
    return snippet


list_file = "list_file.txt"

files = [line[:-1].split(",") for line in open(list_file, "r")]

snippet_list = [create_snippet(file) for file in files]

snippet = "{\n\n" + "\n\n".join(snippet_list) + "\n\n}"
with open("snippet.txt", "w") as f:
    f.write(snippet)

