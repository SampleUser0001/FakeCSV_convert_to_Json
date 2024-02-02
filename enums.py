from enum import Enum

class TypeEnum(Enum):
    PATTERN_A = "PATTERN_A"
    PATTERN_B = "PATTERN_B"

    @staticmethod
    def get_empty_dict():
        return_dict = {}
        for e in TypeEnum:
            return_dict[e.name] = {
                "header": None,
                "data": []
            }
        return return_dict