#  File: Flipped.py

#  Description: Flip a matrix both horizontally and vertically

# Student Name: Soomin Hyun

# Student UT EID: sh52679

# Course Name: CS 313E

# Unique Number: 52600


# Input: matrix is a 2d list
# Output: return the equivalent matrix that has been flipped both horizontally and vertically
def flip_matrix(matrix):
    new_matrix = []
    new_num = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            new_num.append(matrix[i][j])
        new_matrix.append(new_num)

    n = len(matrix) - 1
    for i in range(len(matrix) // 2):
        new_matrix[i] = matrix[n - i]

        new_matrix[n - i] = matrix[i]

    new_line = []
    another_new_matrix = []
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix[i])):
            new_line.append(new_matrix[i][j])
        print(new_line)
        another_new_matrix.append(new_line)
        print(another_new_matrix)




    n = len(new_matrix[0]) - 1
    print(another_new_matrix)
    for i in range(len(new_matrix)):
        for j in range(len(new_matrix) // 2):
            another_new_matrix[i][j] = new_matrix[i][n - j]
            print(another_new_matrix[i][j], new_matrix[i][n-j])
            another_new_matrix[i][n - j] = new_matrix[i][j]
            print(another_new_matrix[i][n - j], new_matrix[i][j])
            print(another_new_matrix)

    print(another_new_matrix)

    return another_new_matrix


def main():
    # read number of rows of matrix
    n = int(input())

    matrix = []
    # read data from standard input
    for _ in range(n):
        matrix.append(list(map(int, input().split())))

    # get the result from your call to flip_matrix()
    result = flip_matrix(matrix)

    # print the result to standard output

    for i in range(len(result)):
        for j in range(len(result[0])):
            print('{:2d}'.format(result[i][j]), end=' ')  # makes good spacing
        print()

if __name__ == "__main__":
    main()
