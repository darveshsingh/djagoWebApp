from django.contrib.auth.models import User
from django.db import models


# Create your models here.
class Topic(models.Model):
    name = models.CharField(max_length=200)
    category = models.CharField(max_length=200)

    def __str__(self): return str(self.name)


class Course(models.Model):
    topic = models.ForeignKey(Topic, related_name='courses', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    for_everyone = models.BooleanField(default=True)
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self): return str(self.name)


class Student(User):
    CITY_CHOICES = [('WS', 'Windsor'), ('CG', 'Calgery'), ('MR', 'Montreal'), ('VC', 'Vancouver')]
    school = models.CharField(max_length=50, null=True, blank=True)
    city = models.CharField(max_length=2, choices=CITY_CHOICES, default='WS')
    interested_in = models.ManyToManyField(Topic)

    def __str__(self): return str(self.username)


class Order(models.Model):
    course = models.ManyToManyField(Course)
    student = models.ForeignKey(Student, related_name='students', on_delete=models.CASCADE)
    ORDER_CHOICES = [(0, 'Cancelled'), (1, "Order Confirmed")]
    order_status = models.IntegerField(choices=ORDER_CHOICES, default=1)
    levels = models.IntegerField(default=1)
    order_date = models.DateField(auto_now=True)

    def __str__(self):
        order_string = 'NoOrder'
        is_more_than0 = False
        all_courses = self.course.values_list("name")
        for order_course_name in all_courses:
            if not is_more_than0:
                order_string = str(''.join(order_course_name))
                is_more_than0 = True
            else:
                order_string = order_string + ' and ' + str(''.join(order_course_name))
        return order_string + ' by ' + self.student.first_name + ' ' + self.student.last_name
        # return self.course.values_list("name")

    def total_cost(self):
        total_cost = 0
        for course in self.course:
            total_cost = course.price + total_cost
        return total_cost
