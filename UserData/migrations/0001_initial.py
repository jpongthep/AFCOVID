# Generated by Django 3.2.5 on 2021-07-25 03:34

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Unit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FullName', models.CharField(default=None, max_length=90)),
                ('ShortName', models.CharField(default=None, max_length=90)),
            ],
            options={
                'verbose_name_plural': 'หน่วยขึ้นตรง ทอ. [Unit]',
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('Rank', models.PositiveIntegerField(choices=[(30101, 'พล.อ.อ.*'), (30102, 'พล.อ.อ.*หญิง'), (30211, 'พล.อ.อ.'), (30212, 'พล.อ.อ.หญิง'), (30221, 'พล.อ.ท.'), (30222, 'พล.อ.ท.หญิง'), (30231, 'พล.อ.ต.'), (30232, 'พล.อ.ต.หญิง'), (30301, 'น.อ.(พ)'), (30302, 'น.อ.(พ) หญิง'), (30411, 'น.อ.'), (30412, 'น.อ.หญิง'), (30421, 'น.ท.'), (30422, 'น.ท.หญิง'), (30431, 'น.ต.'), (30432, 'น.ต.หญิง'), (30511, 'ร.อ.'), (30512, 'ร.อ.หญิง'), (30521, 'ร.ท.'), (30522, 'ร.ท.หญิง'), (30531, 'ร.ต.'), (30532, 'ร.ต.หญิง'), (30541, 'กห.ส.'), (30542, 'กห.ส.หญิง'), (30611, 'พ.อ.อ.(พ)'), (30612, 'พ.อ.อ.(พ) หญิง'), (30711, 'พ.อ.อ.'), (30712, 'พ.อ.อ.หญิง'), (30721, 'พ.อ.ท.'), (30722, 'พ.อ.ท.หญิง'), (30731, 'พ.อ.ต.'), (30732, 'พ.อ.ต.หญิง'), (30811, 'จ.อ.'), (30812, 'จ.อ.หญิง'), (30821, 'จ.ท.'), (30822, 'จ.ท.หญิง'), (30831, 'จ.ท.'), (30832, 'จ.ต.หญิง'), (30841, 'กห.ป.'), (30842, 'กห.ป.หญิง'), (31411, 'ว่าที่ น.อ.'), (31412, 'ว่าที่ น.อ.หญิง'), (31421, 'ว่าที่ น.ท.'), (31422, 'ว่าที่ น.ท.หญิง'), (31431, 'ว่าที่ น.ต.'), (31432, 'ว่าที่ น.ต.หญิง'), (31511, 'ว่าที่ ร.อ.'), (31512, 'ว่าที่ ร.อ.หญิง'), (31521, 'ว่าที่ ร.ท.'), (31522, 'ว่าที่ ร.ท.หญิง'), (31531, 'ว่าที่ ร.ต.'), (31532, 'ว่าที่ ร.ต.หญิง'), (40200, 'พนง.อาวุโสหญิง'), (40201, 'พนง.อาวุโส'), (40400, 'พนง.หญิง'), (40401, 'พนง.'), (0, '')], default=0, null=True)),
                ('Position', models.CharField(blank=True, max_length=250, null=True)),
                ('OfficePhone', models.CharField(blank=True, max_length=10, null=True)),
                ('MobileTel', models.CharField(blank=True, max_length=20, null=True)),
                ('Unit', models.CharField(blank=True, max_length=150, null=True)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'permissions': (('User_AF_CMO', 'User AF CMO'), ('User_Unit_CMO', 'User Unit CMO'), ('User_PMD', 'User PMD'), ('User_CRC', 'User CRC'), ('User_Hospital', 'User Hospital')),
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]
