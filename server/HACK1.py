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

def profit_calc(vehicle_name,bill): #2nd parameter is bill value
    if vehicle_name=="TATA ACE":
        profit = bill - 1500
        return profit
    elif vehicle_name=="BIKE":
        profit = bill - 600
        return profit
    else:
        return False

time = 10.00                         # initial time is 10am

def delivery_time(time1):           # 10 min of delivery time
    return time1 + .166              

def time_calc(vehicle_name,distance):  #get distance from API
    if vehicle_name=="TATA ACE":
        time = distance/20             # distance in km
        delivery_time(time)            # add delivery time
        return time
    elif vehicle_name=="BIKE":
        time = distance/30
        delivery_time(time)
        return time
    else:
        return False