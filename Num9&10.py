# Number 9
import matplotlib.pyplot as plt
ans9 = []
ans10 = []


for i in range (-10,10,1):
    if i !=0:
     x9 = (((i**3)/ 2*i)-10*i)
     x10 = ((i+2)*(i+3)*(i-4))
     ans9.append(x9)
    ans10.append(x10)
    print(ans9)
    print(ans10)
  

plt.plot(ans9, color = 'magenta', label= 'Equation 9')
plt.plot(ans10, color = 'cyan', label= 'Equation 10')
plt.axhline(y=0, color='k')
plt.axvline(x=0, color='k')
plt.title('Graph of (x^3 / (2x)) - 10x and f(x)= (x+2)(x+3)(x-4)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()


