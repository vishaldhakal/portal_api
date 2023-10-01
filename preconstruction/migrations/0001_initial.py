# Generated by Django 3.1.6 on 2023-08-31 14:43

from django.db import migrations, models
import django.db.models.deletion
import django_summernote.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=1000, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Developer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('name', models.CharField(max_length=500)),
                ('phone', models.CharField(blank=True, max_length=200)),
                ('website_link', models.TextField(blank=True)),
                ('details', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_description', django_summernote.fields.SummernoteTextField(blank=True)),
                ('event_date', models.DateTimeField()),
                ('event_link', models.CharField(default='#', max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='PreConstruction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('builder_sales_email', models.CharField(max_length=500)),
                ('builder_sales_phone', models.CharField(max_length=500)),
                ('project_name', models.CharField(max_length=500)),
                ('slug', models.CharField(max_length=1000, unique=True)),
                ('price_starting_from', models.FloatField(default=0)),
                ('price_to', models.FloatField(default=0)),
                ('project_type', models.CharField(choices=[('Condo', 'Condo'), ('Townhome', 'Townhome'), ('Semi-Detached', 'Semi-Detached'), ('Detached', 'Detached'), ('NaN', 'NaN')], default='NaN', max_length=500)),
                ('description', django_summernote.fields.SummernoteTextField(blank=True)),
                ('project_address', models.CharField(max_length=500)),
                ('status', models.CharField(choices=[('Upcoming', 'Upcoming'), ('Selling', 'Selling'), ('Planning Phase', 'Planning Phase'), ('Sold out', 'Sold out')], default='Upcoming', max_length=500)),
                ('co_op_available', models.BooleanField(default=False)),
                ('date_of_upload', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preconstruction.city')),
                ('developer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preconstruction.developer')),
            ],
            options={
                'ordering': ('-date_of_upload',),
            },
        ),
        migrations.CreateModel(
            name='PreConstructionImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.FileField(upload_to='')),
                ('preconstruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to='preconstruction.preconstruction')),
            ],
        ),
        migrations.CreateModel(
            name='PreConstructionFloorPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floorplan', models.FileField(upload_to='')),
                ('preconstruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='floorplan', to='preconstruction.preconstruction')),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('news_title', models.CharField(max_length=1000)),
                ('news_thumbnail', models.FileField(blank=True, upload_to='')),
                ('news_description', django_summernote.fields.SummernoteTextField(blank=True)),
                ('date_of_upload', models.DateField(auto_now_add=True)),
                ('last_updated', models.DateField(auto_now=True)),
                ('news_link', models.CharField(default='#', max_length=2000)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='preconstruction.city')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteNews',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news_agent', to='accounts.agent')),
                ('news', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='news', to='preconstruction.news')),
            ],
        ),
        migrations.CreateModel(
            name='FavouriteEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event_agent', to='accounts.agent')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='event', to='preconstruction.event')),
            ],
        ),
        migrations.CreateModel(
            name='Favourite',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('agent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='agent', to='accounts.agent')),
                ('preconstruction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='preconstruction', to='preconstruction.preconstruction')),
            ],
        ),
    ]
