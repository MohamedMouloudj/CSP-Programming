from algorithms.csp_framework import CSP
import copy

def FC(csp: CSP, assignment=None, domains=None):
    """
    Forward Checking Algorithm for CSP
    
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
    
    # Base case: all variables assigned
    if csp.is_complete(assignment):
        return assignment
    
    # Choose an unassigned variable
    unassigned = [v for v in csp.variables if v not in assignment]
    Xi = unassigned[0]
    
    for vi in domains[Xi]:
        new_assignment = assignment.copy()
        new_assignment[Xi] = vi
        
        # Check consistency with current assignment
        if not csp.is_consistent(new_assignment):
            continue
        
        # Forward checking: filter future domains
        new_domains = copy.deepcopy(domains)
        new_domains[Xi] = [vi]  # Fix Xi to vi
        
        consistent = True
        
        # For each unassigned variable
        for Xj in unassigned:
            if Xj == Xi:
                continue
            
            # Remove incompatible values from Xj's domain
            filtered_domain = []
            for vj in new_domains[Xj]:
                test_assignment = new_assignment.copy()
                test_assignment[Xj] = vj
                
                if csp.is_consistent(test_assignment):
                    filtered_domain.append(vj)
            
            new_domains[Xj] = filtered_domain
            
            # Domain wipeout - no valid values left
            if len(new_domains[Xj]) == 0:
                consistent = False
                break
        
        # If all future domains are non-empty, continue search
        if consistent:
            result = FC(csp, new_assignment, new_domains)
            if result is not None:
                return result
    
    return None