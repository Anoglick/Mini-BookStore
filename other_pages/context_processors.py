def user_info(request):
    """
    Добавляем информацию о текущем пользователе в контекст шаблонов.
    """
    return {
        'user': request.user 
    }