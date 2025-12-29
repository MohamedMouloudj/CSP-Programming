from algorithms.csp_framework import CSP
from algorithms.get_algorithm import GET
from algorithms.sra_algorithm import SRA
from algorithms.fc_algorithm import FC
from algorithms.look_ahead_algorithm import Look_Ahead, MAC_Look_Ahead


def create_sudoku_mini():
    """
    Mini 4x4 Sudoku for testing
    """
    variables = [f'X{i}{j}' for i in range(4) for j in range(4)]
    domains = {var: [1, 2, 3, 4] for var in variables}
    
    initial = {
        'X01': 3,
        'X10': 4,
        'X23': 4,
        'X32': 2
    }
    
    for var, val in initial.items():
        domains[var] = [val]
    
    def sudoku_constraints(assignment):
        # Check rows
        for i in range(4):
            row_vals = [assignment.get(f'X{i}{j}') for j in range(4) if f'X{i}{j}' in assignment]
            if len(row_vals) != len(set(row_vals)):
                return False
        
        # Check columns
        for j in range(4):
            col_vals = [assignment.get(f'X{i}{j}') for i in range(4) if f'X{i}{j}' in assignment]
            if len(col_vals) != len(set(col_vals)):
                return False
        
        # Check 2x2 boxes
        for box_row in range(2):
            for box_col in range(2):
                box_vals = []
                for i in range(2):
                    for j in range(2):
                        var = f'X{box_row*2+i}{box_col*2+j}'
                        if var in assignment:
                            box_vals.append(assignment[var])
                if len(box_vals) != len(set(box_vals)):
                    return False
        
        return True
    
    return CSP(variables, domains, sudoku_constraints)


if __name__ == "__main__":
    print("="*60)
    print("Testing Mini Sudoku (4x4)")
    print("="*60)
    sudoku_csp = create_sudoku_mini()
    
    print("\n--- Using GET Algorithm ---")
    solution = GET(sudoku_csp)
    if solution:
        print("GET Solution found:")
        for i in range(4):
            row = [str(solution[f'X{i}{j}']) for j in range(4)]
            print(' '.join(row))
    else:
        print("No solution found!")
    
    print("\n--- Using SRA Algorithm ---")
    solution = SRA(sudoku_csp)
    if solution:
        print("SRA Solution found:")
        for i in range(4):
            row = [str(solution[f'X{i}{j}']) for j in range(4)]
            print(' '.join(row))
    else:
        print("No solution found!")

    print("\n--- Using FC Algorithm ---")
    solution = FC(sudoku_csp)
    if solution:
        print("FC Solution found:")
        for i in range(4):
            row = [str(solution[f'X{i}{j}']) for j in range(4)]
            print(' '.join(row))
    else:
        print("No solution found!")
    
    print("\n--- Using Look-Ahead Algorithm ---")
    solution = Look_Ahead(sudoku_csp)
    if solution:
        print("LA Solution found:")
        for i in range(4):
            row = [str(solution[f'X{i}{j}']) for j in range(4)]
            print(' '.join(row))
    else:
        print("No solution found!")
    
    print("\n--- Using MAC Look-Ahead Algorithm ---")
    solution = MAC_Look_Ahead(sudoku_csp)
    if solution:
        print("MAC Solution found:")
        for i in range(4):
            row = [str(solution[f'X{i}{j}']) for j in range(4)]
            print(' '.join(row))
    else:
        print("No solution found!")
