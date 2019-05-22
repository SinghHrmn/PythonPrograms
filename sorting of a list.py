'''list_1 = [20,30,40,50,67,77,12]
list_2 = [12,13,14,17,15,22]
decend = []
list_3 = list_1 + list_2
while list_3 != []:
    maxnum = max(list_3)
    decend.append(maxnum)
    list_3.remove(maxnum)
print('The decending order of the list is :',decend,end=' ')'''
list_1 = ['Kriti','Harman','Nikhil','Yuvraj','Keerat','Shikha']
list_2 = ['Arshdeep','Jaspreet','Sukhman','Sahil']
acend = []
list_3 = list_1 + list_2
while list_3 != []:
    mincharc = min(list_3)
    acend.append(mincharc)
    list_3.remove(mincharc)
for charc in acend:
    ans = charc
    print(charc, end=' ')


