# *args
# **kwargs

# def emp(name,sal,dept,*address):
#     print(name)
#     print(sal)
#     print(dept)
#     print(address)
#
# emp('Ram',25000,'IT','Delhi')
# emp('Ram',25000,'IT','Delhi','Pune')
# emp('Ram',25000,'IT','Delhi','Pune','Noida')

def add(*x):
    # print(sum(x))
    count = 0
    for i in range(len(x)):
        count += x[i]
    print(count)

add(2,3,4,5)
add(6,8,3,54,7,87)
add(2,3)
