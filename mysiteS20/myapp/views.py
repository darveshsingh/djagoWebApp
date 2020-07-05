from django.shortcuts import render, get_object_or_404
import sys
from django.http import HttpResponse
from .models import Topic, Course, Student, Order
# Create your views here.


def index(request):
    top_list = Topic.objects.all().order_by('id')[:10]
    response = HttpResponse()
    heading1 = '<p>' + 'List of topics: ' + '</p>'
    response.write(heading1)
    for topic in top_list:
        para = '<p>'+ str(topic.id) + ': ' + str(topic) + '</p>'
        response.write(para)

    course_list = Course.objects.all().order_by("-price")[:5]
    heading2 = '<p>' + 'List of top 5 courses in descending order: ' + '</p>'
    response.write(heading1)
    for course in course_list:
        para = '<p>' + str(course.name) + ': ' + str(course.price)
        if course.for_everyone:
            para = para + " (This course is for Everyone) </p>"
        else:
            para = para + " (This course is Not for Everyone) </p>"
        response.write(para)

    return response


def about(request):
    about_str = "This is an E-learning Website!\nSearch our Topics to find all available Courses."
    response = HttpResponse()
    response.write(about_str)
    return response


def detail(request, top_no):
    print("Received Number: "+top_no)
    topic_id = int(top_no)
    response = HttpResponse()

    topic = get_object_or_404(Topic, id=topic_id)
    response.write("<h2>"+top_no+": "+topic.category+"</h2>")
    para1 = "<p>List of courses for the category "+topic.category+": </p>"
    response.write(para1)

    course_list_for_topic = Course.objects.filter(topic__name=topic.name)
    counter = 0
    for course in course_list_for_topic:
        counter = counter + 1
        para = "<p>"+str(counter)+": "+course.name+"</p>"
        response.write(para)
    return response
