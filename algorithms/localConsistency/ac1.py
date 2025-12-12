from algorithms.csp_framework import CSP
from algorithms.localConsistency.revise import REVISE
import copy

def AC1(csp: CSP, domains: dict | None = None):
    """
    AC-1 (Arc Consistency 1) Algorithm
    
    Args:
        csp: CSP problem instance
        domains: initial domains (optional)
    
    Returns:
        filtered domains or None if inconsistency detected
    """
    if domains is None:
        domains = copy.deepcopy(csp.domains)
    
    # Node consistency first (already handled in domain initialization)
    
    # Get all arcs (pairs of variables that have constraints)
    arcs = []
    for i, Xi in enumerate(csp.variables):
        for j, Xj in enumerate(csp.variables):
            if i != j:
                arcs.append((Xi, Xj))
    
    # Repeat until no changes
    changed = True
    while changed:
        changed = False
        
        for Xi, Xj in arcs:
            if REVISE(Xi, Xj, domains, csp):
                changed = True
                
                # Check for domain wipeout
                if len(domains[Xi]) == 0:
                    return None  # Inconsistency detected
    
    return domains
