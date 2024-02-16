# Generated by Django 4.2.6 on 2023-12-04 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='bio',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='block',
            field=models.ManyToManyField(null=True, related_name='blocked', to='social.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='dob',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='following',
            field=models.ManyToManyField(null=True, related_name='followed_by', to='social.userprofile'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='phone',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='profilepics'),
        ),
    ]
