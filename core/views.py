from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignupForm
from .forms import LoginForm
from .models import Users
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.hashers import check_password
# Create your views here.

def homepage(request):
  return render(request, 'homepage.html')

def usersDeta(request):
  all_users=Users.objects.all()
  print(all_users)
  return render(request, "loginrecord.html", {"users":all_users})

def signupForm(request):
   # confim the request type
  if request.method=="POST":
    # process the post request
    # create the form instance with the incoming request
     # validate the data
    form = SignupForm(request.POST)
    # extract the form clean data
    if form.is_valid():
      username = form.cleaned_data["username"]
      email=form.cleaned_data["email"]
      phone=form.cleaned_data["phone"]
      password=form.cleaned_data["password"]
      # save the data as record in the database
      Users.objects.create(
          username= username,
          email= email,
          phone= phone,
          password=make_password(password),
        )
      return redirect("homepage")
      # or return render(request, "student_registration.html", {"msg": "congratulations your registration is successful"})
    else:
      return render(request, "sign_up.html", {"form": form})


  # create the form studentRegistrationForm instance
  form=SignupForm()
  return render(request, "sign_up.html", {"form": form})


def loginForm(request):

    form = LoginForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = Users.objects.get(email__iexact=email)

                if check_password(password, user.password):

                    request.session['user_id'] = user.id

                    return redirect('products')

                else:
                    error = "Incorrect password. please try again"

            except Users.DoesNotExist:
                error = "Account does not exist. Please sign up."

            return render(request, 'login.html', {
                'form': form,
                'error': error
            })

    return render(request, 'login.html', {'form': form})