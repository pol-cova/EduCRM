from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from .forms import SignupForm, LoginForm, StudentCreationForm, StudentRubric 
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.http import HttpResponseRedirect
# Add models
from .models import Course, Student
# Index main route
def index(request):
    return render(request, 'index.html')

# User logged route
def user_dashboard(request):
    user = request.user
    courses = Course.objects.filter(teacher=user)
    return render(request, 'dashboard.html', {'courses': courses})

# User signup route
def user_signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            # Create user
            form.save()
            # Redirect user to login
            return redirect('login')
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})

# User login route
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                return redirect('dashboard')
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form':form})

# User Logout route
def user_logout(request):
    logout(request)
    return redirect('login')

# Create course route
@login_required 
def create_course(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        teacher = request.user
        # Create course
        course = Course.objects.create(title=title, description=description, teacher=teacher)
        return redirect('dashboard')
    return render(request, 'create_course.html')

# Add student route
def add_student(request):
    if request.method == 'POST':
        form = StudentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to a list view of students
    else:
        form = StudentCreationForm()

    return render(request, 'add_student.html', {'form': form})

# Groups route
def group_list_pp(request):
    course_pp_group = Student.objects.filter(courses_enrolled=1).values('group').distinct()

    course_pp_data = []

    for group in course_pp_group:
        students = Student.objects.filter(courses_enrolled=1, group=group['group'])
        course_pp_data.append({
            'group': group['group'],
            'students': students
        })
    

    return render(request, 'groups_pp.html', {'course_pp_data': course_pp_data})

# Groups route ex
def group_list_ex(request):
    course_ex_group = Student.objects.filter(courses_enrolled=2).values('group').distinct()
    
    course_ex_data = []

    for group in course_ex_group:
        students = Student.objects.filter(courses_enrolled=2, group=group['group'])
        course_ex_data.append({
            'group': group['group'],
            'students': students
        })

    return render(request, 'groups_ex.html', {'course_ex_data': course_ex_data})

# Students pp route
def students_list_pp_a(request):
    course_id = 1  # Adjust the course ID as needed
    students = Student.objects.filter(courses_enrolled=course_id, group='A')
    form = StudentRubric()

    return render(request, 'students_pp_a.html', {'students': students, 'form': form})

def students_list_pp_b(request):
    course_id = 1  # Adjust the course ID as needed
    students = Student.objects.filter(courses_enrolled=course_id, group='B')
    form = StudentRubric()

    return render(request, 'students_pp_b.html', {'students': students,  'form': form})

def students_list_ex_a(request):
    course_id = 2  # Adjust the course ID as needed
    students = Student.objects.filter(courses_enrolled=course_id, group='A')
    form = StudentRubric()

    return render(request, 'students_ex_a.html', {'students': students, 'form': form})

def students_list_ex_b(request):
    course_id = 2  # Adjust the course ID as needed
    students = Student.objects.filter(courses_enrolled=course_id, group='B')
    form = StudentRubric()

    return render(request, 'students_ex_b.html', {'students': students, 'form': form})

def students_list_ex_c(request):
    course_id = 2  # Adjust the course ID as needed
    students = Student.objects.filter(courses_enrolled=course_id, group='C')
    form = StudentRubric()

    return render(request, 'students_ex_c.html', {'students': students, 'form': form})

# Eval student 
def eval_student(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentRubric(request.POST, instance=student)

        if form.is_valid():
            form.save()
            print('Form updated')
            student.status = 1
            student.save()
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/')) 

    else:
        form = StudentRubric(instance=student)

    return render(request, 'students_pp_a.html', {'form': form, 'student': student})