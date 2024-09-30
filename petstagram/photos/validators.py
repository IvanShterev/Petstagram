from django.core.exceptions import ValidationError


def validate_size(image_obj):
    if image_obj.size > 5 * 1024 * 1024:
        raise ValidationError('File is too big')
