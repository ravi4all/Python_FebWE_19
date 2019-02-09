Python 3.6.2 (v3.6.2:5fd33b5, Jul  8 2017, 04:57:36) [MSC v.1900 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
 RESTART: C:/Users/asus/Documents/Data/DataTransfer/BMPL_Batches/2019/Feb/Python_WE+Morning/String_1.py 
hello this is python programming
>>> a[0]
'h'
>>> a[7]
'h'
>>> a[-1]
'g'
>>> a[0:4]
'hell'
>>> a[5:12]
' this i'
>>> a[12:1]
''
>>> a[1:12]
'ello this i'
>>> a[12:1]
''
>>> a[1:12:1]
'ello this i'
>>> a[0:12:2]
'hloti '
>>> a
'hello this is python programming'
>>> a[0:20:2]
'hloti spto'
>>> a[0:20:3]
'hltssyo'
>>> a[12:1]
''
>>> a[12]
's'
>>> a[20]
' '
>>> a[12:16]
's py'
>>> a[16:12:-1]
'typ '
>>> a[-1:-20]
''
>>> a[-1:-20:-1]
'gnimmargorp nohtyp '
>>> a[-20:-1]
's python programmin'
>>> len(a)
32
>>> a.capitalize()
'Hello this is python programming'
>>> a.title()
'Hello This Is Python Programming'
>>> a.upper()
'HELLO THIS IS PYTHON PROGRAMMING'
>>> a.lower()
'hello this is python programming'
>>> a
'hello this is python programming'
>>> a.replace('hello','bye')
'bye this is python programming'
>>> a
'hello this is python programming'
>>> a.index('p')
14
>>> a.find('p')
14
>>> a.rfind('p')
21
>>> a.find('o')
4
>>> a.rfind('o')
23
>>> a.find('o',5)
18
>>> a.count('o')
3
>>> b = a.find('o')
>>> a.endswith()
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    a.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
>>> 
>>> a.endswith()
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    a.endswith()
TypeError: endswith() takes at least 1 argument (0 given)
'
>>> a.startswith('h')
True
>>> a.istitle()
False
>>> a.isprintable()
True
>>> a.zfill(20)
'hello this is python programming'
>>> a.zfill(33)
'0hello this is python programming'
>>> a.zfill(34)
'00hello this is python programming'
>>> a.zfill(40)
'00000000hello this is python programming'
>>> a.center(33)
' hello this is python programming'
>>> a.center(34)
' hello this is python programming '
>>> a.center(50)
'         hello this is python programming         '
>>> a = a.center(50)
>>> a
'         hello this is python programming         '
>>> a.strip()
'hello this is python programming'
>>> a = a.strip()
>>> a
'hello this is python programming'
>>> a.center(50,'#')
'#########hello this is python programming#########'
>>> a.split()
['hello', 'this', 'is', 'python', 'programming']
>>> b = a.split()
>>> b[3:4]
['python']
>>> b
['hello', 'this', 'is', 'python', 'programming']
>>> b[:]
['hello', 'this', 'is', 'python', 'programming']
>>> b[0:]
['hello', 'this', 'is', 'python', 'programming']
>>> b[:5]
['hello', 'this', 'is', 'python', 'programming']
>>> b[::-1]
['programming', 'python', 'is', 'this', 'hello']
>>> a[::-1]
'gnimmargorp nohtyp si siht olleh'
>>> 
