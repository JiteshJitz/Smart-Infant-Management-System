from firebase import firebase

firebase= firebase.FirebaseApplication('https://myfirst-869f2.firebaseio.com')

result = firebase.post('notification/temp', {'time':'12345678', 'value':'345', 'staus':'critical'})
print(result)


'''

result = firebase.post('PythonWala', {'message':'Hello'})

'''