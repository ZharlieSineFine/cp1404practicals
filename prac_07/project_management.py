"""CP1404/CP5632 Practical - Client code to use the Project class.
Estimate: 40 minutes
Time started: 13:40
Time finished: 14:24
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
    projects = []
    project_info_categories = []

    print(MENU)
    user_option = input(">>> ").upper()
    while user_option != 'Q':
        if user_option == 'L':
            in_file = open(FILENAME, 'r')
            project_info_categories = in_file.readline().strip().split('\t')
            print(project_info_categories)
            for line in in_file:
                elements = line.strip().split('\t')
                loaded_project = Project(elements[NAME_INDEX], elements[START_DATE_INDEX],
                                         int(elements[PRIORITY_INDEX]),
                                         float(elements[COST_INDEX]), int(elements[PERCENTAGE_INDEX]))
                projects.append(loaded_project)
            print(f"{len(projects)} projects has been read and stored into the projects list.")
            print(projects)
            in_file.close()

        elif user_option == 'S':
            out_file = open(FILENAME, 'w')
            print("\t".join(category for category in project_info_categories), file=out_file)
            for project in projects:
                project_to_write = [project.name, project.start_date, project.priority, project.cost_estimate,
                                    project.completion_percentage]
                print("\t".join(element for element in project_to_write), file=out_file)
            out_file.close()

        elif user_option == 'D':
            incomplete_projects = [project for project in projects if project.completion_percentage
                                   != COMPLETE_PERCENTAGE]
            print("Incomplete projects: ")
            for incomplete_project in incomplete_projects:
                print()
            print(incomplete_projects)

        print(MENU)
        user_option = input(">>> ").upper()


if __name__ == '__main__':
    main()
