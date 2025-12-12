
from algorithms.csp_framework import CSP

def REVISE(Xi, Xj, domains:dict, csp: CSP):
    """
    Remove values from D[Xi] that have no compatible value in D[Xj]
    
    Args:
        Xi: variable to revise
        Xj: variable to check against
        domains: current domains
        csp: CSP problem instance
    
    Returns:
        True if domain of Xi was changed, False otherwise
    """
    deleted = False
    
    for vi in domains[Xi][:]:
        has_compatible = False
        
        for vj in domains[Xj]:
            test_assignment = {Xi: vi, Xj: vj}
            if csp.is_consistent(test_assignment):
                has_compatible = True
                break
        
        if not has_compatible:
            domains[Xi].remove(vi)
            deleted = True
    
    return deleted

