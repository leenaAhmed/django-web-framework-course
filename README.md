
# Setting Up a Django Project

## Step 1: Install `virtualenv`
```bash
pip install virtualenv
```

## Step 2: Create a Virtual Environment
Navigate to your desired folder:
```bash
cd E:\file_name\django
```

Create a virtual environment:
```bash
virtualenv .
```

Or create a virtual environment with a specific name:
```bash
virtualenv newapp
```

## Step 3: Activate the Virtual Environment
```bash
newapp\Scripts\activate
```

## Step 4: Install Django
```bash
pip install django
```

## Step 5: Create a Django Project
Navigate to the virtual environment directory and create a new Django project:
```bash
django-admin startproject medocApp
```

## Step 6: Run the Development Server
Navigate to the project directory and start the server:
```bash
python manage.py runserver
```

## Step 7: Run Migrations
To apply initial migrations:
```bash
python manage.py migrate
```

## Step 8: Collect Static Files
```bash
python manage.py collectstatic
```

## Step 9: Rollback Migrations (Optional)
To rollback migrations for a specific app (e.g., `pages`) to zero:
```bash
python manage.py migrate pages zero
```


## The django.views.generic:
  The django.views.generic module contains several view classes that provide the functionality required to perform tasks such as rendering a template, showing an instance, showing the list of instances, adding a new model instance, updating an instance and so on. 


## reverse() function
  However, the hard-coded URLs make the application less scalable and difficult to maintain as the project grows. In such a case, you can obtain the URL from the name parameter used in the path() function.

  Start the Django shell.

```bash
    from django.urls import reverse 
```
Django’s `reverse()` function returns the URL path to which it is mapped.

```bash
  >>> from django.urls import reverse 
  >>> reverse('index') 
```

## Application namespace
 The application namespace is created by defining `app_name` variable in the application’s urls.py and assigning it the name of the app `app_name='demoapp'` 


 