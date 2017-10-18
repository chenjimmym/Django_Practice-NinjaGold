from django.shortcuts import render, redirect
import random

# Create your views here.
def index(request):
    if not 'gold_amount' in request.session:
        request.session['gold_amount'] = 0
    return render(request, 'gold/index.html')

def process_gold(request):
    if request.method == "POST":
        if request.POST['place'] == 'farm':
            request.session['gold_amount'] += random.randrange(10,21)
        if request.POST['place'] == 'cave':
            request.session['gold_amount'] += random.randrange(5,11)
        if request.POST['place'] == 'house':
            request.session['gold_amount'] += random.randrange(2,6)
        if request.POST['place'] == 'casino':
            request.session['gold_amount'] += random.randrange(-50,50)
        if request.POST['place'] == 'reset':
            request.session['gold_amount'] = 0
    return redirect('/')