class NQueens:
  """Generate all valid solutions for the n queens puzzle"""
  def __init__(self, size):
    # Store the puzzle (problem) size and the number of valid solutions
    self.size = size
    self.solutions = 0
    self.solve()

  def solve(self):
  #Solve the n queens puzzle and print the number of solutions
    positions = [-1] * self.size
    self.put_queen(positions, 0)
    print("Found", self.solutions, "solutions.")

  def put_queen(self, positions, target_row):
  # Base (stop) case - all N rows are occupied
    if target_row == self.size:
      self.show_full_board(positions)
      self.solutions += 1
    else:
    # For all N columns positions try to place a queen
      for column in range(self.size):
      # Reject all invalid positions
        if self.check_place(positions, target_row, column):
          positions[target_row] = column
          self.put_queen(positions, target_row + 1)

  def check_place(self, positions, ocuppied_rows, column):
    for i in range(ocuppied_rows):
      if positions[i] == column or \
        positions[i] - i == column - ocuppied_rows or \
        positions[i] + i == column + ocuppied_rows:

          return False
    return True

  def show_full_board(self, positions):
    for row in range(self.size):
      line = ""
      for column in range(self.size):
        if positions[row] == column:
          line += "Q "
        else:
          line += ". "
      print(line)
    print("\n")

def main():
  game = NQueens(8)


if __name__ == "__main__":
  # execute only if run as a script
  main()