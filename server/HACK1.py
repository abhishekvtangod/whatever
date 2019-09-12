class Vehicle:
    tata_ace = 8    # 4(DETS & D+F)  1FNF 1PP 1HUL
    tata_ace_wt = None
    bike = 6        # 2 each for FNB PP and HUL
    bike_wt = None 
    total = tata_ace + bike
    tata_bill = None
    bike_bill = None

    def tata_wt_constraint(self,tata_ace_wt):        #returns 1 if constraint satisfied else 0
        if tata_ace_wt>=500 and tata_ace_wt<=700:
            return 1
        else:
            return 0
    
    def bike_wt_constraint(self,bike_wt):
        if bike_wt>=20 and bike_wt<=25:
            return 1
        else:
            return 0
    
    def tata_bill_constraint(self,tata_bill):
        if tata_bill>=20 and tata_bill<=25:
            return 1
        else:
            return 0
    
    def bike_bill_constraint(self,bike_bill):
        if bike_bill>=10 and bike_bill<=25:
            return 1
        else:
            return 0
