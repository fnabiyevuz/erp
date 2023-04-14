# Generated by Django 4.2 on 2023-04-13 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0003_rename_staffcategory_position_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='type',
            field=models.CharField(choices=[('Staff', 'Staff'), ('Intern', 'Intern')], default='Staff', max_length=25, verbose_name='Staff type'),
        ),
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated at')),
                ('lated_minutes', models.PositiveIntegerField(default=0)),
                ('is_absent', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_attendance', to='staff.staff')),
            ],
            options={
                'verbose_name': 'Attandance',
                'verbose_name_plural': 'Attandances',
            },
        ),
    ]
