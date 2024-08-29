import re

class Element:
    def accept(self, visitor):
        # Get the calling class name.
        calling_class=type(self).__name__
        # Convert the class name from camel-case to snake-case.
        # r         -> raw string, meaning that "\" does not escape.
        # (?<!^)    -> Regex negative lookbehind. The following character shall not be at the first position of the string.
        # (?=[A-Z]) -> Regex positive lookbehind. The follwing character shall be between A and Z.
        snake_case_string = re.sub(r"(?<!^)(?=[A-Z])", "_", calling_class).lower()
        # Create the calling method name.
        method_name = f"visit_{snake_case_string}"
        # Get the visitor method.
        visitor_method = getattr(visitor, method_name)
        # Provide the self environment to the visitor method.
        visitor_method(self)
