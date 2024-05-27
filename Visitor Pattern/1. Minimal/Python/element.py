import re

class Element:
    def accept(self, visitor):
        snake_case_string = re.sub(r"(?<!^)(?=[A-Z])", "_", type(self).__name__).lower()
        method_name = f"visit_{snake_case_string}"
        visitor_method = getattr(visitor, method_name)
        visitor_method(self)
