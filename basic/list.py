product_name = ['p1','p2','p3','p4','p5','p6']

product_name2 = ['a9','p10','p11','p12','p13','p14']

size = len(product_name)

print("Before Append",product_name)

product_name.append('p7')

print("After Append",product_name)

product_name.insert(2,'p8')

print("After Insert",product_name)

p  = product_name.copy()

print(p)

count_p = product_name.count('p1')

print(count_p)

product_name.extend(product_name2)

print(product_name)

x = product_name.index('p2')

print(x)

product_name.pop(1)

product_name.remove("p8")

product_name.reverse()

print(product_name)

product_name.sort()

print(product_name)

