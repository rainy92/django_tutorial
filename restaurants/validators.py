from django.core.exceptions import ValidationError


CATEGORIES = ['Mexican', 'American', 'Veg', 'Italian']

def validate_category(value):
    category = value.capitalize()
    
    if not value in CATEGORIES and not category in CATEGORIES:
        raise ValidationError("{value} is not a valid category".format(value=value))
