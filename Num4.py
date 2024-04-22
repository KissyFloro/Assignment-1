# Number 4
import matplotlib.pyplot as plt
ans4 = []

for i in range (-10,10,1):
    x4 = (i**4)+(i**3)+(i**2)+(i)+1
    ans4.append(x4)
    print(ans4)
   
   
plt.plot(ans4, color='g',  label='Equation 4')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of x^4 + x^3 + x^2 + x + 1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
