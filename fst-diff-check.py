#!/usr/bin/env python3
import sys
import csv

def usage():
  print("./fst-mapping.py <SNP-file> <q95LL> <q95UL> <q99LL> <q99UL> <q999LL> <q999UL>")

def loadFiles(flist):
  matrix = []
  data = {}
  for i, path in enumerate(flist):
    isBaseFile = i == 0
    key = ""
    if i == 0: key = "value"
    elif i == 1: key = "95LL"
    elif i == 2: key = "95UL"
    elif i == 3: key = "99LL"
    elif i == 4: key = "99UL"
    elif i == 5: key = "999LL"
    else: key = "999UL"
    
    with open(path, "r") as f:
      csvreader = csv.DictReader(f, delimiter=";")
      for j, row in enumerate(csvreader):
        if isBaseFile: 
          if j == 0: matrix.append([]) # prepare headers line
          matrix.append([])            # prepare content line
        siteR = row.get("")
        for siteC, val in row.items():
          if isBaseFile: 
            if j == 0: matrix[j].append(siteC)
            matrix[j+1].append(val)
          try:
            name = f'{siteR}<>{siteC}'
            valFloat = float(val)
            if data.get(name) is None:
              data[name] = {key: valFloat}
            else:
              data[name][key] = valFloat
          except ValueError as e: continue
            
  return matrix, data

def computeDiff(data) -> dict:
  for d in data.values():
    val = d.get("value")
    diffIndicator = "NA"
    if (val > d["95LL"] and val < d["95UL"]): diffIndicator = "ns"
    elif (val > d["99LL"] and val < d["99UL"]): diffIndicator = "*"
    elif (val > d["999LL"] and val < d["999UL"]): diffIndicator = "**"
    else: diffIndicator = "***"

    d["diffIndicator"] = diffIndicator
  return data

def print_matrix(m):
  for i in range(len(m)):
    line = ""
    line += "[[ " if i == 0 else " [ "
    for j, cell in enumerate(m[i]):
      line += f"{cell}"
      line += " " if j == len(m) - 1 else ", "
    line += "]]" if i == len(m) - 1 else "]"
    print(line)

def generate_csv(matrix, data):
  print_matrix(matrix)
  return None

def main(argv):
  if (len(argv) < 8):
    usage()
    exit(1)
  csvMatrix, extractedValues = loadFiles(argv[1:])
  computedDiff = computeDiff(extractedValues)
  # print values in the console
  # for sites, d in computedDiff.items():
  #   print(sites, d["diffIndicator"])
  generate_csv(csvMatrix, computedDiff)

main(sys.argv)