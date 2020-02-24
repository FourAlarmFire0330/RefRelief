from refrelief.models import Englishcourse
from refrelief.models import Events
from refrelief.models import Schools
from refrelief.models import Scholarship
from refrelief.models import Communitycourse
from refrelief.models import Suburb
import django_filters
from django.forms.widgets import SelectMultiple, Select, Textarea, CheckboxSelectMultiple


class DynamicChoiceMixin(object):
    @property
    def field(self):
        queryset = self.parent.queryset
        field = super(DynamicChoiceMixin, self).field

        choices = list()
        have = list()
        # iterate through the queryset and pull out the values for the field name
        for item in queryset:
            name = getattr(item, self.field_name)
            if name in have:
                continue
            have.append(name)
            choices.append((name, name))
        field.choices = choices
        return field


class DynamicChoiceFilter(DynamicChoiceMixin, django_filters.ChoiceFilter):
    pass


class CoursesFilter(django_filters.FilterSet):

    type = DynamicChoiceFilter(field_name='type', empty_label="Categories")
    day = DynamicChoiceFilter(field_name='weekday', empty_label="Days")
    distance_filter = DynamicChoiceFilter(field_name='distance_filter', empty_label="Range")

    class Meta:
        model = Englishcourse
        fields = ['type', 'day', 'distance_filter']


class EventsFilter(django_filters.FilterSet):
    category = DynamicChoiceFilter(field_name='category', empty_label="Type of Events")
    distance_filter = DynamicChoiceFilter(field_name='distance_filter', empty_label='Range')

    class Meta:
        model = Events
        fields = ['category', 'distance_filter']


class SchoolsFilter(django_filters.FilterSet):
    school_type = DynamicChoiceFilter(field_name='school_type', empty_label="Categories")
    suburb = django_filters.CharFilter(field_name='address_town', lookup_expr='icontains')
    postcode = django_filters.CharFilter(field_name='address_postcode', lookup_expr='icontains')

    class Meta:
        model = Schools
        fields = ['school_type', 'suburb', 'postcode']


class ScholarshipFilter(django_filters.FilterSet):
    provider = DynamicChoiceFilter(field_name='provider', empty_label="Providers")
    degree = DynamicChoiceFilter(field_name='degree', empty_label="Degree")

    class Meta:
        model = Scholarship
        fields = ['provider', 'degree']


class CommunityClassesFilter(django_filters.FilterSet):
    suburb = DynamicChoiceFilter(field_name='suburb', empty_label="Suburb")
    country = DynamicChoiceFilter(field_name='country', empty_label="Country")
    time = DynamicChoiceFilter(field_name='weekday', empty_label="Days")
    distance_filter = DynamicChoiceFilter(field_name='distance_filter', empty_label="Range")

    class Meta:
        model = Communitycourse
        fields = ['suburb', 'country', 'time', 'distance_filter']


class SuburbFilter(django_filters.FilterSet):
    suburb = DynamicChoiceFilter(field_name='suburb')
    postcode = DynamicChoiceFilter(field_name='postcode')

    class Meta:
        model = Suburb
        fields = ['suburb', 'postcode']