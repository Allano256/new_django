# Generated by Django 4.2.13 on 2024-05-28 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_exerpt'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='updated_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

    #You create a migration on the class and then push it to the database
    #Type python3 manage.py migrate at the terminal to apply the migrations to the database.
    #python3 manage.py makemigrations' to make new migrations
    #python3 manage.py migrate blog zero.... while debugging to reset or reverse migrations
    #pip3 freeze --local > requirements.txt