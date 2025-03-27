# Constants for time conversion
DAYS_PER_YEAR: int = 365
HOURS_PER_DAY: int = 24
MIN_PER_HOUR: int = 60
SEC_PER_MIN: int = 60

def main():
    # Calculate seconds in a year using the constants
    seconds_per_year: int = DAYS_PER_YEAR * HOURS_PER_DAY * MIN_PER_HOUR * SEC_PER_MIN


    print(f"There are {seconds_per_year} seconds in a year!")




if __name__ == '__main__':
    main()
