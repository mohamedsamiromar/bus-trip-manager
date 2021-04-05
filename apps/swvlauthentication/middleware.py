from django.conf import settings
from django.http import HttpResponseRedirect


class PublicMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        current_path = request.get_full_path()
        # print(current_path[-1])
        # if current_path[-1] == '/':
        #     current_path = current_path[0:len(current_path)-1]
        #
        # print(current_path)

        if current_path not in settings.PUBLIC_URLS:
            if request.user is None or request.user.is_anonymous:
                return HttpResponseRedirect(settings.LOGIN_URL)

        return self.get_response(request)
