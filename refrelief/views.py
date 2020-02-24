from refrelief.filters import CoursesFilter
from refrelief.filters import EventsFilter
from refrelief.filters import SchoolsFilter
from refrelief.filters import ScholarshipFilter
from refrelief.filters import CommunityClassesFilter
from refrelief.filters import SuburbFilter
from refrelief.models import Schools
from refrelief.models import Englishcourse
from refrelief.models import Scholarship
from refrelief.models import Events
from refrelief.models import Communitycourse
from refrelief.models import Suburb
from django.shortcuts import render
from geopy.distance import geodesic
from datetime import date, timedelta
import os


# Create your views here.
def render_html(request):
    today = date.today()
    event_list = Events.objects.all()
    # Set the time interval to 6 days, filter the result
    end_date = today + timedelta(days = 6)
    event_list = event_list.filter(start__range = [today, end_date])
    # Get the three nearest Events for upcoming events
    event_list = event_list.filter()[:4]

    return render(request, 'index.html', {'upcoming_events' : event_list})


# Get English course lists by different filters
def English_Course_list(request):
    courses_list = Englishcourse.objects.all()
    before_suburb_chosen = read_file("/var/www/Refugee/static/courses_action.txt")
    course_error_code = 0
    suburb_postcode_chosen = request.GET.get('suburb_postcode_submit', '')
    suburb_postcode_chosen = suburb_postcode_chosen.strip(' ')

    # Get all suburbs and postcodes for Victoria to calculate the distance
    suburb_postcode_list = Suburb.objects.values('suburb_postcode').distinct()
    suburb_postcode_list = list(suburb_postcode_list)
    suburbs_postcodes = []
    suburb_chosen = before_suburb_chosen
    for i in suburb_postcode_list:
        suburbs_postcodes.append(i['suburb_postcode'].strip(' '))

    # Get the latitude and longitude for the chosen location, otherwise set to default
    if suburb_postcode_chosen is not '':
        if suburb_postcode_chosen in suburbs_postcodes:
            create_str_to_txt(suburb_postcode_chosen, "/var/www/Refugee/static/courses_action.txt")
            # Format the suburb_postcode value
            suburb_chosen = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).suburb_postcode
            latitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lat
            longitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lon
            location_chosen = (latitude, longitude)
        else:
            # Error code for the wrong input Suburb and Postcode
            course_error_code = 1
            location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                               Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)
    else:
        location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                           Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)
    after_suburb_chosen = read_file("/var/www/Refugee/static/courses_action.txt")

    # Calculate the distance between selected area and destination
    for course in courses_list:
        location = (course.lat, course.lng)
        distances = round(geodesic(location_chosen, location).km, 2)
        if after_suburb_chosen != before_suburb_chosen:
            if 50 < distances <= 100:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='50 km - 100 km')
            elif 20 < distances <= 50:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='20 km - 50 km')
            elif 10 < distances <= 20:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='10 km - 20 km')
            elif 5 < distances <= 10:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='5 km - 10 km')
            elif 2 < distances <= 5:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='2 km - 5 km')
            elif distances <= 2:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='< 2 km')
            else:
                Englishcourse.objects.filter(index=course.index).update(distance=distances, distance_filter='beyond 100 km')

    courses_list = courses_list.order_by('distance')
    course_filter = CoursesFilter(request.GET, queryset=courses_list)
    if course_filter.qs.count() == 0:
        # No matching result based on the selected filter
        course_error_code = 1
    return render(request, 'Course/courses.html', {'filter' : course_filter, 'suburbs_postcodes' : suburbs_postcodes,  'suburb_chosen' : suburb_chosen, 'course_error_code' : course_error_code})


# Get Event lists by different filters
def events_list(request):
    events_list = Events.objects.all()
    before_suburb_chosen = read_file("/var/www/Refugee/static/events_action.txt")
    event_error_code = 0
    suburb_postcode_chosen = request.GET.get('suburb_postcode_submit', '')
    suburb_postcode_chosen = suburb_postcode_chosen.strip(' ')

    # Get all suburbs and postcodes for Victoria to calculate the distance
    suburb_postcode_list = Suburb.objects.values('suburb_postcode').distinct()
    suburb_postcode_list = list(suburb_postcode_list)
    suburbs_postcodes = []
    suburb_chosen = before_suburb_chosen
    for i in suburb_postcode_list:
        suburbs_postcodes.append(i['suburb_postcode'].strip(' '))

    # Get the latitude and longitude for the chosen location, otherwise set to default
    if suburb_postcode_chosen is not '':
        if suburb_postcode_chosen in suburbs_postcodes:
            create_str_to_txt(suburb_postcode_chosen, "/var/www/Refugee/static/events_action.txt")
            # Format the suburb_postcode value
            suburb_chosen = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).suburb_postcode
            latitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lat
            longitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lon
            location_chosen = (latitude, longitude)
        else:
            # Error code for the wrong input Suburb and Postcode
            event_error_code = 1
            location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                               Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)
    else:
        location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                           Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)

    after_suburb_chosen = read_file("/var/www/Refugee/static/events_action.txt")

    # Calculate the distance between selected area and destination
    for event in events_list:
        location = (event.latitude, event.longitude)
        distances = round(geodesic(location_chosen, location).km, 2)
        if after_suburb_chosen != before_suburb_chosen:
            if 50 < distances <= 100:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='50 km - 100 km')
            elif 20 < distances <= 50:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='20 km - 50 km')
            elif 10 < distances <= 20:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='10 km - 20 km')
            elif 5 < distances <= 10:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='5 km - 10 km')
            elif 2 < distances <= 5:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='2 km - 5 km')
            elif distances <= 2:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='< 2 km')
            else:
                Events.objects.filter(index=event.index).update(distance=distances, distance_filter='beyond 100 km')

    events_list = events_list.order_by('distance')
    event_filter = EventsFilter(request.GET, queryset=events_list)
    if event_filter.qs.count() == 0:
        event_error_code = 1
    return render(request, 'Event/event.html', {'filter' : event_filter, 'suburbs_postcodes' : suburbs_postcodes, 'suburb_chosen' : suburb_chosen, 'event_error_code': event_error_code})


# Get school lists by different filters
def school_list(request):
    school_list = Schools.objects.all()
    school_error_code = 0
    school_filter = SchoolsFilter(request.GET, queryset=school_list)

    # Get all suburbs and postcodes for Victoria to calculate the distance
    suburb_list = Schools.objects.values('address_town').distinct()
    suburb_list = list(suburb_list)
    suburbs_list = []
    for i in suburb_list:
        suburbs_list.append(i['address_town'].strip(' '))

    postcode_list = Schools.objects.values('address_postcode').distinct()
    postcode_list = list(postcode_list)
    postcodes_list = []
    for j in postcode_list:
        postcodes_list.append(j['address_postcode'])

    if school_filter.qs.count() == 0:
        school_error_code = 1
    return render(request, 'School/school.html', {'filter' : school_filter, 'school_error_code' : school_error_code, 'suburbs_list' : suburbs_list, 'postcodes_list' : postcodes_list})


# Get school lists by different filters
def scholarship_list(request):
    scholarships_list = Scholarship.objects.all()
    scholarship_error_code = 0
    scholarship_filter = ScholarshipFilter(request.GET, queryset=scholarships_list)
    if scholarship_filter.qs.count() == 0:
        # No matching result based on the selected filter
        scholarship_error_code = 1
    return render(request, 'Scholarship/scholarship.html', {'filter' : scholarship_filter, 'scholarship_error_code' : scholarship_error_code})


def community_class_list(request):
    community_classes_list = Communitycourse.objects.all()
    before_suburb_chosen = read_file("/var/www/Refugee/static/community_action.txt")
    community_class_error_code = 0
    suburb_postcode_chosen = request.GET.get('suburb_postcode_submit', '')
    suburb_postcode_chosen = suburb_postcode_chosen.strip(' ')

    # Get all suburbs and postcodes for Victoria to calculate the distance
    suburb_postcode_list = Suburb.objects.values('suburb_postcode').distinct()
    suburb_postcode_list = list(suburb_postcode_list)
    suburbs_postcodes = []
    suburb_chosen = before_suburb_chosen
    for i in suburb_postcode_list:
        suburbs_postcodes.append(i['suburb_postcode'].strip(' '))

    # Get the latitude and longitude for the chosen location, otherwise set to default
    if suburb_postcode_chosen is not '':
        if suburb_postcode_chosen in suburbs_postcodes:
            create_str_to_txt(suburb_postcode_chosen, "/var/www/Refugee/static/community_action.txt")
            # Format the suburb_postcode value
            suburb_chosen = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).suburb_postcode
            latitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lat
            longitude = Suburb.objects.get(suburb_postcode=suburb_postcode_chosen).lon
            location_chosen = (latitude, longitude)
        else:
            # Error code for the wrong input Suburb and Postcode
            community_class_error_code = 1
            location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                               Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)
    else:
        location_chosen = (Suburb.objects.get(suburb_postcode=before_suburb_chosen).lat,
                           Suburb.objects.get(suburb_postcode=before_suburb_chosen).lon)

    after_suburb_chosen = read_file("/var/www/Refugee/static/community_action.txt")

    # Calculate the distance between selected area and destination
    for community_class in community_classes_list:
        location = (community_class.lat, community_class.lng)
        distances = round(geodesic(location_chosen, location).km, 2)
        if after_suburb_chosen != before_suburb_chosen:
            if 50 < distances <= 100:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='50 km - 100 km')
            elif 20 < distances <= 50:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='20 km - 50 km')
            elif 10 < distances <= 20:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='10 km - 20 km')
            elif 5 < distances <= 10:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='5 km - 10 km')
            elif 2 < distances <= 5:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='2 km - 5 km')
            elif distances <= 2:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='< 2 km')
            else:
                Communitycourse.objects.filter(index=community_class.index).update(distance=distances, distance_filter='beyond 100 km')

    community_classes_list = community_classes_list.order_by('distance')
    community_classes_filter = CommunityClassesFilter(request.GET, queryset=community_classes_list)
    if community_classes_filter.qs.count() == 0:
        community_class_error_code = 1
    return render(request, 'Community/community.html', {'filter' : community_classes_filter, 'suburbs_postcodes' : suburbs_postcodes, 'suburb_chosen' : suburb_chosen, 'community_class_error_code' : community_class_error_code})


# Get the specific scholarship after clicking on Read More
def specific_scholarship(request):
    scholarship_id = request.GET.get('scholarship_id', '')
    scholarship = Scholarship.objects.get(index=scholarship_id)
    return render(request, 'Scholarship/scholarship-single.html', {'scholarship' : scholarship})


def create_str_to_txt(str_data, path_file_name):
    with open(path_file_name, "w") as f:
        f.write(str_data)


def read_file(path_file_name):
    with open(path_file_name, 'r') as f:
        data = f.readline()
        return data


def Iraq_map(request):
    return render(request, 'Community/Maps/Iraq.html')


def Syria_map(request):
    return render(request, 'Community/Maps/Syria.html')


def Burma_map(request):
    return render(request, 'Community/Maps/Burma.html')


def directions(request):
    location = request.GET.get('location_set', '')
    location = location.split(',')
    current_lat = location[0]
    current_lng = location[1]
    dest_lat = location[2]
    dest_lng = location[3]
    return render(request, 'Community/Maps/directions.html',
                  {'current_lat' : current_lat, 'current_lng' : current_lng,
                   'dest_lat' : dest_lat, 'dest_lng' : dest_lng})