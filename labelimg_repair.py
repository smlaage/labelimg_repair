#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
labelimg_repair.py

This simple scripts applies to the labelImg package.
See: https://github.com/HumanSignal/labelImg

Once the package is installed on your local machine, the script repairs the type error
that occurs with the most recently published version of labelImg. The script requires write access
to the files 'canvas.py' and 'labelImg.py'. It scans through the files and converts the arguments
for drawLine(), drawRect() and setValue() calls to int data types. That's all.

SLW 2024-04
"""

import sys
import os


def cover_by_int(s):
    repair = False
    s = s.strip(' ')
    if s[0] not in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
        if len(s) >= 4 and s[:4] != "int(":
            s = "int(" + s + ")"
            repair = True
    return repair, s
    

def repair_line(l):
    keys = ('drawLine', 'drawRect', 'setValue')
    repair = False

    # Remove comment if there is any
    pos = l.find('#')
    if pos > 0:
        l = l[:pos] + '\n'

    # Find keyword
    pos = 0
    for key in keys:
        pos = l.find(key)
        if pos > 0:
            break
    if pos < 0:
        return False, l

    # Analyze statement
    first_bracket_pos = l.find('(')
    if first_bracket_pos < 0:
        print(" - syntax error: " + l)
        return False, l
    new_line = l[:first_bracket_pos] + '('
    last_bracket_pos = l[first_bracket_pos :].rfind(')')
    if last_bracket_pos < 0:
        print(" - syntax error: " + l)
        return False, l

    # Create list of arguments
    arguments = l[first_bracket_pos + 1 : last_bracket_pos + first_bracket_pos].split(',')
    repair_cnt = 0
    for idx, a in enumerate(arguments):
        repair, arguments[idx] = cover_by_int(a)
        if repair:
            repair_cnt += 1

    # Reconstructing line
    if repair_cnt <= 0:
        return False, l
    for a in arguments:
        new_line += a + ", "
    new_line = new_line.rstrip(' ')    
    new_line = new_line.rstrip(',')
    new_line += ") # repaired by labelimg_repair.py"
    return True, new_line
    
# main program starts here ======================================================

print()
print("labelimg_repair.py")
print("Script to repair the labelimg application")
print("SLW 04-2024")
print()

if len(sys.argv) > 1:
    labelimg_dir = sys.argv[1]
else:
    print("Enter path to labelImg package")
    print("E.g. C:\\Users\\xyz\\AppData\\Local\\Programs\\Thonny\\Lib\\site-packages")
    labelimg_dir = input("-> ")
    if len(labelimg_dir) < 2:
        sys.exit("Nothing to do!")

if not os.path.isdir(labelimg_dir):
    sys.exit("Invalid directory '" + labelimg_dir + "'")
else:
    print("Directory found")

labelimg_dir = labelimg_dir.strip(' ')
labelimg_dir = labelimg_dir.strip('\\')
if labelimg_dir[-5:] == '\\libs':
    labelimg_dir = labelimg_dir[:-4]
if labelimg_dir[-9:] == '\\labelImg':
    labelimg_dir = labelimg_dir[:-9]
if labelimg_dir[-9:] == '\\labelimg':
    labelimg_dir = labelimg_dir[:-9]

print("Repairing canvas.py ...")
canvas_filename = os.path.join(labelimg_dir, 'libs', 'canvas.py')
if not os.path.isfile(canvas_filename):
    sys.exit("Can't find file '" + canvas_filename + "'")
try:
    with open(canvas_filename, "r") as f:
        lines = f.readlines()
except IOError:
    sys.exit("Can't open file '" + canvas_filename + "'")
print(" - " + str(len(lines)) + " read")
repair_cnt = 0
for idx, l in enumerate(lines):
    repair, new_line = repair_line(l)
    if repair:
        print(" - repairing line " + str(idx))
        repair_cnt += 1
        lines[idx] = new_line
if repair_cnt > 0:
    print(" - saving file")
    try:
        with open(canvas_filename, "w") as f:
            for l in lines:
                f.write(l)
    except IOError:
        sys.exit("Can't save file '" + canvas_filename + "'")
else:
    print(" - nothing to do")

print("Repairing labelimg.py ...")
labelimg_filename = os.path.join(labelimg_dir, 'labelImg', 'labelImg.py')
if not os.path.isfile(labelimg_filename):
    sys.exit("Can't find file '" + canvas_filename + "'")
try:
    with open(labelimg_filename, "r") as f:
        lines = f.readlines()
except IOError:
    sys.exit("Can't open file '" + labelimg_filename + "'")
print(" - " + str(len(lines)) + " read")
repair_cnt = 0
for idx, l in enumerate(lines):
    repair, new_line = repair_line(l)
    if repair:
        print(" - repairing line " + str(idx))
        repair_cnt += 1
        lines[idx] = new_line
if repair_cnt > 0:
    print(" - saving file")
    try:
        with open(labelimg_filename, "w") as f:
            for l in lines:
                f.write(l)
    except IOError:
        sys.exit("Can't save file '" + labelimg_filename + "'")
else:
    print(" - nothing to do")

print("Done")

