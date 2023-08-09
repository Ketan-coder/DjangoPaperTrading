# custom_exceptions.py

class MultipleFieldsFilledError(Exception):
    def __init__(self, field_names):
        self.field_names = field_names
        super().__init__("Only one field should be filled among: " + ', '.join(field_names))

    def __str__(self):
        return f"MultipleFieldsFilledError: {super().__str__()}"
