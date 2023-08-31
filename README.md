# Feed Template for BO

AA.csv -- This CSV file contains the output of the scrape from the respective proposals done using AA360.
          This CSV file would be an input file for the python script "ReadFromInputCSV.py"

Feed.py -- Python script to manage the output fields from the scrape

ReadFromInputCSV.py -- Iterates on the AA.csv file to populate data and write it to the Output.txt file

Output.txt -- The final output that will be sent out to the Data specialists for verification
          
