"""CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class."""

from cp1404practicals.prac_06.programming_language import ProgrammingLanguage


def main():
    """Test programming language class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)

    programming_languages = [python, ruby, visual_basic]
    dynamic_typing_languages = [language for language in programming_languages if language.is_dynamic()]
    print("The dynamically typed languages are:")
    for dynamic_language in dynamic_typing_languages:
        print(dynamic_language.name)


if __name__ == '__main__':
    main()
