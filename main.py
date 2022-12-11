# try:
#     Number1 = (int(input("Enter the Number: ")))                 #Task 1
#     operator = input("+,-,/,*,**,%,//")
#     Number2 = (int(input("Enter The Number: ")))
#
#     if operator == "+":
#         print(Number1 + Number2)
#     elif operator == "-":
#         print(Number1 - Number2)
#     elif operator == "/":
#         print(Number1 / Number2)
#     elif operator == "*":
#         print(Number1 * Number2)
#     elif operator == "**":
#         print(Number1 ** Number2)
#     elif operator == "%":
#         print(Number1 % Number2)
#     elif operator == "//":
#         print(Number1 // Number2)
#
#     else:
#         print("Error: Operator is Invalid")
#
# except ZeroDivisionError:
#     print("∞")
# except ValueError:
#     print("Error: Number is not integer")











#Task 2
# number1 = int(input("Enter Six Digit Number: "))





try:
  month_number = int(input("Enter Month Number: ")) #Task 2
  if month_number == 12:
      print("Winter")
  elif month_number == 1:
     print("Winter")
  elif month_number == 2:
    print("Winter")
  elif month_number == 3:
    print("Spring")
  elif month_number == 4:
     print("Spirng")
  elif month_number == 5:
     print("Spring")
  elif month_number == 6:
     print("Summer")
  elif month_number == 7:
     print("Summer")
  elif month_number == 8:
     print("Summer")
  elif month_number == 9:
     print("Autumn")
  elif month_number == 10:
     print("Autumn")
  elif month_number == 11:
     print("Autumn")
  else:
     print("Error")
except ValueError:
  print("Error: The number should be an integer")