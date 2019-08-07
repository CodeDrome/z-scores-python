from statistics import mean, pstdev


def calculate(data):

    """
    Returns a dictionary containing:
    The arithmetic mean of the data
    The population standard deviation of the data
    A list of dictionaries containing each data value
    and its corresponding Z-Score.
    """

    arithmetic_mean = mean(data)
    standard_deviation_population = pstdev(data)

    zscores = []

    for item in data:
        zscore = (item - arithmetic_mean) / standard_deviation_population
        zscores.append({"Value": item, "Z-Score": zscore})

    result = {"arithmetic_mean": arithmetic_mean,
              "standard_deviation_population": standard_deviation_population,
              "zscores": zscores}

    return result
