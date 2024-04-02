# a={'good','bad','good'}
# print(type(a))
# print(a)
# typecasting list to set
# a=set(['mohit','geeta','hari','hare krishna'])
# print(a)
# adding items to the set
# a={"parul","deepika","radharani","krishna"}
# a.add("balram")
# print(a)
# noraml set is mutable whereas frozen set is immutable

# adding element to the set by using iterator
# a={"parul","deepika","radharani","krishna"}
# for i in a:
#     print(i)

# union -set1{a,b,c}+set2{b,c,d}-:{a,b,c,d}
# intersection -set1{a,b,c}+set2{b,c,d}-:{b,c}
# set1-set2-:{a}
# set2-set1-:{d}

# union using "|" operator
# a={"parul","deepika","radharani","krishna"}
# b={"balram","chaitanye mahaprabhu","parul"}
# c=a|b
# print(c)

# intersection of two sets
# a={"parul","deepika","radharani","krishna"}
# b={"balram","chaitanye mahaprabhu","parul"}
# c=a&b
# print(c)

# difference of set using difference function
# a={"parul","deepika","radharani","krishna"}
# b={"balram","chaitanye mahaprabhu","parul"}
# c=a.difference(b)
# d=b.difference(a)
# print(c)
# print(d)

# clearing of set
# a={"parul","deepika","radharani","krishna"}
# b={"balram","chaitanye mahaprabhu","parul"}
# print(b)
# print(a)
# b.clear()
# print(a)
# print(b)