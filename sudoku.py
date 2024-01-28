import random
from colorama import Fore, init
init(autoreset=True)

class Sudoku:
    def __init__(self) -> None:
        pass
    
    def show(self, board) -> None:
        table_color = Fore.RED
        numbers_color = Fore.BLUE
        separator = f"{table_color}-------------------------"
        
        for i, row in enumerate(board):
            if i % 3 == 0:
                print(separator)
            print(f"{table_color}|", end=" ")
            for j, element in enumerate(row):
                print(f"{numbers_color}{element}" if element != 0 else " ", end=" ")
                if (j + 1) % 3 == 0:
                    print(f"{table_color}|", end=" ")
            print()
        print(separator)

    def is_valid(self, board, row, col, num) -> bool:
        if num in board[row] or num in [board[i][col] for i in range(9)]:
            return False

        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if board[i][j] == num:
                    return False

        return True
    
    def generateBoard(self) -> None:
        self.board = [[0] * 9 for _ in range(9)]
        
        for i in range(9):
            elements = list(range(1, 10))
            random.shuffle(elements)
            
            for j in range(9):
                valid_elements = [element for element in elements if self.is_valid(self.board, i, j, element)]
                if not valid_elements:
                    return self.generateBoard()
                self.board[i][j] = random.choice(valid_elements)

    def clearSomeElements(self, difficulty: int) -> None:
        self.cleared_board = [row.copy() for row in self.board]
        chance = list(range(1, difficulty))
        
        for i, row in enumerate(self.cleared_board):
            for j, element in enumerate(row):
                if random.randint(1, 100) in chance:
                    self.cleared_board[i][j] = '_'

def main():
    sudoku = Sudoku()
    sudoku.generateBoard()
    difficulty = int(input('Enter the percentage of the empty cells: '))
    sudoku.clearSomeElements(difficulty)

    print("Generated Sudoku Board:")
    sudoku.show(sudoku.cleared_board)
    
    while True:
        code = random.randint(1000, 9999)
        if input(f'Enter {code} to see the solution: ') == str(code):
            sudoku.show(sudoku.board)
            break
        
if __name__ == "__main__":
    main()
    input()
