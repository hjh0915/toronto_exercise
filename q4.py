def get_valid_month() -> int:
    """
    Return a valid month number input by user after (possibly repeated) prompting.
    A valid month number is an int between 1 and 12 inclusive.
    """
    prompt = 'Enter a valid month number: '
    error_message = 'Invalid input! Read the instructions and try again!'
    # Use this statement as many times as needed for input:
    # month = input(prompt)
    # Use this statement as many times as needed for output:
    # print(error_message)
    month = input(prompt)
    if int(month) > 12 or int(month) < 1 or not month.isdigit():
        print(error_message)
    else:
        return int(month)

if __name__ == '__main__':
    print(get_valid_month())
