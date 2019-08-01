from django.db import models

#Create blog model(s)
#With title, publication date, text/body, image

class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to='images/')

    def summary(self):
        return self.body[:20]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        return self.title

#Add the Blog app to the settings.py

#Create a migration

#Migrate

#Add to the admin
