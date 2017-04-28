# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models

# Unable to inspect table 'AcessoFechadura'
# The error was: 'NoneType' object has no attribute 'groups'

class AcessoFechadura(models.Model):
    id_acesso = models.AutoField(primary_key=True)
    num_documento = models.ForeignKey('Pessoa')
    id_fechadura = models.ForeignKey('Fechadura')

    def __str__(self):
        return str(self.id_acesso) + ' - ' + str(self.num_documento) + ' - ' + str(self.id_fechadura)

class Alarme(models.Model):
    alarmeid = models.IntegerField(primary_key=True)
    setor = models.TextField(blank=True, null=True)
    andar = models.TextField()
    estado = models.BooleanField()

    class Meta:
        db_table = 'Alarme'

    def __str__(self):
        return 'Alarme ' + str(self.alarmeid) + ' Setor ' + self.setor + ' Andar ' + self.andar 


class ControleLampada(models.Model):
    id = models.AutoField(primary_key=True)
    id_lampada = models.ForeignKey('Lampada')
    data = models.DateTimeField(null=False, blank=False)
    id_usuario = models.ForeignKey('UsuarioApp') 

    def __str__(self):
        return str(self.id_usuario) + ' - ' + str(self.id_lampada) + ' em ' + str(self.data)


class Fechadura(models.Model):
    numero_serie = models.CharField(primary_key=True, max_length=15, blank=False, null=False)
    setor = models.IntegerField(blank=True, null=True)
    ip = models.TextField()

    class Meta:
        db_table = 'Fechadura'

    def __str__(self):
        return 'Fechadura ' + self.numero_serie


class HistoricoAlarme(models.Model):
    data = models.DateTimeField(primary_key=True)
    id_alarme = models.ForeignKey('Alarme')

    def __str__(self):
        return str(self.id_alarme) + ' - ' + str(self.data)


# Unable to inspect table 'HistoricoFechadura'
# The error was: 'NoneType' object has no attribute 'groups'

#class HistoricoFechadura(models.Model):
 #   id_acesso = models.AutoField(primary_key=True)
  #  id_fechadura = models.ForeignKey('Fechadura')
   # Timestamp = models.DateTimeField(null=False)

class Lampada(models.Model):
    lampadaid = models.IntegerField(primary_key=True)
    setor = models.IntegerField(db_column='SETOR', blank=True, null=True)  # Field name made lowercase.
    andar = models.TextField(blank=True, null=True)
    estado = models.BooleanField()

    class Meta:
        db_table = 'Lampada'

    def __str__(self):
        return 'Lampadas do setor ' + str(self.setor) + ' - andar ' + self.andar


class Pessoa(models.Model):
    num_documento = models.CharField(primary_key=True, max_length=11)
    nome = models.CharField(null=False, max_length=100)
    cargo = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, null=False)
    tipoDocumento = models.ForeignKey('TipoDocumento')
    
    def __str__(self):
        return self.num_documento + ' - ' + self.nome


class TipoDocumento(models.Model):
    id = models.AutoField(primary_key=True)  
    tipo = models.CharField(db_column='Tipo', max_length=30)  # Field name made lowercase.

    class Meta:
        db_table = 'TipoDocumento'

    def __str__(self):
        return self.tipo


class UsuarioApp(models.Model):
    num_documento = models.ForeignKey('Pessoa')
    nome = models.CharField(unique=True, max_length=30)
    senha = models.CharField(max_length=128)

    class Meta:
        db_table ='UsuarioApp'

    def __str__(self):
        return self.nome

class AuthGroup(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)
    name = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()
    username = models.CharField(unique=True, max_length=30)

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    id = models.IntegerField(primary_key=True)  # AutoField?
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    action_time = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.AutoField(primary_key=True)  # AutoField?
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
