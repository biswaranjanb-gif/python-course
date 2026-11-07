class Employee:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

class SalaryEmployee (Employee):
    def __init__(self, fname, lname, salary):
        super().__init__(fname, lname)
        self.salary = salary
    def calculate_pay_check(self):
        return self.salary / 52

class HourlyEmployee (Employee):
    def __init__(self, fname, lname, hours_worked, hourly_rate):
        super().__init__(fname, lname)
        self.hours_worked = hours_worked
        self.hourly_rate = hourly_rate
    def calculate_pay_check(self):
        return self.hours_worked * self.hourly_rate

class CommissionEmployee(SalaryEmployee):
    def __init__(self, fname, lname, salary, sales_num, commision_rate):
        super().__init__(fname, lname, salary)   
        self.sales_num = sales_num
        self.commision_rate = commision_rate

    def calculate_pay_check(self):
        regular_pay = super().calculate_pay_check()
        total_commission = self.sales_num * self.commision_rate
        return regular_pay + total_commission
    


    
