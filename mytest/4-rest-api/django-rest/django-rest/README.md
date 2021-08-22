# Django REST Sample

## 1. Environment Setup

### Create new fresh project
- Generate project structure
```bash
# Setup virtual env
python -m venv venv
source venv/Scrips/activate

# Install django, mysql-client, django-rest-framework
pip install django
pip install mysqlclient
pip install djangorestframework
pip install pycodestyle
# Start new project
django-admin startproject myapi
cd myapi
python manage.py start_app book_api
```
- Update DB connection in `myapi/myapi/settings.py`
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'django_api',
        'USER': 'root',
        'PASSWORD': '123456',
        'HOST': 'localhost',
        'PORT': '3306',
    }
}
```
- Configure application in Django Project in `myapi/myapi/settings.py`
```python
INSTALLED_APPS = [
    ...
    'rest_framework',
    'rest_framework.authtoken',
    'book_api',
]
```
- Perform migration
```bash
python manage.py migrate
```
### Using with this source
```bash
python -m venv venv
source venv/Scrips/activate

pip install -r req
```

## 2. Models
- Create new model classes <strong>Author, Category, Book</strong>
```python
from django.db import models


# More reference at: https://docs.djangoproject.com/en/3.2/ref/models/fields/
class Category(models.Model):
    name = models.CharField(max_length=255)

    # Timestamp properties
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name


class Author(models.Model):
    NONE_GENDER = 'N'
    MALE_GENDER = 'M'
    FEMALE_GENDER = 'F'

    GENDER_CHOICES = [
        (MALE_GENDER, 'Male'),
        (FEMALE_GENDER, 'Female'),
    ]
    name = models.CharField(max_length=255)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES,
        default=NONE_GENDER,
    )

    # Timestamp properties
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Author'
        verbose_name_plural = 'Authors'

    def __str__(self):
        return self.name


class Book(models.Model):
    DRAFT_MODE = 'D'
    PUBLISHED_MODE = 'P'
    BOOK_STATUS_CHOICES = [
        (DRAFT_MODE, 'Draft'),
        (PUBLISHED_MODE, 'Published'),
    ]
    # Main properties
    title = models.CharField(max_length=255)
    summary = models.TextField()
    code = models.CharField(max_length=10, unique=True)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    highlight = models.BooleanField(default=False)
    status = models.CharField(
        max_length=2,
        choices=BOOK_STATUS_CHOICES,
        default=DRAFT_MODE,
    )
    deleted = models.BooleanField(default=False)
    # Relationship properties
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT, default=None)

    # Timestamp properties
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    # Metadata
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Book'
        verbose_name_plural = 'Books'

    def __str__(self):
        return self.title

```
```bash
# Under 'myapi' location
python manage.py makemigrations
python manage.py migrate
```
- Create Serializer class
```python
from rest_framework import serializers

from .models import Author, Book, Category


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'summary',
            'code', 'price', 'highlight', 'category', 'author'
        ]


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'name', 'gender']
```


## 3. API Authentication
https://www.django-rest-framework.org/api-guide/authentication/
```bash
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ]
}
```


## 4. Function-based view vs Class-based view
### 4.1. Function-based view
<strong>Benefits</strong>
- Easy to read, understand and implement.
- Explicit code flow.
- Straightforward usage of decorators.
- Good for the specialized functionality.

<strong>Drawbacks</strong>
- Code redundancy and hard to extend.
- Conditional branching will be used to handle HTTP methods.

### 4.2. Class-based view
<strong>Benefits</strong>
- Advantage of the class-based view is inheritance, it can be modified for the different use cases.
- It helps you in following the DRY principle.
- Using Mixins, you can extend class-based views, and you can add more functionalities.
- Better code structuring. In class-based views, we can use different class instance methods to generate different HTTP requests.
- Leverage Built-in generic class-based views.

<strong>Drawbacks</strong>
- Complex to implement and harder to read
- Implicit code flow.
- Extra import or method override required in view decorators.

## 5. Trade-offs between Views vs ViewSets
- Using viewsets can be a really useful abstraction. 
- It helps ensure that URL conventions will be consistent across your API, minimizes the amount of code you need to write, and allows you to concentrate on the interactions and representations your API provides rather than the specifics of the URL conf.
- Using viewsets is less explicit than building your views individually.