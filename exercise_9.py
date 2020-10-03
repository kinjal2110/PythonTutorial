# Akhbaar padhke sunao

import requests
import json

def speak(str):
    from win32com.client import Dispatch
    speak = Dispatch("SAPI.SpVOice")
    speak.Speak(str)

if __name__ == '__main__':
    speak("News for Today")
    url = "http://newsapi.org/v2/everything?q=bitcoin&from=2020-05-22&sortBy=publishedAt&apiKey=5cbbc5ec3cf649a19d5356a47f0161c8"
    news = requests.get(url).text
    news_dict = json.loads(news)
    # print(news["status"])               #status is ok
    print(news_dict["articles"])
    arts = news_dict["articles"]
    for article in arts:
        speak(article['title'])
        speak("Moving on tho the next news.. Listen carefully")

    speak("Thanks for listening")