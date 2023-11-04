from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.core.paginator import Paginator
from .models import Course
from .forms import CourseForm

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def course_list(request):
    courses = Course.objects.all()

    # Handle the search query parameter
    query = request.GET.get('query')
    if query:
        courses = courses.filter(title__icontains=query)

    # Configure the number of items per page
    items_per_page = 5  # You can adjust this value

    # Create a Paginator instance
    paginator = Paginator(courses, items_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        courses = paginator.page(page)
    except PageNotAnInteger:
        # If the page is not an integer, deliver the first page.
        courses = paginator.page(1)
    except EmptyPage:
        # If the page is out of range, deliver the last page.
        courses = paginator.page(paginator.num_pages)

    return render(request, 'course/short-course-view.html', {'courses': courses, 'query': query})

# def course_list(request):
#     courses = Course.objects.all()
#     print(courses.__dict__)
#     return render(request, 'course/short-course-view.html', {'courses': courses})

#     # Handle course list view here, including searching and pagination
#     pass
def create_course(request):
    if request.method == 'POST':
        
        form = CourseForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            # Create a new Course object with the form data
            form.save()
            return redirect('course_list')
        else:
            print("aaaaaaaaaaaaaaaaaaaaaaa")
    else:
        form = CourseForm()
    return render(request, 'course/short-course-create.html', {'form': form})
# def create_course(request):
#     return render(request, 'course/short-course-create.html')
#     # Handle course creation here
#     pass

def edit_course(request, course_id):
    
    course = get_object_or_404(Course, id=course_id)

    if request.method == 'POST':
        # Create a CourseForm instance with the POST data and the instance to edit
        form = CourseForm(request.POST, request.FILES, instance=course)

        if form.is_valid():
            # Save the edited course
            form.save()
            return redirect('course_list')  # Redirect to the course list page

    else:
        # Create a CourseForm instance with the course data to pre-fill the form
        form = CourseForm(instance=course)

    return render(request, 'course/short-course-create.html', {'form': form, 'course': course})
    # Handle course editing here
    pass



def delete_course(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    if course:
        course.delete()
        return redirect('course_list')
    
    return render(request, 'course/short-course-view.html', {'course': course})


def search_courses(request):
    print("pppppppppppppp========")
    print(request.method)
    query = request.GET.get("query")
    results = Course.objects.filter(title__icontains=query).values("title")

    return JsonResponse(list(results), safe=False)
