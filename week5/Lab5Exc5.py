size = int(input("Size: "))

# size = 5
#     *     5 space -> 1 star
#    * *    4 space -> 1 star -> 1 space -> 1 star 
#   * * *   3 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star
#  * * * *  2 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star
# * * * * * 1 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star
#  * * * *  2 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star
#   * * *   3 space -> 1 star -> 1 space -> 1 star -> 1 space -> 1 star
#    * *    4 space -> 1 star -> 1 space -> 1 star 
#     *     5 space -> 1 star


for i in range(size):
    print((size-i)*" ", end="") #print space
    print("* "*(i+1)) #print star and space
for j in range(size-2, -1, -1):
    print(" " * (size - j), end="")
    print("* " * (j + 1))