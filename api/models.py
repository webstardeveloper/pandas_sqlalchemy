# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desidered behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class Data(models.Model):
    number_of_records = models.IntegerField(db_column='Number of Records', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    artist_gid = models.TextField(db_column='Artist Gid', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    normalized_count = models.FloatField(db_column='Normalized Count', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    percentage = models.IntegerField(db_column='Percentage', blank=True, null=True)  # Field name made lowercase.
    track = models.TextField(db_column='Track', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'data'
