from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, QuestionForm, AnswerForm
from .models import Question, Answer
from django.contrib.auth.models import User
from django.contrib import messages
from .forms import RegisterForm


def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email    = request.POST.get('email')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken.')
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already taken.')
            return redirect('register')


        user = User.objects.create_user(username=username, email=email, password=password)
        login(request, user)
        messages.success(request, 'Registered successfully!')
        return redirect('login')
    return render(request,'portal/register.html')


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        if not User.objects.filter(username=username).exists():
            messages.error(request, "User does not exist. Please register first.")  
            return redirect('register')

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, "Login successful!")  
            return redirect('home')
        else:
            messages.warning(request, "Incorrect password.")  

    return render(request, 'portal/login.html')

def logout_view(request):
    logout(request)
    return redirect('login')

@login_required
def home(request):
    questions = Question.objects.all().order_by('-created_at')
    form = QuestionForm(request.POST or None)
    if form.is_valid():
        q = form.save(commit=False)
        q.user = request.user
        q.save()
        return redirect('home')
    return render(request, 'portal/home.html', {'questions': questions, 'form': form})

@login_required
def question_detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    answers = question.answers.all()
    form = AnswerForm(request.POST or None)
    if form.is_valid():
        ans = form.save(commit=False)
        ans.user = request.user
        ans.question = question
        ans.save()
        return redirect('question_detail', question_id=question_id)
    return render(request, 'portal/question_detail.html', {
        'question': question,
        'answers': answers,
        'form': form
    })

@login_required
def like_answer(request, answer_id):
    answer = get_object_or_404(Answer, id=answer_id)
    if request.user not in answer.likes.all():
        answer.likes.add(request.user)
    return redirect('question_detail', question_id=answer.question.id)



@login_required
def edit_question(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    form = QuestionForm(request.POST or None, instance=question)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'portal/edit_question.html', {'form': form})

@login_required
def delete_question(request, pk):
    question = get_object_or_404(Question, pk=pk, user=request.user)
    question.delete()
    return redirect('home')

@login_required
def edit_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk, user=request.user)
    form = AnswerForm(request.POST or None, instance=answer)
    if form.is_valid():
        form.save()
        return redirect('question_detail', question_id=answer.question.id)
    return render(request, 'portal/edit_answer.html', {'form': form})

@login_required
def delete_answer(request, pk):
    answer = get_object_or_404(Answer, pk=pk, user=request.user)
    question_id = answer.question.id
    answer.delete()
    return redirect('question_detail', question_id=question_id)
