def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.pdf', '.docx']
    if not ext.lower() in valid_extensions:
        raise ValidationError(u'the File must be .docx or .pdf')
