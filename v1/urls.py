from django.urls import include, path

urlpatterns = [
    path('users/', include('users.urls'), name='users'),
    path('products/', include('products.urls'), name='products'),
]