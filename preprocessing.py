import csv
import json

rows = []
finalData = []

with open('dataset.csv',encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for item in csv_reader:
        if(item[11] == 'TRUE' or item[11]=='FALSE'):
            # print(item[11] + " | " + item[16])
            sentiment = "Negative"
            if(item[11] == "TRUE"):
                sentiment = "Positive"
            finalData.append ({
                'text' : item[16],
                'sentiment': sentiment
            })
            
# print(finalData)

with open('reviews.txt','w') as jsonfile:
        json.dump(finalData,jsonfile,indent=4)

# print(rows[11])
