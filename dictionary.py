import operator
d={1:2,3:4,3:2,2:1,0:0}
print("original dic",d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print("dic is ace. order by value",sorted_d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1),reverse=true)
print("dic in dec. order by value",sorted_d)
