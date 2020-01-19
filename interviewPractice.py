from typing import List
import numpy as np
from collections import Counter
from itertools import product


class CommonTechniquesBasic:
    def __init__(self):
        self.mb_containsDuplicates = self.containsDuplicates(a=[1, 2, 3, 1])
        self.mb_sumOfTwo = self.sumOfTwo([1, 2, 3], b=[10, 20, 30, 40], v=42)
        self.sumInRange(nums=[3, 0, -2, 6, -3, 2], queries=[[0, 2], [2, 5], [0, 5]])

    def containsDuplicates(self, a):
        if (len(a) < 2):
            return False
        a.sort()
        for i in range(len(a) - 1):
            if a[i] == a[i + 1]:
                return True
        return False

    def sumOfTwo(self, a, b, v):
        if not a or not b:
            return False
        b = set(b)  # kill duplicates
        for i in range(len(a)):
            diff = v - a[i]
            if diff in b:
                return True
        return False

    def sumInRange(self, nums, queries):  # one hidden test fails, execution time limit
        res = nums[:]
        sums = []
        for i in range(len(queries)):
            first = queries[i][0]
            last = queries[i][1]
            sublist = res[first:last + 1]
            temp = sum(sublist)
            sums.append(temp)
        return sum(sums) % (10 ** 9 + 7)


class NumberTheory:
    def __init__(self):
        self.mi_missingNumber = self.missingNumber(arr=[3, 1, 0])

    def missingNumber(self, arr):
        labels = sum(list(range(len(arr) + 1)))
        currentArr = sum(arr)
        missingLabel = labels - currentArr
        return missingLabel


class Sorting:
    def __init__(self):
        self.ml_bubbleSort = self.bubbleSort(items=[2, 4, 1, 5])
        self.ml_bubbleSort2 = self.bubbleSort2(items=[2, 2, 2, 3, 7, 8, 9, 10, 3])

    def bubbleSort(self, items):
        is_sorted = False
        while not is_sorted:
            is_sorted = True
            for i in range(len(items) - 1):
                if items[i + 1] < items[i]:
                    self.swap(i, i + 1, items)
                    is_sorted = False
        return items

    def swap(self, i, j, items):
        items[i], items[j] = items[j], items[i]

    def bubbleSort2(self, items):

        def swap(firstIndex, secondIndex):
            temp = items[firstIndex]
            items[firstIndex] = items[secondIndex]
            items[secondIndex] = temp

        length = len(items) - 1

        for i in range(length):
            j = 0
            stop = length - i
            while j < stop - 1:
                if items[j] > items[j + 1]:
                    swap(j, j + 1)
                j += 1
        return items


class Counting:
    def __init__(self):
        self.ms_pressingButtons = self.pressingButtons(buttons='9')

    def pressingButtons(self, buttons):
        if len(buttons) == 0:
            return []
        numb = ['2', '3', '4', '5', '6', '7', '8', '9']
        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        d = dict(zip(numb, letters))
        cartesian = list(product(*[d[i] for i in buttons]))
        res = [*map("".join, cartesian)]
        return res


if __name__ == "__main__":
    coomtechb = CommonTechniquesBasic()
    numTheo = NumberTheory()
    sortTech = Sorting()
    counti = Counting()

    print('TheEnd')
