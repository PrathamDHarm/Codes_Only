def remove_items_containing_a_or_A(list_a):
    for i in range(len(list_a)):
       if ('a' in list_a[i])or ('A' in list_a[i]):
           list_b.append(list_a[i])
    result = list(filter(lambda x:x not in list_b,list_a))
    return result
list_a=['car','place','tree','under','grass','price']
list_b=[]    
print(remove_items_containing_a_or_A(list_a))
 
