# #set & get
# class Person:
#     name = 'No name'
#     def setName(self,new_name):
#         self.name = new_name
#     def getName(self):
#         return self.name
#
# a=Person()
# a.setName('Totongaos')
# print(a.getName())

# #thay đổi giá trị của thuộc tính
# class Person:
#     age = 0
#     def setAge(self, newAge):
#         self.age = newAge
#         self.age += 1
#     def getAge(self):
#         return self.age
#
# b = Person()
# b.setAge(10)
# print(b.getAge())

#  Gọi phương thức trong một phương thức khác
# class Person:
#     age = 0
#     def setAge(self,newAge):
#         self.age = newAge
#         self.age += 1
#         return self.age
#     def sayHi(self):
#         print(self.setAge(self.age))
#         if self.setAge(self.age) >= 18:
#             print('Bạn đã đủ tuổi đi tù :)))')
#
# b = Person()
# b.setAge(10)
# print(b.sayHi())

lst = ['dao','18','2000']
name,tuoi,nam = lst
print(name, tuoi, nam)