from .models import GlobalSetting


def business_module(request):
    setting = GlobalSetting.load()
    return {
        'is_business_module_active': setting.is_business_module_active,
    }
