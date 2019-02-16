Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> chatData = []
>>> chatData = ['hi','hello','hey','hi there',23,45,78,22,5,45.66,32.56,]
>>> chatData
['hi', 'hello', 'hey', 'hi there', 23, 45, 78, 22, 5, 45.66, 32.56]
>>> type(chatData)
<class 'list'>
>>> emp = []
>>> emp.append('ram')
>>> emp
['ram']
>>> emp.append('shyam')
>>> emp.append('sumit')
>>> emp.append('rohit')
>>> emp
['ram', 'shyam', 'sumit', 'rohit']
>>> emp[1]
'shyam'
>>> emp[0:2]
['ram', 'shyam']
>>> emp.insert(2,'ram')
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'rohit']
>>> names = ['amit','aman','deepak','virat']
>>> emp + names
['ram', 'shyam', 'ram', 'sumit', 'rohit', 'amit', 'aman', 'deepak', 'virat']
>>> emp.append(names)
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'rohit', ['amit', 'aman', 'deepak', 'virat']]
>>> del emp[-1]
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'rohit']
>>> emp.extend(names)
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'rohit', 'amit', 'aman', 'deepak', 'virat']
>>> emp.pop()
'virat'
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'rohit', 'amit', 'aman', 'deepak']
>>> emp.pop(4)
'rohit'
>>> emp
['ram', 'shyam', 'ram', 'sumit', 'amit', 'aman', 'deepak']
>>> emp.count('ram')
2
>>> emp.index('amit')
4
>>> emp.remove('ram')
>>> emp
['shyam', 'ram', 'sumit', 'amit', 'aman', 'deepak']
>>> sorted(emp)
['aman', 'amit', 'deepak', 'ram', 'shyam', 'sumit']
>>> emp
['shyam', 'ram', 'sumit', 'amit', 'aman', 'deepak']
>>> emp.sort()
>>> emp
['aman', 'amit', 'deepak', 'ram', 'shyam', 'sumit']
>>> 
