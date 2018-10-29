# Generates Random data and sends it to Firebase

from firebase import firebase
import random, datetime, string

def id(size=6, chars=string.ascii_uppercase + string.digits):
	return ''.join(random.choice(chars) for _ in range(size))

firebase = firebase.FirebaseApplication('https://xbee-d18df.firebaseio.com/', None)

data = str(random.randint(1,1000))
time =  str(datetime.datetime.now().replace(hour=random.randint(0,23), 
	minute=random.randint(0,59)) + datetime.timedelta(days=random.randint(0,10)))

result = firebase.put('/recyclerview', id(), {"data": data, "time": time})
print(result)
