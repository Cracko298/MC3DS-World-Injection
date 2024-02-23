import os
from mc3dslib import BlangFile
from sys import argv

def to_JSON(file,out):
    blangFile = BlangFile().open(file)
    blangFile.toJson(out)

def to_BLANG(file,out):
    blangFile = BlangFile().fromJson(file)
    blangFile.export(out)

file_path = argv[1]
mode = argv[2]
file_path = file_path.replace('"','')
out_path = f"{os.path.dirname(file_path)}\\out"
os.makedirs(f"{out_path}",exist_ok=True)

if mode == "1":
    to_JSON(file_path,out_path)
else:
    to_BLANG(file_path,out_path)
