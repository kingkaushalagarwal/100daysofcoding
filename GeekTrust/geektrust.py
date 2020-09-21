class Node:
    def __init__(self,name,gender,partner):
        self.name = name
        self.gender = gender
        self.child =[]
        self.parent = None
        self.partner = partner
class Gender:
    def __init__(self):
        self.Male = "male"
        self.Female = "female"


class FamilyTree:
    def __init__(self):
        self.root = Node("dummy",None)
        king = Node("King Shan",Gender().Male,"Queen Ange")
        queen = Node("Queen Ange",Gender().Female,"King Shan")
        self.root.child.append(king,queen)




