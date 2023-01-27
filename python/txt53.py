list_a=['car','place','tree','under','grass','price']
list_b=[]
def remove_items_containing_a_or_A ():
    for i in range(len(list_a)):
       if ('a' in list_a[i])or ('A' in list_a[i]):
           list_b.append(list_a[i])
remove_items_containing_a_or_A()
def index(list_a,list_b):
    result = list(filter(lambda x:x not in list_b,list_a))
    return result
print(index(list_a,list_b)) 