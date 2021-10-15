# def add(a, b):
#     return a + b


# def subtract(a, b):
#     return a - b


# def multiply(a, b):
#     return a * b


# def divide(a, b):
#     return a / b


# print("Select operation.")
# print("1.Add")
# print("2.Subtract")
# print("3.Multiply")
# print("4.Divide")

# while True:
    
#     choice = input("Enter choice(1/2/3/4): ")

    
#     if choice in ('1', '2', '3', '4'):
#         num1 = float(input("Enter first number: "))
#         num2 = float(input("Enter second number: "))

#         if choice == '1':
#             print(num1, "+", num2, "=", add(num1, num2))

#         elif choice == '2':
#             print(num1, "-", num2, "=", subtract(num1, num2))

#         elif choice == '3':
#             print(num1, "*", num2, "=", multiply(num1, num2))

#         elif choice == '4':
#             print(num1, "/", num2, "=", divide(num1, num2))
        
        
#         next_calculation = input("Let's do next calculation? (yes/no): ")
#         if next_calculation == "no":
#           break
    
#     else:
#         print("Операция не поддерживается")




# lst = [-1,-199,-19,-50,139,-100,-99]
# for number in lst:
#     if number != 0:
#         print(number, end=' ')
#     elif number == 139:
#         break



# def is_year_leap(year) :
#     return year % 4==0 and year % 100 !=0 or year % 400==0
# print(is_year_leap(2020))

# def square(a):
# 	p = 4*a
# 	s = a*a
# 	d = (a**2) / 2
# 	d = d**0.5
	
# 	k = (p, s, d)
	
# 	return k
	
# print(square(16))


# n = int(input())
# m = int(input())
# y = int(input())

# def bank(n, m, y):
#         nal = n
#         year = y
#         def money():
#             if year >0:
#                 nal = n*1.1+m
#                 year = year -1
#                 return money()
#             else:
#                 return nal

# print (100000)



# def season(month):
#     season={(12,1,2):'Zima',(3,4,5):'vesna',(6,7,8):'leto',(9,10,11):'OSEN',}
#     for key, Value in season.items():
#         if month in key :
#              season=Value
#              break
#     return season
    
# print(season(4))
  

# import random
# res=random.randrange(1,1000)
# print(res)



# def date(date,month,year):
#     if date >= 1 and date <= 31:
#         if month >= 1 and month <=12:
#             if year >= 1 and year <=9999:
#                 print(True)
#     else:
#         print(False)
        


