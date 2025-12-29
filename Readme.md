# Constraint Satisfaction Problem (CSP) Solver

Python implementation of classical CSP solving algorithms for educational purposes.

## Algorithms Implemented

### Complete Search Algorithms

- **GET** - Generate and Test (brute force)
- **SRA** - Simple Recursive Backtracking
- **FC** - Forward Checking
- **Look-Ahead** - Look-Ahead Consistency
- **Look-Ahead (MAC)** - Maintaining Arc Consistency

### Local Consistency Algorithms

- **AC1** - Arc Consistency 1
- **AC3** - Arc Consistency 3
- **AC3-Incremental** - Incremental AC3
- **REVISE** - Domain filtering helper

## Test Problems

- **N-Queens** - Place N queens on N×N chessboard
- **Map Coloring** - Color adjacent regions differently
- **Mini Sudoku** - 4×4 Sudoku puzzle

## Usage

```python
from algorithms.csp_framework import CSP
from algorithms.sra_algorithm import SRA

# Create CSP instance
csp = create_nqueens_csp(8)

# Solve
solution = SRA(csp)
print(solution)
```

## 📂 Project Structure

```
CSP/
├── algorithms/
│   ├── utils.py
│   ├── csp_framework.py
│   ├── completeSearch/
│   │   ├── get_algorithm.py
│   │   ├── sra_algorithm.py
│   │   ├── fc_algorithm.py
│   │   └── look_ahead.py
│   └── localConsistency/
│       ├── revise.py
│       ├── ac1.py
│       └── ac3.py
├── N-Queens_Problem.py
└── Index.ipynb
```

## University Course

CSP - Semester 7, 2025

