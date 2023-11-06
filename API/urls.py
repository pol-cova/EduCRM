from django.urls import path
# Import API views
from . import views

urlpatterns = [
    path('', views.index, name='index' ),
    path('login/', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('logout/', views.user_logout, name='logout'),
    path('my/', views.user_dashboard, name='dashboard'),
    path('create/', views.create_course, name='create_course'),
    path('add_student/', views.add_student, name='add_student'),
    path('grupos/power-point/', views.group_list_pp, name='grupos_pp'),
    path('grupos/excel/', views.group_list_ex, name='grupos_ex'),
    path('api/student/group/A/power-point/', views.students_list_pp_a, name='students_list_pp_A'),
    path('api/student/group/B/power-point/', views.students_list_pp_b, name='students_list_pp_B'),
    path('api/student/group/A/excel/', views.students_list_ex_a, name='students_list_ex_A'),
    path('api/student/group/B/excel/', views.students_list_ex_b, name='students_list_ex_B'),
    path('api/student/group/C/excel/', views.students_list_ex_c, name='students_list_ex_C'),
    path('eval/<int:student_id>', views.eval_student, name='eval'),
]