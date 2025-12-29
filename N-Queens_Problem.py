from algorithms.csp_framework import CSP
from algorithms.get_algorithm import GET
from algorithms.sra_algorithm import SRA
from algorithms.fc_algorithm import FC
from algorithms.look_ahead_algorithm import Look_Ahead, MAC_Look_Ahead

def create_nqueens_csp(n):
    """
    Create N-Queens CSP
    - Variables: Queen positions (one per row)
    - Domain: Column positions (0 to n-1)
    - Constraints: No two queens attack each other
    """
    variables = [f'Q{i}' for i in range(n)]
    domains = {var: list(range(n)) for var in variables}
    
    def nqueens_constraints(assignment):
        """Check if queens don't attack each other"""
        positions = list(assignment.items())
        
        for i in range(len(positions)):
            for j in range(i + 1, len(positions)):
                row1, col1 = int(positions[i][0][1:]), positions[i][1]
                row2, col2 = int(positions[j][0][1:]), positions[j][1]
                
                # same column
                if col1 == col2:
                    return False
                
                # same diagonal
                if abs(row1 - row2) == abs(col1 - col2):
                    return False
        
        return True
    
    return CSP(variables, domains, nqueens_constraints)


def print_nqueens_solution(solution, n):
    """Pretty print the N-Queens solution"""
    if solution is None:
        print("No solution found!")
        return
    
    print(f"\nN-Queens (n={n}) Solution:")
    for i in range(n):
        row = ['.'] * n
        col = solution[f'Q{i}']
        row[col] = 'Q'
        print(' '.join(row))
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Testing All CSP Algorithms with N-Queens Problem")
    print("=" * 60)
    
    # Test with different sizes
    for n in [4, 8]:
        print(f"\n{'='*60}")
        print(f"{n}-Queens Problem")
        print('='*60)
        
        csp = create_nqueens_csp(n)
        
        algorithms = [
            ("GET", GET),
            ("SRA", SRA),
            ("FC", FC),
            ("Look-Ahead", Look_Ahead),
            ("MAC Look-Ahead", MAC_Look_Ahead)
        ]
        
        for name, algo in algorithms:
            print(f"\n--- Using {name} Algorithm ---")
            if name in ["Look-Ahead", "MAC Look-Ahead"]:
                solution = algo(csp, verbose=True)
            else:
                solution = algo(csp)
            print_nqueens_solution(solution, n)
            if solution:
                print(f"{name} Solution:")
                for var in sorted(solution.keys()):
                    print(f"{var} = {solution[var]}")
            print("-" * 50)