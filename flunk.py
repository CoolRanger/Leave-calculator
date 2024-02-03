import datetime

mon = ["國文", "粒子", "英作", "數甲", "加深加廣", "加深加廣", "能斯特方"] #課表
tue = ["多元", "多元", "選化四", "選化三", "國文", "數甲", "生涯"]
wed = ["彈性", "藝術", "藝術", "體育", "週會", "班會", "彈性"]
thu = ["英文", "數甲", "選物三", "選物三", "國文", "英文", "彈性"]
fri = ["體育", "英作", "選化三", "國防", "國文", "選物四", "數甲"]

holiday = ["2023 9 29", "2023 10 9", "2023 10 10", "2024 1 1"] #國定假日
makeup = ["2023 9 23 2023 10 9"] #"補課日 補假日"

all = []
all.append(mon)
all.append(tue)
all.append(wed)
all.append(thu)
all.append(fri)

times = {} #每周幾堂
for i in all:
    for j in i:
        if not j in times:
            times[j]=1
        else:
            times[j]+=1

dic = {} #請假科目/數

def cal(d):
    for i in all[d]:
        if not i in dic:
            dic[i] = 1
        else:
            dic[i]+=1
while 1:
    try:
        l = list(map(int, input().split()))
        d = datetime.date(l[0], l[1], l[2]).isoweekday()
        if d == 6:
            d = 1
        if len(l)>3:
            s = all[d-1][l[3]-1]
            if not s in dic:
                dic[s]=1
            else:
                dic[s]+=1
        else:
            cal(d-1)
            
    except:
        break

for i in dic: #18周
    times[i] *= 18

for i in holiday: #扣除國定假日
    l = list(map(int, i.split()))
    d = datetime.date(l[0], l[1], l[2]).isoweekday()
    for j in all[d-1]:
        if not j in dic:
            times[j] = -1
        else:
            times[j]-=1

for i in dic:
    if i =="X":
        continue
    print(f"{i}:{dic[i]}/{times[i]} (還可以請{times[i]//3-dic[i]}節)")


"""
2023 9 1 1
2023 9 6 5 6 7
2023 9 8
2023 9 23 1
2023 9 28
2023 10 6 7
2023 10 18
2023 10 27
2023 11 1 
2023 11 10 1
2023 11 13 1
2023 11 17
2023 11 20
2023 11 22
2023 12 1
2023 12 5 1 2
2023 12 19 5 6 7
2023 12 26 5 6 7
2024 1 4 2 3 4 5 7
2024 1 8 1 2 4
2024 1 10 1
2024 1 11
2024 1 15
2024 1 16
2024 1 17
2024 1 18
"""