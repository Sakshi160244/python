import numpy as np
arr = np.array([1,2,3,4,5])  # array in list
print(arr)
print(type(arr))
print(np.version)

arr1 = np.array((1,2,3,4,5,6,7,8))      # array in tuple
print(arr1)

arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
print(arr2)

## array in 1D, 2D, 3D
a=np.array(12)
print(a.ndim)
print(a)
b=np.array([1,2,3,4,5])
print(b.ndim)
print(b)
c=np.array([[1,2,3],[4,5,6]])
print(c.ndim)
print(c)
d=np.array([[[1,2,3,4],[5,6,7,8]],[[9,10,11,12],[13,14,15,16]]])
print(d.ndim)
print(d)