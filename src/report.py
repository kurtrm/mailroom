"""funciton to run if user choose to make a report on donor information"""


donors_info = {'Sam Wippy': [100000], 'Willy Wonka': [12, 13, 14], 'Garth Brooks': [1]}


def create_report():
    """making a list for each column from dict data then populate row data into a table"""
    donor_list = [] # For tests
    donor_name = donors_info.keys()
    donor_name.insert(0, "Donor_Name")
    donation = donors_info.values()
    num_of_donation = [str(len(a)) for a in donation]
    num_of_donation.insert(0, "Number_of_Donation")
    total_donation = [str(sum(a)) for a in donation]
    total_donation.insert(0, "Total_Donation")
    average_donation = [str(sum(a)/len(a)) for a in donation]
    average_donation.insert(0, "Average_Donation")
    for row in zip(donor_name, total_donation, num_of_donation, average_donation):
        print '\t '.join(row)
        donor_list.append(', '.join(row)) # For tests
    return sorted(donor_list) # For tests
