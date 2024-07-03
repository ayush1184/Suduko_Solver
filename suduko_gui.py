import tkinter as tk
from tkinter import messagebox
from solver import solve_sudoku

class SudokuGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Sudoku Solver")
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        self.original_board = [[0 for _ in range(9)] for _ in range(9)]
        self.create_widgets()

        # Bind the Enter key to trigger the solve function
        self.root.bind('<Return>', lambda event: self.solve())
        # Bind the Esc key to reset the board
        self.root.bind('<Escape>', lambda event: self.reset())
        # Bind arrow keys to move the active cell
        self.root.bind('<Up>', self.move_up)
        self.root.bind('<Down>', self.move_down)
        self.root.bind('<Left>', self.move_left)
        self.root.bind('<Right>', self.move_right)

        self.active_cell = (0, 0)  # Start with the top-left cell active
        self.entries[0][0].focus_set()

    def create_widgets(self):
        frame = tk.Frame(self.root)
        frame.pack()

        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(frame, width=2, font=("Arial", 18), justify="center")
                self.entries[i][j].grid(row=i, column=j, padx=5, pady=5)

        solve_button = tk.Button(self.root, text="Solve", command=self.solve)
        solve_button.pack(pady=10)
        
        reset_button = tk.Button(self.root, text="Reset", command=self.reset)
        reset_button.pack(pady=10)

    def solve(self):
        self.read_board()
        self.original_board = [row[:] for row in self.board]
        if solve_sudoku(self.board):
            self.display_solution()
        else:
            messagebox.showerror("Error", "No solution exists for the given Sudoku")

    def reset(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(fg='black')  # Reset color to black
        self.board = [[0 for _ in range(9)] for _ in range(9)]
        self.original_board = [[0 for _ in range(9)] for _ in range(9)]

    def read_board(self):
        for i in range(9):
            for j in range(9):
                value = self.entries[i][j].get()
                self.board[i][j] = int(value) if value else 0

    def display_solution(self):
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].insert(0, str(self.board[i][j]))
                if self.original_board[i][j] == 0:
                    self.entries[i][j].config(fg='green')  # Change color of the new numbers to green
                else:
                    self.entries[i][j].config(fg='white')  # Original numbers remain white

    def move_up(self, event):
        row, col = self.active_cell
        if row > 0:
            self.active_cell = (row - 1, col)
            self.entries[row - 1][col].focus_set()

    def move_down(self, event):
        row, col = self.active_cell
        if row < 8:
            self.active_cell = (row + 1, col)
            self.entries[row + 1][col].focus_set()

    def move_left(self, event):
        row, col = self.active_cell
        if col > 0:
            self.active_cell = (row, col - 1)
            self.entries[row][col - 1].focus_set()

    def move_right(self, event):
        row, col = self.active_cell
        if col < 8:
            self.active_cell = (row, col + 1)
            self.entries[row][col + 1].focus_set()

if __name__ == "__main__":
    root = tk.Tk()
    gui = SudokuGUI(root)
    root.mainloop()
