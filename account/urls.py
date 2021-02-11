from django.urls import path
from account.views import (
                            register_view,
                            login_view,
                            logout_view,
                            account_view,
                            # account_search_view,
                            )


app_name = 'account'

urlpatterns = [
      path('register/',register_view,name="register"),
      path('login/',login_view,name="login"),
      path('logout/',logout_view,name="logout"),
      path('<user_id>/',account_view,name="view"),
      # path('search/',account_search_view,name="search"),



]
