import csv

#Function 1 of Part 2
def read_csv_header(csv_r):
  header = next(csv_r)
  return header

#Function 2 of Part 2
def read_data(csv_r,keys):
  list1 = []
  for line in csv_r:
    dict1 = {}
    for i in range(0,len(keys)):
      dict1[keys[i]] = line[i]
    list1.append(dict1)
  return list1

#Function 3 of Part 2
def write_csv_header(csv_w,dict1):
  list1 = []
  keys = dict1.keys() 
  csv_w.writerow(keys)
  for i in keys:
    list1.append(i)
  return list1

#Function 4 of Part 2
def write_dictionaries_to_csv(csv_w,data,keys):
  list1 = []
  for i in data: 
    for j in range(0,len(keys)):
      list1.append(i.get(keys[j]))
    csv_w.writerow(list1)
    list1.clear()

import json
import urllib.request

#Function 1 of Part 3
def get_data(url):
  response = urllib.request.urlopen(url)  
  content = response.read().decode()  
  results = json.loads(content)  
  return results

#Function 2 of Part 3
def minimize_dictionaries(list1,keys):
  list2 = []
  for i in list1:
    dict1 = {}
    for j in keys:
      if(j in keys):
        dict1[j] = i.get(j) 
    list2.append(dict1)
  return list2

#Function 3 of Part 3
def write_cache(list1,name):
  list2 = []
  list3 = []
  duplicate = []
  with open(name,'w') as f:
    writer = csv.writer(f) 
    for i in list1:
      for j in i:
        list2.append(j)
    for i in list2:
      if(i not in duplicate):
        duplicate.append(i)
    writer.writerow(duplicate)
    for i in list1:
      for j in range(0,len(duplicate)):
        list3.append(i.get(duplicate[j]))
      writer.writerow(list3)
      list3.clear()

#Function 4 of Part 3
def read_cache(name):
 list1 = []
 keys = []
 with open(name,'r') as f:
   reader = csv.reader(f)  
   header = next(reader)
   for i in header:
     keys.append(i)
   for line in reader:
     dict1 = {}
     for i in range(0,len(keys)):
      dict1[keys[i]] = line[i]
     list1.append(dict1)
 return list1