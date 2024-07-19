from django.urls import path, include
from .views import *

urlpatterns = [
    path("", HomePageView.as_view(), name='home'),   # has to be int:pk
    path("product/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
    path("platform/<slug:platform>", GamePlatformView.as_view(), name='gameplatform'),
    path("rating", CreateFeedbackView.as_view(), name='rating'),
    path("rating/update", UpdateFeedbackView.as_view(), name='update_rating'),
    path("rating/confim_delete", DeleteFeedbackView.as_view(), name='confirm_delete'),

]






