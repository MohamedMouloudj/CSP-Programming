from algorithms.localConsistency.ac3 import AC3
import copy

def Look_Ahead(csp, assignment=None, domains=None):
    """
    Look-Ahead Algorithm using AC3 (Maintaining Arc Consistency - MAC)
    
    Args:
        csp: CSP problem instance
        assignment: current partial assignment (dict)
        domains: current domains for each variable (dict)
    
    Returns:
        solution assignment or None if no solution exists
    """
    if assignment is None:
        assignment = {}
    
    if domains is None:
        domains = copy.deepcopy(csp.domains)
    
    # Apply AC3 to maintain arc consistency
    domains = AC3(csp, domains)
    
    # Check for domain wipeout
    if domains is None:
        return None
    
    # Check if any domain is empty
    for var in csp.variables:
        if var not in assignment and len(domains[var]) == 0:
            return None
    
    # Check if all domains are singletons (one value each)
    all_singletons = True
    for var in csp.variables:
        if var not in assignment:
            if len(domains[var]) > 1:
                all_singletons = False
                break
            elif len(domains[var]) == 1:
                assignment[var] = domains[var][0]
    
    if all_singletons:
        return assignment if csp.is_complete(assignment) else None
    
    # Choose an unassigned variable
    unassigned = [v for v in csp.variables if v not in assignment]
    if not unassigned:
        return assignment if csp.is_consistent(assignment) else None
    
    Xi = unassigned[0]
    
    # Try each value in domain
    for vi in domains[Xi]:
        new_assignment = assignment.copy()
        new_assignment[Xi] = vi
        
        # Create new domains with Xi fixed to vi
        new_domains = copy.deepcopy(domains)
        new_domains[Xi] = [vi]
        
        result = Look_Ahead(csp, new_assignment, new_domains)
        if result is not None:
            return result
    
    return None