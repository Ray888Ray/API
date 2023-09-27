from django.urls import path
from webapp.views import LessonList, LessonDetail, product_statistics

app_name = 'webapp'

urlpatterns = [
    path('', LessonList.as_view(), name='lesson-list'),
    path('lessons/<int:product_id>/', LessonDetail.as_view(), name='lesson-list-by-product'),
    path('product-statistics/', product_statistics, name='product-statistics'),
]
