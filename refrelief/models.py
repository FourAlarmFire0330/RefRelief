# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Englishcourse(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    class_name = models.TextField(db_column='Class name', blank=True,
                                  null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    type = models.TextField(db_column='Type', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    suburb = models.TextField(db_column='Suburb', blank=True, null=True)  # Field name made lowercase.
    contact = models.TextField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    weekday = models.TextField(blank=True, null=True)
    provider = models.TextField(blank=True, null=True)
    start = models.TextField(db_column='Start', blank=True, null=True)  # Field name made lowercase.
    end = models.TextField(db_column='End', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    distance_filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'EnglishCourse'


class Communitycourse(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    class_name = models.TextField(db_column='class name', blank=True,
                                  null=True)  # Field renamed to remove unsuitable characters.
    address = models.TextField(blank=True, null=True)
    contact = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    field_start_time = models.TextField(db_column=' Start Time', blank=True,
                                        null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters. Field renamed because it started with '_'.
    end_time = models.TextField(db_column='End Time', blank=True,
                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    weekday = models.TextField(blank=True, null=True)
    community = models.TextField(db_column='Community', blank=True, null=True)  # Field name made lowercase.
    suburb = models.TextField(db_column='Suburb', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    review = models.TextField(blank=False, null=False)
    website = models.TextField(blank=True, null=True)
    distance_filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'communitycourse'


class Events(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    start = models.TextField(blank=True, null=True)  # This field type is a guess.
    link = models.TextField(blank=True, null=True)
    title = models.TextField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    category = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    website = models.TextField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    distance_filter = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'events'


class Kindergarten(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    address = models.TextField(blank=True, null=True)
    name = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'kindergarten'


class Medical(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    region = models.TextField(db_column='Region', blank=True, null=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    service = models.TextField(db_column='Service', blank=True, null=True)  # Field name made lowercase.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    contact = models.TextField(db_column='Contact', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'medical'


class Scholarship(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    provider = models.TextField(db_column='Provider', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    type_of_study = models.TextField(db_column='Type of study', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    tuition_costs_covered = models.TextField(db_column='Tuition costs covered', blank=True,
                                             null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    link_to_more_information = models.TextField(db_column='Link to more information', blank=True,
                                                null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    notes = models.TextField(db_column='Notes', blank=True, null=True)  # Field name made lowercase.
    verified = models.TextField(db_column='Verified', blank=True, null=True)  # Field name made lowercase.
    degree = models.TextField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lng = models.FloatField(blank=True, null=True)
    review = models.TextField(blank=True, null=False)

    class Meta:
        managed = False
        db_table = 'scholarship'


class Schools(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    education_sector = models.TextField(db_column='Education_Sector', blank=True,
                                        null=True)  # Field name made lowercase.
    entity_type = models.IntegerField(db_column='Entity_Type', blank=True, null=True)  # Field name made lowercase.
    school_no = models.IntegerField(db_column='School_No', blank=True, null=True)  # Field name made lowercase.
    school_name = models.TextField(db_column='School_Name', blank=True, null=True)  # Field name made lowercase.
    school_type = models.TextField(db_column='School_Type', blank=True, null=True)  # Field name made lowercase.
    school_status = models.TextField(db_column='School_Status', blank=True, null=True)  # Field name made lowercase.
    address_line_1 = models.TextField(db_column='Address_Line_1', blank=True, null=True)  # Field name made lowercase.
    address_line_2 = models.TextField(db_column='Address_Line_2', blank=True, null=True)  # Field name made lowercase.
    address_town = models.TextField(db_column='Address_Town', blank=True, null=True)  # Field name made lowercase.
    address_state = models.TextField(db_column='Address_State', blank=True, null=True)  # Field name made lowercase.
    address_postcode = models.IntegerField(db_column='Address_Postcode', blank=True,
                                           null=True)  # Field name made lowercase.
    postal_address_line_1 = models.TextField(db_column='Postal_Address_Line_1', blank=True,
                                             null=True)  # Field name made lowercase.
    postal_address_line_2 = models.TextField(db_column='Postal_Address_Line_2', blank=True,
                                             null=True)  # Field name made lowercase.
    postal_town = models.TextField(db_column='Postal_Town', blank=True, null=True)  # Field name made lowercase.
    postal_state = models.TextField(db_column='Postal_State', blank=True, null=True)  # Field name made lowercase.
    postal_postcode = models.IntegerField(db_column='Postal_Postcode', blank=True,
                                          null=True)  # Field name made lowercase.
    full_phone_no = models.TextField(db_column='Full_Phone_No', blank=True, null=True)  # Field name made lowercase.
    lga_id = models.IntegerField(db_column='LGA_ID', blank=True, null=True)  # Field name made lowercase.
    lga_name = models.TextField(db_column='LGA_Name', blank=True, null=True)  # Field name made lowercase.
    x = models.FloatField(db_column='X', blank=True, null=True)  # Field name made lowercase.
    y = models.FloatField(db_column='Y', blank=True, null=True)  # Field name made lowercase.
    website = models.TextField(db_column='website', blank=True, null=True)
    distance = models.IntegerField(blank=True, null=True)
    review = models.TextField(db_column='review', blank=True, null=True)
    rating = models.TextField(db_column='rating', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'schools'


class Services(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    organisation = models.TextField(db_column='Organisation', blank=True, null=True)  # Field name made lowercase.
    services_provided = models.TextField(db_column='Services provided', blank=True,
                                         null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    address = models.TextField(db_column='Address', blank=True, null=True)  # Field name made lowercase.
    phone = models.TextField(db_column='Phone', blank=True, null=True)  # Field name made lowercase.
    email_address = models.TextField(db_column='Email Address', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    website = models.TextField(db_column='Website', blank=True, null=True)  # Field name made lowercase.
    opening_hours = models.TextField(db_column='Opening Hours', blank=True,
                                     null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.

    class Meta:
        managed = False
        db_table = 'services'


class Suburb(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    state = models.TextField(blank=True, null=True)
    dc = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    lat = models.FloatField(blank=True, null=True)
    lon = models.FloatField(blank=True, null=True)
    suburb_postcode = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'suburb'


class Distance(models.Model):
    index = models.AutoField(primary_key=True, blank=True)
    distance = models.TextField(blank=True, null=True)
    explain = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'distance'
