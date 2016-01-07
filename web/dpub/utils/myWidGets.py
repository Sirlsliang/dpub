#-*-coding:utf-8-*-
import copy
from itertools import chain

from django.conf import settings
from django.forms.utils import flatatt, to_current_timezone
from django.utils import formats, six
from django.utils.datastructures import MergeDict, MultiValueDict
from django.utils.encoding import force_text, python_2_unicode_compatible
from django.utils.html import conditional_escape, format_html, html_safe
from django.utils.safestring import mark_safe
from django.utils.six.moves.urllib.parse import urljoin
from django.utils.translation import ugettext_lazy

from django.forms import widgets

class MySelect(widgets.Select):
    def render(self,name,value,attrs=None,choices=()):
        if value is None:
            value = ''
        final_attrs = self.build_attrs(attrs, name=name)
        output = [format_html('<select{}>', flatatt(final_attrs))]
        options = self.render_options(choices, [value])
        if options:
            output.append(options)
        output.append('</select>')
        return mark_safe('\n'.join(output))   

    def render_options(self, choices, selected_choices):
        # Normalize to strings.
        selected_choices = set(force_text(v.modelName) for v in selected_choices)
        output = []
        for option_value, option_label in chain(self.choices, choices):
            if isinstance(option_label, (list, tuple)):
                output.append(format_html('<optgroup label="{}">', force_text(option_value)))
                for option in option_label:
                    output.append(self.render_option(selected_choices, *option))
                output.append('</optgroup>')
            else:
                output.append(self.render_option(selected_choices, option_value, option_label))
        return '\n'.join(output)   


