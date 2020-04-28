import os
import json
allJsonFiles = os.listdir('collection')
intents = {}
for jsonFile in allJsonFiles:
    data_file = open('collection/' + jsonFile).read()
    intentLoaded = json.loads(data_file)
    intents.update(intentLoaded)
    
print(intents)
# from collect import Collect
# collecting = Collect()
# collecting.do('https://answers.yahoo.com/question/index?qid=20200426020533AA3PJu8')
