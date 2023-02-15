from django.urls import path


from . import views  # O . indica a pasta atual

app_name = 'recipes'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),  # noqa: E261, E501
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
