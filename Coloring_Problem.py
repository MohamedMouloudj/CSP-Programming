from algorithms.csp_framework import CSP
from algorithms.get_algorithm import GET
from algorithms.sra_algorithm import SRA
from algorithms.fc_algorithm import FC
from algorithms.look_ahead_algorithm import Look_Ahead, MAC_Look_Ahead

def create_map_coloring():
    """
    Simple map coloring problem
    Variables: Regions (A, B, C, D)
    Domain: Colors (Red, Green, Blue)
    Constraints: Adjacent regions must have different colors
    """
    variables = ['A', 'B', 'C', 'D']
    domains = {var: ['Red', 'Green', 'Blue'] for var in variables}
    
    # Adjacency: A-B, A-C, B-C, B-D, C-D
    def map_constraints(assignment):
        adjacencies = [('A', 'B'), ('A', 'C'), ('B', 'C'), ('B', 'D'), ('C', 'D')]
        for v1, v2 in adjacencies:
            if v1 in assignment and v2 in assignment:
                if assignment[v1] == assignment[v2]:
                    return False
        return True
    
    return CSP(variables, domains, map_constraints)

if __name__ == "__main__":
    print("="*60)
    print("Testing Map Coloring Problem")
    print("="*60)
    map_csp = create_map_coloring()
    
    print("\n--- Using GET Algorithm ---")
    solution = GET(map_csp)
    print(f"GET Solution: {solution}\n")
    
    print("--- Using SRA Algorithm ---")
    solution = SRA(map_csp)
    print(f"SRA Solution: {solution}\n")
    
    print("--- Using FC Algorithm ---")
    solution = FC(map_csp)
    print(f"FC Solution: {solution}\n")
    
    print("--- Using Look-Ahead Algorithm ---")
    solution = Look_Ahead(map_csp, verbose=True)
    print(f"LA Solution: {solution}\n")
    
    print("--- Using MAC Look-Ahead Algorithm ---")
    solution = MAC_Look_Ahead(map_csp, verbose=True)
    print(f"MAC Solution: {solution}\n")