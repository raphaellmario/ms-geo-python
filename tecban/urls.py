from rest_framework.routers import DefaultRouter

from tecban.views import TerminalViewSet

app_name = 'tecban'

router = DefaultRouter(trailing_slash=False)
router.register(r'terminal', TerminalViewSet)

urlpatterns = router.urls
