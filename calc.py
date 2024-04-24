def add(x, y):
  return x + y


def subtract(x, y):
  return x - y


def multiply(x, y):
  return x * y


def divide(x, y):
  return x / y


def floor(x, y):
  return x // y


def expo(x, y):
  return x**y


def modulo(x, y):
  return x % y


# to run the loop till we want to exit
while True:

  print("Select operation.")
  print("Calculator Menu")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Floor")
  print("6.Exponent")
  print("7.Modulo")
  print("0.Exit")

  # choice to choose the operation to perform.
  choice = input("Enter choice : ")
  # if choice is 0 then exit the loop
  if choice == '0':
    print("Exiting...")
    break
  # if choice is not 0 then take input from user
  elif choice in ('1', '2', '3', '4', '5', '6', '7'):
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if choice == '1':
      print("Result", add(num1, num2), end=" new start \n\n")
    elif choice == '2':
      print("Result", subtract(num1, num2), end=" new start \n\n")
    elif choice == '3':
      print("Result", multiply(num1, num2), end=" new start \n\n")
    elif choice == '4':
      print("Result", divide(num1, num2), end=" new start \n\n")
    elif choice == '5':
      print("Result", floor(num1, num2), end=" new start \n\n")
    elif choice == '6':
      print("Result", expo(num1, num2), end=" new start \n\n")
    elif choice == '7':
      print("Result", modulo(num1, num2), end=" new start \n\n")
  else:
    print("Invalid choice. Please enter a valid choice.")
