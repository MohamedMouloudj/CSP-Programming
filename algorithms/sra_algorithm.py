from algorithms.csp_framework import CSP

def SRA(csp: CSP, assignment=None):
    """
    Simple Recursive Backtracking Algorithm (SRA) for CSP
    
    Args:
        csp: CSP problem instance
        assignment: current partial assignment (dict)
    
    Returns:
        solution assignment or None if no solution exists
    """
    if assignment is None:
        assignment = {}
    
    # Base case: all variables assigned
    if csp.is_complete(assignment):
        return assignment
    
    # Choose an unassigned variable
    unassigned = [v for v in csp.variables if v not in assignment]
    Xi = unassigned[0]
    
    for v in csp.domains[Xi]:
        new_assignment = assignment.copy()
        new_assignment[Xi] = v
        
        # Check consistency with previous assignments
        if csp.is_consistent(new_assignment):
            result = SRA(csp, new_assignment)
            if result is not None:
                return result
    
    return None