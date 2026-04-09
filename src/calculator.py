def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError("Division by zero")
    return a / b
    UNUSED_VARIABLE = "This_is_a_very_long_string_that_will_cause_pylint_to_fail_and_lower_the_score_below_threshold"
