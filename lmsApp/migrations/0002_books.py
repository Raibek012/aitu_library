
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('lmsApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn', models.CharField(max_length=250)),
                ('title', models.CharField(max_length=250)),
                ('description', models.TextField(blank=True, null=True)),
                ('author', models.TextField(blank=True, null=True)),
                ('publisher', models.CharField(max_length=250)),
                ('date_published', models.DateTimeField()),
                ('status', models.CharField(choices=[('1', 'Active'), ('2', 'Inactive')], default=1, max_length=2)),
                ('delete_flag', models.IntegerField(default=0)),
                ('date_added', models.DateTimeField(default=django.utils.timezone.now)),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('sub_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lmsApp.subcategory')),
            ],
            options={
                'verbose_name_plural': 'List of Books',
            },
        ),
    ]
