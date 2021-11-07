
class cars:
    def __init__(self,name,color, model):
        self.cname = name
        self.ccolor = color
        self.cmodel = model

    def print_attr (self):
        print("Car name:", self.cname)
        print("Car color:", self.ccolor)
        print("Car model:", self.cmodel)

c1 = cars('corolla','red', 2015)
c2 = cars('honda', 'black', 2013)

c1.print_attr()
c2.print_attr()
