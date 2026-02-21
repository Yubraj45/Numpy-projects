import numpy as np


# array = np.array([
#     [['A','B','C'], ['D','E','F'], ['G','H','I']],
#     [['J','K','L'], ['M','N','O'], ['P','Q','R']],
#     [['S','T','U'], ['V','W','X'], ['Y','Z',' ']]
# ])

# word= array[0,1,2]+ array[2,0,2]+array[0,0,2]+array[1,0,1]
# print(word)

# SLICING

# array = np.array([[1, 2, 3, 4],
#                   [5, 6, 7, 8],
#                   [9, 10, 11, 12],
#                   [13, 14, 15, 16]])

# array[start:end:step]

# print(array[::-2])

# column selection
# print(array[:,::-2])


# row and column selection at the same time
# print(array[0:2,0:2])
# print(array[2:,:2])


# SCALAR ARITHMETIC
# array=np.array([1,2,3])
# print(array+1)
# print(array-2)
# print(array*3)
# print(array/4)
# print(array**5)


# VECTOR ARITHMETIC
# array=np.array([1.01,2.2,3.23])

# print(np.round(array))
# print(np.ceil(array))
# print(np.floor(array))
# print(np.pi)


# VECTORIZED MATH FUNCTION
# radii = np.array([1, 2, 3])

# print(np.round(np.pi * radii**2))




#ELEMENT-WISE ARITHMETIC
# array1=np.array([1,2,3])
# array2=np.array([4,5,6])

# print(array1+array2)
# print(array1-array2)
# print(array1*array2)
# print(array1/array2)
# print(array1**array2)





#COMPARISON OPERATOR

# scores= np.array([91,55,100,73,82,64])

# scores[scores<60]=0

# print(scores)









#BROADCASTING

# array1=np.array([[1,2,3,4],
#                  [5,6,7,8],
#                  [9,10,11,12],
#                  [13,14,15,16]])
# array2=np.array([[1,2],[2,3],[3,4],[4]])

# print(array1.shape)
# print(array2.shape)

# print(array1*array2)







# array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
# array2=np.array([[1],[2],[3],[4],[5],[6],[7],[8],[9],[10]])

# print(array1.shape)
# print(array2.shape)

# print(array1*array2)









#AGGREGATE FUNCTION
#---> SUMMERIZE DATA AND TYPICALLY RETURN A SINGLE VALUE

# array=np.array([[1,2,3,4,5],
#                 [6,7,8,9,10]])


# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))
# print(np.var(array))
# print(np.min(array))
# print(np.max(array))

# print(np.argmin(array))#-->gives the position of the minimum value 
# print(np.argmax(array))#-->gives the position of the maximum value 




# print(np.sum(array,axis=0))#---> for adding the column values
# print(np.sum(array,axis=1))#---> for adding the row values








# FILTERING
#--> refers to the process of selecting elements from an array that match a given condition

# ages=np.array([[21,17,19,20,16,30,18,65],
#                [39,22,15,99,18,19,20,21]])

# teenagers= ages[ages<18]
# adults=ages[(ages>=18) & (ages<65)]
# seniors=ages[ages>=65]
# evens=ages[ages%2==0]
# odds=ages[ages%2!=0]

# print(odds)
# print(evens)
# print(seniors)
# print(teenagers)
# print(adults)


# for preservng the original shape of the array even after filtering 
# -->using where
# adults=np.where(ages >=18,ages,0)
# print(adults)






# random number
# rng= np.random.default_rng()#we can also guve seed which will give the same random choice, number.

# # print(rng.integers(1,7))
# #or we can use this also , they are the same just writing low and high      and also the high value is exclusive
# print(rng.integers(low=1,high=101,size=3))


# forseed
# np.random.seed(seed=1)

# print(np.random.uniform(-1,1,size=(3,2)))













#SHUFFELING AN ARRAY
# rng=np.random.default_rng()

# array=np.array([1,2,3,4,5])

# rng.shuffle(array)
# print(array)


# for random choice
rng=np.random.default_rng()

fruits=np.array(["apple","orange","banana","coconut","pineapple"])

fruit=rng.choice(fruits,size=(3,3))

print(fruit)