from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Import custom models
from .models import Course, Student
# Signup form using the user model 
class SignupForm(UserCreationForm):
    email = forms.EmailField(required=True, label='Email')
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
# Basic login form that will validate user and password
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

# Create student form 
class StudentCreationForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'last_name', 'group', 'courses_enrolled']

# Create rubric form
class StudentRubric(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['question_1', 'question_2', 'question_3', 'question_4', 'question_5', 'question_6', 'question_7', 'question_8', 'question_9']
        labels = {
            'question_1': 'Identificar las pestañas de la cinta de opciones (Inicio, Insertar, Diseño de página, etc.)',
            'question_2': 'Seleccionar una pestaña específica de la cinta de opciones',
            'question_3': 'Reconocer y utilizar funciones comunes en la pestaña (Inicio) (Negrita, Cursiva, Subrayado, Copiar, Pegar)',
            'question_4': 'Utilizar atajos de teclado para acciones básicas (por ejemplo, Ctrl+C para copiar, Ctrl+V para pegar)',
            'question_5': 'Identificar al menos dos pestañas adicionales y sus funciones (por ejemplo, Diseño de página, Fórmulas)',
            'question_6': 'Utilizar herramientas de formato básico (color de fuente, tamaño de fuente, alineación)',
            'question_7': 'Conocer y utilizar el botón Guardar para guardar un archivo',
            'question_8': 'Usar la barra de acceso rápido para acceder a funciones frecuentes',
            'question_9': 'Explicar la utilidad de la cinta de opciones',
        }