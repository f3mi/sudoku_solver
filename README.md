# sudoku_solver
A Python-based Sudoku solver that utilizes the backtracking algorithm to solve any 9x9 Sudoku puzzle.
This project demonstrates the power of algorithms and data structures in solving constraint satisfaction problems.

🚀 Features
Backtracking Algorithm: Efficiently explores possible solutions to find the correct one.
Validation Logic: Ensures the numbers follow Sudoku rules for rows, columns, and 3x3 subgrids.
Readable Output: Displays the puzzle before and after solving in a clear, grid-like format.
Customizable Input: Modify the puzzle to test different scenarios.
🛠️ Installation
Clone this repository:

bash
Copy code
git clone https://github.com/f3mi/sudoku-solver.git
cd sudoku-solver
Ensure you have Python installed. You can check by running:

bash
Copy code
python --version
Run the script:

bash
Copy code
python sudoku_solver.py
📋 How It Works
Input Format: The Sudoku puzzle is represented as a 9x9 grid in the form of a 2D list. Empty cells are denoted by 0.
Example:

python
Copy code
puzzle = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    ...
]
Algorithm:

The solve function applies backtracking to try numbers from 1-9 in empty cells.
The is_valid function ensures that the number placement adheres to Sudoku rules.
Output: The solved puzzle is printed in a readable grid format.
