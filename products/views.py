from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from products.serializers import ProductDetailSerializer, ProductListSerializer
from products.models import product
from products.permissions import IsOwnerOrReadOnly
from rest_framework.authentication import TokenAuthentication

class ProductCreateView(generics.CreateAPIView):
    serializer_class = ProductDetailSerializer

class ProductListView(generics.ListAPIView):
    serializer_class = ProductListSerializer
    queryset = product.objects.all()
    permission_classes = (IsAuthenticated, )

class ProductDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductDetailSerializer
    queryset = product.objects.all()
    authentication_classes = (TokenAuthentication, )
    permission_classes = (IsOwnerOrReadOnly, )