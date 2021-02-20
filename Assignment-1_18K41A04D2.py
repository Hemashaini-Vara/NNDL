#!/usr/bin/env python
# coding: utf-8

# In[106]:


from sympy import *
x = Symbol('x')
f = x**4+3*x**2+10
n=-0.001
itr=1000
i=0
fd = f.diff(x)
f = lambdify(x, f)
fd= lambdify(x, fd)


# In[107]:


y=10
while i<itr:
    y=y+(n*fd(y))
    i=i+1
else:
    f=int(f(y))
    y=int(y)
    print("Minimum value of f(x)= "+str(f)+" at x= "+str(y))

