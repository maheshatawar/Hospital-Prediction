# Generated by Django 4.1.5 on 2023-02-02 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient_data',
            name='patient_sym2',
            field=models.CharField(choices=[('default', 'Select Symptom'), ('0', 'itching'), ('1', 'skin_rash'), ('2', 'nodal_skin_eruptions'), ('3', 'continuous_sneezing'), ('4', 'shivering'), ('5', 'chills'), ('6', 'joint_pain')], default=34, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='patient_sym3',
            field=models.CharField(choices=[('default', 'Select Symptom'), ('0', 'itching'), ('1', 'skin_rash'), ('2', 'nodal_skin_eruptions'), ('3', 'continuous_sneezing'), ('4', 'shivering'), ('5', 'chills'), ('6', 'joint_pain')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='patient_sym4',
            field=models.CharField(choices=[('default', 'Select Symptom'), ('0', 'itching'), ('1', 'skin_rash'), ('2', 'nodal_skin_eruptions'), ('3', 'continuous_sneezing'), ('4', 'shivering'), ('5', 'chills'), ('6', 'joint_pain')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='patient_data',
            name='patient_sym5',
            field=models.CharField(choices=[('default', 'Select Symptom'), ('0', 'itching'), ('1', 'skin_rash'), ('2', 'nodal_skin_eruptions'), ('3', 'continuous_sneezing'), ('4', 'shivering'), ('5', 'chills'), ('6', 'joint_pain')], default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='patient_data',
            name='patient_sym1',
            field=models.CharField(choices=[('default', 'Select Symptom'), ('0', 'itching'), ('1', 'skin_rash'), ('2', 'nodal_skin_eruptions'), ('3', 'continuous_sneezing'), ('4', 'shivering'), ('5', 'chills'), ('6', 'joint_pain')], max_length=50),
        ),
    ]
