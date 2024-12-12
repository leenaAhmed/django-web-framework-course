
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


### To add a URL pattern with regex, you use the re_path() function instead of the path() function.


## What's the Migrations 
  - Migrations are how Django records changes made to models and implements these changes to the database schema.  
  - Migrations are tied into Django models and stored as migration files in a Migrations folder inside each app.

### Model 
  - In Django, the User table is created using a model which you may recall is a `class-based` representation of the User table in the database. 
  - So instead of writing the `SQL` query, you only need to add the new attribute to the model then run the migration scripts to implement the changes. 
  - Once the migration scripts run, the changes are applied.

## Benefits of Using Migrations in Django

  ### Syncing Issues
  - Reduces syncing issues between the model and database.
  - Helps ensure local databases are consistent across team members.
  - Developers can update their local database to the latest version using migration scripts stored in the code repository.

### Version Control
  - Acts as a version control system for the database schema.
  - Keeps an entire history of changes across the application.
  - Tracks who made changes and what changes were added.
  - Avoids issues associated with running scripts directly on the database, which are outside version control.

### Ease of Maintenance:
 - Migrations simplify maintenance by managing database changes within the codebase.
 - Developers don’t need to write direct SQL queries or figure out where to store database scripts for team access.

## How to use migrations

###  the difference between MakeMigrations and migrate 
 - MakeMigrations is Django's way of preparing the changes to be made in the model. 
 - For example, it creates a database such as this one named db.sqlite3. 
 - So you can think of `makemigrations` as the command that generates the sql commands and
  `migrate` as the command where those sql commands are executed.
- **migrate is responsible for applying and undoing migrations.**
- The X symbol represents the status of applying migrations after making them

## The Django object-relational mapping (ORM):
  - The ORM layer maps this model to a database table in the Django project. 
    Each attribute of a model class represents a field in the table. 

  - The Object-Relational Mapper (ORM) is one of Django’s most powerful features, allowing you to interact with your database in the same way that you would with SQL.
  
  - Django’s ORM is essentially a pythonic technique to build SQL to query and edit your database and obtain results.

  ### Django fields
  ***Field properties*** :  
    - primary_key
      Primary keys serve as unique identifiers for each row in a database table. Foreign keys link data in one table to the data in another table
    - `default` , `unique` ,`choices` ,

## Admin permission by shell 

```
  >>> from django.contrib.auth.models import User
  >>> user =  User.objects.create_user('aya', 'aya@gmail.com' , '#123abA')
  >>> user_name = User.objects.get(username= 'aya')
```

### MySQL Vs SQLite
- The SQLite database has a lot of limitations.
- It is serverless and doesn't have a user management system. 
- It is useful for smaller applications and for the development of a prototype to be upgraded eventually for   databases that are scalable and support client-server architecture.

 - MySQL is an open-source database and has a lot of advantages over SQLite, such as scalability and authentication. 