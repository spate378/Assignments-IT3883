# IT 3883 - Final Exam
# Sprint 2 - Update Coin Sentence to Dollar Converter

def coinSentenceToDollarConverter(sentence: str) -> float:
    """
    Convert a sentence with coins into a dollar amount.
    Ex. "1 penny and 2 nickels" -> 0.11
    """
    # Clean up the user sentence
    UserSentence = sentence.strip().lower()
    if UserSentence == "":
        return 0.0

    # Split the coins by the word "and"
    CoinParts = [part.strip() for part in UserSentence.split("and")]
    totalCents = 0

    for part in CoinParts:
        if part == "":
            continue
        words = part.split()
        if len(words) < 2:
            # Skip if there is not enouh input
            print(f"There are not enough words input: {part}")
            continue

        # Quantity of coins then the names/values
        CoinQty = words[0]
        CoinName = words[1]
        # Convert quantity amount to int
        try:
            quantity = int(CoinQty)
        except ValueError:
            print(f"The quantity is invalid: {CoinQty}")
            continue

        # Add values to coins
        if CoinName in ("penny", "pennies"): # This allows the program to accept plural form of penny
            coinValue = 1
        elif CoinName in ("nickel", "nickels"):
            coinValue = 5
        elif CoinName in ("dime", "dimes"):
            coinValue = 10
        elif CoinName in ("quarter", "quarters"):
            coinValue = 25
        else:
            print(f"You entered an invalid coin: {CoinName}")
            continue

        # calculate the total value of coins entered
        totalCents += quantity * coinValue

        # Convert to dollar amount for every 100 value
    totalDollar = totalCents / 100.0
    return totalDollar

def main():
    print("Sprint 1 - Coin to Dollar Converter")
    print("Ex. 1 penny and 2 nickels")
    print("To STOP the program, enter a blank line.\n")

    while True:
        # Get the user input
        userInput = input("Enter a coin sentence: ").strip()

        # If user enters blank line, end program
        if userInput == "":
            print("You have now exit the program.")
            break
        # Print final output with 2 decimal places
        TotalAmount = coinSentenceToDollarConverter(userInput)
        print(f"The total is : {TotalAmount:.2f}\n")

if __name__ == "__main__":
    main()
