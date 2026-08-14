import numpy as np
import math

def MarvellousEucDistance(p1, p2):
    Ans = math.sqrt((p1['X'] - p2['X'])**2 +
                    (p1['Y'] - p2['Y'])**2)
    return Ans


def MarvellousKNNClassifier(new_pointX, new_pointY, k=3):
    border = "-" * 50

    Data = [
        {'point':'A','X':1,'Y':2,'label':'Red'},
        {'point':'B','X':2,'Y':3,'label':'Red'},
        {'point':'C','X':3,'Y':1,'label':'Blue'},
        {'point':'D','X':5,'Y':6,'label':'Blue'},
        
    ]

    new_point = {
        'X': new_pointX,
        'Y': new_pointY
    }

    print(border)
    print("Marvellous KNN Classifier")
    print(border)

    for i in Data:
        print(i)

    print(border)

    print("Distances of all points :")
    print(border)

    for d in Data:
        d['distance'] = MarvellousEucDistance(d, new_point)

    for d in Data:
        print(d)

    print(border)

    sorted_data = sorted(Data, key=lambda item: item['distance'])

    print(border)
    print("Sorted Data :")
    print(border)

    for d in sorted_data:
        print(d)

    print(border)

    nearest = sorted_data[:k]

    print(border)
    print("Nearest 3 members are :")
    print(border)

    for d in nearest:
        print(d)

    print(border)

    # Voting
    votes = {}

    for neighbours in nearest:
        label = neighbours['label']
        votes[label] = votes.get(label, 0) + 1

    print(border)
    print("Voting Result is :")
    print(border)

    for d in votes:
        print("Name :", d, "Number of votes :", votes[d])

    print(border)

    iMax = 0
    Name = ""

    for d in votes:
        if votes[d] > iMax:
            iMax = votes[d]
            Name = d

    print("Final Prediction is :", Name)


def main():
    new_pointX = int(input("Enter X Coordinate : "))
    new_pointY = int(input("Enter Y Coordinate : "))

    MarvellousKNNClassifier(new_pointX, new_pointY)


if __name__ == "__main__":
    main()