import numpy as np
import matplotlib.pyplot as plt
sp=float(input("enter sp:"))
sl=float(input("enter ss:"))
wp=float(input("enter wp:"))
ws=float(input("enter ws:"))
t=(1/sp**2)-1
q=(1/sl**2)-1
a=t/q
h=(wp/ws)
r=np.log10(h)
y=np.log10(a)
n=0.5*(y/r)
N=np.ceil(n)
x=0.5*(1/N)
wc=(wp/(t)**x)
print N
print wc
w=np.arange(0,1000,1)
j=[]
for w in range(1000):
	u=(w/wc)**(2*N)
	o=1+u
	e=(1/(o)**(0.5))
	j.append(e)
plt.plot(j)
plt.show()
