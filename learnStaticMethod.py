class Superman:
    power = 50
    def __init__(self, para_name, para_weapons, para_color):
        self.name = para_name
        self.weapons = para_weapons
        self.color = para_color

    @staticmethod
    def transfigure(): #khi xài @staticmethod thì ta ko n thêm self vào
        print("1,2,3. Sieu nhan bien hinh")

superman_A = Superman("red superman", "sword", 'red')
superman_A.transfigure()