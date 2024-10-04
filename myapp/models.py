from django.db import models

# Create your models here.
# creating a models
# table name is Info
class Contact(models.Model):
    # elements of table name column
    name = models.CharField(max_length=122)
    # email column
    email = models.EmailField( max_length=254)
    # phone number column
    phone = models.IntegerField(max_length=10)
    # description column
    desc = models.CharField(max_length=200)
    # date column 
    date = models.DateField()

#  this function will show the name of the person instead of contact.object(id)
    def __str__(self):
        return self.email + "  ( " + self.name + " )"
    


# makemigrations - adds all the changes in the model in a file 
# migrate - creates models or tables for that changes evaluated by makemigrations

    #  to read the changes that you have done in models run command :-  python manage.py makemigrations

    
