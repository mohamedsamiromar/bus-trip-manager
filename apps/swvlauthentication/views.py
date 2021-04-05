
from django.contrib.auth import authenticate, login

from django.shortcuts import render, redirect
from apps.swvlauthentication.form import SignUpForm, UserForm, ProfileForm
from apps.swvl_admin.models import Captin, Passenger
from apps.swvlauthentication.models import Profile


def loginView(request):
    if request.method == 'GET':
        return render(request, 'registration/login.html')
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)

    if user is not None:
        login(request, user)

        if hasattr(user, 'admin'):
            return redirect('admin_page')
        elif hasattr(user, 'captin') and user.captin.exists():
            return redirect('/take_trip')
        if hasattr(user, 'passenger') and user.passenger.exists():
            return redirect('/home')
        else:
            return redirect('registration/login.html')

    else:
        return render(request, 'registration/login.html', {'error': "Invalid username and password"})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            selects = request.POST.get('user_type')
            if selects == 'passenger':
                passanger = Passenger(user=user, phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'])
                passanger.save()
            elif selects == 'admin':
                admin = Passenger(user=user, age=form.cleaned_data['age'], email=form.cleaned_data['email'])
                admin.save()
            elif selects == 'captin':
                captin = Captin(user=user, phone_number=form.cleaned_data['phone_number'], email=form.cleaned_data['email'])
                captin.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            if selects == 'passenger':
                return render(request, 'passenger/where_to.html', {'form': form})
            elif selects == 'captin':
                return render(request, 'captin/take_trip.html', {'form': form})
            elif selects == 'admin':
                return render(request, 'swvl_admin/admin_page.html', {'form': form})
            return redirect('where_to')
        else:
            return render(request, 'registration/signup.html', {'form': form})
    else:
        form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


def edit_profile(request):
    profile = Profile.objects.get(user=request.user)
    if request.method == 'POST':
        userform = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=profile)
        if userform.is_valid() and profile_form.is_valid():
            userform.save()
            myform = profile_form.save(commit=False)
            myform.user = request.user
            myform.save()
        return redirect('/registration/login')
    elif request.method == 'GET':

        userform = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=profile)
        return render(request, 'registration/edit_profile.html', {
            'userform': userform,
            'profile_form': profile_form
        })
