"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self, name, contractAmount, hours = 0, commissionAmount = 0, contractNum = 0):
        self.name = name
        self.contractAmount = contractAmount
        self.hours = hours
        self.commissionAmount = commissionAmount    
        self.contractNum = contractNum

    def get_pay(self):
        base_pay = self.hours * self.contractAmount if self.hours else self.contractAmount
        commission_pay = self.contractNum * self.commissionAmount if self.contractNum else self.commissionAmount
        
        return base_pay + commission_pay

    def __str__(self):
        result = f"{self.name} works on a "
        if self.hours:
            result += f"contract of {self.hours} hours at {self.contractAmount}/hour"
        else :
            result += f"monthly salary of {self.contractAmount}"
            
        if self.commissionAmount:
            if self.contractNum:
                result += f" and receives a commission for {self.contractNum} contract(s) at {self.commissionAmount}/contract."
            else:
                result += f" and receives a bonus commission of {self.commissionAmount}."
        else :
            result += f"."
        result += f" Their total pay is {self.get_pay()}."

        return result
    

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, 0, 200, 4)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 600)
