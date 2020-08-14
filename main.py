import bottle
import json
import cache
import backend

#Route 1
@bottle.route("/")
def index():
  f = bottle.static_file("index.html",root='.')
  return f

#Route 2
@bottle.route("/script.js")
def script():
  f = bottle.static_file("script.js",root='.')
  return f

#Route 3
@bottle.route("/towsByDay")
def scatter():
  data = cache.read_cache('cached_data.csv')
  content = backend.count_by_day(data) 
  response = json.dumps(content)
  return response

#Route 4
@bottle.route("/towsByDistrict")
def pie():
  length = []
  data = cache.read_cache('cached_data.csv')
  distA = backend.get_matches(data,'police_district','District A')
  distB = backend.get_matches(data,'police_district','District B')
  distC = backend.get_matches(data,'police_district','District C')
  distD = backend.get_matches(data,'police_district','District D')
  distE = backend.get_matches(data,'police_district','District E')
  length.append(len(distA))
  length.append(len(distB))
  length.append(len(distC))
  length.append(len(distD))
  length.append(len(distE))
  response = json.dumps(length) 
  return response

#Route 5
@bottle.route("/towsByDescription")
def line():
  data = cache.read_cache('cached_data.csv')
  list1 = []
  a = backend.count_by_month(backend.get_matches(data,'tow_description','ILLEGAL VEHICLE'))
  list1.append(a)
  b = backend.count_by_month(backend.get_matches(data,'tow_description','ACCIDENT'))
  list1.append(b)
  c = backend.count_by_month(backend.get_matches(data,'tow_description','ABANDONED VEHICLE'))
  list1.append(c)
  d = backend.count_by_month(backend.get_matches(data,'tow_description','STOLEN VEHICLE'))
  list1.append(d)
  e = backend.count_by_month(backend.get_matches(data,'tow_description','ILLEGALLY PARKED'))
  list1.append(e)
  f = backend.count_by_month(backend.get_matches(data,'tow_description','IMPOUNDED'))
  list1.append(f)
  g = backend.count_by_month(backend.get_matches(data,'tow_description','GONE ON ARRIVAL'))
  list1.append(g)
  response = json.dumps(list1)
  return response  

import os.path
def load_data():
  csv_file = 'cached_data.csv'
  if not os.path.isfile(csv_file):
    query_str = "?$limit=10000"
    url = "https://data.buffalony.gov/resource/5c88-nfii.json" + query_str
    data = cache.get_data(url)
    data = cache.minimize_dictionaries(data, ['tow_date', 'tow_description', 'police_district'])
    cache.write_cache(data, csv_file)


load_data()
bottle.run(host="0.0.0.0",port=8080,debug=True)