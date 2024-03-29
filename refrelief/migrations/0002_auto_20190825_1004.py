# Generated by Django 2.2.4 on 2019-08-25 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('refrelief', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codename', models.CharField(max_length=100)),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
                ('last_name', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('change_message', models.TextField()),
                ('action_flag', models.PositiveSmallIntegerField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Englishcourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unnamed_0', models.IntegerField(blank=True, db_column='Unnamed: 0', null=True)),
                ('class_field', models.TextField(blank=True, db_column='Class', null=True)),
                ('time', models.TextField(blank=True, db_column='Time', null=True)),
                ('class_name', models.TextField(blank=True, db_column='Class name', null=True)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
                ('cost', models.TextField(blank=True, db_column='Cost', null=True)),
                ('registration_required', models.TextField(blank=True, db_column='Registration required', null=True)),
                ('website', models.TextField(blank=True, db_column='Website', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('contact', models.TextField(blank=True, db_column='Contact', null=True)),
                ('email', models.TextField(blank=True, db_column='Email', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
            ],
            options={
                'db_table': 'EnglishCourse',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Medical',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('region', models.TextField(blank=True, db_column='Region', null=True)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('service', models.TextField(blank=True, db_column='Service', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('contact', models.TextField(blank=True, db_column='Contact', null=True)),
            ],
            options={
                'db_table': 'medical',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='RefugeeSchool',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.CharField(db_column='School', max_length=50)),
                ('project_type', models.CharField(db_column='Project_Type', max_length=50)),
                ('cohort', models.CharField(db_column='Cohort', max_length=50)),
                ('partner_agency', models.CharField(db_column='Partner_Agency', max_length=50)),
            ],
            options={
                'db_table': 'refugee_school',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Scholarship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('provider', models.TextField(blank=True, db_column='Provider', null=True)),
                ('state', models.TextField(blank=True, db_column='State', null=True)),
                ('type_of_study', models.TextField(blank=True, db_column='Type of study', null=True)),
                ('value', models.TextField(blank=True, db_column='Value', null=True)),
                ('eligiblity_criteria', models.TextField(blank=True, db_column='Eligiblity criteria', null=True)),
                ('tuition_costs_covered', models.TextField(blank=True, db_column='Tuition costs covered', null=True)),
                ('link_to_more_information', models.TextField(blank=True, db_column='Link to more information', null=True)),
                ('opening_date', models.TextField(blank=True, db_column='Opening date', null=True)),
                ('closing_date', models.TextField(blank=True, db_column='Closing date', null=True)),
                ('notes', models.TextField(blank=True, db_column='Notes', null=True)),
                ('verified', models.TextField(blank=True, db_column='Verified', null=True)),
            ],
            options={
                'db_table': 'scholarship',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Schools',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.TextField(blank=True, db_column='School', null=True)),
                ('project_type', models.TextField(blank=True, db_column='Project_Type', null=True)),
                ('cohort', models.TextField(blank=True, db_column='Cohort', null=True)),
                ('partner_agency', models.TextField(blank=True, db_column='Partner_Agency', null=True)),
            ],
            options={
                'db_table': 'schools',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organisation', models.TextField(blank=True, db_column='Organisation', null=True)),
                ('services_provided', models.TextField(blank=True, db_column='Services provided', null=True)),
                ('address', models.TextField(blank=True, db_column='Address', null=True)),
                ('phone', models.TextField(blank=True, db_column='Phone', null=True)),
                ('email_address', models.TextField(blank=True, db_column='Email Address', null=True)),
                ('website', models.TextField(blank=True, db_column='Website', null=True)),
                ('opening_hours', models.TextField(blank=True, db_column='Opening Hours', null=True)),
            ],
            options={
                'db_table': 'services',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]
