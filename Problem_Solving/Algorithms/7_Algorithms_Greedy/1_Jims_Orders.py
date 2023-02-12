
#* Jim's Burgers has a line of hungry customers. Orders vary in the time it takes to prepare them.
#* Determine the order the customers receive their orders. Start by numbering each of the customers
#* from 1 to n, front of the line to the back. You will then be given an order number and a preparation
#* time for each customer. 
#* The time of delivery is calculated as the sum of the order number and the preparation time. If two
#* orders are delivered at the same time, assume they are delivered in ascending customer number order.


#? How I solved it initially:
# [5, 16] means that their order number is 5 and preparation time is 16
a = [
    [1,8], # 9
    [3,4], # 7
    [5,16], # 21
    [6, 1] # 7
]

def jimOrders(orders):
    counter = 1
    order_received = []
    for element in orders:
        element.insert(0,counter)
        counter += 1
    sorted_orders = sorted(
        orders,
        key= lambda x: ((x[1] + x[2]), x[0]) # sort by (order no. + prep time, customer no.)
    )
    for element in sorted_orders:
        order_received.append(element[0])
    return order_received

# print(jimOrders(a))
# [2, 4, 1, 3]


#? The return statement below is adjusted to use list comprehension for a
#? one line way to get the first element from each list triplet

#? sorted_orders = [
#? [2, 3, 4],
#? [4, 6, 1],
#? [1, 1, 8],
#? [3, 5, 16]
#? ]

#* syntax: newlist = ['expression' for 'item' in 'iterable' if 'condition == True']

def jimOrders_listcomprehension(orders):
    counter = 1
    for element in orders:
        element.insert(0,counter)
        counter += 1
    sorted_orders = sorted(
        orders,
        key= lambda x: ((x[1] + x[2]), x[0]) # sort by (order no. + prep time, customer no.)
    )
    return [order[0] for order in sorted_orders]

# print(jimOrders_listcomprehension(a))
# [2, 4, 1, 3]


#? Below is how to access elements after you enumerate them

def accessing_enum(orders):
    orders = enumerate(orders, start=0)
    for i, order in orders:
        print(i, order)

# accessing_enum(a)
# 0 [1, 8]
# 1 [3, 4]
# 2 [5, 16]
# 3 [6, 1]

#? Alternative way to access enumerated elements by converting to list
#? so that you can iterate multiple times
#! You cannot iterate the enumerate object itself multiple times
#! This is because it can only be iterated once, and it is used up when
#! you call the object (iterate for the first time)
# https://stackoverflow.com/questions/64698188/enumerate-object-is-empty-after-converting-to-a-list

def also_accessing_enum(orders):
    orders = list(enumerate(orders, start=0))
    print(orders)

# also_accessing_enum(a)
# [(0, [1, 8]), (1, [3, 4]), (2, [5, 16]), (3, [6, 1])]

#? Below is a shorter, more complex method to get the answer
#? Using list(enumerate()) and list comprehension



b = [
    [8, 1],
    [4, 2],
    [5, 6],
    [3, 1],
    [4, 3]
]

def jimOrders_enum(orders):
    orders = list(enumerate(orders, start=1))
    orders.sort(key= lambda x: sum(x[1]))
    return [order[0] for order in orders]


# print(jimOrders_enum(b))
# [4, 2, 5, 1, 3]