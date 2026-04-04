
total_bookings=0
rejections=0
total_tickets_sold=0
remaining_seats=350

while  remaining_seats>0 :
    tickets=int(input("enter number of tickets"))
    if tickets==0 :
        break
    elif tickets >= 1 and  tickets<=15 :
        print("valid booking")
    else:
        print("BOOKING REJECTED - Invalid ticket count")
        rejections+=1
        continue
    if tickets > remaining_seats :
        print("housefull")
        rejections+=1
        continue
    verfication = True
    for i in range(tickets):
        age = int(input(f"enter age for person {i+1}:")) ##most important roto iterate values which is depending on number of tickets
        if age<12 :
            print("BOOKING REJECTED - Age restriction")
            rejections+=1
            verfication =False
            break
    if verfication==True:
        print(f"BOOKING CONFIRMED - {tickets} tickets")
        total_bookings+=1
        total_tickets_sold+=tickets
        remaining_seats-= tickets
print(f"Final Report : total bookings: {total_bookings},"
      f"Total tickets sold :{total_tickets_sold},"
      f"Rejected bookings: {rejections},"
      f"Remaining seats :{remaining_seats}")#final code as expected

