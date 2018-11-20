from django.db import models

# Create your models here.


class Blog (models.Model):
    title = models.CharField(default='文章标',max_length=50)
    date = models.DateField()
    image = models.ImageField(default='default.jpg',upload_to='images/')
    text = models.TextField(default='正文题')

    def __str__(self):
        return self.title

    def summary_text(self):
        sum = str(self.text)
        return sum[:20] + '...'
            