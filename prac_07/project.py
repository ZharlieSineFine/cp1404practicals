"""CP1404/CP5632 Practical - Project class.
Estimate: 40 minutes
Time started: 13:25
Time finished: 13:54
"""


class Project:
    """Represent a project object."""

    def __init__(self, name="", start_date="", priority=0, cost_estimate=0.0, completion_percentage=0):
        """Construct a project instance."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __str__(self):
        """Return string of a project."""
        return (f"{self.name} starts at {self.start_date}, its priority is {self.priority}.It costs roughly "
                f"around {self.cost_estimate}. {self.completion_percentage} of the project has been completed.")

    def __repr__(self):
        """Return representation of a project class."""
        return (f"{self.name} starts at {self.start_date}, its priority is {self.priority}.It costs roughly "
                f"around {self.cost_estimate}. {self.completion_percentage} of the project has been completed.")

    def __lt__(self, other):
        """Compare if the current project's priority is less than others."""
        return self.priority < other.priority

    def __eq__(self, other):
        """Compare if the current project's priority is equal to others."""
        return self.priority == other.priority

    def __le__(self, other):
        """Compare if the current project's priority is less than or equal to others."""
        return self.priority <= other.priority

    def __gt__(self, other):
        """Compare if the current project's priority is greater than others."""
        return self.priority > other.priority

    def update_project(self, new_percentage, new_priority):
        """Update the completion percentage and priority of the project."""
        self.completion_percentage = new_percentage
        self.priority = new_priority


