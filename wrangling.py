import pandas as pd

#adding labels to the columns since the csv does not have a header
columnLabels = ['source node', 'target node', 'rating', 'time']

#reading in csv from our chosen dataset
df = pd.read_csv('data\soc-sign-bitcoinotc.csv', header=None, names=columnLabels)

#converting to human readable times
df['time'] = df['time'].map(lambda time: pd.to_datetime(time, unit='s'))

#saving as new csv
#df.to_csv('data\\bitcoinotcTimeStamps.csv')

#printing out the beginning and end of the data
head = df.head(10)
tail = df.tail(10)
print("FIRST 10 ENTRIES\n", head)
print("LAST 10 ENTRIES \n", tail)