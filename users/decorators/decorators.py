from django.http import JsonResponse


def json_login_required(view_func):
    def wrapper(requests, *args, **kwargs):
        if not requests.user.is_authenticated:
            return JsonResponse({'authenticate': False}, safe=False)
        return view_func(requests, *args, **kwargs)
    return wrapper
