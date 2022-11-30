from django.db import models
from django.urls import reverse
from django.utils import timezone


class Author(models.Model):
    name = models.CharField(max_length=128)
    surname = models.CharField(max_length=128, blank=True, null=True)
    born = models.DateField(blank=True, null=True)
    portrait = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return f'{self.name} {self.surname}'
    
    def genres(self):
        # g_list = []
        # for book in self.books.all():
        #     for genre in book.genres.all():
        #         if genre not in g_list:
        #             g_list.append(genre)
        # return g_list
        return Genre.objects.filter(books__author=self).distinct()
    
    def url(self):
        return reverse('lib:author_detail', kwargs={'pk': self.id})
    
    def comments(self):
        return Comment.objects.filter(book__author=self)


class Genre(models.Model):
    name = models.CharField(max_length=64)
    
    def __str__(self):
        return self.name

    def url(self):
        return reverse(viewname='lib:genre_list') + f'#section-{self.id}'

    class Meta:
        ordering = ['name']


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField(blank=True, null=True)
    cover = models.URLField(blank=True, null=True)
    genres = models.ManyToManyField(Genre, related_name='books', blank=True)
    
    def __str__(self):
        return self.title
    
    def url(self):
        return reverse('lib:book_detail', kwargs={'pk': self.id})


class Comment(models.Model):
    text = models.TextField()
    author = models.CharField(max_length=128)
    book = models.ForeignKey(Book, related_name='comments', on_delete=models.CASCADE)
    published = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return self.text
    
    class Meta:
        ordering = ['-published']
        
        
class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.SET_NULL, null=True, related_name='instances')
    LOAN_STATUS = (
        ('a', 'available'),
        ('o', 'on loan'),
        ('m', 'maintenance'),
        ('r', 'reserved')
    )
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default='a')
    due_back = models.DateField(null=True, blank=True)
    
    def __str__(self):
        return f'{self.id} - {self.book} - "{self.status}"'
    