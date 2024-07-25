from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from .forms import FacultyForm
from .models import Faculty

def index(request):
    if request.method == 'POST':
        form = FacultyForm(request.POST)
        if form.is_valid():
            name=form.cleaned_data['name']
            CL=form.cleaned_data['CL']
            RH=form.cleaned_data['RH']
            TL=CL+RH
            remaining_TL=14-TL
            per=(TL/14)*100
            status=update_status(TL,CL,RH)
            record=Faculty(
                name=name,
                CL=CL,
                RH=RH,
                TL=TL,
                remaining_TL=remaining_TL,
                per=per,
                status=status
            )
            record.save()
            return redirect('index')
    else:
        form = FacultyForm()
    faculties = Faculty.objects.all()
    return render(request, 'index.html', {'form': form})


def update_status(TL,CL,RH):
    if TL == 14 and CL== 12 and RH == 2:
        status="completed"
    elif TL == 7:
        status="half"
    elif TL == 0:
        status="not taken"
    elif TL > 7:
        status="more than half"
    elif TL < 7:
        status="less than half"
    elif TL < 0 or CL <0  or RH <0:
        status="invalid"
    return  status

def display_table(request):
    faculties=Faculty.objects.all()
    return render(request, 'table.html', {'faculties': faculties})

def BV_TC(request):
    result1=list()
    result2=list()
    result3=list()
    result4=list()
    f1=Faculty.objects.all()
    for f in f1:
        if f.RH <0  or f.CL<0 :
            result2.append(f)
        elif f.per <= 100 and f.per >70:
            result1.append(f)
        elif f.per <= 70 and f.per >40:
            result3.append(f)
        elif f.per <=40 and f.per >0:
            result4.append(f)
    return render(request,"BVtable.html",{'result1':result1,'result2':result2,'result3':result3,'result4':result4,})

def home(request):
    return render(request,"home.html")