from collections import deque
from algorithms.csp_framework import CSP
from algorithms.localConsistency.ac3 import AC3, AC3_Incremental
from algorithms.utils import display_domains
import copy

def MAC_Look_Ahead(csp: CSP, assignment:dict|None=None, domains:dict|None=None, verbose=False):
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
    
    domains = AC3(csp, domains)
    
    if verbose and domains is not None:
        display_domains(domains, f"MAC: After AC3 (assigned: {list(assignment.keys())})")
    
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
        
        result = MAC_Look_Ahead(csp, new_assignment, new_domains, verbose)
        if result is not None:
            return result
    
    return None


from collections import deque
from algorithms.csp_framework import CSP
from algorithms.localConsistency.ac3 import AC3, AC3_Incremental
from algorithms.utils import display_domains
import copy

def Look_Ahead(csp: CSP, assignment: dict | None = None, domains: dict | None = None, verbose=False):
    """
    Look-Ahead Algorithm using Incremental AC3
    
    Args:
        csp: CSP problem instance
        assignment: current partial assignment (dict)
        domains: current domains for each variable (dict)
    
    Returns:
        solution assignment or None if no solution exists
    """
    # Initialize on first call (root node)
    if assignment is None:
        assignment = {}
    
    # Root node: run full AC3
    if len(assignment) == 0:
        if domains is None:
            domains = copy.deepcopy(csp.domains)
        
        domains = AC3(csp, domains)
        
        if verbose and domains is not None:
            display_domains(domains, "LA: After initial AC3")
        
        if domains is None:
            return None
    
    # If domains not initialized yet, copy from csp
    if domains is None:
        domains = copy.deepcopy(csp.domains)
    
    # Check if any domain is empty
    for var in csp.variables:
        if var not in assignment and len(domains[var]) == 0:
            return None
    
    # Check if all variables assigned
    if csp.is_complete(assignment):
        return assignment
    
    # Choose an unassigned variable
    unassigned = [v for v in csp.variables if v not in assignment]
    Xi = unassigned[0]
    
    for vi in domains[Xi]:
        new_assignment = assignment.copy()
        new_assignment[Xi] = vi
        
        new_domains = copy.deepcopy(domains)
        new_domains[Xi] = [vi]
        
        # Incremental propagation: create queue of arcs (Xj, Xi)
        Q = deque()
        for Xj in csp.variables:
            if Xj != Xi:  # All variables that have constraints with Xi
                Q.append((Xj, Xi))
        
        filtered_domains = AC3_Incremental(csp, new_domains, Q)
        
        if verbose and filtered_domains is not None:
            display_domains(filtered_domains, f"LA: After AC3_Inc for {Xi}={vi}")
        
        if filtered_domains is not None:
            result = Look_Ahead(csp, new_assignment, filtered_domains, verbose)
            if result is not None:
                return result
    
    return None