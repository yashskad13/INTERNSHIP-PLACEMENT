from django import template

register = template.Library()


@register.filter(name="is_student")
def is_student(user, suser):
    for u in suser:
        if(u.username == user.username):
            return True
    return False


@register.filter(name="student_yourname")
def student_yourname(username, suser):
    for u in suser:
        if(u.username == username):
            return u.yourname


@register.filter(name="email")
def email(username, suser):
    for u in suser:
        if(u.username == username):
            return u.email


@register.filter(name="student_branch")
def student_branch(username, suser):
    for u in suser:
        if(u.username == username):
            return u.branch


@register.filter(name="yog")
def yog(username, suser):
    for u in suser:
        if(u.username == username):
            return u.yog


@register.filter(name="contact")
def contact(username, suser):
    for u in suser:
        if(u.username == username):
            return u.contact


@register.filter(name="company_name")
def company_name(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.companyname


@register.filter(name="address")
def address(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.address


@register.filter(name="company_email")
def company_email(username, cuser):
    for u in cuser:
        if(u.username == username):
            return u.companyemail

@register.filter(name="complacement")
def complacement(email, pinfo):
    for p in pinfo:
        print(p,pinfo)
        if(email == p.company_email):
            print("Hi")
            return p
