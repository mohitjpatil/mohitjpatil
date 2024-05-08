n=10
m=5
result = 0
choise = int(input(" Enter Your Choise as per\n1. ADD\n2.Sub\n3.Mul\n4.Div\n So WHat is Your choise : "  ))
if choise==1:
  result= n + m
elif choise==2:
  result= n - m
elif choise==3:
  result= n * m
if choise==4:
  result= n / m
else:
  print("your are not selecting Correct option " )

print("THE RESULT IS : " , result)

            
