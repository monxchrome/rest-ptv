from slugify import slugify


def unique_slug_generator(instance, slug: str = None, number: int = 0):
    Get_class = instance.__class__
    if not slug:
        slug = slugify(instance.title)
        slug_candidate = slug
    else:
        slug_candidate = slug + f"-{number}"
    qs_exists = Get_class.objects.filter(slug=slug_candidate).exists()

    if qs_exists:
        number += 1
        return unique_slug_generator(instance, slug, number)
    else:
        slug = slug_candidate
    return slug
