# List methods
friend = ['John', 'Anne', 'Charlie', 3, 25.65, False, ]

l1 = [3, 5, 1, 2, 4]


# 1. List slicing - Get the specific range of elements from the list
#List slicing  work same as string slicing  
print(friend[2:5])  # Output: ['Charlie', 3, 25.65]



# 2. List length - Get the number of elements in the list
print(len(friend))  # Output: 6



# 3. List append - Add new element to the list
friend.append('Smith')
print(friend)  # Output: ['John', 'Anne', 'Charlie', 3, 25.65, False, 'Smith']



# 4. List insert - Add new element at specific index
friend.insert(1, 'Bob')
print(friend)  # Output: ['John', 'Bob', 'Anne', 'Charlie', 3, 25.65, False, 'Smith']



# 5. List remove - Remove element from the list
friend.remove('Bob')
print(friend)  # Output: ['John', 'Anne', 'Charlie', 3, 25.65, False, 'Smith']



# 6. List pop - Remove element from the list at specific index
value = friend.pop(4)
print(friend)  # Output: ['John', 'Anne', 'Charlie', 3, False, 'Smith']

# value will contain the removed element from the list
print(value)  # Output: 25.65 



# 7. List sort - Sort the list
l1.sort()
print(l1)  # Output: [1, 2, 3, 4, 5]



# 8. List reverse - Reverse the list
l1.reverse()
print(l1)  # Output: [5, 4, 3, 2, 1]



# 9. List copy - Copy the list
friend_copy = friend.copy()
print(friend_copy)  # Output: ['Rolf', 'Anne', 'Charlie', 3, False]



# 10. List extend - Add elements of one list to another list
friend.extend(friend_copy)
print(friend)  # Output: ['Rolf', 'Anne', 'Charlie', 3, False, 'Rolf', 'Anne', 'Charlie', 3, False]



# 11. List index - Get the index of the element
print(friend.index('Charlie'))  # Output: 2



# 12. List count - Get the number of times the element is present in the list
print(friend.count('Charlie'))  # Output: 2



# 13. List clear - Remove all elements from the list
friend.clear()
print(friend)  # Output: []



# 14. List delete - Delete the list completely
del friend
