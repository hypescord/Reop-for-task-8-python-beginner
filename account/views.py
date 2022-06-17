from django.shortcuts import render, redirect
from home.models import Customer, Record

# Create your views here.
def register(request):
    if request.method == 'POST':

        Occupant_nam = request.POST.get('Occupant_name')
        Occupant_emai = request.POST.get('Occupant_email')
        Occupant_occupatio = request.POST.get('Occupant_occupation')    #Customer details terminates here

        Room_numbe = request.POST.get('Room_number')                            
        Amount_pai = request.POST.get('Amount_paid')
        Num_of_night = request.POST.get('Num_of_nights')
        Start_dat = request.POST.get('Start_date')
        End_dat = request.POST.get('End_date')
        Custome = request.user                                          #Hotel record pertaining to customer terminates here

        Customer(Occupant_name=Occupant_nam, Occupant_email=Occupant_emai, Occupant_occupation=Occupant_occupatio)                              #to save the data from the Customer frontend to the database
        Record(Room_number=Room_number, Amount_paid=Amount_paid, Num_of_nights=Num_of_nights, Start_date=Start_date, End_date=End_date).save()  #to save the data from the Record frontend to the database
       
        return redirect('records:registerview')
    return render(request, 'records/register.html')
   
def checkdetails(request):
    return render(request, 'records/checkdetails.html')
def customer(request):
    return render(request, 'records/customer.html')