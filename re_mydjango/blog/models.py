from django.db import models


class Post(models.Model):
    STATUS_CHOICES = [
        ("draft", "임시"),
        ("published", "공개"),
        ("private", "비공개"),
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="draft")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
    )
    content = models.CharField(
        max_length=1000,
    )
