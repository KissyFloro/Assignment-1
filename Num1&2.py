# Number 1 and 2
import matplotlib.pyplot as plt
ans1 = []
ans2 = []

for i in range (-10,10,1):
    x1 = (i**2)-10
    x2 = (i**3)+ i -100
    ans1.append(x1)
    ans2.append(x2)
    print(ans1)
    print(ans2)
   
plt.plot(ans1, label = "Equation 1")
plt.plot(ans2, color='y', label = 'Equation 2')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of x^2 - 10 and x^3 + x - 100')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()
