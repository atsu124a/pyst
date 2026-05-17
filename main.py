#def fizz_buzz(num):
#
 #   if num % 3 == 0 and num % 5 == 0:
 #       return "FizzBuzz"
 #   elif num % 3 == 0:
 #       return "Fizz"
 #   elif num % 5 == 0:
 #       return "Buzz"
 #   else:
 #       return str(num)
    
#print(fizz_buzz(int(input ("自然数を入力してください: "))))


def fizz_buzz(n, x, y):
   if n % x == 0 and n % y == 0:
       return "FizzBuzz"
   elif n % x == 0:
       return "Fizz"
   elif n % y == 0:
       return "Buzz"
   else:
       return str(n)  
print(fizz_buzz(int(input("nを入力してください: ")), int(input("xを入力してください: ")), int(input("yを入力してください: "))))