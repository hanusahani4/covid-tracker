from covid import Covid
for i in range(0,100):
    print(" ")
    
    print("Covid Tracker")
    cv=Covid()
    act=cv.get_total_active_cases()
    rec=cv.get_total_recovered()
    death=cv.get_total_deaths()
    con=cv.get_total_confirmed_cases()
    dt=cv.get_data()
    print("1.Global Count")
    print("2.Active Cases")
    print("3.Confirmed Cases")
    print("4.Recovered Cases")
    print("5.Deceased")
    print("6.Get covid update by country name")
    print("7.datas")
    choice=input("Enter a number of your choice :")
    if choice == '1':
        print("active cases :",act, "\nConfirmed Cases :",con,"\nRecovered Cases :",rec,"\nDeceased :",death)
    elif choice =='2':
        print("Active Cases :",act)
    elif choice =='3':
        print("Confirmed Cases :",con)
    elif choice =='4':
        print("Recovered Cases :",rec)
    elif choice =='5':
        print("Deceased :",death)
    elif choice =='6':
        str = i =input("Enter country name :")
        cname=cv.get_status_by_country_name(i)
        print(cname)
    elif choice =='7':
        print("datas :",dt)
    else:
        print("Invalid Input")

    
