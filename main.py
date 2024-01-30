import random
import numpy as np
a = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a)

b = np.array((0, 1, 2, 3, 4, 5, 6, 7, 8, 9))
print(b)

c = np.arange(10)
print(c)

print('----------------------------------')
d = np.arange(2, 10, 2)
print(d)
print(d.ndim) #кол-во измерений
print(d.shape) #кол-во элементов в каждом измерении
print(d.size) #общее кол-во элементов
print(d.dtype) #определение типа массива
print(d.itemsize) #определяет размер в байтах одного символа
print(d.nbytes) #общий размер массива
print(d.size * d.itemsize)
print('----------------------------------')

#e = list(range(2, 5.5, 0.5))
#print(e)

e = np.arange(2, 5.5, 0.5)
print(e)

f = np.array([1, 2, 3, 4, 5], float)
print(f)
print(f.dtype)

g = np.array(42)
print(g)
print(d.ndim)
print(d.shape)
print(d.size)

h = np.array([[1, 2, 3], [4, 5, 6]])
print(h)

i = np.arange(12).reshape(2, 2, 3)
print(i)
print(i.ndim)
print(i.shape)
print(i.size)

j = np.zeros(5)
print(j)

k = np.zeros((2, 3))
print(k)

l = np.ones((2, 2, 3))
print(l)

m = np.full((2, 3), 4)
print(m)

p = np.empty((3, 2))
print(p)