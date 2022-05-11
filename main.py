from pickle import FALSE
from turtle import pd
from cv2 import mean
import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv
import plotly.graph_objects as go

df = pd.read_csv("data.csv")
data = df["average"].tolist()

population_mean = statistics.mean(data)
print("population_mean: ", population_mean)

population_stdev = statistics.stdev(data)
print("population_stdev: ", population_stdev)


fig = ff.create_distplot([data], ['average'], show_hist = False)
#fig.show()

def random_set_of_mean(counter):
    dataset = []
    for i in range(0, counter):
        random_index = random.randint(0, len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def show_fig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("mean of sampling distribution: ", mean )
    fig = ff.create_distplot([df], ['average'], show_hist = False)
    fig.show()

def setup():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(50)
        mean_list.append(set_of_means)
    show_fig(mean_list)

setup()

def stdev():
    mean_list = []
    for i in range(0, 100):
        set_of_means = random_set_of_mean(50)
        mean_list.append(set_of_means)
    standard_dev = statistics.stdev(mean_list)
    print("standard dev of sampling distribution", standard_dev)

stdev()