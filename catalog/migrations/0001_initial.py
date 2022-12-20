# Generated by Django 4.1.4 on 2022-12-19 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('amount', models.IntegerField(blank=True, default=1)),
                ('description', models.CharField(max_length=300)),
                ('quality', models.CharField(choices=[('good', 'Good'), ('bad', 'Bad'), ('regular', 'Regular'), ('excellent', 'Excellent')], max_length=15)),
                ('details', models.CharField(blank=True, max_length=250, null=True)),
                ('language', models.CharField(blank=True, max_length=50, null=True)),
                ('cover', models.ImageField(default='books/default.jpg', upload_to='books/')),
                ('authors', models.ManyToManyField(related_name='books', to='catalog.author')),
                ('editorial', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='books', to='catalog.editorial')),
                ('genres', models.ManyToManyField(related_name='books', to='catalog.genre')),
            ],
        ),
    ]
