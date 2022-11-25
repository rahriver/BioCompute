from statistics import mean, median, mode, stdev, variance

# Calculates mean, median, mode, standard deviation, and variance
def statis(*nums):

    print("Mean:", mean(nums))
    print("Median:", median(nums))
    print("Mode:", mode(nums))
    print("Sum", sum(nums))
    print("Stdev:", round(stdev(nums), 2))
    print("Variance:", round(variance(nums), 2))

# Reads in numbers from user and calculates statistics with some conditions
def run():

    while True:
        nums = input("Enter numbers separated by comma: ").split(',')
        if nums != [""]:
            nums = [int(i) for i in nums]
            statis(*nums)
            save = input("Save to file? (y/n): ")

            if save == "y":
                csv = input("CSV or TXT? (csv/txt): ")

                if csv == "csv":
                    with open("stat.csv", "w") as f:
                        f.write(f"Mean: {mean(nums)}" + "\n")
                        f.write(f"Median: {median(nums)}" + "\n")
                        f.write(f"Mode: {mode(nums)}" + "\n")
                        f.write(f"Sum: {sum(nums)}" + "\n")
                        f.write(f"Stdev: {round(stdev(nums), 2)}" + "\n")
                        f.write(f"Variance: {round(variance(nums), 2)}" + "\n")
                        print("Saved to stat.csv...")
                        break
                elif csv == "txt":
                    with open("stat.txt", "w") as f:
                        f.write(f"Mean: {mean(nums)}" + "\n")
                        f.write(f"Median: {median(nums)}" + "\n")
                        f.write(f"Mode: {mode(nums)}" + "\n")
                        f.write(f"Sum: {sum(nums)}" + "\n")
                        f.write(f"Stdev: {round(stdev(nums), 2)}" + "\n")
                        f.write(f"Variance: {round(variance(nums), 2)}" + "\n")
                        print("Saved to stat.txt...")
                        break
            elif save == "n":
                cont = input("Continue? (y/n): ")
                while cont != "y" and cont != "n":
                    print("Invalid input")
                    cont = input("Continue? (y/n): ")
                if cont == "n":
                    print("Bye!")
                    break
                elif cont == "y":
                    continue
        else:
            print("Please enter numbers!")

run()
