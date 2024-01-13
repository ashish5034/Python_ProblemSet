# accept number from user and display such elements which are even and divisible by 5
evenno = lambda no :(no%2==0)
divby5 = lambda no :(no%5==0)
data = []
print(f"Enter size of list {data}")
size = int(input())

for val in range(size):
    val =int(input())
    data.append(val)
print(data)

evenvalues = list(filter(evenno, data))
print(evenvalues)

div = list(filter(divby5,evenvalues))
print(div)