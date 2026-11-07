contacts = {
    'number': 4,
    'students':
        [
            {'name': 'Biswa', 'email': 'biswaranjan.b@gmail.com'},
            {'name': 'John', 'email': 'john.doe@gmail.com'},
            {'name': 'Jane', 'email': 'jane.doe@gmail.com'},
            {'name': 'Alice', 'email': 'alice.doe@gmail.com'}          
        ]       
    }

print(contacts['number'])

for student in contacts['students']:
    print(student['name'])

for student in contacts['students']:
    print(student['email'])
