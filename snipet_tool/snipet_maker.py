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

def create_snipet(file):
    filename, prefix, description = file
    try:
        code =["\t\t\t" + '"' + line[:-1] + '"' + "\n" for line in open(filename, "r")]
    except:
        print("something wrong with "+filename)
        return None
    code = ["\t\t\t"] + code + ["\n"]
    code = ",\n\t\t\t".join(code)
    snipet = "\t" + '"' + filename + '"' + " : {\n" \
    + "\t\t" + '"' + "prefix" + '"' + " : " + '"' + prefix + '"' + "\n\n" \
    + "\t\t" + '"' + "body" + '"' + " : [\n" + code + "\t\t" + "]" + "\n\n" \
    + "\t\t" + '"' + "description" + '"' + " : " + '"' + description + '"' + "\n\n" \
    + "\t" + "}"
    return snipet


list_file = input()

files = [line[:-1].split(",") for line in open(list_file, "r")]

snipet_list = [create_snipet(file) for file in files]

snipet = "{\n\n" + "\n\n".join(snipet_list) + "\n\n}"
