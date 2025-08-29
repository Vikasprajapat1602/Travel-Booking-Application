
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import TravelOption, Booking
from django.contrib import messages

# User Registration
def register_view(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect('register')

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists!")
            return redirect('register')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Account created successfully! Please login.")
        return redirect('login')

    return render(request, "core/register.html")


# User Login
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')
    return render(request, "core/login.html")


# User Logout
def logout_view(request):
    logout(request)
    return redirect('login')


def home_view(request):
    return render(request, "core/home.html")

# Profile Page
@login_required
def profile_view(request):
    if request.method == "POST":
        request.user.email = request.POST['email']
        request.user.save()
        messages.success(request, "Profile updated successfully")
        return redirect('profile')
    return render(request, "core/profile.html")


@login_required
def travel_list(request):
    options = TravelOption.objects.all()

    travel_type = request.GET.get('travel_type')
    source = request.GET.get('source')
    destination = request.GET.get('destination')
    date = request.GET.get('date')

    if travel_type:
        options = options.filter(travel_type__iexact=travel_type)
    if source:
        options = options.filter(source__icontains=source)
    if destination:
        options = options.filter(destination__icontains=destination)
    if date:
        options = options.filter(date_time__date=date)

    context = {
        'options': options,
    }
    return render(request, 'core/travel_list.html', context)




@login_required
def book_travel(request, travel_id):
    travel = get_object_or_404(TravelOption, id=travel_id)

    if request.method == "POST":
        seats = int(request.POST['seats'])

        if seats > travel.available_seats:
            messages.error(request, "Not enough seats available.")
            return redirect('travel_list')

        total_price = seats * travel.price

        booking = Booking.objects.create(
            user=request.user,
            travel_option=travel,
            number_of_seats=seats,
            total_price=total_price
        )

        # reduce available seats
        travel.available_seats -= seats
        travel.save()

        messages.success(request, "Booking confirmed successfully!")
        return redirect('my_bookings')

    return render(request, "core/book_travel.html", {"travel": travel})


@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, "core/my_bookings.html", {"bookings": bookings})


@login_required
def cancel_booking(request, booking_id):
    booking = get_object_or_404(Booking, id=booking_id, user=request.user)
    booking.status = "Cancelled"
    booking.save()
    messages.success(request, "Booking cancelled successfully.")
    return redirect('my_bookings')
