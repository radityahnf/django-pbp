from django.urls import path
from wishlist.views import filtered_json_return , filtered_xml_return, show_wishlist, xml_return, json_return, register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('xml/', xml_return, name='xml_return'), 
    path('json/', json_return, name='json_return'), 
    path('json/<int:id>', filtered_json_return, name='filtered_json_return'),
    path('xml/<int:id>', filtered_xml_return, name='filtered_xml_return'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]