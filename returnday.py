#18/03/22
#Noela completed returnday.py
day={1:"Monday",2:"Tuesday",3:"Wednesday",4:"Thursday",5:"Friday",6:"Saturday",7:"Sunday"}
def ret_day(s_day, l_stay):
    s=(l_stay//7) + s_day
    print("the returrn day is",day[s])
ret_day(int(input("enter s_day")),int(input("enter l_stay")))
