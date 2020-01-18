# Generated by Django 3.0.2 on 2020-01-17 02:27

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonationAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contactNumber', models.CharField(max_length=70)),
                ('meetingDate', models.DateField()),
                ('completeDate', models.DateTimeField(blank=True, null=True)),
                ('approval', models.CharField(default='yet', max_length=20)),
                ('completed', models.CharField(default='yet', max_length=20)),
            ],
            options={
                'ordering': ('id',),
            },
        ),
        migrations.CreateModel(
            name='DonationRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('majorCategory', models.CharField(max_length=100)),
                ('minorCategory', models.CharField(max_length=100)),
                ('amount', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(50000)])),
                ('writeDate', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('progress', models.CharField(default='후원가능', max_length=20)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Member')),
            ],
            options={
                'ordering': ('-writeDate',),
            },
        ),
        migrations.CreateModel(
            name='DonorEvaluation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starNumber', models.IntegerField()),
                ('note', models.TextField(blank=True, null=True)),
                ('donationAction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestlist.DonationAction')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Member')),
            ],
            options={
                'ordering': ('-id',),
            },
        ),
        migrations.CreateModel(
            name='DonationSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('decided', models.BooleanField(default=False)),
                ('donationRequest', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestlist.DonationRequest')),
                ('donor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Member')),
            ],
        ),
        migrations.AddField(
            model_name='donationaction',
            name='donationRequest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='requestlist.DonationRequest'),
        ),
        migrations.AddField(
            model_name='donationaction',
            name='donor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Member'),
        ),
    ]