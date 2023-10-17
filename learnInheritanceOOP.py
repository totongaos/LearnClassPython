class dad:
    def __init__(self, asset, bloodGroup, skinColor):
        self.asset = asset
        self.bloodGroup = bloodGroup
        self.skinColor = skinColor
class son(dad):
    def __init__(self, asset, bloodGroup, skinColor, hobby):
        super().__init__(asset, bloodGroup, skinColor) #super là lấy các thuộc tính của cha xuống
        self.hobby = hobby
Gapython = son(1000,'A','Yellow','nghe nhac')
print(Gapython.__dict__)  #xài __dict__ print ra giúp ta dễ hình dung hơn