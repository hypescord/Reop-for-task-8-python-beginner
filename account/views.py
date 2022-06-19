from django.shortcuts import render, redirect
from home.models import Customer, Record

# Create your views here.
def register(request):
    if request.method == 'POST':

        occupant_name = request.POST.get('Occupant_name')
        occupant_email = request.POST.get('Occupant_email')
        occupant_occupation = request.POST.get('Occupant_occupation')    #Customer details terminates here

        room_number = request.POST.get('Room_number')                            
        amount_paid = request.POST.get('Amount_paid')
        num_of_nights = request.POST.get('Num_of_nights')
        start_date = request.POST.get('Start_date')
        end_date = request.POST.get('End_date')
        customer = request.user                                          #Hotel record pertaining to customer terminates here

        new_customer = Customer(Occupant_name=occupant_name, Occupant_email=occupant_email, Occupant_occupation=occupant_occupation)                              #to save the data from the Customer frontend to the database
        new_record = Record(Room_number=room_number, Amount_paid=amount_paid, Num_of_nights=num_of_nights, Start_date=start_date, End_date=end_date)  #to save the data from the Record frontend to the database
        new_customer.save()
        new_record.save()
        
        return redirect('records:registerview')
    return render(request, 'records/register.html')
   
def checkdetails(request):
    return render(request, 'records/checkdetails.html')
def customer(request):
    return render(request, 'records/customer.html')