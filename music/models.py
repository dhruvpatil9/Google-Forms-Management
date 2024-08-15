# # -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import Permission, User
from django.db import models


# class Album(models.Model):
#     user = models.ForeignKey(User, default=1)
#     artist = models.CharField(max_length=250)
#     album_title = models.CharField(max_length=500)
#     genre = models.CharField(max_length=100)
#     album_logo = models.FileField()
#     is_favorite = models.BooleanField(default=False)

#     def __str__(self):
#         return self.album_title + ' - ' + self.artist


# class Song(models.Model):
#     album = models.ForeignKey(Album, on_delete=models.CASCADE)
#     song_title = models.CharField(max_length=250)
#     audio_file = models.FileField(default='')
#     is_favorite = models.BooleanField(default=False)

#     def __str__(self):
#         return self.song_title

# # First - UserID, FormID, FormName, FormDescr
# # Second - QuesID, Label, Type, Text
TYPE_CHOICES = (
    ('multiline','Multi Line Text'),
    ('singleline', 'Single line Text'),
    ('number', 'Number'),
    ('num_range', 'Numeric Range'),
    ('url','URL'),
    ('checkbox','Checkbox'),
    ('dropdown','Dropdown'),
    ('radio','Radio Buttons'),
    ('file_upload', 'Upload File'),
    ('email', 'E-mail')
)


class Gform(models.Model):
    user = models.ForeignKey(User, default=1)
    # form_id = models.IntegerField(default=1)
    gform_name = models.CharField(max_length=50,default="")
    gform_desc = models.CharField(max_length=500,default="")
    	

    def __str__(self):
        return self.gform_name + " " + self.gform_desc


class Question(models.Model):
    #ques_id = models.IntegerField(default=1)
    gform = models.ForeignKey(Gform, on_delete=models.CASCADE, default=1)
    #ques_type = models.CharField(max_length=500)
    ques_type = models.CharField(max_length=50, choices=TYPE_CHOICES, default="multiline")
    ques_text = models.CharField(max_length=500)
    choices = models.CharField(max_length=500,default="")
    is_req = models.BooleanField(default=False)
    is_vis = models.BooleanField(default=False)
    #color = models.CharField(max_length=6, choices=COLOR_CHOICES, default='green')


    def __str__(self):
        return self.ques_text + " " +self.ques_type

    def choices_as_list(self):
    	return self.choices.split(',')


class Response(models.Model):

	gform = models.ForeignKey(Gform, on_delete=models.CASCADE, default=1)
	resp_text = models.CharField(max_length=2000)

	def __str__(self):
		return self.resp_text


# # class Data1(models.Model):
# #     client= models.CharField(max_length=100,default='Hi')
# #     Answer1= models.CharField(max_length=100,default='Hi')
# #     Answer2= models.CharField(max_length=200,default='Hi')
# #     Answer3= models.CharField(max_length=200,default='Hi')
    
# # class Data2(models.Model):
# #     client= models.CharField(max_length=100,default='Hi')
# #     Answer1= models.CharField(max_length=100,default='Hi')
# #     Answer2= models.CharField(max_length=200,default='Hi')
# #     Answer3= models.CharField(max_length=200,default='Hi')

# # class QuesType(models.Model):
# #     TypeID= models.IntegerField()
# #     Type= models.CharField(max_length=50,default='Hi')

# # class UserForm(models.Model):
# #     UserID= models.IntegerField()
# #     FormID= models.IntegerField()
# #     FormName=models.CharField(max_length=100,default='Hi')

# #     class Meta:
        
# #         unique_together=(("UserID","FormID"),)

# # class Question(models.Model):
# #     QuesID= models.IntegerField()
# #     FormID= models.ForeignKey(UserForm,on_delete=models.CASCADE)
# #     TypeID= models.IntegerField()
# #     Questxt= models.CharField(max_length=100,default='Hi')

# #     class Meta:
# #         unique_together=(("QuesID","FormID"),)


# # class Mcq(models.Model):
# #     QuesID= models.ForeignKey(Question,on_delete=models.CASCADE)
# #     Options= models.CharField(max_length=100,default='Hi')
