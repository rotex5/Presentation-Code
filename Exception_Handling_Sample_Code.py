a = 10
b = 2

try:
    print("RESOURCE OPEN")
    print(a/b)

    k = int(input("Enter a number: "))
    print(k)
    
except ZeroDivisionError as e:
    print("Hey, You cannot divide a Number by Zero", e)

except ValueError as e:
    print("Invalid Input")

except Exception as e:
    print("Something went Wrong...")

finally:
    print("RESOURCE CLOSED")
