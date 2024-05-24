"""Import the Account class from the Account.py file."""

# ADD YOUR CODE HERE

import Account


def create_savings_account(balance, interest_rate, months):
    """Creates a CD account, calculates interest earned, and updates the account balance.

    Args:
        balance (float): The initial CD account balance.
        interest_rate (float): The APR interest rate for the CD account.
        months (int): The length of months for the CD.

    Returns:
        float: The updated CD account balance after adding the interest earned.
        And returns the interest earned.
    """
    # Create an instance of the `Account` class and pass in the balance and interest parameters.
    #  Hint: You need to add the interest as a value, i.e, 0.
    # ADD YOUR CODE HERE
    account = Account.Account(balance=balance, interest=0)

    print("I'm in create_cd_account")

    # Calculate interest earned
    # ADD YOUR CODE HERE
    interest = balance * (interest_rate/100) * (months/12)
    account.set_interest(interest=interest)
    account.set_balance(balance=balance + interest)
    # Update the Savings account balance by adding the interest earned
    # ADD YOUR CODE HERE

    # Pass the updated_balance to the set balance method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Pass the interest_earned to the set interest method using the instance of the CDAccount class.
    # ADD YOUR CODE HERE

    # Return the updated balance and interest earned.
    
  # ADD YOUR CODE HERE
    return account.balance, account.interest


    #### ?
