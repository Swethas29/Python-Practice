class laptop:
  def __init__(self):
    self.brand = ""
    self.RAM = ""
    self.storage=""
  def configuration(self):
    self.brand=input("Enter the Brandname: ")
    self.RAM=input("Enter the RAM: ")
    self.storage=input("Enter the storage: ")
  def test(self):
        print("Brand:", self.brand)
        print("RAM:", self.RAM)
        print("Storage:", self.storage)
lapobject = laptop()
lapobject.configuration()
lapobject.test()

class product:
  def __init__(self):
    self.ID = ""
    self.Name = ""
    self.quality=""
    self.price=""
  def display(self):
    self.ID=input("Enter the ID: ")
    self.Name=input("Enter the Name: ")
    self.quality=input("Enter the quality: ")
    self.price=input("Enter the price: ")

  def test(self):
        print("Brand:", self.ID)
        print("Name:", self.Name)
        print("quality:", self.quality)
        print("price:", self.price)
productobject = product()
productobject.display()

class Movie:
    def __init__(self):
        self.name = "Leo"
        self.director = "Lokesh Kanagaraj"
        self.language = "Tamil"
        self.year = 2023

    def display(self):
        print("Movie Name:", self.name)
        print("Director:", self.director)
        print("Language:", self.language)
        print("Release Year:", self.year)
movieobject = Movie()
movieobject.display()
productobject.test()

class rectangle:
  def __init__(self):
    self.length = ""
    self.breadth= ""
    self.area =""
  def display(self):
    self.length=int(input("Enter length of the Rectangle : "))
    self.rectangle=int(input("Enter breadth of the Rectangle: "))
    self.area= self.length * self.rectangle
  def test(self):
        print("length:", self.length)
        print("rectangle:", self.rectangle)
        print("area:", self.area)
rectobject = rectangle()
rectobject.display()
rectobject.test()
