import pandas as pd

movie_file = 'moviesdataset.txt'
movie_columns = ['ID', 'NAME', 'RELEASE', 'RATING', 'DURATION']

movie_data = pd.read_csv(movie_file, sep=',', names=movie_columns)


def prob_A():
    k1 = 0
    for j in movie_data['RELEASE']:
        if j > 1950 and j < 1960:
            k1 += 1
    print('No. of Movies Released between 1950 and 1960:', k1)


def prob_B():
    k2 = 0
    for j in movie_data['RATING']:
        if j > 4:
            k2 += 1
    print('No. of Movies having rating more than 4:', k2)


def prob_C():
    k3 = []
    grpby = movie_data.groupby(['NAME', 'RATING'])
    for j in grpby:
        if j[0][1]>3 and j[0][1]<4:
            k3.append(j[0][0])
    print('The List of Movies having Rating between 3 and 4:\n\n',k3)


def prob_D():
    k4 = 0
    for j in movie_data['DURATION']:
        if j > 7200:
            k4 += 1
    print('No. of Movies with duration more than 2 hours (7200 second):', k4)


def prob_E():
    l5 = []
    for j in movie_data['RELEASE']:
        if j in l5:
            pass
        else:
            l5.append(j)
    l5.sort()
    print('The list of years:\n\n',l5,'\n\n')
    for y in l5:
        k5 = 0
        for y1 in movie_data['RELEASE']:
            if y1 == y:
              k5 += 1
        print('number of movies released in ',y,':',k5)


def prob_F():
    print('Total no. of movies in this datalist:',len(movie_data['ID']))



print('>>> SOLUTION-A\n')
prob_A()

print('\n\n\n>>> SOLUTION-B\n')
prob_B()

print('\n\n\n>>> SOLUTION-C\n')
prob_C()

print('\n\n\n>>> SOLUTION-D\n')
prob_D()

print('\n\n\n>>> SOLUTION-E\n')
prob_E()

print('\n\n\n>>> SOLUTION-F\n')
prob_F()