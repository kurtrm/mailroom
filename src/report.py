"""funciton to run if user choose to make a report on donor information"""


donors_info = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def create_report(donors_info):
    """making a list for each column from dict data then populate row data into a table"""
    donor_list = [] # For tests
    donor_name = list(donors_info.keys())
    donation = donors_info.values()
    num_of_donation = [len(a) for a in donation]
    total_donation = [sum(a) for a in donation]
    average_donation = [sum(a)/len(a) for a in donation]
    sorted_donations = sorted(list(zip(donor_name, total_donation, num_of_donation, average_donation)), key=lambda tup: tup[1], reverse=True)
    print("Donor Name{}Total Amount{}Number of Donations{}Average Donation Amount{}".format(
        ' ' * 20,
        ' ' * 18,
        ' ' * 11,
        ' ' * 8))
    for row in sorted_donations:
        print('{}{}{}{}{}{}{}{}'.format(
            row[0], ' ' * (30 - len(str(row[0]))),
            row[1], ' ' * (30 - len(str(row[1]))),
            row[2], ' ' * (30 - len(str(row[2]))),
            row[3], ' ' * (30 - len(str(row[3])))))
        donor_list.append('{}\t {}\t {}\t {}'.format(
        row[0],
        row[1],
        row[2],
        row[3])
        ) # For tests
    return sorted(donor_list) # For tests
