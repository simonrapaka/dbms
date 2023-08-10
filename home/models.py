from django.db import models

# Create your models here.
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Disease(models.Model):
    did = models.IntegerField(db_column='DID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    symptoms = models.CharField(max_length=100, blank=True, null=True)
    type = models.CharField(max_length=40, blank=True, null=True)
    branc_of_med = models.CharField(max_length=60, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'disease'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class HealthcareProviders(models.Model):
    hpid = models.IntegerField(db_column='HPID', primary_key=True)  # Field name made lowercase.
    mfid = models.ForeignKey('MedicalFacilities', models.DO_NOTHING, db_column='MFID', blank=True, null=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.IntegerField(blank=True, null=True)
    area_of_expertise = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'healthcare_providers'


class MedicalFacilities(models.Model):
    mfid = models.IntegerField(db_column='MFID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='Name', max_length=100, blank=True, null=True)  # Field name made lowercase.
    street = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    emailid = models.CharField(db_column='EmailID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='Phoneno', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medical_facilities'


class MedicalRecord(models.Model):
    mrid = models.IntegerField(db_column='MRID', primary_key=True)  # Field name made lowercase.
    patid = models.ForeignKey('Patient', models.DO_NOTHING, db_column='PatID', blank=True, null=True)  # Field name made lowercase.
    hpid = models.ForeignKey(HealthcareProviders, models.DO_NOTHING, db_column='HPID', blank=True, null=True)  # Field name made lowercase.
    mfid = models.ForeignKey(MedicalFacilities, models.DO_NOTHING, db_column='MFID', blank=True, null=True)  # Field name made lowercase.
    did = models.ForeignKey(Disease, models.DO_NOTHING, db_column='DID', blank=True, null=True)  # Field name made lowercase.
    prescid = models.ForeignKey('Prescription', models.DO_NOTHING, db_column='PrescID', blank=True, null=True)  # Field name made lowercase.
    disease = models.CharField(max_length=40, blank=True, null=True)
    date_time = models.DateField(blank=True, null=True)
    diagnosis = models.TextField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    weight = models.IntegerField(blank=True, null=True)
    chronic = models.CharField(max_length=40, blank=True, null=True)
    disability = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medical_record'


class Medicine(models.Model):
    medid = models.IntegerField(db_column='MedID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(max_length=100, blank=True, null=True)
    description = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'medicine'


class Patient(models.Model):
    patid = models.IntegerField(db_column='PatID', primary_key=True)  # Field name made lowercase.
    fname = models.CharField(db_column='Fname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(db_column='Lname', max_length=20, blank=True, null=True)  # Field name made lowercase.
    emailid = models.CharField(db_column='EmailID', max_length=50, blank=True, null=True)  # Field name made lowercase.
    phoneno = models.IntegerField(db_column='Phoneno', blank=True, null=True)  # Field name made lowercase.
    dob = models.DateField(db_column='DOB', blank=True, null=True)  # Field name made lowercase.
    addr = models.CharField(db_column='Addr', max_length=100, blank=True, null=True)  # Field name made lowercase.
    chronic = models.CharField(db_column='Chronic', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'patient'


class Prescription(models.Model):
    prescid = models.IntegerField(db_column='PrescID', primary_key=True)  # Field name made lowercase.
    medid = models.ForeignKey(Medicine, models.DO_NOTHING, db_column='MedID', blank=True, null=True)  # Field name made lowercase.
    dosage = models.CharField(max_length=40, blank=True, null=True)
    frequency = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'prescription'
