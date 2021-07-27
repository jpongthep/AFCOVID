# from django.contrib.auth.models import Group
from django import template

register = template.Library()

@register.simple_tag
def url_replace(request, field, value):

    print('urlreplace:', field)
    print('request.GET.copy():', request.GET.copy())


    dict_ = request.GET.copy()

    dict_[field] = value

    return dict_.urlencode()


# @register.filter(name='has_group')
# def has_group(user, group_name):
#     group = Group.objects.get(name=group_name)
#     return True if group in user.groups.all() else False


# @register.filter(name='in_group')
# def in_group(user, groups_name):
#     GroupListText = groups_name.split(", ")

#     StayGroup = False
#     for GroupText in GroupListText:
#         group = Group.objects.get(name=groups_name)
#         if group in user.groups.all():
#             StayGroup = True
#             break    
#     return StayGroup

