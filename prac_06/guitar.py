"""CP1404/CP5632 Practical - Guitar class.
Estimate: 20 minutes
Time started: 11:25
Time finished:
"""


class Guitar:
    """Represent a guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Construct a guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return the guitar info."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Calculate how old the guitar is in years."""
        return 2023 - self.year


