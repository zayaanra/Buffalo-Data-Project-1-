#Function 1 of Part 1
def get_matches(data,key,value):
  newList = []
  for i in data:
    if(i.get(key)==value):
      newList.append(i)
  return newList

#Function 2 of Part 1
def list_descriptions(data):
  list1 = []
  list2 = []
  for i in data:
    a = i.get('tow_description')
    list1.append(a)
  for i in list1:
    if i not in list2:
      list2.append(i)
  return list2 

#Function 3 of Part 1
def count_by_month(data):
  list1 = []
  list2 = [0,0,0,0,0,0,0,0,0,0,0,0]
  for i in data: 
    val = i.get("tow_date")
    month = int(val[5]+val[6])
    list1.append(month)
    list1.sort()
  for i in list1:
    list2[i-1] = list2[i-1] + 1
  return list2

#Function 4 of Part 1
def count_by_day(data):
  list1 = []
  list2 = []
  for i in range(1,32):
    list2.append(0)
  for i in data:
    val = i.get("tow_date")
    day = int(val[8]+val[9])
    list1.append(day)
    list1.sort
  for i in list1:
    list2[i-1] = list2[i-1] + 1
  return list2