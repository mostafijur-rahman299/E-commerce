# Generated by Django 2.2.6 on 2019-10-31 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0021_auto_20191031_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.CharField(help_text='i. Keep an unique email.', max_length=255, unique=True),
        ),
    ]