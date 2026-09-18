'''
SEP17 PYTHON CLASS
#if the same above BMI scenario we want it to be repeated for specific number
#of items
#repitation statements---> for,while

print("---BMI calculation---")
for i in range(5):
        weight =int(input("enter the weight in kgs:"))
        height =float(input("enter the height in meters:"))
        name = input("enter the name")
        if weight>0 and height>0:
            bmi=(weight/(height)**2)
            if bmi<18.5:
                 print(f'bmi of {name} is {bmi}and you are underweight-->eat well')
            elif bmi>=18.5 and bmi<=24.9:
                print(f'BMI of {name} is {bmi}and you are healty-->keep consistent')
            elif bmi>=25 and bmi<=29.9:
                print(f'BMI of {name} is {bmi}and you are overweight-->star exercising')
            elif bmi>=30:
                print(f'BMI of {name} is ( in obese category and bmi is {bmi}')
        else:
            print("do enter only +ve value greater than0")

#store the name,weight and height in a dictionary/lists
#in this case we want 5 iterations to be happened

print("---BMI calculation---")
details ={'names':[],
          'weights':[],
          'height':[]}
n = int(input("enter how many times you want to repeat:"))
for i in range(n):
    weight =int(input("enter the weight in kgs:"))
    details['weights'].append(weight)
    height =float(input("enter the height in meters:"))
    details['heights'].append(height)
    name = input("enter the name")
    details['names'].append(name)
    if weight>0 and height>0:
        bmi=(weight/(height)**2)
        if bmi<18.5:
          print(f'bmi of {name} is {bmi}and you are underweight-->eat well')
        elif bmi>=18.5 and bmi<=24.9:
            print(f'BMI of {name} is {bmi}and you are healty-->keep consistent')
        elif bmi>=25 and bmi<=29.9:
            print(f'BMI of {name} is {bmi}and you are overweight-->star exercising')
        elif bmi>=30:
                print(f'BMI of {name} is ( in obese category and bmi is {bmi}')
        else:
            print("make sure to enter only +ve values and must greaterthan 0")
        print(details)

#exception handling-->
#exception handiling is a mechanism to a program which responds to run time
#errors or compilations

#simple senario to understand the excepction

a,b = map(int,input("enter the value").split('.'))
try:
    result =a/b
    print(result)
except exception as e:
     print("find it")
#same above case accept inputs in try block
try:
  a,b = map(int,input("enter the values").split(','))
  result =a/b
  print(result)
except exception as e:
     print("find it")
     print(e)
 
# in above case we will get Value Error, ZeroDivisionError...
#possible types of errors -->TypeError,ValueError,NameError,
#IndexError,ZeroDivisionError,AttributeError,ArthimeticError..

try:
 a,b = map(int,input("enter the values").split(','))
 result =a/b
 print(result)
except ValueError:
    print("Bossu sairigaa chusi enter cheyyu only integers")
except ZeroDivisionError:
    print("make sure to give denominator greater than zero")
except NameError:
    print("please first understand the syntax and be good at spellings")
except AttributeError:
     print("please check the methods/functions names properly")
finally:
    print("its done now you have understood exception handling")

task:grade check

marks =int(input("enter your marks:"))
if marks<0 or marks>100:
    print("Invalid marks entered")
elif marks>=90:
    print("Grade: A")
    print("Remark: Outstanding marks")
elif marks>=80:
    print("Grade: B")
    print("Remark:excellent marks")
elif marks>=70:
    print("Grade: c")
    print("Remark:good marks")
elif marks>=60:
    print("Grade: D")
    print("Remark:fair,needs improvement")
elif marks>=50:
    print("Grade:E")
    print("Remark:poor, needs serious improvement")
else:
    print("Grade: F")
    print("Remark:failed,needs improvement")

2.even-odd checker

num=int(input("enter a number:"))
if num == 0:
  print("Zero is neither even or odd")
elif num < 0 and num %2==0:
 print("negitive even number")
elif num< 0 and num %2!=0:
 print( "negative  odd number")
elif num%2==0:
    print("even number")
else:
    print("odd numbers")
3.season identifier
'''
month =int(input("enter a month number:"))
if month ==12 or month ==1 or month ==2:
    print("season: winter")
elif month ==3 or month ==4 or month ==5:
    print("season: spring")
elif month ==6 or month ==7 or month ==8:
    print("season: summer")
elif month ==9 or month ==10 or month ==11:
    print("season: antunum")
else:
    print("invalid month`entered")




 


    
              








                  
