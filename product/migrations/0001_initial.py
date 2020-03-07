# Generated by Django 3.0.3 on 2020-03-02 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=225)),
                ('price', models.IntegerField()),
                ('cat_id', models.IntegerField()),
                ('image', models.ImageField(upload_to='')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
