from bs4 import BeautifulSoup as BS
import json
from urllib.request import urlopen
import time

class Collect:
    def string_escape(self, s, encoding='utf-8'):
        return (s.encode('latin1')
                .decode('unicode-escape')
                .encode('latin1')
                .decode(encoding, errors='ignore'))
    def do(self, url):
        # intentsFile = open('intents.json',)
        # intents = json.load(intentsFile)
        timeStamp = time.strftime("%Y%m%d-%H%M%S")

        QUESTION = ''
        TAG = ''
        ANSWER_LIST = []

        html = urlopen(url)
        soup = BS(html)
        question = soup.find("h1", {"class": "Question__title___3_bQf"})
        tagDabba = soup.find("div", {"class": "Question__subtitle___14CZz"})
        answers = soup.find("ul", {"class": "AnswersList__answersList___1GjcP"})
        li = answers.findChildren("li" , recursive=False)
        tag = tagDabba.findChildren("a" , recursive=False)

        QUESTION = self.string_escape(question.text.strip()) 
        TAG = self.string_escape(tag[0].text.strip())


        for answer in li:
            lili = answer.findChildren("div", {"class": "ExpandableContent__content___NoJJI"})
            try:
                ANSWER_LIST.append(self.string_escape(lili[0].text.strip()))
            except:
                pass

        x = {
            "tag": TAG,
            "patterns": [QUESTION],
            "responses": ANSWER_LIST,
            "context":[""]
        }
        # intents.update(x)

        with open('collection/' + timeStamp + '.json', 'w') as outfile:
            json.dump(x, outfile, indent=4, sort_keys=True)


        print("DONE")
        return x