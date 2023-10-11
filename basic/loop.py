# product_name = ['p1','p2','p3','p4','p5','p6']
# product_name_size = len(product_name)
# # print(product_name[0])

# # for i in range(product_name_size): #start=0, i<5, step = 1 = i=i+1
# #     print(i,product_name[i]) #product_name[0], #product_name[1], #product_name[2]


# dict1 = {"name":"salman","roll":16}

# # for i in product_name: 
# #     print(i) 


# for i in dict1.items(): 
#     print(i) 

list1 = []

num = int(input("how many values you want to keep in your list: "))

for i in range(num):
    x = int(input("give your list value: "))
    list1.append(x)

sum = 1
for i in list1:
    sum = sum*i 
print(sum)

if(sum%2==0):
    print("The value is even")

else:
    print("The value is odd")




print(list1)