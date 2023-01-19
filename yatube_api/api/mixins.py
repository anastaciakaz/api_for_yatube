from rest_framework import mixins, viewsets


class CreateRetrieveViewSet(mixins.ListModelMixin,
                            mixins.CreateModelMixin,
                            viewsets.GenericViewSet):
    pass