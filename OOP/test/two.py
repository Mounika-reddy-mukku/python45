class Account:
    min_Bal=500
    def open_acc(self):
        self.acc_bal=500
        self.a="Mounika"
    def depost(cls):
        cls.ammount=876
a1=Account()
a2=Account()
a1.open_acc()
a2.depost()
print(a1.__dict__)
print(a2.__dict__)
print(Account.__dict__)