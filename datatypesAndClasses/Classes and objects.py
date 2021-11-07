class employee(object):
    def __init__(self, nm, sal, age):
        self.name=nm
        self.salary=sal
        self.age=age

    def totSal(self,sal,incr):
        self.salary = sal + incr
hl
return self.salary

emp1 = employee('shree',1000,30)
print(emp1.name)
print(emp1.salary)
print(emp1.age)

print(emp1.totSal(1000,200 ))


