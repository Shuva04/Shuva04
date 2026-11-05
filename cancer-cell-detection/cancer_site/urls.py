from django.urls import path
from classifier.views import home, predict_api

urlpatterns = [
    path("", home, name="home"),
    path("api/predict/", predict_api, name="predict_api"),
]
