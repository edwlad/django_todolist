from rest_framework.routers import DefaultRouter
from .views import MyListApi

# from main.models import MyList

# router = DefaultRouter(trailing_slash=False)
router = DefaultRouter()

# app_name = "articlesapp"

router.register(
    prefix="tasks",
    viewset=MyListApi,
    basename="tasks",
)

urlpatterns = router.urls
