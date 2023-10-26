def shouldFlip(catagory, filepath):
    with open ("TestData/TrainingResults/" + filepath + "/" + catagory, 'r') as file:
        line = file.read()
        results = line.split(',')
        if results[1] == "0":
            q = 1
        else:
            q = float(results[0]) / float(results[1])
        if q < .5:
            return True
        else:
            return False


def determineResults(prediction, shouldFlip):
    return False



def updateFlips(catagory, filepath, success):
    return 1