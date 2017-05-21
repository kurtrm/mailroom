"""Function to run if the user wants to send a thank you note."""
import sys
list_of_donor_names = {'Sam I am': [100000], 'Willy F. Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def send_thank_you():
    """Give user choices to send a thank you note to a donor."""
    while True:
        full_name = input(
            """Enter the full name of the person you'd like to send a thank you to.
            Type 'list' to see a list of previous donors.
            Type 'back' to return to the main menu.
            Type 'quit' to quit the program.\n
            > """).lower()
        if full_name == 'quit':
            # This isn't working the way we need it to.
            sys.exit()
        elif full_name == 'back':
            break
        elif full_name == 'list':
            print(sorted(list_of_donor_names.keys()), '\n')
        else:
            if full_name not in list_of_donor_names.keys().lower():
                list_of_donor_names[full_name] = []
            while True:
                donation_amount = input("Enter donation amount: ")
                try:
                    donation_amount = int(donation_amount)
                    list_of_donor_names[full_name].append(donation_amount)
                    print(sorted(list_of_donor_names.items()))
                    break
                except ValueError:
                    print("Please enter a valid, numerical donation.")
                    continue
        # if isinstance(donation_amount, int) and donation_amount >= 0:
        #     Perform entry validation
        #     ask_for_a_number
        # else:
        #     append_donation_amount_to_the_value_in_dictionary_which_is_a_list
        # print(f"Thank you for generous donation {full_name}.")
        # return to original prompt
