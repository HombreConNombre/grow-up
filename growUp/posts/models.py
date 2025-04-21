from django.db import models
from django.contrib.auth.models import User

class Posts(models.Model):
    author = models.ForeignKey( User,
                               on_delete=models.CASCADE,
                               related_name= 'Posts')
    content = models.CharField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f""" Post by: {self.author.username}-
        content: {self.content[:30]}-
        when: {self.created_at.strftime('%d/%m/%Y. %H:%M:%S')}
        """