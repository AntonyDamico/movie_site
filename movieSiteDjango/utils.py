import random
import string
from django.utils.text import slugify 

def random_string_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

def get_unique_slug(instance, title=None, new_slug=None):
    if new_slug is not None:
        slug = new_slug
    elif title is not None:
        slug = slugify(title)

    ClassInstance = instance.__class__
    slug_exists = ClassInstance.objects.filter(slug=slug).exists()

    if slug_exists:
        rand_str = random_string_generator(size=4)
        new_slug = f"{slug}-{rand_str}"
        return get_unique_slug(instance, title, new_slug=new_slug)
    return slug
