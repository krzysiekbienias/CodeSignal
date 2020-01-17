from typing import List
import numpy as np
from collections import Counter


class IntroGates:
    # 8 problems
    def __init__(self):
        self.mintTwoDigits = self.addTwoDigits(n=15)
        self.mintMaxMultiple=self.maxMultiple(divisor=3,bound=10)
        self.miLateRide=self.lateRide(n=1439)

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

    def maxMultiple(self, divisor, bound) -> int:#does not work
        i = 1
        while i <= bound:
            N = i * divisor
            if N % divisor == 0 and N <= bound:
                i += 1
            else:
                return N

    def circleOfNumbers(self) -> int: #i have seen the result but i don't understand
        pass

    def lateRide(self,n) -> int:
        entireHours=n//60
        minutes=n-entireHours*60
        a=entireHours//10
        b=entireHours%10
        c=minutes//10
        d=minutes%10
        return a+b+c+d


    def phoneCall(self,min1, min2_10, min11, s) -> int:#duration of the longest call
        centsLeftAfter1Taryf=s-min1
        if centsLeftAfter1Taryf<0:
            return 0# there is not enough money for 1 min

        minutesBetween1and10=1
        if minutesBetween1and10*min2_10>centsLeftAfter1Taryf:
            minutesBetween1and10+=1
        centsLeftAfter2Taryf=centsLeftAfter1Taryf-min2_10
        if centsLeftAfter1Taryf<0:
                return minutesBetween1and10
        minutesMoreThan10=1
        if minutesMoreThan10 * min11>centsLeftAfter2Taryf:
            minutesMoreThan10+=1
        centsLeftAfter3Taryf=centsLeftAfter2Taryf-min11
        if centsLeftAfter3Taryf<0:
            return minutesMoreThan10



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
        self.miRepresentationSum=self.countSumOfTwoRepresentations2(n=6,l=2,r=4)




    def leastFactorial(self, n):
        pass

    def countSumOfTwoRepresentations2(self, n, l, r):
        counter=0
        a=0
        b=0
        while a>=l and b<=r:

            if n==a+b:
                counter+=1
        if n<a+b
        a += 1
        b += 1
        return counter


    def magicalWell(self, a, b, n):
        pass

    def lineUp(self, commands):
        pass

    def additionWithoutCarrying(self, param1, param2):
        pass


class ListForestEdge:
    def __init__(self):
        self.mlArray = self.createArray(size=5)
        self.mlReplaicement = self.arrayReplace(inputArray=[1, 2, 1], elemToReplace=1, substitutionElem=3)
        self.mlFirstReverse = self.firstReverseTry(arr=[1, 2, 3, 4, 5])
        self.mlRemovePart = self.removeArrayPart(inputArray=[2, 3, 2, 3, 4, 5], l=2, r=4)
        self.mbMiddle = self.isSmooth(arr=[4, 5, 6, 7, 10, 3])
        self.mlReplaceMiddle = self.replaceMiddle(arr=[7, 2, 2, 5, 10, 7])

    def createArray(self, size):
        return [1] * size

    def arrayReplace(self, inputArray, elemToReplace, substitutionElem):
        for i in range(len(inputArray)):
            if inputArray[i] == elemToReplace:
                inputArray[i] = substitutionElem
        return inputArray

    def firstReverseTry(self, arr: List[int]) -> List[int]:
        if len(arr) == 0:
            return []
        else:
            f = arr[0]
            l = arr[-1]
            arr[0] = l
            arr[-1] = f
            return arr

    def removeArrayPart(self, inputArray: List[int], l: int, r: int) -> List[int]:
        left = inputArray[:l]
        right = inputArray[r + 1:]
        return left + right

    def isSmooth(self, arr):
        l = len(arr)
        if l % 2 == 0:
            rightMiddlIndex = len(arr) // 2
            leftMiddleIndex = rightMiddlIndex - 1
            u = arr[rightMiddlIndex] + arr[leftMiddleIndex]
            if (arr[0] == arr[l - 1] == u):
                return True
            else:
                return False
        else:
            middleIndex = (0 + l - 1) // 2
            u = arr[middleIndex]
            if arr[0] == arr[l - 1] == u:
                return True
            else:
                return False

    def replaceMiddle(self, arr):
        l = len(arr)
        if l % 2 == 0:
            rightMiddlIndex = len(arr) // 2
            leftMiddleIndex = rightMiddlIndex - 1
            u = arr[rightMiddlIndex] + arr[leftMiddleIndex]

            arr.pop(rightMiddlIndex)
            arr.pop(leftMiddleIndex)
            arr.insert(leftMiddleIndex, u)
            return arr

        else:
            return arr

    def makeArrayConsecutive2(self, statues: List[int]) -> int:
        statues.sort()
        missingStatues = []
        for i in range(len(statues) - 1):
            if statues[i + 1] - statues[i] > 1:
                dif = statues[i + 1] - statues[i]

                lGaps = list(range(1, dif))
                for j in range(len(lGaps)):
                    temp = statues[i] + lGaps[j]
                    missingStatues.append(temp)
                i += 1
        return len(missingStatues)


class LabyrinthOfNestedLoops:
    def __init__(self):
        pass


class BookMarket:
    def __init__(self):
        self.msBrackets = self.encloseInBrackets(inputString="lala")
        self.msNoun = self.properNounCorrection(noun='mercedes')
        self.mbTandem = self.isTandemRepeat(inputString='tandemtandem')

    def encloseInBrackets(self, inputString: str) -> str:
        return "(" + inputString + ")"

    def properNounCorrection(self, noun: str) -> str:
        firstLetter = noun[0].upper()
        theRest = noun[1:].lower()
        return firstLetter + theRest

    def isTandemRepeat(self,
                       inputString):  # nope check len of the first half of the string is equal to the second half of the string.
        d1 = {}
        for ch in inputString:
            d1[ch] = d1.get(ch, 0) + 1

        return d1


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
