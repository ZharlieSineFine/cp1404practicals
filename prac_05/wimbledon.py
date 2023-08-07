"""
Emails
Estimate: 25 minutes
Actual:   40 minutes
"""


def main():
    """Apply various functions to display requested results."""
    champion_to_victory = {}
    countries = set()
    filename = "wimbledon.csv"
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        wimbledon_infos = read_file_into_list(in_file)
        for info in wimbledon_infos:
            champion_to_victory[info[2]] = champion_to_victory.get(info[2], 0) + 1

        # countries.add(detail[1])
    countries = sorted(countries)

    # print(wimbledon_info)
    print(champion_to_victory)
    print(f"These {len(countries)} countries have won Wimbledon:")
    print(", ".join(countries))


def read_file_into_list(in_file):
    """Read the csv file data into a list."""
    wimbledon_infos = [line.strip().split(",") for line in in_file.readlines()][1:]
    return wimbledon_infos


main()
