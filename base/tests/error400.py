from django.http import HttpResponse, HttpResponseBadRequest
from django.views.decorators.http import require_http_methods
import re


@require_http_methods(["POST"])
def validate_user_phone(request):
    phone = request.POST.get('phone', '')
    
    if not (phone.startswith('+7') or phone.startswith('8')) or len(phone) != 12:
        return HttpResponseBadRequest('неверный номер телефона')
    return HttpResponse('телефон валиден.', content_type="")


