import requests
import json
import unicodecsv as csv

#f = open("/Users/michelleglewis/Downloads/ira_tweets_csv_hashed.csv", "rb")
userinput = input('Enter name of file ')
f = open(userinput, "rb")
df = csv.reader(f, encoding = 'utf-8')

dictionary = {}

count = 0
_ = next(df)

for i in df:
    words = i[12].split()
    for x in words:
        if x not in dictionary:
            dictionary[x] = [i[12]]
        else:
            dictionary[x].append(i[12])
    if count%100000 == 0:
        print (count)
    count = count + 1
    if count >= 10:
        break
    
#listofwords = [(x, dictionary[x]) for x in dictionary.keys()]

searchterm = input("Enter a word ")
while searchterm!= "":
    if searchterm in dictionary:
        for tweet in dictionary[searchterm]:
            print (tweet)
    else:
        print("Word not found")'
    searchterm = input("Enter a word")

#listofwords = [(list(dictionary.keys())[i], list(dictionary.values())[i]) for i in range(len(dictionary.keys()))]
#sortedlist = sorted(listofwords, key=lambda tup: tup[1], reverse=True)

