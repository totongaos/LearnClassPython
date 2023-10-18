# class Superman:
#     power = 50
#     def __init__(self, para_name, para_weapons, para_color):
#         self.name = para_name
#         self.weapons = para_weapons
#         self.color = para_color
#
#     @classmethod
#     def from_string(cls,infor_str): #thường những phương thức xử lý thế này hay có tên là from
#         lst = infor_str.split('-')
#         new_lst = [i.strip() for i in lst]
#         name, weapons, color = new_lst
#         return cls(name,weapons,color)
#
# infor_str = "red superman - sword - red"
# superman_A = Superman.from_string(infor_str)
# print(superman_A.__dict__)


class Superman:
    power = 50
    def __init__(self, para_name, para_weapons, para_color):
        self.name = para_name
        self.weapons = para_weapons
        self.color = para_color

    @classmethod
    def from_string(cls,para_power): #thường những phương thức xử lý thế này hay có tên là from
        cls.power = para_power

superman_A = Superman("red superman", "sword", 'red')
print(Superman.power)
print(superman_A.power)

superman_A.from_string(40)
print(Superman.power)
print(superman_A.power)

Superman.from_string(30)
print(Superman.power)
print(superman_A.power)
