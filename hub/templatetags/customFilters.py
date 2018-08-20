from django import template

register = template.Library()


@register.filter('duration_format')
def duration_format(value):
    if value:
        value = int(value)
        h = 'hour'
        m = 'minute'
        hours = int(value/60)
        minutes = value%60
        if hours != 1:
            h += 's'

        if minutes != 1:
            m += 's'

        return '%s %s , %s %s' % (hours, h, minutes, m)
    else:
        return None

@register.filter('clean')
def clean_format(value):
    if value:
        value = str(value)
        cValue = value.replace(':','').replace(' ', '').replace('.','')

        return cValue
    else:
        return None