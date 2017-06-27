# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import Course, CourseManager

# Create your views here.
def index(request):
    context = {
        "courses" : Course.objects.all()
    }
    return render(request, 'courses_app/index.html', context)

def course_entry(request):
    postData = {
        "name" : request.POST['name'],
        "description" : request.POST['description']
    }

    new_course = Course.objects.no_blank_field(postData)
    return redirect('/')


def are_you_sure(request, id):
    context = {
        # "id" : id,
        "course" : Course.objects.get(id=id)
    }
    print context
    return render (request, 'courses_app/destroy.html', context)

def destroy(request, id):
    remove_course = Course.objects.remove_course(id)
    return redirect ('/')
