from lib.stats_lib import mean, median, mode, variance, sd

def main():
    data = [1, 2, 2, 3, 4]

    print(f"Mean: {mean(data)}")
    print(f"Median: {median(data)}")
    print(f"Mode: {mode(data)}")
    print(f"Variance: {variance(data)}")
    print(f"Standard Deviation: {sd(data)}")

if __name__ == "__main__":
    main()