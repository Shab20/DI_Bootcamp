import random


def get_random_temp(season_int):
    """Generate a random float between -10 (inclusive) and 40 (inclusive/exclusive).
    Return the generated float.
    """

    spring = "spring"
    summer = "summer"
    autumn = "autumn"
    winter = "winter"

    season = ""
    if season_int >= 3 and season_int <= 5:
        season = spring
    elif season_int >= 6 and season_int <= 8:
        season = summer
    elif season_int >= 9 and season_int <= 11:
        season = autumn
    elif (season_int >= 1 and season_int <= 2) or season_int == 12:
        season = winter
    else:
        print(f"We received a bad value for season. ({season_int})")

    season_limits = {
        summer: {"lower": 33, "upper": 40},
        autumn: {"lower": 24, "upper": 33},
        winter: {"lower": -10, "upper": 17},
        spring: {"lower": 17, "upper": 24},
    }

    random_float = random.uniform(
        season_limits[season]["lower"], season_limits[season]["upper"]
    )
 
    return random_float


def main():

    user_season_int = 0

    while user_season_int <= 0 or user_season_int >= 13:
        user_season_int = int(input("Please enter the season (1-12): "))

    random_temperature = get_random_temp(user_season_int)

    print(f"The temperature right now is {random_temperature} degrees Celsius.")

    if random_temperature < 0:
        print(f"Brrr, that’s freezing! Wear some extra layers today")
    elif random_temperature >= 0 and random_temperature < 16:
        print(f"Quite chilly! Don’t forget your coat")
    elif random_temperature >= 16 and random_temperature < 24:
        print(f"Nice weather")
    elif random_temperature >= 24 and random_temperature < 32:
        print(f"It's getting hot out here")
    elif random_temperature >= 32 and random_temperature < 40:
        print(f"It's way too hot, I'm staying at home.")
    else:
        print(f"Woops, something went wrong, the temperature is way too high!")


main()
