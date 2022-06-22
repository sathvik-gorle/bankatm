class Atm(object):
   def __init__(self, cardnum, pinnum, balance):
      self.CardNumber = cardnum
      self.PinNumber = pinnum
      self.Balance = int(balance)
   def CashWithdrawal(self, amt):
      self.Balance = self.Balance-int(amt)
      print("Cash Withdrawn!\nAmount Withdrawn = ", amt, "\n Thank You!")
   def BalanceEnquiry(self):
      print("Your Bank Balance = ", self.Balance, ". Thank You!")

def main():
   card = input("Kindly enter your card number: ")
   pin = input("Kindly enter your pin number: ")
   bal = input("Kindly enter your balance: ")
   obj = Atm(card, pin, bal)
   withdraw = input("Would you like to withdraw money? (Y/N)")
   if withdraw=="Y":
      a = int(input("How much money would you like to withdraw? "))
      obj.CashWithdrawal(a)
   b = input("Would you like to check your bank balance? (Y/N)")
   if b=="Y":
      obj.BalanceEnquiry()

main()