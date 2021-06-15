
class Bank_account :
    def __init__(self,name, phone_number):
            self.name=name
            self.balance=0
            self.phone_number=phone_number
            self.loan=loan
            self.statement=[]
            self.loan=0

    def show_balance(self):
         return f"Hello this is my {self.balance}"   
    def withdraw(self,amount):
        return self.show_balance()    

    def borrow_loan(self,amount):

        return f"congratulation you have borrowed {amount}"
        try:
            10 + amount
        except TypeError:
           return f"the amount must be in figure" 
    def repay_loan(self,amount):
           return f"You have  repaid {amount}" 
    def show_statement(self):
           amount=transacation["amount"]
           narration=transacation["narration"]
           time=transacation["time"]
           date=time.strftime["%d/%m/%y"]
           date=time.strftime("%d/%m/%y") 
           print( f"{date}:{narration} {amount}")
           return
    def borrow(self,amount):
        try:
            10 + amount
        except TypeError:
            return f"the amount must be in figure"     
        if amount < 0:
            return f"you have no outstanding loan { self.amount}"
        elif self.loan>0:
            return f"You have reach the limit borrowing loan {self.amount}"
        elif amount<0.1 *self. balance:
            return f"you did qualify for the loan of ksh{amount}"
        else:
            loan=amount*1.05
            self.loan=loan 
            self.balance +=amount
            return f"your  outstanding loan is{self.loan}"
    def repay_loan(self,amount):
        try:
            20+=amount
            except TypeErrow:
                return f"commfirm you clear the amount"
        if amount < 0:
            return f"you cannot repay with that "
        elif amount > self.loan:
            return f"you repay the loan with decrease {self.amount}"

        elif amount < self.loan:
            self.loan-=amount
            return f"you have successful repaid {self.loan}"
        else:
            diff=amount-self .loan
            self ._loan=0 
            self .deposit(diff)
            now=datetime.now()
            transaction={

            }
            self.statement.append(transaction)
            return self.show_balance()

    def show_statement(self):
            for transacation in self.statement:
                amount= transacation["amount"]
                narration=transacation["narration"]
                time=transacation["time"]
                date=time.strftime("%d/%m/%y") 
                print( f"{date}:{narration} {amount}")
                class Account:

class   MobilemoneyAccount (Account):
    def __init__(self,name,phone_number,sevrice_provider):
             Account.__init__(name,phone_number)
             self.service_provider=sevrice_provider
    def buyAirtime(self,amount):
            try:
                 5+amount
            except TypeError:
                return f"hello write in fugure"
            if amount<0:
                return f"hello{self.name} you balance{amount}"
            elif self.balance<amount:
                return f"dear customer your amount is low"
            else:
             self.balance-=amount
            return f"dear customer you have bought airtime for {amount}"
            self,name,phone_number,sevrice_provider):
            Account.__init__(name,phone_number)
            self.service_provider=sevrice_provider
def buyAirtime(self,amount):
            try:
                 5+amount
            except TypeError:
                return f"hello write in figure"
            if amount<0:
                return f"hello{self.name} you balance{amount}"
            elif self.balance<amount:
                return f"dear customer your amount is low"
            else:
             self.balance-=amount
            return f"dear customer you have bought airtime for {amount}"













