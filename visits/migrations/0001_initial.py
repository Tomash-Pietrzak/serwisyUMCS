# Generated by Django 3.2.9 on 2021-12-10 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0003_delete_visit'),
    ]

    operations = [
        migrations.CreateModel(
            name='Visit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(default='', max_length=255)),
                ('date', models.DateTimeField(default='')),
                ('doctor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.doctor')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
            ],
            options={
                'ordering': ['date'],
            },
        ),
    ]
