import sys; input = sys.stdin.readline
import random

random.seed(327438444)
K = 7

def generate_random_vector(nRows):
  return [random.randint(0, 1) for _ in range(nRows)]

# multiply matrix with column and return resulting column
def matrix_multiply_column(matrix, column):
  result = []
  for row in matrix:
    assert(len(row) == len(column))
    row_sum = 0
    for pair in zip(row, column):
      n0, n1 = pair
      row_sum += n0 * n1
    result.append(row_sum)
  return result


TC = int(input())

input_read_numbers = lambda : [int(x) for x in input().split(" ")]

def input_read_matrix(nRows, nCols):
  result = []
  for _ in range(nRows):
    col_values = input_read_numbers()
    assert(len(col_values) == nCols)
    result.append(col_values)
  return result

while TC > 0:
  input() # skip line

  n, x, y, m = input_read_numbers()

  is_invalid = False
  # invalid case
  if x != y:
    print("Inner matrix dimensions must agree")
    is_invalid = True

  # read matrices
  A = input_read_matrix(n, x)
  B = input_read_matrix(y, m)
  C = input_read_matrix(n, m)

  if is_invalid:
    TC-=1
    continue

  correct=True
  for i in range(K):
    rand_vector = generate_random_vector(m)
    B_0 = matrix_multiply_column(matrix=B, column=rand_vector)
    AB_0 = matrix_multiply_column(matrix=A, column=B_0)
    C_0 = matrix_multiply_column(C, rand_vector)
    if AB_0 != C_0:
      correct=False
      break
  print("AC" if correct else "WA")
  TC-=1


