from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions
from rest_framework import pagination, viewsets
from rest_framework.decorators import action
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from .filters import AdFilter
from ads.models import Ad, Comment
from .permissions import IsOwnerOrStaff
from .serializers import AdSerializer, CommentSerializer


class AdPagination(pagination.PageNumberPagination):
    page_size = 4


class AdViewSet(viewsets.ModelViewSet):
    queryset = Ad.objects.all()
    pagination_class = AdPagination
    filter_backends = (DjangoFilterBackend,)
    filterset_class = AdFilter
    serializer_class = AdSerializer

    def get_queryset(self):
        if self.action == "me":
            return Ad.objects.filter(author=self.request.user.id).all()
        return Ad.objects.all()

    def get_permissions(self):
        if self.action in ["list", "retrieve", "me", "create"]:
            self.permission_classes = [permissions.IsAuthenticated]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()

    @action(detail=False, methods=['get'])
    def me(self, request, *args, **kwargs):
        return super().list(self, request, *args, **kwargs)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().select_related('ad')
    serializer_class = CommentSerializer

    default_permission = [AllowAny(), ]
    permission_classes = {
        'retrieve': [IsAuthenticated(), ],
        'create': [IsAuthenticated(), ],
        'update': [IsAuthenticated(), IsOwnerOrStaff(), ],
        'partial_update': [IsAuthenticated(), IsOwnerOrStaff(), ],
        'destroy': [IsAuthenticated(), IsOwnerOrStaff(), ],

    }

    def get_queryset(self, *args, **kwargs):
        ad_id = self.kwargs.get('ad_pk')
        ad = get_object_or_404(Ad, pk=ad_id)

        return self.queryset.filter(ad=ad)

    def get_permissions(self):
        return self.permission_classes.get(self.action, self.default_permission)

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(author=self.request.user, ad_id=self.kwargs.get('ad_pk'))


