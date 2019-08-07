import zscores


def main():

    print("-----------------")
    print("| codedrome.com |")
    print("| Z-Scores      |")
    print("-----------------\n")

    physics_results = [38,40,43,43,49,54,55,57,61,62,62,63,64,64,65,66,66,67,68,68,69,75,76,78,78,79,80,82,85,87]
    history_results = [53,55,58,58,64,68,69,69,69,70,70,72,76,76,77,77,77,77,78,79,79,79,79,80,80,81,81,83,86,88]

    physics_zscores = zscores.calculate(physics_results)
    history_zscores = zscores.calculate(history_results)

    print_zscores("Physics", physics_zscores)
    print_zscores("History", history_zscores)


def print_zscores(subject, zscores):

    """
    Print the mean, standard deviation and z-scores
    in the zscores dictionary in a grid format.
    """

    width = 28

    print("-" * width)
    print("| {:^24} |".format(subject))
    print("-" * width)
    print("| Mean        {:>12.2f} |".format(zscores["arithmetic_mean"]))
    print("| Std.Dev.    {:>12.2f} |".format(zscores["standard_deviation_population"]))
    print("-" * width)
    print("|   Scores   |  Z-Scores   |")
    print("-" * width)

    for item in zscores["zscores"]:
        print("|{:>12.2f}| {:>12.2f}|".format(item["Value"], item["Z-Score"]))

    print("-" * width)


main()
