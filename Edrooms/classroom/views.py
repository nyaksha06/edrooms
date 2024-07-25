from django.shortcuts import render, get_object_or_404,redirect
from .models import Classroom, Tutorial, Discussion
from django.contrib.auth.decorators import login_required

from .forms import ClassroomForm, TutorialForm, DiscussionForm

# Create your views here.

def classroom_list(request):
    classrooms = Classroom.objects.all()
    return render(request, 'classroom/classroom_list.html', {'classrooms': classrooms})

def classroom_detail(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    return render(request, 'classroom/classroom_detail.html', {'classroom': classroom})

@login_required(login_url="login")
def classroom_create(request):
    if request.method == 'POST':
        form = ClassroomForm(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.user=request.user
            instance.save()
            return redirect('classroom:classroom_list')
    else:
        form = ClassroomForm()    


    return render(request,'classroom/classroom_create.html',{'form':form})



@login_required(login_url="login")
def add_tutorial(request, classroom_id):
    classroom = get_object_or_404(Classroom, id=classroom_id)
    if request.method == 'POST':
        form = TutorialForm(request.POST, request.FILES)
        if form.is_valid():
            tutorial = form.save(commit=False)
            tutorial.classroom = classroom
            tutorial.created_by = request.user
            tutorial.save()
            return redirect('classroom:classroom_detail', classroom_id=classroom.id)
    else:
        form = TutorialForm()
    return render(request, 'classroom/add_tutorial.html', {'form': form, 'classroom': classroom})

@login_required(login_url="login")
def tutorial_detail(request, tutorial_id):
    tutorial = get_object_or_404(Tutorial, id=tutorial_id)
    discussions = Discussion.objects.filter(tutorial=tutorial)
    if request.method == 'POST':
        form = DiscussionForm(request.POST)
        if form.is_valid():
            discussion = form.save(commit=False)
            discussion.tutorial = tutorial
            discussion.created_by = request.user
            discussion.save()
            return redirect('tutorial_detail', tutorial_id=tutorial.id)
    else:
        form = DiscussionForm()
    return render(request, 'classroom/tutorial_detail.html', {'tutorial': tutorial, 'discussions': discussions, 'form': form})