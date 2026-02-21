import numpy as np


def get_matrix(name):
    rows = int(input(f"Enter rows for Matrix {name}: "))
    cols = int(input(f"Enter cols for Matrix {name}: "))
    
    matrix = np.zeros((rows, cols))
    print(f"Enter elements for Matrix {name}:")
    
    for i in range(rows):
        for j in range(cols):
            matrix[i][j] = float(input(f"  [{i}][{j}]: "))
    return matrix



def multiply(A,B):
    if A.shape[1]!= B.shape[0]:
        print(f" Can't multiply! Columns of A ({A.shape[1]}) must equal rows of B ({B.shape[0]})")
        return None
    else:
        return np.dot(A,B)
    

    

A=get_matrix("A")
B=get_matrix("B")

result=multiply(A,B)
if result is not None:
    print("\nResult A x B:")
    print(result)



while True:
        again = input("\nDo you want to multiply again? (y/n): ")
        if again.lower()=="y":
             if result is None:
                  print("previous multiplication failed, can't multiply, Please restart the program.")
                  break
             C=get_matrix("C")
             result=multiply(result,C)

             if result is not None:
                  print("Chained multiply:")
                  print(result)
        elif again.lower()=="n":
             print("Final Result:")
             print(result)
             print("Goodbye!")
             break
        else:
            print("Invalid input! Try again!!")


