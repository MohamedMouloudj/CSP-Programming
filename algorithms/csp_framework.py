class CSP:
    """Base class for Constraint Satisfaction Problems"""
    
    def __init__(self, variables:list, domains:dict, constraints:callable):
        """
        variables: list of variable names
        domains: dict mapping variables to their possible values
        constraints: function that checks if assignment is valid
        """
        self.variables = variables
        self.domains = domains
        self.constraints = constraints
    
    def is_consistent(self, assignment):
        """Check if current assignment satisfies all constraints"""
        return self.constraints(assignment)
    
    def is_complete(self, assignment):
        """Check if all variables are assigned"""
        return len(assignment) == len(self.variables)