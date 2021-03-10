import plotly.figure_factory as ff 
import plotly.graph_objects as go
import pandas as pd 
import statistics
import random
import csv

df=pd.read_csv("data.csv")

data=df["temp"].tolist()

population_mean=statistics.mean(data)
population_std=statistics.stdev(data)

print("mean of population")
print(population_mean)

def getMeanOfSample(counter):
    dataset=[]

    for i in range(0, 100):
        randomindex=random.randint(0, len(data))
        value=data[randomindex]
        dataset.append(value)

    mean=statistics.mean(dataset)
    return mean

def showFig(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    
    fig=ff.create_distplot([df], ["temp"], show_hist=False)
    fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 1], mode="lines", name="Mean"))
    fig.show()

def setup():
    meanlist=[]
    for i in range(0, 1000):
        setofmeans=getMeanOfSample(100)
        meanlist.append(setofmeans)
    
    showFig(meanlist)

    mean=statistics.mean(meanlist)
    print("Mean of sampling distribution:")
    print(mean)

setup()

print("st_dev of population")
print(population_std)

def stdOfSample():
    meanlist=[]
    for i in range(0, 1000):
        setofmeans=getMeanOfSample(100)
        meanlist.append(setofmeans)

    std=statistics.stdev(meanlist)
    print("st dev of sampling distribution:")
    print(std)

stdOfSample()