from src.reqstool_decorators.decorators.decorators import Requirements


@Requirements("REQ_001", "REQ_222")
class RequirementsClass:
    pass


@Requirements("REQ_333")
def requirements_function():
    # Test function for Requirements decorator
    pass
