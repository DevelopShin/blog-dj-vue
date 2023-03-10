from django.db import models


class Post(models.Model):
    category = models.ForeignKey(
        'Category', on_delete=models.SET_NULL, blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    title = models.CharField('TITLE', max_length=50)
    description = models.CharField(
        'DESCRIPTION', max_length=100, blank=True, help_text='simple on-line text.')
    content = models.TextField('CONTENT')
    image = models.ImageField(
        'IMAGE', upload_to='post/%Y/%m/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    like = models.PositiveSmallIntegerField('LIKE', default=0)
    watch = models.PositiveSmallIntegerField('WATCH', default=0)

    def __str__(self):
        return self.title


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.CharField(
        'DESCRIPTION', max_length=100, blank=True, help_text='simple on-line text.')

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, blank=True, null=True)
    content = models.TextField('CONTENT')
    nickname = models.CharField('NICKNAME', max_length=20, null=True, default='hi')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @property
    def short_content(self):
        return self.content[:10]

    def __str__(self):
        return self.short_content
