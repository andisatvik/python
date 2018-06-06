#One line code for compressing a list to show only even numbers

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

even_list = [even for even in a if(even%2==0) ]

print(even_list)

