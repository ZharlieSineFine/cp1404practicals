"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from cp1404practicals.prac_06.programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)


if __name__ == '__main__':
    main()
