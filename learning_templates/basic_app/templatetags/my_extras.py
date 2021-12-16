from django import template

register = template.Library()
@register.filter(name='cut')
def cut(value,arg):
    """
    this cut args from str
    """
    return value.replace(arg,'')


#register.filter('cut',cut)