from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from .models import Student, Club
from .forms import RegisterForm, StudentForm


# 🔹 Приветственная страница
def hello(request):
    return render(request, "students/hello.html")


# 🔹 Регистрация пользователя
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            User.objects.create_user(
                username=form.cleaned_data["username"],
                email=form.cleaned_data["email"],
                password=form.cleaned_data["password"]
            )
            return redirect("login")
    else:
        form = RegisterForm()
    return render(request, "students/register.html", {"form": form})


# 🔹 Список студентов (вход обязателен)
@login_required
def student_list(request):
    students = Student.objects.all()
    return render(request, "students/index.html", {"students": students})


# 🔹 Добавление студента (только у кого есть право add_student)
@permission_required('students.add_student', raise_exception=True)
def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()

            # ✅ сохраняем клубы, если выбраны
            if "clubs" in request.POST:
                student.clubs.set(request.POST.getlist("clubs"))

            return redirect("student_list")
    else:
        form = StudentForm()

    all_clubs = Club.objects.all()
    return render(request, "students/add_student.html", {
        "form": form,
        "all_clubs": all_clubs
    })


# 🔹 Просмотр одного студента (вход обязателен)
@login_required
def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    return render(request, "students/detail.html", {"student": student})


@permission_required('students.change_student', raise_exception=True)
def edit_student(request, pk):
    student = get_object_or_404(Student, pk=pk)

    if request.method == "POST":
        form = StudentForm(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()  # сохраняем изменения
            return redirect("student_list")
        else:
            print("❌ Ошибки формы:", form.errors)
    else:
        form = StudentForm(instance=student)

    return render(request, "students/edit_student.html", {"form": form})


@permission_required('students.delete_student', raise_exception=True)
def delete_student(request, pk):
    student = get_object_or_404(Student, pk=pk)
    student.delete()
    return redirect("student_list")

