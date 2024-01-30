# Function to demonstrate printing pattern:
def pypart(n):
    # Outer loop to handle the number of rows
    for i in range(0, n):
        #Inner loop to handle the number of columns:
        for j in range(0, i+1):
            print("* ", end="")
        print("\r")
n = int(input("Enter the number of rows needed: "))
pypart(n)