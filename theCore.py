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

    def reachNextLevel(self, experience, threshold, reward):
        if experience + reward >= threshold:
            return True
        else:
            return False

    def knapsackLight(self, value1: int, weight1: int, value2: int, weight2: int, maxW: int) -> int:
        if weight1 + weight2 <= maxW:
            return value1 + value2
        elif min(weight2,weight1)>maxW:
            return 0
        elif min(weight2,weight1)==maxW:
            return max(value2,value1)
        elif max(weight1,weight2)<=maxW:
            return max(value1,value2)


    def extraNumber(self):
        pass

    def isInfiniteProcess(self):
        pass

    def arithmeticExpression(self):
        pass

    def tenisSet(self):
        pass

    def willYou(self):
        pass

    def metroCard(self):
        pass


class CornerOf0sAnd1s:
    def __init__(self):
        pass


class LoopTunnel:
    def __init__(self):
        pass


class ListForestEdge:
    def __init__(self):
        pass


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
