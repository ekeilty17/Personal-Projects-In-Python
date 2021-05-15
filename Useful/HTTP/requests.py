import requests

# in order to use this you need to be running some local server with simple get and post requests

print

# GET contents of website
r = requests.get('http://localhost:8080/')
print r.content
print

# If you have to login
r = requests.get('https://github.com', auth=('ekeilty17', 'Sports99!'))
print r.content
print

# POST
data = {'id': 'python', 'name': 'Python', 'description': 'Whether iPyhton or Python, 2.7 or 3.6, I love it!'}
r = requests.post('http://localhost:8080/post', json=data)
r = requests.get('http://localhost:8080/post')
print r.content
r = requests.get('http://localhost:8080/post/python')
print r.content
print

# PUT
new_data = {'id': 'python', 'name': 'Python', 'description': 'Whether iPyhton or Python, 2.7 or 3.6, I love it! And its wayyy better than Java.'}
r = requests.put('http://localhost:8080/post/python', json=new_data)
r = requests.get('http://localhost:8080/post')
print r.content
print

# DELETE
r = requests.delete('http://localhost:8080/post/python')
r = requests.get('http://localhost:8080/post')
print r.content
print
