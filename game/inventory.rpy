init python:
    class item:
        def __init__(self, name, image, hover):
            self.name = name
            self.image = image
            self.imageH = hover

    class inv:
        def __init__(self):
            self.items = []
            self.amount = 0

        def add(self, itemname, itemimage, hover):
            self.items.append(item(itemname,itemimage,hover))
            self.amount += 1

        def add(self, item):
            self.items.append(item)
            self.amount+=1

        def remove(self,item):
            self.items.remove(item)
            self.amount -=1