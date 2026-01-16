def check_temperature(temp_str):
    """Checks if the input Temperature is valid to let plants grow"""
    print(f"Testing temperature: {temp_str}")
    if isinstance(temp_str, str):
        print(f"Error: '{temp_str}' is not a valid number")
    elif temp_str > 40:
        print(f"Error: {temp_str}ºC is too hot for plants (max 40ºC)")
    elif temp_str < 0:
        print(f"Error: {temp_str}ºC is too clod for plants (min 0ºC)")
    elif isinstance(temp_str, str):
        print(f"Error: '{temp_str}' is not a valid number")
    else:
        print(f"Temperature {temp_str}ºC is perfect for plants!")


def test_temperature_input():
    print("=== Garden Temperature Checker ===")
    give_input = input("Set a Temperature: ")
    try:
        number = int(give_input)
        check_temperature(number)
    except ValueError:
        check_temperature(give_input)
    give_input = input("Set a Temperature: ")
    try:
        number = int(give_input)
        check_temperature(number)
    except ValueError:
        check_temperature(give_input)
    give_input = input("Set a Temperature: ")
    try:
        number = int(give_input)
        check_temperature(number)
    except ValueError:
        check_temperature(give_input)
    give_input = input("Set a Temperature: ")
    try:
        number = int(give_input)
        check_temperature(number)
    except ValueError:
        check_temperature(give_input)
    print("All tests completed - program didn't crash!")


test_temperature_input()
