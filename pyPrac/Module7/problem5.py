# Problem5_Squares.py
# Baatyrbek Turatov
# June 18, 2024
# Problem 5: Print square pattern using loops.
def printSquares(n):
    for i in range(n):
        for j in range(n):
            print("*", end=" ")
        print()

printSquares(5)