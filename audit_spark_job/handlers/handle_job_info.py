"""
    This module prints the data flow for this job. Used for development and training.
    This is not intended to pe used in production.
"""

# Standard Library Imports <- This is not required but useful to separate out imports
from helper_printer import print_header


def job_diagram() -> None:
    """
    Prints a basic data flow diagram for this job

    Examples:
        job_diagram()

    Returns:
        Void
    """
    # https://altcodeslist.com
    print_header(
        " 2 AUDIT JOB                                                                                                \n"
        "                                                                                                            \n"
        "          ┌             ┌──────┐                                                                            \n"
        "          │             │source│                                                                            \n"
        "EXTRACT───┤             └──╥───┘                                                                            \n"
        "          │            ╔═══╩════╗                                                                           \n"
        "          │            ║  READ  ║                                                                           \n"
        "          │            ╚═══╦════╝                     ┐─────────────┌                                       \n"
        "          │                ╠══════════════════════════╡ INPUT AUDIT │                                       \n"
        "          │                ║                          │    VALUES   │                                       \n"
        "          └                ║                          ┘────╥────────└                                       \n"
        "          ┌          ╔═════╩═══════╗                       ║                                                \n"
        "          │          ║ CHANGE TYPE ║                       ║                                                \n"
        "          │          ╚══════╦══════╝                  ┐────╨────────┌                                       \n"
        "          │                 ╠═════════════════════════╡ INPUT AUDIT │                                       \n"
        "          │     ╔══════╦════╩═══╦════════╗            │    VALUES   │                                       \n"
        "          │ ┌───╨──┐┌──╨───┐┌───╨──┐┌────╨────┐       ┘────╥────────└                                       \n"
        "          │ │delete││update││insert││no_change│            ║                                                \n"
        "TRANSFORM─┤ └───╥──┘└───╥──┘└───╥──┘└─────────┘            ║                                                \n"
        "          │     ║ ╔═════╩═════╗ ║                          ║                                                \n"
        "          │     ║ ║ UPPERCASE ║ ║                          ║                                                \n"
        "          │     ║ ║  STRINGS  ║ ║                          ║                                                \n"
        "          │     ║ ╚═════╦═════╝ ║                          ║                                                \n"
        "          │     ╚═══════╩═══╦═══╝                          ║                                                \n"
        "          │            ╔════╩═════╗                        ║                                                \n"
        "          │            ║ PERCENT  ║                        ║                                                \n"
        "          │            ║ OF TOTAL ║                        ║                                                \n"
        "          └            ╚════╦═════╝                        ║                                                \n"
        "          ┌             ╔═══╩═══╗                          ║                                                \n"
        "          │             ║ WRITE ║                          ║                                                \n"
        "LOAD──────┤             ╚═══╦═══╝                          ║                                                \n"
        "          │           ┌─────╨─────┐                        ║                                                \n"
        "          │           │destination│                        ║                                                \n"
        "          └           └─────╥─────┘                        ║                                                \n"
        "          ┌             ╔═══╩════╗                         ║                                                \n"
        "          │             ║  READ  ║                         ║                                                \n"
        "          │             ╚═══╦════╝                         ║                                                \n"
        "          │           ┐─────╨────────┌                     ║                                                \n"
        "          │           │ OUTPUT AUDIT │                     ║                                                \n"
        "          │           │    VALUES    │                     ║                                                \n"
        "          │           ┘───────────╥──└   ╔═════════════════╝                                                \n"
        "          │                     ┐─╨──────╨──┌                                                               \n"
        "          │                     │ RUN AUDIT │                                                               \n"
        "AUDIT─────┤                     ┘─╥───────╥─└                                                               \n"
        "          │                   ╔═══╩═══╗╔══╩════╗                                                            \n"
        "          │                   ║ WRITE ║║ ALERT ║                                                            \n"
        "          │                   ╚═══╦═══╝╚═══════╝                                                            \n"
        "          │                 ┌─────╨─────┐                                                                   \n"
        "          │                 │destination│                                                                   \n"
        "          └                 └───────────┘                                                                   \n"
    )
    print_header(
        " LEGEND                                        DATA╗     ┌─────┐ ┐─────┌ ┼─────┼ ╔════════╗ ╗═════╔ ╬═════╬ \n"
        "                                               ╔═══╬══╦═ │state│ │AUDIT│ │     │ ║ ACTION ║ ║     ║ ║     ║ \n"
        "                                                   FLOW  └─────┘ ┘─────└ ┼─────┼ ╚════════╝ ╝═════╚ ╬═════╬ \n"
    )
    return None


if __name__ == '__main__':
    job_diagram()
