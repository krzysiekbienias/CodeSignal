from typing import List
import numpy as np
from collections import Counter


class IntroGates:
    # 8 problems
    def __init__(self):
        self.mintTwoDigits = self.addTwoDigits(n=15)

    def addTwoDigits(self, n: int) -> int:
        a = n % 10
        b = int(n // 10)
        return a + b

    def largestNumber(self) -> int:
        pass

    def candies(self) -> int:
        pass

    def seatsInTheater(self) -> int:
        pass

    def maxMultiple(self) -> int:
        pass

    def circleOfNumbers(self) -> int:
        pass

    def lateRide(self) -> int:
        pass

    def phoneCall(self) -> int:
        pass


class atTheCrossroads:
    def __init__(self):
        self.mbRpgNextLevel = self.reachNextLevel(experience=10, threshold=15, reward=5)
        self.mintknapsackLight = self.knapsackLight(value1=15, weight1=2, value2=20, weight2=3, maxW=2)
        # self.mbIsInfinite=self.isInfiniteProcess(a=2,b=3)#does not work
        self.btenis = self.tenisSet(score1=7, score2=7)

    def reachNextLevel(self, experience, threshold, reward):
        if experience + reward >= threshold:
            return True
        else:
            return False

    def knapsackLight(self, value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
        if weight1 + weight2 <= maxW:
            return value1 + value2
        elif min(weight2, weight1) > maxW:
            return 0
        elif weight1 <= maxW and weight2 > maxW:
            return value1
        elif weight2 <= maxW and weight1 > maxW:
            return value2
        elif weight1 <= maxW and weight2 <= maxW and weight1 + weight2 > maxW:
            return max(value1, value2)

    def extraNumber(self, a: int, b: int, c: int) -> int:
        if (a == b):
            return c
        if (a == c):
            return b
        if (b == c):
            return a

    def isInfiniteProcess(self, a: int, b: int) -> bool:  # does not work
        while a != b:
            a += 1
            b -= 1
        if a == b:
            return False
        else:
            return True

    def arithmeticExpression(self, a: float, b: float, c: float) -> bool:

        if a + b == c or a - b == c or a * b == c or a / b == c:
            return True
        else:
            return False

    def tenisSet(self, score1, score2):  # does not work hiden 17/20 test passed

        if (score1 == 6 and score2 < 5) or (score2 == 6 and score1 < 5):
            return True
        elif ((score1 == 7 and score1 - score2 <= 2) or (score1 == 5 and score2 - score1 <= 2)) and (score1 != score2):
            return True
        else:
            return False

    def willYou(self):
        pass

    def metroCard(self):
        pass


class CornerOf0sAnd1s:
    def __init__(self):
        pass


class LoopTunnel:
    def __init__(self):
        self.miLeastFactorial = self.leastFactorial(n=17)

    def leastFactorial(self, n):
        pass

    def countSumOfTwoRepresentations2(self, n, l, r):
        pass

    def magicalWell(self, a, b, n):
        pass

    def lineUp(self, commands):
        pass

    def additionWithoutCarrying(self, param1, param2):
        pass


class ListForestEdge:
    def __init__(self):
        self.mlArray=self.createArray(size=5)
        self.mlReplaicement=self.arrayReplace(inputArray=[1,2,1],elemToReplace=1,substitutionElem=3)
        self.mlFirstReverse=self.firstReverseTry(arr=[1, 2, 3, 4, 5])
        self.mlRemovePart=self.removeArrayPart(inputArray=[2, 3, 2, 3, 4, 5],l=2,r=4)
        self.mbMiddle=self.isSmooth(arr=[4,5,6,7,10])


    def createArray(self,size):
            return [1] * size

    def arrayReplace(self,inputArray, elemToReplace, substitutionElem):
        for i in range(len(inputArray)):
            if inputArray[i]==elemToReplace:
                inputArray[i]=substitutionElem
        return inputArray

    def firstReverseTry(self,arr:List[int])->List[int]:
        if len(arr)==0:
            return []
        else:
            f=arr[0]
            l=arr[-1]
            arr[0]=l
            arr[-1]=f
            return arr

    def removeArrayPart(self,inputArray:List[int], l:int, r:int)->List[int]:
        left=inputArray[:l]
        right=inputArray[r+1:]
        return left+right

    def isSmooth(self,arr):
        l=len(arr)
        if l%2==0:
            rightMiddlIndex=len(arr)/2
            leftMiddleIndex=rightMiddlIndex-1
            middleIndex=(leftMiddleIndex+rightMiddlIndex)/2

        else:
            middleIndex = (0 + l - 1) // 2
            return arr[middleIndex]






class LabyrinthOfNestedLoops:
    def __init__(self):
        pass


class BookMarket:
    def __init__(self):
        pass


class MirrorLake:
    def __init__(self):
        pass


class WellOfIntegration:
    def __init__(self):
        pass


if __name__ == "__main__":
    introGates = IntroGates()
    crossRoads = atTheCrossroads()
    corner0sAnd1s = CornerOf0sAnd1s()
    tunel = LoopTunnel()
    forestedge = ListForestEdge()
    nestedLoops = LabyrinthOfNestedLoops()
    bookMarket = BookMarket()
    mirrorLake = MirrorLake()
    integration = WellOfIntegration()

    print('the end')
