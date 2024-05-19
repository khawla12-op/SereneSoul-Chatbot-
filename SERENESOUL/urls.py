
from django.contrib import admin
from django.urls import path , include
from blogs.views import blog_posts



urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("CLIENT.urls")),
    path("blog/", blog_posts, name='blog_posts'),
]

handler404 = 'CLIENT.views.error_404'
handler500 = 'CLIENT.views.error_500'