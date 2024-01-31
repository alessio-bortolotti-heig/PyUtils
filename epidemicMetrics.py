def calculate_r0(beta, gamma):
    """
    Calculate the Basic Reproduction Number (R0) of an epidemic.

    :param beta: Transmission rate (infections per day per infected individual)
    :param gamma: Recovery rate (recoveries per day per infected individual)
    :return: The value of R0
    """
    return beta / gamma

def calculate_hit(r0):
    """
    Calculate the Herd Immunity Threshold (HIT) to stop the epidemic.

    :param r0: Basic Reproduction Number (R0)
    :return: The percentage of herd immunity required
    """
    return 1 - (1 / r0)

# Example of usage
if __name__ == "__main__":
    beta = 0.5  # Transmission rate
    gamma = 0.2  # Recovery rate

    r0 = calculate_r0(beta, gamma)
    hit = calculate_hit(r0)

    print(f"R0: {r0}")
    print(f"HIT: {hit * 100}%")
