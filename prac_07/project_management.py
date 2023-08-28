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
            projects.sort()

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
                print(incomplete_project)
            complete_projects = [project for project in projects if project.completion_percentage ==
                                 COMPLETE_PERCENTAGE]
            print("Completed projects: ")
            for complete_project in complete_projects:
                print(complete_project)

        elif user_option == 'F':
            after_date_string = input("Show projects that start after date (dd/mm/yy): ")
            after_date = datetime.datetime.strptime(after_date_string, "%d/%m/%Y").date()
            print(f"That day is/was {after_date.strftime('%A')}")
            print(after_date.strftime("%d/%m/%Y"))
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

            for after_date_project in sort_by_after_date_projects:
                print(after_date_project)

        elif user_option == 'A':
            print("Let's add a new project")
            new_project_name = input("Name: ")
            new_project_start = input("Start date (dd/mm/yy): ")
            new_project_priority = int(input("Priority: "))
            new_project_cost = float(input("Cost estimate: $"))
            new_project_percent = int(input("Percent complete: "))
            new_project = Project(new_project_name, new_project_start, new_project_priority,
                                  new_project_cost, new_project_percent)
            projects.append(new_project)
            projects.sort()

        else:  # user_option == 'U'
            number_to_project = {i: project for i, project in enumerate(projects, 0)}

            for i in number_to_project.keys():
                print(f"{i} {number_to_project[i]}")
            project_choice = int(input("Project choice: "))
            # TODO: error checking
            updated_project = number_to_project[project_choice]
            print(updated_project)
            print(type(updated_project))
            try:
                update_percentage = int(input("New Percentage: "))
                updated_project.update_project_percentage(update_percentage)
                update_priority = int(input("New Priority: "))
                updated_project.update_project_priority(update_priority)
            except ValueError:
                pass


        print(MENU)
        user_option = input(">>> ").upper()


if __name__ == '__main__':
    main()
