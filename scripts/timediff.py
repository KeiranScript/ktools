import click
from datetime import datetime
from dateutil.relativedelta import relativedelta


class bcolors:
    HEADER = "\033[95m"
    OKBLUE = "\033[94m"
    OKCYAN = "\033[96m"
    OKGREEN = "\033[92m"
    WARNING = "\033[93m"
    FAIL = "\033[91m"
    ENDC = "\033[0m"
    BOLD = "\033[1m"
    UNDERLINE = "\033[4m"


@click.command()
@click.argument("start_date", type=str)
@click.argument("end_date", type=str)
@click.option(
    "--unit",
    type=click.Choice(["days", "hours", "minutes", "months"], case_sensitive=False),
    default="days",
    help="The unit of time to represent the difference.",
)
def main(start_date, end_date, unit):
    """Calculate the time difference between two dates."""
    date_format = "%d/%m/%Y"

    try:
        start = datetime.strptime(start_date, date_format)
        end = datetime.strptime(end_date, date_format)
    except ValueError:
        print(
            bcolors.FAIL
            + f"Error: Dates must be in 'DD/MM/YYYY' format."
            + bcolors.ENDC
        )
        return

    if start > end:
        print(
            bcolors.FAIL + "Error: Start date must be before end date." + bcolors.ENDC
        )
        return

    # Calculate the difference based on the unit
    if unit == "days":
        difference = (end - start).days
    elif unit == "hours":
        difference = (end - start).total_seconds() / 3600
    elif unit == "minutes":
        difference = (end - start).total_seconds() / 60
    elif unit == "months":
        difference = relativedelta(end, start).months + (
            relativedelta(end, start).years * 12
        )

    print(
        bcolors.OKGREEN
        + f"The difference between {start_date} and {end_date} is {difference} {unit}."
        + bcolors.ENDC
    )


if __name__ == "__main__":
    main()
