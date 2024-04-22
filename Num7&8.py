# Number 7
import matplotlib.pyplot as plt
import math
ans7 = []
ans8 = []

for i in range (-10,10,1):
    if i !=0:
     x7 = (((i**3))+(2*i**2))-(10*i)+3
     x8 = ((math.cos(i)/ (5*i)))
     ans7.append(x7)
     ans8.append(x8)
     print(ans7)
     print(ans8)
  
   
plt.plot(ans7, color = 'orange', label= 'Equation 7')
plt.plot(ans8, color = 'indigo', label= 'Equation 8')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of x^3+2x^2-10x+3 and Cos(x)/ 5x')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
