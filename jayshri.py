names = ["ishika", "jayshri", "hitakshi"]
print (names)

names2 = ("Peter", "Paul", "Mary")
print(names2[1])
print(names2,type(names2))

obj = {
    "fname" : "jayshri",
    "Iname" :  "Fulzele",
    "email" : "jayshrifulzele71@gmail.com",
    "phone" : 9604213200
}
print(obj,type(obj))
print(obj["fname"])
print(obj.keys())
print(obj.values())
print(obj.items())

num = {1,2,3,1,1,2}
print(num,type(num))



#Phase1 : CSV Read
import csv
with open(file='DTD.csv',mode='r') as f:
    csv_reader = csv.reader(f)