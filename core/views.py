from django.shortcuts import render
from django.views.generic import View
# Create your views here.

obj =   [ 
            {'rate':1,
             'slab':0},
            {'rate':15,
             'slab':350000},
            {'rate':20,
             'slab':450000},
            {'rate':25,
             'slab':650000},
            {'rate':30,
             'slab':1200000}
        ]


def calc(amount_obj, amount, obj_id):
    tax = 0
    detail =[]
    excess = amount - amount_obj.get('slab')
    amount = amount_obj.get('slab')
    tax += (excess * amount_obj.get('rate')) / 100
    
    detail.append("Tax for amount "+str(excess)+" is "+str(tax)+ " at "+str(amount_obj.get('rate'))+"%.")
    
    if amount != 0:
        new_tax, new_detail = calc(obj[obj_id-1] , amount, obj_id-1)
        tax += new_tax
        detail += new_detail
    return tax, detail



class Calculatetax(View):
    def get(self, request):
        return render(request, 'home.html')
        
    def post(self, request):
        amount=int(self.request.POST.get('amount'))
        if amount > 1200000:
            obj_id = 4
        elif amount > 650000:
            obj_id = 3
        elif amount > 450000:
            obj_id = 2
        elif amount > 350000: 
            obj_id = 1
        else:
            obj_id = 0
        
        tax, detail = calc(obj[obj_id], amount, obj_id) 
        
        detail.append("Total of Rs."+str(tax)+" tax for Rs."+str(amount))
        return render(request, 'home.html', {'object_list':tax, 'details':detail})
        #from taxcalculator import *; my_income_is(1200000)

