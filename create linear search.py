# creating liner search programm using python
linear search in array
array=[]
n=int(input("total elments in array"))
print("enter the elements")
i=1
# here we use while loop and also append element in array
while(i<=n):
    e=int(input("enter the roll no"))
    array.append(e)
    i+=1
    array.sort()
print(array)

search_element=int(input("enter the element that you want to search"))

# function for linear serach
def linear_search():
    for i in range(len(array)):
        if array[i]==search_element:
            print("element found")
    else:
        print("Sorry element not found")
linear_search()
