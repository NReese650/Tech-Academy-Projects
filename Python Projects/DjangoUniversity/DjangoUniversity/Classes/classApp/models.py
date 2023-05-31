from django.db import models


# Creates model of University Classes
class UniversityClasses(models.Model):
    title = models.CharField(max_length=60, default="", blank=True, null=False)
    course_number = models.IntegerField(default="", blank=True, null=False)
    instructor_name = models.CharField(max_length=60, default="", blank=True, null=False)
    duration = models.FloatField(null=True, blank=True, default=None)

    #Creates model manager
    object = models.Manager()

    #Displays the object output values in the form of a string
    def __str__(self):
        # Returns the input value of the title and instructor name
        # field as a tuple to display in the browser instead of the default titles
        display_course = '{0.title}: {0.instructor_name}'
        return display_course.format(self)

    # Removes added 's' that Django adds to the model name in the browser display
    class Meta:
        verbose_name_plural = "University Classes"


class UniversityCampus(models.Model):
    Campus_Name = models.CharField(max_length=200, default="", blank=True, null=False)
    State = models.CharField(max_length=2, default="", blank=True, null=False)
    Campus_ID = models.IntegerField(default="", blank=True, null=False)

    #Model Manager
    objects = models.Manager()

    class Meta:
        verbose_name_plural = "University Campus"