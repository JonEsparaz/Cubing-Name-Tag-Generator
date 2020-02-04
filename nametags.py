import pandas as pd
import numpy as np
import csv
import random

# Usage: enter competition name of csv file, competition name

csv_name = 'example.csv'
competition_name = 'Example Competition 2020'

# Usage: enter staff, delegates and organizers as strings (delegate AND organizer is acceptable)

staff_list = []
organizers_list = []
delegates_list = []

# Do not edit below this comment! Things will break.

filename = str(competition_name + ' nametags')

def read_data(name_n_id):
    read = pd.read_csv(csv_name)

    names = list(read['Name'])
    temp = read['WCA ID']
    temp2 = temp.replace(np.nan, '', regex=True)
    wcaid = list(temp2)
    for i in names:
        name_n_id.append(i)
    for j in wcaid:
        name_n_id.append(j)

    return(0)

def position_check(data):
    for i in range(0,int(len(data)/2)):
        if data[i] in staff_list:
            data.append('Staff')
        elif (data[i] in organizers_list) and (data[i] in delegates_list):
            data.append('Delegate and Organizer') 
        elif data[i] in organizers_list:
            data.append('Organizer')
        elif data[i] in delegates_list:
            data.append('Delegate')
        else:
            data.append('Competitor')

def latex_output(data):
    latex = open(filename + '.tex','a')
    num = int(len(data)/3)
    for i in range(0,int(len(data)/3)):
        latex.write('\cubingnametag' + '{' + competition_name + '}' + '{' + data[i] + '}' + '{' + data[i+num] + '}' + '{' + data[i+(num*2)] + '}')
        latex.write('\n')
    return(0)

acc = []
read_data(acc)
position_check(acc)
latex_output(acc)
