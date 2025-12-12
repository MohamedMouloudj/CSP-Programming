from algorithms.localConsistency.revise import REVISE
import copy
from collections import deque


def AC3(csp, domains=None):
    """
    AC-3 (Arc Consistency 3) Algorithm
    
    Args:
        csp: CSP problem instance
        domains: initial domains (optional)
    
    Returns:
        filtered domains or None if inconsistency detected
    """
    if domains is None:
        domains = copy.deepcopy(csp.domains)
    
    # Node consistency first (already handled in domain initialization)
    
    # Initialize queue with all arcs
    Q = deque()
    for i, Xi in enumerate(csp.variables):
        for j, Xj in enumerate(csp.variables):
            if i != j:
                Q.append((Xi, Xj))
    
    # Process queue
    while Q:
        Xi, Xj = Q.popleft()
        
        if REVISE(Xi, Xj, domains, csp):
            # Check for domain wipeout
            if len(domains[Xi]) == 0:
                return None  # Inconsistency detected
            
            # Add arcs (Xk, Xi) for all neighbors Xk of Xi (except Xj)
            for Xk in csp.variables:
                if Xk != Xi and Xk != Xj:
                    Q.append((Xk, Xi))
    
    return domains
