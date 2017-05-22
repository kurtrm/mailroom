"""Function to run if the user wants to send a thank you note."""
import os
import sys


def clear_screen():
    """Taken from the Treehouse shopping_list exercise."""
    os.system("cls" if os.name == "nt" else "clear")


donors_info = {
    'Sam Wippy': [100000],
    'Willy Wonka': [12, 13, 14],
    'Garth Brooks': [1]
}


def send_thank_you():
    """Give user choices to send a thank you note to a donor."""
    clear_screen()
    while True:
        # clear_screen()
        full_name = input(
            """Enter the full name of the person you'd like to send a thank you to. Or:
        [L] to see a list of previous donors.
        [B] 'back' to return to the main menu.
        [Q] to quit the program.
        > """).lower()
        if full_name == 'q':
            sys.exit()
        elif full_name == 'b':
            break
        elif full_name == 'l':
            for key in sorted(donors_info.keys()):
                print(key)
        else:
            full_name_not_in_list(full_name)


def full_name_not_in_list(full_name):
    """Take care of managing user input into our data table."""
    clear_screen()
    if full_name not in [key.lower() for key in donors_info.keys()]:
        donors_info[full_name.title()] = []
    while True:
        donation_amount = input("Enter donation amount: ")
        try:
            donation_amount = int(donation_amount)
            donors_info[full_name.title()].append(
                donation_amount)
            print('Added ${1} to {0}\'s donation history.'.format(
                full_name.title(), donation_amount))
            break
        except ValueError:
            clear_screen()
            print("Please enter a valid, numerical donation amount.")
            continue
    print("")
    print('''Email body:''')
    print('''{name}, '''
          .format(
              name=full_name.title()))
    print("")
    print('''Thank you for your generous donation of ${amount}.
        Your donation goes toward accomplishing really cool shit at this place.
        '''
          .format(
              amount=donors_info[full_name.title()][-1]))
    print("")
    print("Sincerely,")
    print("")
    print("The Pants Foundation")
    print("")
    print("")


def create_report(donors_info):
    """Make a list for each column from dict data then populate
    row data into a table.
    """
    donor_name = list(donors_info.keys())
    donation = donors_info.values()
    num_of_donation = [len(a) for a in donation]
    total_donation = [sum(a) for a in donation]
    average_donation = [int(sum(a) / len(a)) for a in donation]
    sorted_donations = sorted(list(zip(
        donor_name,
        total_donation,
        num_of_donation,
        average_donation)), key=lambda tup: tup[1], reverse=True)
    clear_screen()
    print(
        "\nDonor Name{}"
        "Total Amount{}"
        "Number of Donations{}"
        "Average Donation Amount{}"
        .format(
            ' ' * 20,
            ' ' * 18,
            ' ' * 11,
            ' ' * 8
        ))
    for row in sorted_donations:
        print('{}{}{}{}{}{}{}{}'.format(
            row[0], ' ' * (30 - len(str(row[0]))),
            row[1], ' ' * (30 - len(str(row[1]))),
            row[2], ' ' * (30 - len(str(row[2]))),
            row[3], ' ' * (30 - len(str(row[3])))))
    print('\n')


if __name__ == '__main__':
    while True:
        user_menu = input(
            """Welcome to the Mailroom-Tron 3000 v1.5. Type your user selection:
        [E] to EMAIL an existing donor or new donor.
        [R] for REPORT of donors and their donations.
        [Q] to quit the program.
        > """)
        if user_menu.lower() == 'q':
            break
        elif user_menu.lower() == 'e':
            send_thank_you()
            continue
        elif user_menu.lower() == 'r':
            create_report(donors_info)
            continue
