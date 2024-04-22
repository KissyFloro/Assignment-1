# Number 5
import matplotlib.pyplot as plt
import math
ans5 = []
ans6 = []

for i in range (-10,10,1):
    if i !=0:
     x5 = ((i**2)+i+10)/ (2*i)
     x6 = ((math.sin(i)) / (3*i))
     ans6.append(x6)
     ans5.append(x5)
     print(ans5)
     print(ans6)
  
  
plt.plot(ans5, color = 'pink', label= 'Equation 5')
plt.plot(ans6, color = 'purple', label= 'Equation 6')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of (x^2 + x + 10) / (2x) and Sin(x)/ (3x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

   
