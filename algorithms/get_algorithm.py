from algorithms.csp_framework import CSP

def GET(csp: CSP, assignment: dict | None = None):
    """
    Generate and Test algorithm for CSP
    
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
        return assignment if csp.is_consistent(assignment) else None
    
    # Choose an unassigned variable
    unassigned = [v for v in csp.variables if v not in assignment]
    Xi = unassigned[0]  # pick first unassigned variable
    
    for v in csp.domains[Xi]:
        new_assignment = assignment.copy()
        new_assignment[Xi] = v
        
        result = GET(csp, new_assignment)
        if result is not None:
            return result
    
    return None