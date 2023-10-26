with open ('Games.csv' , 'w') as file:
    file.write('')
with open('TestData/TrainingResults/log.txt', 'w') as file:
    file.write('')
with open('TestData/TrainingResults/results.csv', 'w') as file:
    file.write('0,0,0,0,')
with open('TestData/TrainingResults/capital.txt', 'w') as file:
    file.write('100')
with open('TestData/TrainingResults/0-10.csv', 'w') as file:
    file.write('0,0,0,0,')
with open('TestData/TrainingResults/10-20.csv', 'w') as file:
    file.write('0,0,0,0,')
with open('TestData/TrainingResults/20-30.csv', 'w') as file:
    file.write('0,0,0,0,')
with open('TestData/TrainingResults/30-40.csv', 'w') as file:
    file.write('0,0,0,0,')
with open('TestData/TrainingResults/totalEarnings.txt', 'w') as file:
    file.write('0')
with open('TestData/TrainingResults/cutLossesLog.txt', 'w') as file:
    file.write('')
with open('TestData/TrainingResults/earningsLog.txt', 'w') as file:
    file.write('')
with open('log.txt') as file:
    file.write('')

filepath = ['TestData/TrainingResults/over', 'TestData/TrainingResults/spread']
filenames = ['0-5', '5-10', '10-15', '15-20', '20-25', '25-30', '30+']

for f in filepath:
    for name in filenames:
        with open(f + '/' + name + '.csv', 'w') as file:
            file.write('0,0,')