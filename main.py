#Bank System

BALANCE = float(round(0.00, 2))

def Check_balance(BALANCE):
  print(f"***************************\nBalance amount: R {BALANCE}\n***************************")
  return BALANCE 


def Withdraw_balance(BALANCE):
  Withdraw_amount = float(input("Enter Withdrawal Amount :"))
  if Withdraw_amount > BALANCE:
    print("!!Insufficient Funds!!")
  else:
    BALANCE -= Withdraw_amount
    print(f"Successfully withdrew R {Withdraw_amount}.")
  return BALANCE


def Deposit_balance(BALANCE):
  Deposit_amount = float(input("Enter Deposit Amount :"))
  if Deposit_amount <= 0:
    print("!!Insufficient Funds!!")
  else:
    BALANCE += Deposit_amount
    print(f"Deposited Amount R :{BALANCE}")
  return BALANCE

while True:
  print("***************************")
  print("***Bank System Options*****")
  print("***************************")
  print("1) Check Balance")
  print("2) Withdraw Balance")
  print("3) Deposit Balance")
  print("4) Exit")
  print("***************************")
  User_input = input("Enter Your Banking Option :")
  print("***************************")

  

  if User_input == '1':
    BALANCE = Check_balance(BALANCE)
  elif User_input == '2':
    BALANCE = Withdraw_balance(BALANCE)
  elif User_input == '3':
    BALANCE = Deposit_balance(BALANCE)
  elif User_input == '4':
    print()
    print("!!THANK YOU FOR USING OUR SYSTEM!!")
    break
  else:
    print("!!Invalid Choice!!")
    continue

  