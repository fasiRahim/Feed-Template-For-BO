import pandas as pd
from Feed import Feed

def PopulateData():

    global Rows
    Rows = []

    dataFrame = pd.read_csv('./InputCSV.csv')

    for index, row in dataFrame.iterrows():
        #index is a throw away variable, it is generally recommended to use '_' for throw away variable names
        ChildId = row['ChildId']
        ChildAddress = row['ChildAddress']
        ParentName = row['ParentName']
        Internet = row['Internet']
        SourceDate = row['SourceDate']
        DirectPercent = row['DirectPercent']
        TotalPercent = row['TotalPercent']
        ChildNameWebsite = row['ChildNameWebsite']

        currentRow = Feed(ChildId, ChildAddress, ParentName, Internet, SourceDate, DirectPercent, TotalPercent, ChildNameWebsite)

        # The below set of utility functions can be used to modify or format the field values

        currentRow.setSourceDateToRequiredFormat() # To add custom change to source date
        currentRow.setDirectPercentToRequiredFormat() # To add custom change to direct percent

        Rows.append(currentRow)

def WriteToTextFile():

    headers = [
        'ChildId', 'ChildName', 'ChildAddress', 'ChildCity', 'ChildPostcode', 'ChildPerson',
        'ParentId', 'ParentName', 'ParentAddress', 'ParentCity', 'ParentPostcode', 'ParentPerson',
        'Internet', 'ChildBranch', 'ChildBirthDate', 'ParentBirthDate', 'Type', 'SourceNr', 'SourceDate',
        'Origin', 'DirectPercentIndic', 'DirectPercent', 'TotalPercentIndic', 'TotalPercent', 'Voting',
        'Archive', 'DealNumber', 'StartDate', 'EndDate', 'ChildNameWebsite'
    ]


    with open('Output.txt', 'w', encoding='utf-8') as file:
        #Write the headers to the output file
        file.write('\t '.join(headers[:]) + '\n')

        #Write the rows of data to the output file
        for row in Rows:
            file.write(f"{row.ChildId}\t {row.ChildName}\t {row.ChildAddress}\t {row.ChildCity}\t {row.ChildPostcode}\t \
                        {row.ChildPerson}\t {row.ParentId}\t {row.ParentName}\t {row.ParentAddress}\t {row.ParentCity}\t \
                        {row.ParentPostcode}\t {row.ParentPerson}\t {row.Internet}\t {row.ChildBranch}\t {row.ChildBirthDate}\t \
                        {row.ParentBirthDate}\t {row.Type}\t {row.SourceNr}\t {row.SourceDate}\t {row.Origin}\t {row.DirectPercentIndic}\t \
                        {row.DirectPercent}\t {row.TotalPercentIndic}\t {row.TotalPercent}\t {row.Voting}\t {row.Archive}\t {row.DealNumber} \
                        {row.StartDate}\t {row.EndDate}\t {row.ChildNameWebsite} \n")

if __name__ == "__main__":
    PopulateData()
    WriteToTextFile()


