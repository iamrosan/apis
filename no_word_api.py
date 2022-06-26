#Numbers Translator Rapid Api
import http.client
import sys

conn = http.client.HTTPSConnection("numbers-spell.p.rapidapi.com")

headers = {
    'X-FunTranslations-Api-Secret': "<REQUIRED>",
    'X-RapidAPI-Key': "62457c2b65mshabfa50d155b5754p13f85ajsn99c1ef83f4ce",
    'X-RapidAPI-Host': "numbers-spell.p.rapidapi.com"
    }
try:
    number = int(input('Enter your Number : '))
except:
    print("Please enter number only.")
    sys.exit()

conn.request("GET", f"/numbers?text={number}", headers=headers)

res = conn.getresponse()
data = res.read().decode('utf-8')
print(data)
# print(type(data))
# print(data.find('translated'))
if (str(data[data.find('code')+7:data.find(',')])=='429'):
    print('''
    Rate limit: '5 requests per hour'
    api call limit exceed.. 
    Try again later.
    Sorry for inconvience.
    ''')
    sys.exit()
else:
    num_in_word = str(data[data.find('translated')+13:data.find(',')])
print("No in word:", num_in_word)