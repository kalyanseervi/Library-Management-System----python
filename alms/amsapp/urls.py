from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getdata/', views.getdata, name='getdata'),
    path('book_search/', views.book_search, name='book_search'),
    path('register/', views.register, name='register'),
    path('login/', views.loginform, name='login'),
    path('logout/', views.sign_out, name='logout'),
    path('password_reset/', views.password_reset, name='password_reset'),
    path('cart/', views.cart, name='cart'),
    # Add to cart URL with book_id parameter
    path('add_to_cart/<str:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('send_request/', views.send_request, name='send_request'),
    path('review_requests/', views.review_requests, name='review_requests'),
    # Approve and reject request URLs with request_id parameter
    path('approve_request/<str:request_id>/', views.approve_request, name='approve_request'),
    path('reject_request/<str:request_id>/', views.reject_request, name='reject_request'),
    path('user_details/', views.user_details, name='user_details'),
    # Review approved requests URL
    path('review_approved_requests/', views.review_approved_requests, name='review_approved_requests'),
    # Issue book and generate bill URLs with book_id parameter
    path('issue_book/<str:book_id>/', views.issue_book, name='issue_book'),
    path('generate_bill/<str:book_id>/', views.generate_bill, name='generate_bill'),
    path('generate_bill_pdf/<int:bill_id>/', views.generate_bill_pdf, name='generate_bill_pdf'),
    path('bills_list/', views.bills_list, name='bills_list'),
    # path('dealers/', views.dealers_list, name='dealers_list'),
    # path('books_list/', views.books_list, name='books_list'),
    # path('purchases/', views.purchase_list, name='purchase_list'),
    # path('return_purchases/', views.return_purchase_list, name='return_purchase_list'),
    # path('transactions/', views.transaction_list, name='transaction_list'),
    # path('create_dealer/', views.create_dealer, name='create_dealer'),
    # path('add_book/', views.add_book, name='add_book'),
    # path('add_purchase/', views.add_purchase, name='add_purchase'),
    # path('stock_mgmt/', views.stock_mgmt, name='stock_mgmt'),
    # path('create/', views.create_bookstock, name='create_bookstock'),
    # path('list/', views.list_bookstock, name='bookstock_list'),
    path('dealers/create/', views.create_dealer, name='create_dealer'),
    path('dealers/list/', views.dealer_list, name='dealer_list'),
    path('dealers/update/<int:dealer_id>/', views.update_dealer, name='update_dealer'),
    path('dealers/delete/<int:dealer_id>/', views.delete_dealer, name='delete_dealer'),
    path('fetch-more-data', views.fetch_more_data, name='fetch_more_data'),
    path('add_to_wishlist/<str:book_id>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('wishlist/', views.get_wishlist, name='wishlist'),



]
