# Generated by Django 2.2.6 on 2019-10-30 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0018_auto_20191031_0008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='profile_img',
            field=models.ImageField(blank=True, null=True, upload_to='profile/'),
        ),
    ]