class Feed:

    __slots__ = [
                    'ChildId', 'ChildName', 'ChildAddress', 'ChildCity', 'ChildPostcode', 'ChildPerson',
                    'ParentId', 'ParentName', 'ParentAddress', 'ParentCity', 'ParentPostcode', 'ParentPerson',
                    'Internet', 'ChildBranch', 'ChildBirthDate', 'ParentBirthDate', 'Type', 'SourceNr', 'SourceDate',
                    'Origin', 'DirectPercentIndic', 'DirectPercent', 'TotalPercentIndic', 'TotalPercent', 'Voting',
                    'Archive', 'DealNumber', 'StartDate', 'EndDate', 'ChildNameWebsite'
                ]
    
    def __init__(self, ChildId, ChildAddress, ParentName, Internet, SourceDate, DirectPercent, TotalPercent, ChildNameWebsite):

        if ChildId is not None:
            self.ChildId = ChildId
        else:
            self.ChildId = ''
        
        if ChildAddress is not None:
            self.ChildAddress = ChildAddress
        else:
            self.ChildAddress = ''
        
        if ParentName is not None:
            self.ParentName = ParentName
        else:
            self.ParentName = ''

        if Internet is not None:
            self.Internet = Internet
        else:
            self.Internet = ''
        
        if SourceDate is not None:
            self.SourceDate = SourceDate
        else:
            self.SourceDate = ''
        
        if DirectPercent is not None:
            self.DirectPercent = DirectPercent
        else:
            self.DirectPercent = ''
        
        if TotalPercent is not None:
            self.TotalPercent = TotalPercent
        else:
            self.TotalPercent = ''
        
        if ChildNameWebsite is not None:
            self.ChildNameWebsite = ChildNameWebsite
        else:
            self.ChildNameWebsite = ''

        self.ChildName = ''
        self.ChildCity = ''
        self.ChildPostcode = ''
        self.ChildPerson = ''
        self.ParentId = '??'
        self.ParentAddress = ''
        self.ParentCity = ''
        self.ParentPostcode = ''
        self.ParentPerson = 'U'
        self.ChildBranch = ''
        self.ChildBirthDate = ''
        self.ParentBirthDate = ''
        self.Type = '1'
        self.SourceNr = '624'
        self.Origin = 'F'
        self.DirectPercentIndic = ''
        self.TotalPercentIndic = ''
        self.Voting = '1'
        self.Archive = ''
        self.DealNumber = ''
        self.StartDate = ''
        self.EndDate = ''

    
    def setSourceDateToRequiredFormat(self):
        # The website makes use of the format DD.MM.YYYY e.g. 24.8.2023
        # Add logic below to set the source date in the format YYYYMMDD
        
        #self.SourceDate = 'YYYYMMDD'
        pass

    def setDirectPercentToRequiredFormat(self):
        # DirectPercent for example is available as 99,880926 in the website
        # We need to replace the ',' with '.' (decimal point) &
        # Accuracies limited to only 2 decimal places (before and after decimal)
        # An exception in accuracy in case of 100,00 -> 100.00 
        # For e.g 99,880926 is parsed as 99.88 and 0.0823 is parsed as 0.08
        # No Round off is needed
        
        #self.DirectPercent = '100.00'    
        pass
