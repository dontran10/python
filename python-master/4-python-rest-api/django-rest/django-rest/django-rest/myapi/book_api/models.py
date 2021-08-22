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
