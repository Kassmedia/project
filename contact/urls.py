from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
#app_name = 'contact' 

urlpatterns = [
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('', views.home, name='home'),
    path('contact', views.contact_view, name='contact'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('logout/', views.logout_user, name='logout'),
    path('get_chart_data/', views.get_chart_data, name='get_chart_data'),
    path('about/', views.about_view, name='about'),
    path('affiliate/', views.affiliate, name='affiliate'),
    path('article1/', views.article1, name='article1'),
    path('article2/', views.article2, name='article2'),
    path('article3/', views.article3, name='article3'),
    path('article4/', views.article4, name='article4'),
    path('article5/', views.article5, name='article5'),
    path('article6/', views.article6, name='article6'),
    path('bank-payment/', views.bank_payment, name='bank-payment'),
    path('base/', views.base, name='base'),
    path('blog-post/', views.blog_post, name='blog-post'),
    path('checkout/', views.checkout, name='checkout'),
    path('community-forum/', views.community_forum, name='community-forum'),
    path('confirmation/', views.confirmation, name='confirmation'),
   
    path('data-analysis/', views.data_analysis, name='data-analysis'),
    path('Delivery_logistics/', views.Delivery_logistics, name='Delivery_logistics'),
    path('FarmerProfiles/', views.FarmerProfiles, name='farmerProfiles'),
    path('farmer/<int:farmer_id>/', views.farmer_detail, name='farmer_detail'),
    path('farmer_profile/', views.farmer_profile, name='farmer_profile'),
    path('farmers-dashboard/', views.farmers_dashboard, name='farmers_dashboard'),
    path('government-ngo-partnership/', views.Government_NGO_Paternership, name='government-ngo-partnership'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('login/', views.login, name='login'),
    path('marketplace/', views.marketplace, name='marketplace'),
    path('password/', views.password, name='password'),
    path('payment-processing/', views.payment_processing, name='payment-processing'),
    path('payment/', views.payment, name='payment'),
    path('privacy/', views.privacy, name='privacy'),
    path('product/', views.product, name='product'),
    path('productlink/', views.productlink, name='productlink'),
    path('reset-password-done/', views.resetpassword_done, name='reset-password-done'),
    path('reset-password/', views.resetpassword, name='reset-password'),
    path('rewards/', views.reward, name='rewards'),
    path('seasonal-calendar/', views.seasonal_calendar, name='seasonal-calendar'),
    path('signup/', views.signup_view, name='signup'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('terms/', views.terms, name='terms'),
    path('create-order/', views.create_order, name='create_order'),
    path('track-order/', views.track_order_home, name='track_order_home'),
    path('track-order/<str:tracking_number>/', views.track_order, name='track_order'),

    path('ussd-payment/', views.ussdPayment, name='ussd-payment'),
    path('welcome/', views.welcome, name='welcome'),
    path('blog/', views.blog_post, name='blog'),
    path('list-product/', views.list_product, name='list_product'),
    path('verify-payment/', views.verify_payment, name='verify_payment'),
    path('notifications/', views.notifications_view, name='notifications'),
    path('change-password/', views.change_password_view, name='change_password'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),
    path('products/', views.product_list, name='product_list'),
    path('add_post/', views.add_post, name='add_post'),
    path('add_event/', views.add_event, name='add_event'),
    path('add_feedback/', views.add_feedback, name='add_feedback'),
    path('feedback-success/', views.addfeedback, name='feedback_success'),
    path('submit-product/', views.submit_product, name='submit_product'),
    path('success/', views.success_page, name='success_page'),
    path('dashboardOverview_view/', views.dashboard_view, name='dashboardoverview'),
    path('settings/', views.settings_view, name='settings'),
    path('update_privacy/', views.update_privacy, name='update_privacy'),
    path('messages/', views.messages_view, name='messages'),
    path('help/', views.help_support_view, name='help_support'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)