def deposit(balance, amount) -> TypeError | ValueError | float:
    """
    :param balance: amount of money stored in the account
    :param amount: amount of money input to be deposited into account
    function that determines if the input was valid for both accounts as well as computing balance + amount
    :return TypeError, ValueError, float:
    """
    try:
        amount = float(amount)
        if amount <= 0:
            return TypeError
        else:
            balance += amount
            return balance
    except ValueError:
        return ValueError

def withdraw(balance, amount) -> TypeError | ValueError | float:
    """
    :param balance: amount of money stored in the account
    :param amount: amount of money input to be withdrawn from account
    function that determines if the input was valid for the regular account as well as computing balance - amount
    :return TypeError, ValueError, float:
    """
    try:
        amount = float(amount)
        if amount <= 0:
            return ValueError
        else:
            balance -= amount
            if balance < 0:
                return TypeError
            else:
                return balance
    except ValueError:
        return ValueError

def saving_withdraw(balance, amount) -> TypeError | ValueError | float:
    """
    :param balance: amount of money stored in the account
    :param amount: amount of money input to be withdrawn from account
    function that determines if the input was valid to be deposited in saving account
    as well as computing balance - amount
    :return TypeError, ValueError, float:
    """
    try:
        amount = float(amount)
        if amount <= 0:
            return ValueError
        else:
            balance -= amount
            if balance < 100:
                return TypeError
            else:
                return balance
    except ValueError:
        return ValueError