rom django.contrib import admin
from django.apps import AppConfig


class BloodConfig(AppConfig):
    name = 'blood'


from django import forms

from . import models


class BloodForm(forms.ModelForm):
    class Meta:
        model=models.Stock
        fields=['bloodgroup','unit']

class RequestForm(forms.ModelForm):
    class Meta:
        model=models.BloodRequest
        fields=['patient_name','patient_age','reason','bloodgroup','unit']
        
 


from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]

    dependencies = [
        ('blood', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BloodRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.PositiveIntegerField()),
                ('mobile', models.CharField(max_length=20)),
                ('disease', models.CharField(max_length=100)),
                ('reason', models.CharField(max_length=500)),
                ('bloodgroup', models.CharField(max_length=10)),
                ('unit', models.PositiveIntegerField(default=0)),
                ('status', models.CharField(default='Pending', max_length=20)),
            ],
        ),
    ]
    
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('patient', '0001_initial'),
        ('donor', '0001_initial'),
        ('blood', '0002_bloodrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='bloodrequest',
            old_name='age',
            new_name='patient_age',
        ),
        migrations.RenameField(
            model_name='bloodrequest',
            old_name='name',
            new_name='patient_name',
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='disease',
        ),
        migrations.RemoveField(
            model_name='bloodrequest',
            name='mobile',
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_donor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='donor.Donor'),
        ),
        migrations.AddField(
            model_name='bloodrequest',
            name='request_by_patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='patient.Patient'),
        ),
    ]
    
    

class Migration(migrations.Migration):

    dependencies = [
        ('blood', '0003_auto_20210213_1053'),
    ]

    operations = [
        migrations.AddField(
            model_name='bloodrequest',
            name='date',
            field=models.DateField(auto_now=True),
        ),
    ]
    
from django.db import models
from patient import models as pmodels
from donor import models as dmodels
class Stock(models.Model):
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    def _str_(self):
        return self.bloodgroup

class BloodRequest(models.Model):
    request_by_patient=models.ForeignKey(pmodels.Patient,null=True,on_delete=models.CASCADE)
    request_by_donor=models.ForeignKey(dmodels.Donor,null=True,on_delete=models.CASCADE)
    patient_name=models.CharField(max_length=30)
    patient_age=models.PositiveIntegerField()
    reason=models.CharField(max_length=500)
    bloodgroup=models.CharField(max_length=10)
    unit=models.PositiveIntegerField(default=0)
    status=models.CharField(max_length=20,default="Pending")
    date=models.DateField(auto_now=True)