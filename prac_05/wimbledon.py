"""
Wimbledon
Estimate: 25 minutes
Actual:   40 minutes
"""
WINNING_COUNTRY_INDEX = 1
CHAMPION_NAME_INDEX = 2
FILENAME = "wimbledon.csv"


def main():
    """Apply various functions to display requested results."""

    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        wimbledon_infos = read_file_into_list(in_file)
        champion_to_victory = collect_champion_wins(wimbledon_infos)
        winning_countries = collect_winning_countries(wimbledon_infos)
    winning_countries = sorted(winning_countries)

    maximum_name_length = max(len(champion) for champion in list(champion_to_victory.keys()))
    print("Wimbledon Champions:")

    for champion, wins in (champion_to_victory.items()):
        print(f"{champion:<{maximum_name_length}} {wins}")

    print()
    print(f"These {len(winning_countries)} countries have won Wimbledon:")
    print(", ".join(winning_countries))


def collect_winning_countries(wimbledon_infos):
    """Store winning countries into a set."""
    winning_countries = set()
    for info in wimbledon_infos:
        winning_countries.add(info[WINNING_COUNTRY_INDEX])
    return winning_countries


def collect_champion_wins(wimbledon_infos):
    """Create champion_to_wins dictionary."""
    champion_to_victory = {}
    for info in wimbledon_infos:
        champion_to_victory[info[CHAMPION_NAME_INDEX]] = champion_to_victory.get(info[CHAMPION_NAME_INDEX], 0) + 1
    return champion_to_victory


def read_file_into_list(in_file):
    """Read the csv file data into a list."""
    wimbledon_infos = [line.strip().split(",") for line in in_file.readlines()][1:]
    return wimbledon_infos


main()
