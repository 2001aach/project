# Generated by Django 4.1.3 on 2022-12-22 13:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='replay',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('cash', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homeapp.admin_addwork')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='admin_payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField()),
                ('paid_date', models.DateField(auto_now=True)),
                ('bill_date', models.DateField(auto_now=True)),
                ('status', models.IntegerField(default=0)),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='homeapp.userpage')),
            ],
        ),
    ]