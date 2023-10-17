#class trong python
class Sudent:
    #đếm class Student đã thêm bao nhiêu
    count = 0
    #thuộc tính
    id=""
    name=""
    #phương thức

    def __init__(self, id, name): #hàm khởi tạo
        # print('hàm add student')
        self.id = id
        self.name = name
        Sudent.count+=1

    # def set_id(self): vì id trong SQL ko thể sửa nên mình sẽ ko xài hàm này
    #     self.id = id

    def get_id(self): #phương thức lấy đối tượng
        return self.id

    def set_name(self,name): #phương thức thiết lập đối tượng, truyền đối tượng or sửa đối tượng
        self.name = name
    def get_name(self): #phương thức lấy đối tượng
        return self.name

    def show(self):
        print(f'ID: {self.id}')
        print(f'Name: {self.name}')

