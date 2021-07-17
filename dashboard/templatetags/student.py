from django import template

register = template.Library()

@register.filter(name="is_student")
def is_student(user, suser):
    for u in suser:
        if(u.username==user.username):
               return True
    return False