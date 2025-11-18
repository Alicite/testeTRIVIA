import html
import requests

def fetch_trivia():
    url = 'https://opentdb.com/api.php?amount=5'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        return data['results']
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        return []
    
# print(fetch_trivia())

def fetch_tradutor(text):
    url = 'https://clients5.google.com/translate_a/t?client=dict-chrome-ex&sl=auto&tl=pt-BR&q=' + html.unescape(text)
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()

        return data[0][0]
    else:
        print(f"Error: Unable to fetch data (Status code: {response.status_code})")
        return None
    
# print(fetch_tradutor("Hello world!"))

questions = fetch_trivia()

for question in questions:
    print("Question:", question['question'])
    answer = fetch_tradutor(question['question'])
    print("Translation:", answer)
    print('---')