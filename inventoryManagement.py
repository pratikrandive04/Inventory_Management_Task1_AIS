def display_monthly_details(capacity, demand):
    # Initialize starting values
    month = 0
    remaining_capacity = capacity
    import calendar
    #table headers
    print("Month\t\tCapacity\tDemand\tExtra Demand\tRemaining Capacity")
    
    # Loop through each month
    for demand_month in range(12):
        # Calculate extra demand and remaining capacity for the month
        extra_demand = max(0, demand[demand_month] - capacity)
        remaining_capacity = max(0, capacity - demand[demand_month])
        
        # month name
        month += 1
        month_name = calendar.month_name[month]
        
        # Print
        print("{:<12}\t{:>8}\t{:>6}\t{:>13}\t{:>17}".format(month_name, capacity, demand[demand_month], extra_demand, remaining_capacity))


capacity = 1000
demand = [1000, 100, 1400, 1500, 900, 1300, 800, 1700, 600, 500, 1400, 300]

display_monthly_details(capacity, demand)