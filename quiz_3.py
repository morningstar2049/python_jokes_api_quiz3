import requests
import json
import sqlite3

res = requests.get(
    'https://v2.jokeapi.dev/joke/Programming?type=single&amount=10')

res_structured = json.dumps(res.json(), indent=2)

# for joke in res.json()['jokes']:
#     print(joke['joke'])

# with open('jokes.json', 'w') as file:
#     json.dump(res.json(), file, indent=3)


conn = sqlite3.connect('jokes_db.sqlite')

cursor = conn.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS jokes(  
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category VARCHAR(20),
            joke VARCHAR(150),
            language VARCHAR(10)

)""")  # ვქმნით ცხრილს, რომელსაც ექნება უნიკალური აიდი, ხუმრობის კატეგორია, ხუმრობა და ხუმრობის ენა.

jokes_list = []

for joke in res.json()['jokes']:
    joke_tuple = (joke['id'], joke['category'], joke['joke'], joke['lang'])
    jokes_list.append(joke_tuple)

# print(jokes_list)
# cursor.executemany("INSERT INTO jokes VALUES(?,?,?,?)", jokes_list)

results = cursor.execute("SELECT * FROM jokes").fetchall()
# for result in results:
#     print(result)

conn.commit()
conn.close()
