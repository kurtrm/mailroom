"""Function to run if the user wants to send a thank you note."""
import os
import sys


def clear_screen():  # pragma no cover
    """Taken from the Treehouse shopping_list exercise."""
    os.system("cls" if os.name == "nt" else "clear")


donors_info = {
    'Sam Wippy': [100000],
    'Willy Wonka': [12, 13, 14],
    'Garth Brooks': [1]
}


def send_thank_you():  # pragma no cover
    """Give user choices to send a thank you note to a donor."""
    clear_screen()
    while True:
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
            add_new_or_update_donar_info(full_name)


def add_new_or_update_donor_info(full_name):  # pragma no cover
    """Take care of managing user input into our data table."""
    clear_screen()
    if full_name not in [key.lower() for key in donors_info.keys()]:
        donors_info[full_name.title()] = []
    while True:
        donation_amount = input("Enter donation amount: ")
        try:
            donation_amount = int(donation_amount)
            if donation_amount < 0:
                clear_screen()
                print("Please enter a positive donation amount.")
                continue
            donors_info[full_name.title()].append(
                donation_amount)
            print('Added ${1} to {0}\'s donation history.'.format(
                full_name.title(), donation_amount))
            break
        except ValueError:
            clear_screen()
            print("Please enter a positive, numerical donation amount.")
            continue
    print("""
    ==================================

    Dear {name},

    Thank you for your generous donation of ${amount}. We have so many things
    that we have to do better... and certainly ipsum is one of them.
    Lorem Ispum is a choke artist. It chokes! I think my strongest asset maybe
    by far is my temperament. I have a placeholding temperament.

    Your donation of ${amount} goes toward accomplishing really cool shit at
    this place. Lorem Ipsum is the single greatest threat.
    We are not - we are not keeping up with other websites. When other websites
    give you text, they’re not sending the best. They’re not sending you,
    they’re sending words that have lots of problems and they’re bringing
    those problems with us. They’re bringing mistakes.
    They’re bringing misspellings.

    {name}, they’re typists… And some, I assume, are good words.
    An ‘extremely credible source’ has called my office and told me that Barack
    Obama’s placeholder text is a fraud. I think the only difference between
    me and the other placeholder text is that I’m more honest and my words are
    more beautiful. If Trump Ipsum weren’t my own words, perhaps I’d be dating
    it.

    Sincerely,


    The Pants Foundation

    ==================================""".format(name=full_name.title(),
                                                 amount=donors_info[full_name
                                                 .title()][-1]))


def create_report(donors_info):  # pragma no cover
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


def main():  # pragma no cover
    """The main function."""
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


if __name__ == '__main__':  # pragma no cover
    main()
