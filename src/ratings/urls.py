from django.urls import path
# from .views import (
#     product_create_view,
#     product_detail_view,
#     product_delete_view,
#     product_list_views,
#     dynamic_lookup_view
# )
from .views import (
    RatingsMainView,
    ratings_redirect
)


app_name = 'ratings'

# urlpatterns = [
#     path('<int:my_id>/', dynamic_lookup_view, name='product-detail'),
#     path('<int:my_id>/delete',
#          product_delete_view, name='product-delete'),
#     path('', product_list_views, name='product-list')
# ]

urlpatterns = [
    path('', RatingsMainView.as_view(), name='ratings-home'),
    path('<aspect>/', ratings_redirect, name='ratings-home-redirect')
]
