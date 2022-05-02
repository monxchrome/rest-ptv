from django.core.exceptions import ValidationError

from config.settings import MAX_FILE_SIZE


def validate_size(file):
    file_size = file.file.size
    file_size_in_mb = int(file_size / 1024 / 1024)
    limit_size_mb = MAX_FILE_SIZE
    if file_size_in_mb > limit_size_mb:
        raise ValidationError(f"Размер вашего файла {file_size_in_mb} Мб, максимальный - {limit_size_mb} Мб")
