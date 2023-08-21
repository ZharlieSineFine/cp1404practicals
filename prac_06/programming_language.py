"""CP1404/CP5632 Practical - ProgrammingLanguage class.
Estimated: 10 minutes
Time started: 10:39
Time finished: """


class ProgrammingLanguage:
    """Represent a programming language object."""

    def __init__(self, name="", typing="", reflection=True, year=None):
        """Initialize a programming language instance."""
        self.name = name
        self.typing = typing.title()
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Check if the language typing is dynamic."""
        if self.typing == "Dynamic":
            return True
        else:
            return False
