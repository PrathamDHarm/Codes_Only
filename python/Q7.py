list_a = [1, 2, 3, 4, 5]
class IndexError(Exception):
    def __init__(self, value):
        self.value = value
try:
    n = int(input("enter a index to print the list elements: "))
    if (n >= -5) and (n <= 4):
        print(list_a[n])
    else:
        raise IndexError("The index is incorrect and index should lie between -5 and 4.")
except ValueError:
    print("Use an Integer value as the input.")
