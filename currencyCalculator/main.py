import colorama
from colorama import Fore

def inputValues():
    while True:
        currency = input(f"{Fore.GREEN}Anfangswährung {Fore.CYAN}(EURO, DOLLAR, PFUND): {Fore.RESET}")
        if currency.upper() in ["EURO", "DOLLAR", "PFUND"]:
            currency = currency.upper()
            break
        else:
            print(f"{Fore.RED}Bitte gib eine valide Währung an {Fore.CYAN}(EURO, DOLLAR, PFUND){Fore.RESET}")

    while True:
        value = input(f"{Fore.GREEN}Anfangsbetrag: {Fore.RESET}")
        try:
            value = float(value)
            break
        except ValueError:
            print(f"{Fore.RED}Bitte gib einen validen Betrag an{Fore.RESET}")

    while True:
        targetCurrency = input(f"{Fore.GREEN}Gib deine Zielwährung ein {Fore.CYAN}(EURO, DOLLAR, PFUND): {Fore.RESET}")
        if targetCurrency.upper() in ["EURO", "DOLLAR", "PFUND"]:
            targetCurrency = targetCurrency.upper()
            break
        else:
            print(f"{Fore.RED}Bitte gib eine valide Währung an {Fore.CYAN}(EURO, DOLLAR, PFUND){Fore.RESET}")
    
    return currency, value, targetCurrency

def calculate(currency, value, targetCurrency):
    if currency == targetCurrency:
        print(f"{Fore.RED}Anfangs- und Endwährung können nicht die gleich sein{Fore.RESET}")
        return

    # EUR -> USD
    if currency == "EURO" and targetCurrency == "DOLLAR":
        value *= 1.08
    # USD -> EUR
    elif currency == "DOLLAR" and targetCurrency == "EURO":
        value *= 0.92
    # EUR -> GBP
    elif currency == "EURO" and targetCurrency == "PFUND":
        value *= 0.86
    # GBP -> EUR
    elif currency == "PFUND" and targetCurrency == "EURO":
        value *= 1.17
    # USD -> GBP
    elif currency == "DOLLAR" and targetCurrency == "PFUND":
        value *= 0.79
    # GBP -> USD
    elif currency == "PFUND" and targetCurrency == "DOLLAR":
        value *= 1.26

    print(f"{Fore.GREEN}Es sind {Fore.CYAN}{value} {targetCurrency}{Fore.RESET}")



if __name__ == "__main__":
    currency, value, targetCurrency = inputValues()
    calculate(currency, value, targetCurrency)
