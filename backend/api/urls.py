from django.urls import path
from .views.people_views import people_list, person_detail, person_create, person_edit, person_delete
from .views.pub_views import pubs_list, pub_detail, pub_create, pub_edit, pub_delete
from .views import user_views as views
from .views.quote_views import quotes_list, quote_detail, quote_create, quote_edit, quote_delete
from .views.region_views import regions_list, region_detail, region_create, region_edit, region_delete
from .views.verification_views import verifications_list, verification_detail, verification_create, verification_edit, verification_delete

urlpatterns = [
    path('people/', people_list, name="people-list"),
    path('people/<str:pk>', person_detail, name="person-detail"),
    path('person-create/', person_create, name="person-create"),
    path('person-edit/<str:pk>', person_edit, name="person-edit"),
    path('person-delete/<str:pk>', person_delete, name="person-delete"),

    path('publications/', pubs_list, name="pubs-list"),
    path('publications/<str:pk>', pub_detail, name="pub-detail"),
    path('publication-create/', pub_create, name="pub-create"),
    path('publication-edit/<str:pk>', pub_edit, name="pub-edit"),
    path('publication-delete/<str:pk>', pub_delete, name="pub-delete"),

    path('login/', views.MyTokenObtainPairView.as_view(),name='token_obtain_pair'),
    path('register/', views.registerUser, name='register'),
    path('profile/', views.getUserProfile, name="users-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('users/', views.getUsers, name="users"),
    path('users/<str:pk>/', views.getUserById, name='user'),
    path('users/update/<str:pk>/', views.updateUser, name='user-update'),
    path('users/delete/<str:pk>/', views.deleteUser, name='user-delete'),
    path('logout/', views.logoutUser, name='logout'),

    path('quotes/', quotes_list, name="quotes-list"),
    path('quotes/<str:pk>', quote_detail, name="quote-detail"),
    path('quote-create/', quote_create, name="quote-create"),
    path('quote-edit/<str:pk>', quote_edit, name="quote-edit"),
    path('quote-delete/<str:pk>', quote_delete, name="quote-delete"),

    path('regions/', regions_list, name="regions-list"),
    path('regions/<str:pk>', region_detail, name="region-detail"),
    path('region-create/', region_create, name="region-create"),
    path('region-edit/<str:pk>', region_edit, name="region-edit"),
    path('region-delete/<str:pk>', region_delete, name="region-delete"),

    path('verifications/',verifications_list, name="verifications-list"),
    path('verifications/<str:pk>', verification_detail, name="verification-detail"),
    path('verification-create/', verification_create, name="verification-create"),
    path('verification-edit/<str:pk>', verification_edit, name="verification-edit"),
    path('verification-delete/<str:pk>', verification_delete, name="verification-delete"),
    

    
]