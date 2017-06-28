"""Modified versions of mailroom functions for testing."""

donors_info = {
    'Sam Wippy': [100000],
    'Willy Wonka': [12, 13, 14],
    'Garth Brooks': [1]
}

#  send_thank_you() is not practically testable.
#  It contains mostly inputs and prints which Nick told us was
#  not worth diving into tests for.


def add_new_or_update_donor_info(full_name, test_var):
    """Take care of managing user input into our data table."""
    if full_name not in [key.lower() for key in donors_info.keys()]:
        donors_info[full_name.title()] = []
        donation_amount = test_var
        try:
            donation_amount = float(donation_amount)
            if donation_amount < 0:
                return "Please enter a positive donation amount."
            donors_info[full_name.title()].append(
                donation_amount)
        except ValueError:
            print("Please enter a valid, numerical donation amount.")
            return
    return 'TEST NOTE'


def create_report(donors_info):
    """Make a list for each column from dict data then populate
    row data into a table.
    """
    donor_names = list(donors_info.keys())
    donations = donors_info.values()
    num_of_donations = [len(total) for total in donations]
    total_donations = [sum(total) for total in donations]
    average_donation = [int(sum(a) / len(a)) for a in donations]
    sorted_donations = sorted(list(zip(
        donor_names,
        total_donations,
        num_of_donations,
        average_donation)), key=lambda tup: tup[1], reverse=True)
    return sorted_donations
