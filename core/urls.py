from django.urls import path
from .views import (
    ListViewProduct,
    CrieteViewProduct,
    UpadateViewProduct,
    DeleteViewProduct
)

urlpatterns = [
    path('', 
        ListViewProduct.as_view(),
        name='home'
    ),
    path('criando-produto/',
        CrieteViewProduct.as_view(),
        name='criate_product'
    ),
    path('editando-produto/<int:pk>/',
        UpadateViewProduct.as_view(),
        name='update_product'
    ),
    path('deletando-produto/<int:pk>/',
        DeleteViewProduct.as_view(),
        name='delete_product'
    )
]
