def safe_print_division(a, b):
    try:
        return (a / b)
    except ZeroDivisionError:
        return None
    finally:
        print("Inside result: {}".format(a / b if b != 0 else "None"))