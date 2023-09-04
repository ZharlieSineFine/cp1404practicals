"""CP1404/CP5632 Practical - Client code to use the Project class.
Estimate: 140 minutes
Time started: 13:40
Time finished: 18:50
"""

import datetime
from project import Project

MENU = (
    "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- "
    "(U)pdate project\n- (Q)uit")
FILENAME = 'projects.txt'
VALID_OPTIONS = ('L', 'S', 'D', 'F', 'A', 'U', 'Q')
NAME_INDEX = 0
START_DATE_INDEX = 1
PRIORITY_INDEX = 2
COST_INDEX = 3
PERCENTAGE_INDEX = 4
COMPLETE_PERCENTAGE = 100


def main():
    """Combine each functions to work as a project management device."""
    projects = []

    projects, project_info_categories = load_file(FILENAME, projects)
    projects.sort()

    print(MENU)
    user_option = input(">>> ").upper()
    while user_option != 'Q':
        if user_option == 'L':
            load_filename = input("Filename: ")
            is_valid_filename = False
            while not is_valid_filename:
                try:
                    projects, project_info_categories = load_file(load_filename, projects)
                    is_valid_filename = True
                except FileNotFoundError:
                    print("Invalid filename.")
                    load_filename = input("Filename: ")
            projects.sort()

        elif user_option == 'S':
            save_filename = input("Filename: ")
            save_file(project_info_categories, projects, save_filename)

        elif user_option == 'D':
            display_incomplete_projects(projects)
            display_complete_projects(projects)

        elif user_option == 'F':
            after_date_prompt = "Show projects that start after date (dd/mm/yy): "
            after_date = get_valid_date(after_date_prompt)
            sort_by_after_date_projects = sort_by_after_date(after_date, projects)
            for after_date_project in sort_by_after_date_projects:
                print(after_date_project)

        elif user_option == 'A':
            print("Let's add a new project")
            try:
                new_project_name = input("Name: ")
                new_project_start = get_valid_date("Start date (dd/mm/yy): ")
                new_project_priority = int(input("Priority: "))
                new_project_cost = float(input("Cost estimate: $"))
                new_project_percent = int(input("Percent complete: "))
                new_project = Project(new_project_name, new_project_start.strftime("%d/%m/%Y"), new_project_priority,
                                      new_project_cost, new_project_percent)
                projects.append(new_project)
                projects.sort()
            except ValueError:
                print("Invalid input.")

        elif user_option == 'U':
            number_to_project = {i: project for i, project in enumerate(projects, 0)}
            for i in number_to_project.keys():
                print(f"{i} {number_to_project[i]}")
            project_choice = get_valid_project_choice(number_to_project)

            updated_project = number_to_project[project_choice]
            print(updated_project)
            try:
                update_percentage = int(input("New Percentage: "))
                updated_project.update_project_percentage(update_percentage)
                update_priority = int(input("New Priority: "))
                updated_project.update_project_priority(update_priority)
            except ValueError:
                pass  # Based on the sample output, if an invalid input occurs, the program will jump to the menu
        else:
            print("Invalid option.")
        print(MENU)
        user_option = input(">>> ").upper()
    save_file(project_info_categories, projects, FILENAME)
    print("Thank you for using custom-built project management software.")


def get_valid_project_choice(number_to_project):
    """Get valid project choice."""
    project_choice = int(input("Project choice: "))
    while project_choice not in number_to_project.keys():
        print("Invalid choice.")
        project_choice = int(input("Project choice: "))
    return project_choice


def sort_by_after_date(after_date, projects):
    """Sort the projects by the after_date."""
    after_date_projects = [project for project in projects
                           if datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
                           >= after_date]
    sort_by_after_date_projects = []
    qualified_dates = [datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date()
                       for project in after_date_projects]
    qualified_dates.sort()
    for date in qualified_dates:
        for project in after_date_projects:
            if date == datetime.datetime.strptime(project.start_date, "%d/%m/%Y").date():
                sort_by_after_date_projects.append(project)
    return sort_by_after_date_projects


def get_valid_date(prompt):
    """Get valid date."""
    date_string = input(prompt)
    valid_date = None
    is_valid_date = False
    while not is_valid_date:
        try:
            valid_date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
            is_valid_date = True
        except ValueError:
            print("Invalid date")
            date_string = input(prompt)
    return valid_date


def display_complete_projects(projects):
    """Display all the projects."""
    complete_projects = [project for project in projects if project.completion_percentage ==
                         COMPLETE_PERCENTAGE]
    print("Completed projects: ")
    for complete_project in complete_projects:
        print(complete_project)


def display_incomplete_projects(projects):
    """Display incomplete projects."""
    incomplete_projects = [project for project in projects if project.completion_percentage
                           != COMPLETE_PERCENTAGE]
    print("Incomplete projects: ")
    for incomplete_project in incomplete_projects:
        print(incomplete_project)


def save_file(project_info_categories, projects, save_filename):
    """Save the content to the file."""
    out_file = open(save_filename, 'w')
    print("\t".join(category for category in project_info_categories), file=out_file)
    for project in projects:
        project_to_write = [project.name, project.start_date, project.priority, project.cost_estimate,
                            project.completion_percentage]
        print("\t".join(str(element) for element in project_to_write), file=out_file)
    out_file.close()


def load_file(load_filename, projects):
    """Load the input file and read its content."""
    in_file = open(load_filename, 'r')
    project_info_categories = in_file.readline().strip().split('\t')
    for line in in_file:
        elements = line.strip().split('\t')
        loaded_project = Project(elements[NAME_INDEX], elements[START_DATE_INDEX],
                                 int(elements[PRIORITY_INDEX]),
                                 float(elements[COST_INDEX]), int(elements[PERCENTAGE_INDEX]))
        projects.append(loaded_project)

    # print(f"{len(projects)} projects has been read and stored into the projects list.")

    in_file.close()
    return projects, project_info_categories


if __name__ == '__main__':
    main()
