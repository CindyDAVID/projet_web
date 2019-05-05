
from django.contrib import admin
from django.urls import path
from monAsso import views


urlpatterns = [
    #url page d'accueil
    path(r'',views.getIndex),
    #url inscription
    path(r'sign-up/<str:userType>',views.signup),
    #url page evenements
    path(r'events',views.showEvent),
    #url page log in
    path(r'sign-in',views.signin),
    #url page log out
    path(r'sign-out',views.signout),
    #url access personnal account
    path(r'profile',views.showProfile),
    #url gestion des compte superadmin
    path(r'admin/', admin.site.urls),
    #url create event only for association
    path(r'create-event',views.createEvent),
    #en cours permet de rechercher et d'afficher une association
    path(r'mon-association/<str:asso>', views.ficheAsso)
]