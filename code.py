'''
author: Veronica White 2021
Getting started with Github Exercise
Data Cleaning File
'''
f = open(r'data.txt', 'r')

raw_data = f.read()
data = raw_data.split(";")
f.close()

dictionary = {'0': " ", '1':"a", '2':"b", '3':"c", '4':"d", '5':"e", '6':"f", '7':"g", '8':"h", '9':"i", '10':"j", '11':"k", '12':"l", '13':"m", '14':"n", '15':"o", '16':"p", '17':"q", '18':"r", '19':"s", '20':"t", '21':"u", '22':"v", '23':"w", '24':"x", '25':"y", '26':"z"}

string = ""
for i in data:
    string += dictionary[i]

print(string)