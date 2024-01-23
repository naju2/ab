import numpy
import timeit

s= int(input("Enter the size of the room : "))

# initializing the arrar
arr= numpy.random.choice([0,1], size = (s,s))      

# initial array
print(arr)
print()
# variable to count rooms
count=0     

# cleaning the room
start = timeit.default_timer()
for a in range(s):
    for b in range(s):
        if arr[a][b]==1:
            count+=1
            arr[a][b]=0
end = timeit.default_timer()

# printing the final array
print(arr)
print()
# time calculated in micro-seconds
time_taken = (end-start)*(10**6)
print("Time taken : {0:.4f} ".format(time_taken)) 
print("Total rooms cleared : ",count)            

# calculating performance
prf = (count/(s*s))*100
print("Performance : {0} %".format(prf))


