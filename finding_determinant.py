def cal_det(n, matrix):
    na = n-1
    if n==1:
        return matrix[0][0]
    elif n==2:
        return (matrix[0][0]*matrix[1][1])-(matrix[0][1]*matrix[1][0])
    elif n>=3:
        det_a = 0
        for j in range(0, n):
            minor = []
            for t in range(n):
                minor.append([])
                for h in range(n):
                    minor[t].append(matrix[t][h])
            for k in range(1, len(minor)):
                del minor[k][j]
            del minor[0]
            cofactor = ((-1)**(1+1+j))*(cal_det(na, minor))
            det_a += cofactor*matrix[0][j]

        det_b = 0
        for j in range(0, n):
            minor = []
            for t in range(n):
                minor.append([])
                for h in range(n):
                    minor[t].append(matrix[t][h])
            for k in range(len(minor)):
                del minor[k][0]
            del minor[j]
            cofactor = ((-1)**(1+1+j))*(cal_det(na, minor))
            det_b += cofactor*matrix[j][0]

        if det_a == det_b:
            return det_a

    else:
        return "Matrix can't have less than 1 element"


print("Finding the determinant... let's help you find that stubborn determinant... \n")

row_count = int(input("What's the row/column count (we expect one number, determinants are only to square matrices)?: "))

matrix = []
print("\nOkay, now, enter the elements of this matrix row by row, just type a b c, a, b, and c being the elements, separate the elements by space")
for row in range(row_count):
    row_nums = input(f"Row {row+1}: ")
    matrix.append([int(elem) for elem in row_nums.split()])
    print(" ")
    if len(matrix)==1:
        print(matrix[0])
    else:
        for i in matrix:
            print(i)

print(f"The determinant for your matrix is {cal_det(row_count, matrix)}")