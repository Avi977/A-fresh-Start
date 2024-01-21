weekday = ['monday', 'tuesday', 'thursday']
weekend = ['friday',
           'saturday',
           'sunday']
week=['monday', 'tuesday','wednesday', 'thursday','friday','saturday','sunday']


def main():
    current_date=input("State the current date\tmonth/day/year\n")
    date=int(current_date[3:5])
    month=current_date[0:2]
    day=input("What is the current day?\n")
    end_dates={'01':31,'02':29,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}

    month_salary=get_days(date,end_dates[month],day)
    print(f"By the end of this month, you should earn ${month_salary} more")
    user_input=input("Do you want to go further?\n")
    if user_input:
        pass
def get_salary(day,base):
    if day in weekday:
        hour=4
    elif day in weekend:
        hour=7
    elif day=='wednesday':
        hour=0
    else:
        print("not a valid day")
        return
    return(hour*base)
def get_days(start,end,day):
    pointer=week.index(day)
    ans = 0
    for i in range(start,end+1):
        if pointer>=len(week):
            pointer=0
        current_day=week[pointer]
        ans+=get_salary(current_day,15.5)
        pointer+=1
    return ans



if __name__ == '__main__':
    main()