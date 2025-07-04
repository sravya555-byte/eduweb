from django.shortcuts import render
from admissions.models import Student
from admissions.forms import StudentModelForm
from admissions.forms import VendorForm
from django.views.generic import View,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.http import HttpResponse
from admissions.models import Teacher
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required,permission_required




# Create your views here.
#functionbased views
@login_required
def homepage(request):
    return render(request,'index.html')

def logoutUser(request):
    return render(request,'logout.html')

@login_required

def addAdmission(request):
    form=StudentModelForm
    studentform={'form':form}

    if request.method=='POST':
        form=StudentModelForm(request.POST)
        if form.is_valid():
            form.save()
        return homepage(request)

    return render(request,'admissions/add-admission.html',studentform)


@login_required

def admissionReport(request):

    result=Student.objects.all(); #select * from admissions_student
    students={'allstudents':result}
    return render(request,'admissions/admission-report.html',students)

@login_required
@permission_required('admissions.delete_student')
def deleteStudent(request,id):
    s=Student.objects.get(id=id)  #select * from admissions_student where id=idvalue
    s.delete()
    return admissionReport(request)

@login_required
@permission_required('admissions.change_student')
def updateStudent(request,id):
    s=Student.objects.get(id=id)
    form=StudentModelForm(instance=s)
    dict={'form':form}

    if request.method=='POST':
        form=StudentModelForm(request.POST,instance=s)
        if form.is_valid():
            form.save()
        return admissionReport(request)

    return render(request,'admissions/update-admission.html',dict)

@login_required
def addVendor(request):
    form=VendorForm
    vform={'form':form}

    if request.method=='POST':
        form=VendorForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            print(form.cleaned_data['address'])
            print(form.cleaned_data['contact'])
            print(form.cleaned_data['item'])
        return homepage(request)

    return render(request,'admissions/add-vendor.html',vform)




class FirstClassBasedView(View):
    def get(self,request):
        return HttpResponse("<h1>Hello..This is My First Class Based View</h1>")

class TeacherRead(ListView):
    model=Teacher

class GetTeacher(DetailView):
    model=Teacher

class AddTeacher(CreateView):
    model=Teacher
    fields=('name','exp','subject','contact')

class UpdateTeacher(UpdateView):
    model=Teacher
    fields=('name','exp','subject','contact')

class DeleteTeacher(DeleteView):
    model=Teacher
    success_url=reverse_lazy('listteachers')
