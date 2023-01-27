t_1 = (1,4,9,16,25,36)
t_m=[]
for i in range(0,len(t_1)):
     x=pow(t_i[i],2)
     t_m.append(x)
     t_modified=tuple(t_m)
print("t_1: ",t_1)
print("t_modified: ",t_modified)
print("Element at index 4 of t_modified: ", t_modified[4])
t_sliced=t_modified[1:4]
print("t_sliced: ",t_sliced)
