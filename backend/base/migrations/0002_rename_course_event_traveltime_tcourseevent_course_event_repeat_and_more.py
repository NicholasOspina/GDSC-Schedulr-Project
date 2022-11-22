# Generated by Django 4.0 on 2022-11-22 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tcourseevent',
            old_name='course_event_traveltime',
            new_name='course_event_repeat',
        ),
        migrations.RemoveField(
            model_name='tcourseevent',
            name='course',
        ),
        migrations.AddField(
            model_name='tcourseevent',
            name='course_event_weekday',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='tcourseevent',
            name='course_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tcourse'),
        ),
        migrations.AddField(
            model_name='tstudent',
            name='student_day_endtime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='tstudent',
            name='student_day_starttime',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tcourse',
            name='course_id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tcourse',
            name='course_name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tcourseevent',
            name='course_event_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tpersonalevent',
            name='personal_event_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tpersonalevent',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tstudent'),
        ),
        migrations.AlterField(
            model_name='tschedule',
            name='schedule_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tschedule',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tstudent'),
        ),
        migrations.AlterField(
            model_name='tstudent',
            name='student_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='tstudentcourse',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tcourse'),
        ),
        migrations.AlterField(
            model_name='tstudentcourse',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tstudent'),
        ),
        migrations.AlterField(
            model_name='tstudentcourse',
            name='student_course_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='ttimeslot',
            name='course_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tcourseevent'),
        ),
        migrations.AlterField(
            model_name='ttimeslot',
            name='personal_event',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tpersonalevent'),
        ),
        migrations.AlterField(
            model_name='ttimeslot',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tschedule'),
        ),
        migrations.AlterField(
            model_name='ttimeslot',
            name='timeslot_id',
            field=models.BigAutoField(primary_key=True, serialize=False),
        ),
        migrations.CreateModel(
            name='Tcourseclass',
            fields=[
                ('course_class_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('course_class_name', models.CharField(blank=True, max_length=200, null=True)),
                ('course_class_weekday', models.CharField(blank=True, max_length=50, null=True)),
                ('course_class_duration', models.IntegerField(blank=True, null=True)),
                ('course_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base.tcourse')),
            ],
        ),
    ]
