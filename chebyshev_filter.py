import numpy as np
import matplotlib.pyplot as plt
wp=float(input("enter wp:"))
sp=float(input("enter sp:"))
sl=float(input("enter ss:"))
ws=float(input("enter ws:"))
b=((1/(sp)**2)-1)**0.5
h=((1/(sl)**2)-1)**0.5
e=b
p=np.arccosh((h/b))
u=np.arccosh((ws/wp))
N=(p/u)
print "N value is:",N
print e
w=np.arange(0,10000)
j=[]
q=[]
for w in range(10000):
	o=1/(1+(e**2)*(np.cosh(N*(np.arccosh(w/wp))))**2)**0.5
	j.append(o)
for w in range(10000):
	f=1/(1+(e**2)*(np.cos(N*(np.arccos(w/wp))))**2)**0.5
	q.append(f)
plt.plot(j)
plt.plot(q)
plt.show()
