from rest_framework import generics
from webapp.models import Lesson, Product
from webapp.serializers import LessonSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Sum


class LessonList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        return Lesson.objects.filter(product__owner=user)


class LessonDetail(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        user = self.request.user
        product_id = self.kwargs['product_id']
        return Lesson.objects.filter(product_id=product_id, product__owner=user)


@api_view(['GET'])
def product_statistics(request):
    user = request.user
    products = Product.objects.all()
    statistics = []

    for product in products:
        lessons = Lesson.objects.filter(product=product)
        total_viewed_lessons = lessons.filter(viewed_status=True).count()
        total_viewing_time = lessons.filter(viewed_status=True).aggregate(total_duration=Sum('duration_seconds'))
        total_students = lessons.values('viewed_time').distinct().count()
        total_accesses = product.accesses.count()

        if total_accesses > 0:
            acquisition_rate = (total_students / total_accesses) * 100
        else:
            acquisition_rate = 0

        statistics.append({
            'total_viewed_lessons': total_viewed_lessons,
            'total_viewing_time_seconds': total_viewing_time['total_duration'] or 0,
            'total_students': total_students,
            'acquisition_rate': acquisition_rate,
        })

    return Response(statistics)
