"""Function to run if the user wants to send a thank you note."""
import os
import sys


def clear_screen():
    """Taken from the Treehouse shopping_list exercise."""
    os.system("cls" if os.name == "nt" else "clear")


list_of_donor_names = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def send_thank_you():
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
            # This exits the program but gives a SystemExit exception.
            # I'd like to exit without this exception.
            sys.exit()
        elif full_name == 'b':
            # This will break from this while loop and the function.
            # It should return to the main() loop.
            break
        elif full_name == 'l':
            # This for loop prints a list of names.
            # Should we consider printing the donation history too?
            for key in sorted(list_of_donor_names.keys()):
                print(key)
        else:
            # Since the keys() method returns an iterable, we have to make it
            # a list in order to do our comparison.
            # This checks to see if the name entered is in the list already.
            # If it isn't, it adds it and makes an empty list its value.
            if full_name not in [key.lower() for key in list_of_donor_names.keys()]:
                list_of_donor_names[full_name.title()] = []
            while True:
                # We enter a while loop here for donation validation.
                # the input() function will always return a string,
                # so I used a a try, except here to see if we can make a number
                # out of what they entered.
                # The loop continues while their input is invalid.
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
            # Lastly, it prints the email to the screen.
            # The while loop restarts until the user wants
            # to quit or return to the main screen.
            print('''Email sent:
{name},\n thank you for your generous donation of ${amount}.
Your donation goes toward accomplishing really cool shit at this place.'''
                .format(
                    name=full_name.title(),
                    amount=list_of_donor_names[full_name.title()][-1]))
