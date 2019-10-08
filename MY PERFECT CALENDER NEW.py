import functools
mod='303232332323'   #ood days of every month
date=input('Enter date in the format of ddmmyyyy:')
days={'01':31,'02':29,'03':31,'04':30,'05':31,'06':30,'07':31,'08':31,'09':30,'10':31,'11':30,'12':31}
if len(date)==8:
    year=int(date[4:])
    """if int(date[2:4]) not in days.keys():
        print("invalid date")
        date=input('Enter date in the format of ddmmyyyy:')"""
    if int(date[2:4])>12:              #enter month below 13
        print("invalid date")
    elif int(date[:2])==29 and int(date[2:4])==2 and year%4!=0: #for feb 29 when it is leap year
        print("invalid date")
    elif int(date[:2])>days[date[2:4]]:
        print("invalid date")
    else:
        years=[i for i in range(10000) if i%400==0]   #years=[400,800----]
        list=[]
        for j in range(len(years)-1):
            if years[j]<year:
                list.append(years[j])
        newyear=list[len(list)-1]
        dif=year-newyear-1
        if dif>=300:
            odddays=1     #odd days for 300yrs
        elif dif>=200:
            odddays=3     #odd days for 200yrs
        else:
            odddays=5     #odd days for 100yrs
        difference=str(dif)
        year1=difference[1:]
        leapyears=int(int(year1)/4)
        normalyears=(int(year1))-leapyears
        odddays2=odddays+(leapyears*2)+normalyears      #odd days upto given year-1
        a=int(date[2:4])      #month
        a1=mod[:a]            #odd days of each month upto given month-1
        a2=[]
        for k in range(len(a1)-1):
            a2.append(int(a1[k]))  #for reduce we must have int values in the list or tuple
        def add(x,y):
            return x+y
        if a>2:
            odddays3=functools.reduce(add,a2)  #to add all odd days
        elif a==2:
            odddays3=3
        else:
            odddays3=0
        odddays4=int(date[:2])
        total_odddays=((odddays2)+(odddays3)+(odddays4))%7    #calculation of all odd days
        last=int(date[6:])
        if (last%4)==0:
                 total_odddays=(total_odddays+1)%7  #if the year is leap year we must add 1 odd day 
        print(total_odddays)
        results={0:'SUNDAY',1:'MONDAY',2:'TUESDAY',3:'WEDNESDAY',4:'THURSDAY',5:'FRIDAY',6:'SATURDAY'}
        print(results[total_odddays])
else:
    print("Entered invalid date")
    
