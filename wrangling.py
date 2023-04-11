import pandas as pd
import numpy as np

#converting to iso8601 date format for compatibility with gephi
def convertTimeStamps(df):
    #df['time'] = df['time'].map(lambda time: pd.to_datetime(time, unit='s'))
    time = pd.to_datetime(df['time'], unit='s').dt.strftime('%Y-%m-%dT%H:%M:%SZ')
    df['timeset'] = time
    df = df.drop('time', axis=1)
    return df

#reading in csv from our chosen dataset
def readCSV(file):
    return pd.read_csv(file, header=0)

#save to csv file
def saveCSV(df, file, header=False):
    df.to_csv(file, header = header, index=False)

#print some data from dataframe
def printDF(df):
    head = df.head(10)
    tail = df.tail(10)
    print("FIRST 10 ENTRIES\n", head)
    print("LAST 10 ENTRIES \n", tail)

#finding the unique node ids used
def findUniqueNodes(df):
    #getting nodes from source and target columns
    listOfNodes = df['Source'].unique()
    listOfTargetNodes = df['Target'].unique()
    listOfNodes.sort()
    #merging source and target columns
    listOfAllNodes = np.concatenate((listOfNodes, listOfTargetNodes), axis=None)
    print(listOfNodes.shape)
    print(listOfTargetNodes.shape)
    nodeDF = pd.DataFrame(data = listOfAllNodes)
    print(nodeDF)
    #finding unique nodes from the list of all nodes
    nodes = nodeDF[0].unique()
    print(nodes.shape)
    nodes.sort()
    print(nodes)
    uniqueNodeDF = pd.DataFrame(data = nodes, columns=['node'])
    uniqueNodeDF['id'] = uniqueNodeDF.loc[:, 'node']
    print(uniqueNodeDF.head(10))
    return uniqueNodeDF


#main
originalDF = readCSV('data\soc-sign-bitcoinotc.csv')
convertDF = convertTimeStamps(originalDF)
saveCSV(convertDF, 'data\\bitcoinotcTimeStampsiso8601.csv', header=True)
#df = readCSV('data\\bitcoinotcTimeStamps.csv')
#printDF(df)
#uniqueNodeDF = findUniqueNodes(df)
#printDF(uniqueNodeDF)
#saveCSV(uniqueNodeDF, 'data\\bitcoinotcNodes.csv', ['id', 'node'])


