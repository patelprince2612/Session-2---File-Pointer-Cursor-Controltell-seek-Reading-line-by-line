# 1. Create a Python script that opens a file called lyrics.txt and prints the file pointer's current position using tell() before and after reading the first 10 characters.
file = open('lyrics.txt', 'r')
print(file.tell())
file.read(10)
print(file.tell())
file.close()

# 2. Write a function read_next_line(filename) that opens a file, moves the file pointer to the 20th byte using seek(), and prints the next line from that position. Hint: Use seek(20) before calling readline().
def read_next_line(filename):
    file = open(filename, 'r')
    file.seek(20)
    print(file.readline().strip())
    file.close()

# 3. Simulate a Zomato-style order history: create a file orders.txt with at least 5 lines (each line is an order). Write a script that reads and prints each order line-by-line using a loop, and after reading each line, prints the file pointer's position using tell().
file = open('orders.txt', 'w')
file.write("Pizza\nBurger\nPasta\nFries\nCoke\n")
file.close()

file = open('orders.txt', 'r')
for line in file:
    print(line.strip())
    print(file.tell())
file.close()

# 4. Given a file called playlist.txt containing song names (one per line), write code to jump to the start of the third song using seek() and readline(), then print only that song's name. Constraint: Do not read the whole file into memory at once.
file = open('playlist.txt', 'r')
file.readline()
file.readline()
print(file.readline().strip())
file.close()