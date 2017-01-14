#Functions
def compute_leap_years(years):
    leap_years = []
    for year in years:
        if year%400 == 0:
            leap_years.append(year)
        elif year%4 == 0 and year%100 != 0:
            leap_years.append(year)

    return leap_years

def traverse_dates(start_date,end_date):

    curr_date = [1,'jan',1900] #Initialize current date
    day = 0 #index starts @ mon
    day_of_week = days[day]
    month = 0 #index starts @ jan

    num_sundays = 0
    
    while not(curr_date[0] == 1 and curr_date[1] == 'jan' and curr_date[2] == 2001):

        #Get the max number of days in the current month
        days_in_month = month_days[curr_date[1]]
        
        #Change the day of week
        if day != 6:
            day += 1
        else:
            day = 0

        day_of_week = days[day]
        
        #Upon reaching the last day of the year
        if curr_date[1] == 'dec' and curr_date[0] == 31:
            curr_date[0] = 1
            curr_date[1] = 'jan'
            curr_date[2] = curr_date[2]+1

            month = 0

        #Upon reaching the last day of the month
        elif curr_date[0] == days_in_month:

            #Reset days
            curr_date[0] = 1

            #If leap year ...
            if curr_date[2] in leap_years and curr_date[1] == 'jan':
                month = 1
                curr_date[1] = 'feb_leap'

            #Otherwise
            else:
                month += 1 #Won't reach the month = 11 case here ...
                curr_date[1] = months[month]

        #Otherwise, move forward one day
        else:

            curr_date[0] += 1

        #Check for Sunday
        if curr_date[0] == 1 and day_of_week == 'sun' and curr_date[2] >= 1901:
            #the 1901 check ensures that sundays in 1900 aren't counted
            num_sundays += 1
            
    return num_sundays


#Main Program
months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
years = range(1900,2001)
days = ['mon','tue','wed','thu','fri','sat','sun']
leap_years = compute_leap_years(years)

month_days = {}
month_days['jan'] = 31
month_days['feb'] = 28
month_days['feb_leap'] = 29
month_days['mar'] = 31
month_days['apr'] = 30
month_days['may'] = 31
month_days['jun'] = 30
month_days['jul'] = 31
month_days['aug'] = 31
month_days['sep'] = 30
month_days['oct'] = 31
month_days['nov'] = 30
month_days['dec'] = 31

date_start = [1,'Jan',190]
date_end = [3,'Dec',2000]
num_sundays = traverse_dates(date_start,date_end)

print num_sundays




