'''
Created on Jun 19, 2016

@author: Admin
'''
class LunchMenu:
    def __init__(self):
        self.menuItems = list()
    def addItem(self,menuItem):
        self.menuItems.append(menuItem)
    def printMenu(self):
        for item in self.menuItems:
            print(item)

class DinnerMenu:
    def __init__(self):
        self.dinnerMenu = dict()
    
    def addItem(self,itemName,itemDesc):
        self.dinnerMenu[itemName] = itemDesc
    
    def printMenu(self):
        for key,value in self.dinnerMenu.items():
            print(key)
            
class Menu:
    def __init__(self):
        self.allMenus = list()
    
    def addMenu(self,menuObject):
        self.allMenus.append(menuObject)
    
    def printMenu(self):
        for obj in self.allMenus:
            obj.printMenu()
            
def main():
    menu = Menu()
    
    
    menu.addMenu(LunchMenu())
    menu.addMenu(DinnerMenu())
    
    