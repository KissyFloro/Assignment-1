# Number 3 
import matplotlib.pyplot as plt
ans3 = []

for i in range (-10,10,1):
    x3 = (i**10)-(i**8)+(i**2)-8
    ans3.append(x3)
   
plt.plot(ans3, color = 'r', label = 'Equation 3')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of x^10 - x^8 + x^2 - 8')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
