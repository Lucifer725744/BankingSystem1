from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Customer
from .models import Transfer
# Create your views here.

def index(request):
    return render(request,'bank/index.html')

def viewallcust(request):

    customers=Customer.objects.all()
    n=len(customers)
    params={'customer':customers,'range':range(1,n)}
    return render(request, 'bank/viewallcust.html',params)

def transfer(request):
    customers = Customer.objects.all()
    transfers = Transfer.objects.all()
    params = {'customer': customers}
    return render(request, 'bank/transfer.html',params)

def history(request):
    transfers = Transfer.objects.all()
    customers = Customer.objects.all()
    n = len(transfers)
    params = {'transfer': transfers, 'customer':customers}
    return render(request, 'bank/history.html',params)


def makechange(request):
    customers = Customer.objects.all()
    transfers = Transfer.objects.all()
    if request.method=="POST":
        from_cust=request.POST['from_cust']
        to_cust=request.POST['to_cust']
        amt=request.POST['amt']
        #Trasfer Table Update
        submit = Transfer(trans_amt=int(amt), trans_from_id=int(from_cust), trans_to_id=int(to_cust))
        submit.save()
        #Customer Table Update
        for i in customers:
            if i.cust_id == int(from_cust):
                from_current_bal=int(i.cust_bal)
                from_current_bal = from_current_bal - int(amt)
                sub1=Customer.objects.get(cust_id=i.cust_id)
                sub1.cust_bal=from_current_bal
                sub1.save()
            if i.cust_id==int(to_cust):
                to_current_bal=int(i.cust_bal)
                to_current_bal = to_current_bal + int(amt)
                sub2 = Customer.objects.get(cust_id=i.cust_id)
                sub2.cust_bal = to_current_bal
                sub2.save()

    return redirect('history')