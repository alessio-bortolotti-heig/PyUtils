def calculate_basic_reproduction_number(beta, gamma):
    """
    Calculate the Basic Reproduction Number (R0) of an epidemic.

    :param beta: Transmission rate (infections per day per infected individual)
    :param gamma: Recovery rate (recoveries per day per infected individual)
    :return: The value of R0
    """
    return beta / gamma


def calculate_herd_immunity_threshold(r0):
    """
    Calculate the Herd Immunity Threshold (HIT) to stop the epidemic.

    :param r0: Basic Reproduction Number (R0)
    :return: The percentage of herd immunity required
    """
    return 1 - (1 / r0)

"""
# Example of usage
if __name__ == "__main__":
    beta = 0.5  # Transmission rate
    gamma = 0.2  # Recovery rate

    basic_reproduction_number = calculate_basic_reproduction_number(beta, gamma)
    herd_immunity_threshold = calculate_herd_immunity_threshold(basic_reproduction_number)

    print(f"R0: {basic_reproduction_number}")
    print(f"HIT: {herd_immunity_threshold * 100}%")
"""
