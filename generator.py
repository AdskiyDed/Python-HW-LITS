# dict1={1:0, 2:0, 3:1, 4:2}
# dict2={v:k if dict1.values.count(v)<2 else [dict1[k]+[]} #ne rabotaet dodelat
# dict2={v:k for k,v in dict1.items()} #vtniaet keys and values mestami
# print(dict2)


#уберает минуса у ключей
# dict3={1:-1,2:2, 3:-3, 4:4}
# dict4={k:(v if v>0 else -v) for k,v in dict3.items()}
# print(dict4)


# list1=[[1,2,3],[4,5,6],[7,8,9]]
# list2=[x for y in list1 for x in y]
# print(list2)

# list=[[x+i for i in range (1,4)] for x in range(1,4)]
# print(list)