from student import Sudent

lst_student = []
while True:
    print('''
    Vui lòng chọn chức năng:
    0. Thoát
    1. Xem danh sách sinh viên
    2. Thêm sinh viên
    3. Xóa sinh viên
    4. Sửa sinh viên
    ''')
    select_section = input('Bạn chọn chức năng nào? ')
    if select_section.isdigit():
        select_section = int(select_section)
        if select_section == 0: #0. Thoát
            break
        elif select_section == 1: #1. Xem danh sách sinh viên
            if len(lst_student) == 0: print("Hiện chưa có sinh viên nào. Vui lòng thêm sinh viên!")
            else:
                for i in lst_student:
                    i.show()
        elif select_section == 2: #2. Thêm sinh viên
            id = input("Nhập ID sinh viên:")
            name = input("Nhập tên sinh viên:")
            lst_student.append(Sudent(id,name))
        elif select_section == 3: #3. Xóa sinh viên
            id = input('Nhập ID muốn xóa: ')
            for i in lst_student:
                if i.id == id:
                    lst_student.remove(i)
                    print("Đã xóa thành công sinh viên")
                else:
                    print('ID bạn nhập không có trong danh sách')
        elif select_section == 4: #4. Sửa sinh viên
            id = input('Nhập ID muốn sửa đổi: ')
            for i in lst_student:
                if i.id == id:
                    i.set_name(input("Nhập tên bạn muốn sửa đổi: "))
                    print("Đã sửa đổi thành công")
                else:
                    print('ID bạn nhập không có trong danh sách')
    else:
        print('-'*20,'\nVui lòng chọn lại')
