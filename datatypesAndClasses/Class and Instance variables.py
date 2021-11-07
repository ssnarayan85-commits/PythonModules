class employee(object):
    incr=1.14
    def __init__(self, name, sal):
        self.ename = name
        self.esal = sal

    def calc_incr(self):
        return ( self.esal * self.incr)


e1=employee('john',1000)

print("employee incr", employee.incr)
# e1.incr=2.14
print("e1 obj incr", e1.incr)

print(e1.__dict__, "name=", e1.ename, "totsal = ", e1.calc_incr())

print(employee.__dict__)
