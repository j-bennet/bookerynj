def strip_slash(get_response):
    """https://github.com/vitalik/django-ninja/issues/1058"""

    def middleware(request):
        if request.path.endswith("/"):
            request.path_info = request.path = request.path.rstrip("/")
        return get_response(request)

    return middleware
