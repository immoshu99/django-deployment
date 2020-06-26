from django import templates
register = template.library()
@register.filter(name='cut')
def cut(value,arg):
    return value.replace(arg,'')
#register.filter(cut,'cut')
