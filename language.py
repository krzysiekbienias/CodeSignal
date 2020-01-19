def baseConversion(n, x):
    return hex(int(n, x))[2:]

basehex=baseConversion('100',2)



def listBeautifier(a):
    res = a[:]
    while res and res[0] != res[-1]:
        first, *res, last = res
    return res


beauty=listBeautifier(a=[3, 4, 2, 4, 38, 4, 5, 3, 2])

def catWalk(code):
    res=' '.join(code.split())
    return res

cat=catWalk('def      m   e  gaDifficu     ltFun        ction(x):')


class lambdaIllusions:
    def __init__(self):
        self.m_repeatChart=lambda ch, n: ch * n
        self.mi_getPoints=self.getPoints(answers=[True,True,False,True],p=2)




    def getPoints(self, answers, p):
        questionPoints = lambda i,ans:i+1 if ans else -p
        res = 0
        for i, ans in enumerate(answers):
            res += questionPoints(i, ans)
        return res

    def sortStudents(self,students):
        students.sort(key=...)
        return students

if __name__ == "__main__":
    ilusion=lambdaIllusions()
    print('the end')