# Generated by Django 4.2.5 on 2023-09-24 01:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment', models.FloatField()),
                ('is_payment_done', models.BooleanField(choices=[(False, 'No'), (True, 'Yes')])),
                ('payment_via', models.CharField(max_length=50)),
                ('Parking', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.parking')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.user')),
            ],
        ),
    ]