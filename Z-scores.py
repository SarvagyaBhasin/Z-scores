import pandas as pd
import csv 
import plotly.graph_objects as go
import plotly.figure_factory as ff
import statistics
import random 

df=pd.read_csv("Math_data.csv")
data=df["Math_score"].tolist()

populationmean=statistics.mean(data)
populationsd=statistics.stdev(data)
print("population mean: ", populationmean)
print("population standard deviation: ", populationsd)
def randomsetofmean(counter):
    dataset=[]
    for i in range(0, counter):
        ri=random.randint(0, len(data)-1)
        dataset.append(data[ri])
    mean=statistics.mean(dataset)
    return mean

def showgraph(meanlist):
    df=meanlist
    mean=statistics.mean(df)
    sd=statistics.stdev(df)
    stdev1start, stdev1end=mean-sd, mean+sd
    stdev2start, stdev2end=mean-2*sd, mean+2*sd
    stdev3start, stdev3end=mean-3*sd, mean+3*sd
    #graph=ff.create_distplot([df], ["Math_score"], show_hist=False)
    #graph.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="mean"))
    #graph.add_trace(go.Scatter(x=[stdev1start, stdev1start], y=[0, 0.17], mode="lines", name="sd1start"))
    #graph.add_trace(go.Scatter(x=[stdev1end, stdev1end], y=[0, 0.17], mode="lines", name="sd1end"))
    #graph.add_trace(go.Scatter(x=[stdev2start, stdev2start], y=[0, 0.17], mode="lines", name="sd2start"))
    #graph.add_trace(go.Scatter(x=[stdev2end, stdev2end], y=[0, 0.17], mode="lines", name="sd2end"))
    #graph.add_trace(go.Scatter(x=[stdev3start, stdev3start], y=[0, 0.17], mode="lines", name="sd3start"))
    #graph.add_trace(go.Scatter(x=[stdev3end, stdev3end], y=[0, 0.17], mode="lines", name="sd3end"))
    #graph.show()
    samplemean=meanlist[10]
    zscore=samplemean-mean/ sd
    print("Z-score: ", zscore)

meanlist=[]
for i in range(0, 1000):
    setofmeans=randomsetofmean(100)
    meanlist.append(setofmeans)
showgraph(meanlist)
mean=statistics.mean(meanlist)
print("Mean of sampling distribution: ", mean)
sd=statistics.stdev(meanlist)
print("standard deviation: ", sd)