# -------------------------------------------
# INFO:
#  We will show 3 different concepts to make better functions:
#   * annotations
#   * named parameters
#   * default values
# -------------------------------------------#

# ANNOTATIONS
# ------------------------
# input type v      v return type
def fun1 (n:int) -> int:
    """ Returns the next integer value """
    print(f"I will return {n} + 1")
    return n+1

# input types v     v        v return type
def fun2(n: int, c: str) -> bool:
    """ Returns T/F if a string is the ASCII ord for a character """
    print(f"I will return True (if ord({c}) == {n}) or False (ord({c}) != {n}) ")
    return ord(c) == n


# NAMED PARAMETERS (all functions can be called like this)
# ------------------------
def my_div (denominator, numerator):
    """ Returns a float division """
    print("I will return numerator/denominator")
    return numerator/denominator


# DEFAULT VALUES
# ------------------------
def calculate_balance (principal, months = 1, interest = 0.01):
    """ Returns compound interest given some parameters """
    print("I will return the balance after",months,
        "months, with",interest,"interest")
    return principal*((1 + interest )**months)


# Calling ANNOTATED functions (as normal)
def annotated_functions():
    """ Calls annotated functions """
    num = fun1(5)
    print("fun1 returned",num)
    num = fun2(2, "B")
    print("fun2 returned",num)



# Calling with NAMED PARAMETERS (assigning by name)
def call_named_parameters():
    """ Calls functions using named parameters """
    # my_div has Named Parameters
    division = my_div (numerator = 30, denominator = 3)
    print ("the result is:",division)


def call_with_default_values():
    """ Calls functions assummed to have default values"""
    # I want to get the balance for 1000, 12, 0.02
    balance = calculate_balance(1000, 12, 0.02)
    print ("the result is:",balance)
    # I can also ask with some missing arguments
    balance = calculate_balance(1000)
    print ("the new result is:",balance)

    balance = calculate_balance(200, interest = 0.03)
    print ("the new result is:",balance)


def main():
    """ Calls exampless of fancy functions """

    print("Hello", end="#")

    print("Choose an option:")
    print("\t1: annotated functions")
    print("\t2: named functions")
    print("\t3: default values")
    print("\tAnything else: quit")
    op = input ("your choice: ")
    if op == "1":
        annotated_functions()
    elif op == "2":
        call_named_parameters()
    elif op == "3":
        call_with_default_values()
    else:
        print("Quitting")

if __name__ == "__main__":
    main()