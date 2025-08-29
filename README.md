> # Travel Booking Application
>
> A simple web application built with Django to allow users to browse, book, and manage travel options like flights, trains, and buses.
>
> ## Features
> - User registration, login, and profile management using Django's authentication system.
> - View available travel options with filtering by type, source, destination, and date.
> - Book tickets with seat selection and booking status management.
> - View current and past bookings with option to cancel.
> - Responsive and clean UI using Tailwind CSS.
> - Basic form validation and seat availability checks.
> - MySQL database integration (optional).
>
> ## Technologies Used
> - Python 3.x  
> - Django 4.x  
> - Tailwind CSS for frontend styling  
> - MySQL (optional)  
> - Git for version control  
>
> ## Installation
> 1. Clone the repository:
>    ```
>    git clone https://github.com/Vikasprajapat1602/Travel-Booking-Application.git
>    cd Travel-Booking-Application
>    ```
> 2. Create and activate virtual environment:
>    ```
>    python -m venv venv
>    source venv/bin/activate   # For Windows: venv\Scripts\activate
>    ```
> 3. Install dependencies:
>    ```
>    pip install -r requirements.txt
>    ```
> 4. Configure MySQL database settings in `settings.py`.
> 5. Run migrations:
>    ```
>    python manage.py migrate
>    ```
> 6. Create superuser:
>    ```
>    python manage.py createsuperuser
>    ```
> 7. Run the server:
>    ```
>    python manage.py runserver
>    ```
> 8. Visit `http://127.0.0.1:8000` in your browser.
>
> ## Usage
> - Register a new user or log in with existing credentials.
> - Browse and filter travel options.
> - Book your travel tickets.
> - View and manage your bookings.
>
> ## Deployment
> You can deploy this Django project on any cloud platform like AWS or PythonAnywhere.
>
> ## Contribution
> Feel free to fork this repository and submit pull requests.
>
> ## License
> This project is licensed under the MIT License.
