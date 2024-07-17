# This script formats the branch files in-place

import re
import os

COORD_2_REGEX = re.compile(r"(\[\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\])")
COORD_3_REGEX = re.compile(r"(\[\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*,\s*-?\d+(\.\d+)?\s*\])")

def format_all():
    for project in os.listdir("routes"):
        project_path = os.path.join("routes", project)
        if os.path.isdir(project_path):
            format_project(project_path)

def format_project(path):
    if os.path.isdir(path):
        format_dir(path)

def format_dir(path):
    for subpath in os.listdir(path):
        subpath = os.path.join(path, subpath)
        if os.path.isdir(subpath):
            format_dir(subpath)
        elif os.path.isfile(subpath) and subpath.endswith(".yaml"):
            format_file(subpath)

def format_file(path):
    formatted = False
    output = []
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            formatted_line = format_line(line)
            if formatted_line != line:
                formatted = True
            output.append(formatted_line)
    
    if formatted:
        with open(path, "w", encoding="utf-8") as f:
            f.writelines(output)
        print(path)

def format_line(line):
    match2 = COORD_2_REGEX.findall(line)
    if match2:
        for match in match2:
            coord_str = match[0]
            formatted_coord = format_coord(coord_str)
            line = line.replace(coord_str, formatted_coord)

    match3 = COORD_3_REGEX.findall(line)
    if match3:
        for match in match3:
            coord_str = match[0]
            formatted_coord = format_coord(coord_str)
            line = line.replace(coord_str, formatted_coord)
    
    return line

def format_coord(coord_str):
    coords = [ round(float(x.strip()), 2) for x in coord_str[1:-1].split(",") ]
    return"[" + ", ".join([str(x) for x in coords]) + "]"

if __name__ == "__main__":
    format_all()