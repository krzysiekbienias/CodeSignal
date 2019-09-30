from typing import List
import numpy as np
from collections import Counter


class IntroGates:
    #8 problems
    def __init__(self):
        self.mintTwoDigits=self.addTwoDigits(n=15)


    def addTwoDigits(self,n:int)->int:
        a=n%10
        b=int(n//10)
        return a+b


    def largestNumber(self)->int:
        pass

    def candies(self)->int:
        pass

    def seatsInTheater(self)->int:
        pass


    def maxMultiple(self)->int:
        pass

    def circleOfNumbers(self)->int:
        pass


    def lateRide(self)->int:
        pass

    def phoneCall(self)->int:
        pass




class atTheCrossroads:
    def __init__(self):
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
    introGates=IntroGates()
    crossRoads=atTheCrossroads()
    corner0sAnd1s=CornerOf0sAnd1s()
    tunel=LoopTunnel()
    forestedge=ListForestEdge()
    nestedLoops=LabyrinthOfNestedLoops()
    bookMarket=BookMarket()
    mirrorLake=MirrorLake()
    integration=WellOfIntegration()

    print('the end')


