# filepath: vsls:/project/templatetags/highlight_tags.py
from django import template
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe
import re

register = template.Library()

@register.filter(needs_autoescape=True)
def highlight_words(text, words_to_highlight, autoescape=True):
    if autoescape:
        text = conditional_escape(text)
        
    if not words_to_highlight:
        return mark_safe(text)
        
    highlight_words_list = [word.strip() for word in words_to_highlight.split(',')]
    
    for word in highlight_words_list:
        if word:
            pattern = re.compile(r'\b({})\b'.format(re.escape(word)), re.IGNORECASE)
            replacement = r'<strong style="color: var(--accent-color);">\1</strong>'
            text = pattern.sub(replacement, text)
            
    return mark_safe(text)