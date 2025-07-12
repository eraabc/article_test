def validate(data):
    errors = {}
    title = data.get('title')

    if not title:
        errors['title'] = 'title is required'
    elif len(title) < 3:
        errors['title'] = 'title is too short'

    return errors

