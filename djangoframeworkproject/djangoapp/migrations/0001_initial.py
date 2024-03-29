# Generated by Django 4.2.9 on 2024-01-05 07:50

from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]
    operations = [
        migrations.CreateModel(
            name='Framework',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=20, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('role', models.CharField(max_length=20)),
                ('isActive', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Django',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=12)),
                ('lname', models.CharField(max_length=12)),
                ('contact', models.CharField(max_length=10)),
                ('houseno', models.CharField(max_length=4)),
                ('blockno', models.CharField(max_length=2)),
                ('pic', models.FileField(default="profile.png",upload_to ="media/upload.png")),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='djangoapp.framework')),
            ],
        ),
    ]