from django import template
from django.template.base import VariableDoesNotExist
from django.utils.html import escape
from django.utils.safestring import mark_safe

from random import randint

register = template.Library()

@register.filter(is_safe=True)
def citation(text):
    return mark_safe("&laquo; {} &raquo;".format(escape(text)))

@register.filter
def smart_truncate(text, nbre=20):
    try:
        nbre = int(nbre)
    except ValueError:
        return text
    if len(text) <= nbre :
        return text
    text = text[:nbre + 1]
    if text[-1:] != ' ':
        words = text.split(' ')[:-1]
        text = ' '.join(words)

    else:
        text = text[0:-1]
    return text + '...'

@register.tag
def random(parser, token):
    """ Tag générant un nombre aléatoire, entre les bornes en arguments """
    try:
        nom_tag, begin, end = token.split_contents()
    except ValueError:
        msg = 'Le tag random doit prendre exactement deux arguments.'
        raise template.TemplateSyntaxError(msg)

    return RandomNode(begin, end)

class RandomNode(template.Node):
    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    def render(self, context):
        not_exist = False

        try:
            begin = template.Variable(self.begin).resolve(context)
            self.begin = int(begin)
        except (VariableDoesNotExist, ValueError):
            not_exist = self.begin
        try:
            end = template.Variable(self.end).resolve(context)
            self.end = int(end)
        except (VariableDoesNotExist, ValueError):
            not_exist = self.end

        if not_exist:
            msg = 'L\'argument "%s" n\'existe pas, ou n\'est pas un entier.' % not_exist
            raise template.TemplateSyntaxError(msg)

        # Nous vérifions si le premier entier est bien inférieur au second
        if self.begin > self.end:
            msg = 'L\'argument "begin" doit obligatoirement être inférieur à l\'argument "end" dans le tag random.'
            raise template.TemplateSyntaxError(msg)

        return str(randint(self.begin, self.end))
    