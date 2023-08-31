import pandas as pd # If pandas is not installed in the system, you can use "pip install pandas" to install it
from Feed import Feed

def PopulateData():

    global Rows # Rows is a global variable, which means it can be accessed anywhere in the program.
    Rows = []   # There is no restriction on the scope of the variable
                # The Rows list will contain a list of all the objects.

    # We read the CSV file using the method read_csv() from Pandas. It is the most efficient way to do this.
    
    dataFrame = pd.read_csv('./InputCSV.csv', encoding='utf-8') 

    for index, row in dataFrame.iterrows():
        # index is a throw away variable, it is generally recommended to use '_' for throw away variable names
        # We iterate over each row in the dataFrame to obtain the values from the InputCSV.csv file

        ChildId = row['ChildId'] # This is the bvdID, which would be provided to you as input
        ChildAddress = row['ChildAddress'] # To be obtained from scrape.
        ParentName = row['ParentName'] # To be obtained from scrape.
        Internet = row['Internet'] # To be obtained from scrape.
        SourceDate = row['SourceDate'] # To be obtained from scrape.
        DirectPercent = row['DirectPercent'] # To be obtained from scrape.
        TotalPercent = row['TotalPercent'] # To be obtained from scrape.

        # currentRow is an object of the class "Feed"
        # currentRow will have the access to all the attributes and methods of the class
        # We create an object currentRow will the values that were obtained from the scrape
        currentRow = Feed(ChildId, ChildAddress, ParentName, Internet, SourceDate, DirectPercent, TotalPercent)

        # The below set of utility functions can be used to modify or format the field values

        # The couple of methods below, can be used to add custom changes to the data field
        # You may require to create more methods if required
        # The implementation of these methods have been left to the learners. 
        # Don't worry if you fail to implement these methods. The idea is to learn and create it yourself first.

        currentRow.setSourceDateToRequiredFormat() # To add custom change to source date
        currentRow.setDirectPercentToRequiredFormat() # To add custom change to direct percent

        # We now have a row ready, we will append this to our Global list called Rows.
        Rows.append(currentRow)

def WriteToTextFile():

    # Headers list will used to set the headers in the Output.txt file.
    # Please see Output.txt for reference
    # __slots__ could've been also used to get this list, since they both are same
    # However, we didn't do that for code simplicity :)

    headers = [
        'ChildId', 'ChildName', 'ChildAddress', 'ChildCity', 'ChildPostcode', 'ChildPerson',
        'ParentId', 'ParentName', 'ParentAddress', 'ParentCity', 'ParentPostcode', 'ParentPerson',
        'Internet', 'ChildBranch', 'ChildBirthDate', 'ParentBirthDate', 'Type', 'SourceNr', 'SourceDate',
        'Origin', 'DirectPercentIndic', 'DirectPercent', 'TotalPercentIndic', 'TotalPercent', 'Voting',
        'Archive', 'DealNumber', 'StartDate', 'EndDate'
    ]

    # We now finally write all of the data from Rows list to the output file i.e. Output.txt
    with open('Output.txt', 'w', encoding='utf-8') as file:
        #Write the headers to the output file
        file.write('\t '.join(headers[:]) + '\n') # We start by writing the headers, the first line in the output file

        # Write the rows of data to the output file
        # variable "row" below is a class object, here object of the class "Feed"
        # using the . (dot) operator, we can access the attributes of the class
        # For example, row.ChildId would give the ChildId for the particular object

        for row in Rows:
            file.write(f"{row.ChildId}\t {row.ChildName}\t {row.ChildAddress}\t {row.ChildCity}\t {row.ChildPostcode}\t \
                        {row.ChildPerson}\t {row.ParentId}\t {row.ParentName}\t {row.ParentAddress}\t {row.ParentCity}\t \
                        {row.ParentPostcode}\t {row.ParentPerson}\t {row.Internet}\t {row.ChildBranch}\t {row.ChildBirthDate}\t \
                        {row.ParentBirthDate}\t {row.Type}\t {row.SourceNr}\t {row.SourceDate}\t {row.Origin}\t {row.DirectPercentIndic}\t \
                        {row.DirectPercent}\t {row.TotalPercentIndic}\t {row.TotalPercent}\t {row.Voting}\t {row.Archive}\t {row.DealNumber} \
                        {row.StartDate}\t {row.EndDate}\n")

if __name__ == "__main__":
    # This is the main. Execution of the program starts and ends here.
    PopulateData() # We populate all the data we obtained from the scrape.
    WriteToTextFile() # We write all of the output to the Output.txt file


