from rest_framework import viewsets
from .models import News
from .serializers import NewsSerializer

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        date = self.request.query_params.get('date')

        if date:
            queryset = queryset.filter(published_at__date=date)

        return queryset

