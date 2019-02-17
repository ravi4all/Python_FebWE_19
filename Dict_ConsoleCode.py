Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> num = 45
>>> type(num)
<class 'int'>
>>> num = 45,
>>> type(num)
<class 'tuple'>
>>> num = 45,46,78,2,56
>>> num = (45,46,78,2,56)
>>> num[0]
45
>>> num[0] = 90
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    num[0] = 90
TypeError: 'tuple' object does not support item assignment
>>> data = {1:10}
>>> data
{1: 10}
>>> data[1]
10
>>> data = {"name":"Ram", "sal":25000, "dept":'IT'}
>>> data[0]
Traceback (most recent call last):
  File "<pyshell#12>", line 1, in <module>
    data[0]
KeyError: 0
>>> data["sal"]
25000
>>> data["company"] = "hcl"
>>> data
{'name': 'Ram', 'sal': 25000, 'dept': 'IT', 'company': 'hcl'}
>>> data["name"] = "Shyam"
>>> data
{'name': 'Shyam', 'sal': 25000, 'dept': 'IT', 'company': 'hcl'}
>>> data = {
    "names" : ['Sachin','Kohli','yuvraj','Dhoni','Rohit','Rahul'],
    "scores" : [78,100,56,45,80,41],
    "ranking" : [2,1,3,4,5,6]
}
>>> data["ranking"]
[2, 1, 3, 4, 5, 6]
>>> data["ranking"] < 4
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    data["ranking"] < 4
TypeError: '<' not supported between instances of 'list' and 'int'
>>> import pandas
>>> import pandas as pd
>>> pd.DataFrame(data)
    names  scores  ranking
0  Sachin      78        2
1   Kohli     100        1
2  yuvraj      56        3
3   Dhoni      45        4
4   Rohit      80        5
5   Rahul      41        6
>>> import pprint
>>> import tabulate
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    import tabulate
ModuleNotFoundError: No module named 'tabulate'
>>> pprint(data)
Traceback (most recent call last):
  File "<pyshell#26>", line 1, in <module>
    pprint(data)
TypeError: 'module' object is not callable
>>> pp = pprint.PrettyPrinter(indent = 10)
>>> pp.pprint(data)
{         'names': ['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul'],
          'ranking': [2, 1, 3, 4, 5, 6],
          'scores': [78, 100, 56, 45, 80, 41]}
>>> data
{'names': ['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul'], 'scores': [78, 100, 56, 45, 80, 41], 'ranking': [2, 1, 3, 4, 5, 6]}
>>> data.keys()
dict_keys(['names', 'scores', 'ranking'])
>>> data.values()
dict_values([['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul'], [78, 100, 56, 45, 80, 41], [2, 1, 3, 4, 5, 6]])
>>> data.items()
dict_items([('names', ['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul']), ('scores', [78, 100, 56, 45, 80, 41]), ('ranking', [2, 1, 3, 4, 5, 6])])
>>> for item in data:
	print(item)

	
names
scores
ranking
>>> for item in data.items():
	print(item)

	
('names', ['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul'])
('scores', [78, 100, 56, 45, 80, 41])
('ranking', [2, 1, 3, 4, 5, 6])
>>> for item in data.values():
	print(item)

	
['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul']
[78, 100, 56, 45, 80, 41]
[2, 1, 3, 4, 5, 6]
>>> data.get('names')
['Sachin', 'Kohli', 'yuvraj', 'Dhoni', 'Rohit', 'Rahul']
>>> data.get('name')
>>> 
