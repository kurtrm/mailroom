"""Function to run if the user wants to send a thank you note."""
import os
import sys

"""won't implement clearing screen yet for debugging"""
# def clear_screen():
#     """Taken from the Treehouse shopping_list exercise."""
#     os.system("cls" if os.name == "nt" else "clear")


list_of_donor_names = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}

while True:
    user_menu = input("Type EMAIL, REPORT, or QUIT >")

    if user_menu.lower() == "quit":
        break

    elif user_menu.lower() == "email":
        send_thank_you()
        continue
    elif user_menu.lower() == "report":
        create_report()
        continue

def send_thank_you():
    """Give user choices to send a thank you note to a donor."""
    # clear_screen()
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
            for key in sorted(list_of_donor_names.keys()):
                print(key)
        else:
            full_name_not_in_list(full_name)


def full_name_not_in_list(full_name):
    if full_name not in [key.lower() for key in list_of_donor_names.keys()]:
        list_of_donor_names[full_name.title()] = []
    while True:
        donation_amount = input("Enter donation amount: ")
        try:
            donation_amount = int(donation_amount)
            list_of_donor_names[full_name.title()].append(
                donation_amount)
            print('Added {1} to {0}\'s donation history.'.format(
                full_name.title(), donation_amount))
            break
        except ValueError:
            print("Please enter a valid, numerical donation amount.")
            continue
    print('''Email sent:
{name},\n Thank you for your generous donation of ${amount}.
Your donation goes toward accomplishing really cool shit at this place.'''.format(
            name=full_name.title(),
            amount=list_of_donor_names[full_name.title()][-1]))
    send_thank_you()
