from django.urls import path
from w3music import w3music_views

app_name='w3music'
urlpatterns = [
    
    # path('',w3music_views.index,name="index"),
    path('',w3music_views.index,name="index"),
    path('index-2/',w3music_views.index_2,name="index-2"),
    path('index-3/',w3music_views.index_3,name="index-3"),
    path('index-4/',w3music_views.index_4,name="index-4"),

    path('about-us/',w3music_views.about_us,name="about-us"),
    path('about-me/',w3music_views.about_me,name="about-me"),
    path('faqs/',w3music_views.faqs,name="faqs"),
    path('tickets/',w3music_views.tickets,name="tickets"),
    path('team/',w3music_views.team,name="team"),
    path('artists-list/',w3music_views.artists_list,name="artists-list"),
    path('artists-single/',w3music_views.artists_single,name="artists-single"),
    path('services/',w3music_views.services,name="services"),
    path('events/',w3music_views.events,name="events"),
    path('events-list/',w3music_views.events_list,name="events-list"),
    path('events-table/',w3music_views.events_table,name="events-table"),
    path('events-detail/',w3music_views.events_detail,name="events-detail"),

    path('compact-album-single/',w3music_views.compact_album_single,name="compact-album-single"),
    path('minimal-album-single/',w3music_views.minimal_album_single,name="minimal-album-single"),
    path('gallery-2-columns/',w3music_views.gallery_2_columns,name="gallery-2-columns"),
    path('gallery-3-columns/',w3music_views.gallery_3_columns,name="gallery-3-columns"),
    path('gallery-4-columns/',w3music_views.gallery_4_columns,name="gallery-4-columns"),
    path('gallery-4-columns-wide/',w3music_views.gallery_4_columns_wide,name="gallery-4-columns-wide"),
    path('gallery-5-columns-wide/',w3music_views.gallery_5_columns_wide,name="gallery-5-columns-wide"),
    path('standard-2-columns/',w3music_views.standard_2_columns,name="standard-2-columns"),
    path('standard-3-columns/',w3music_views.standard_3_columns,name="standard-3-columns"),
    path('standard-4-columns/',w3music_views.standard_4_columns,name="standard-4-columns"),
    path('standard-4-columns-wide/',w3music_views.standard_4_columns_wide,name="standard-4-columns-wide"),
    path('standard-5-columns-wide/',w3music_views.standard_5_columns_wide,name="standard-5-columns-wide"),
    path('error-404/',w3music_views.error_404,name="error-404"),
    path('under-maintenance/',w3music_views.under_maintenance,name="under-maintenance"),
    path('coming-soon/',w3music_views.coming_soon,name="coming-soon"),

    path('shop-cart/',w3music_views.shop_cart,name="shop-cart"),
    path('shop-wishlist/',w3music_views.shop_wishlist,name="shop-wishlist"),
    path('shop-checkout/',w3music_views.shop_checkout,name="shop-checkout"),
    path('shop-my-account/',w3music_views.shop_my_account,name="shop-my-account"),
    path('shop-registration/',w3music_views.shop_registration,name="shop-registration"),
    path('product-detail/',w3music_views.product_detail,name="product-detail"),
    path('shop-sidebar/',w3music_views.shop_sidebar,name="shop-sidebar"),
    path('shop-3-column/',w3music_views.shop_3_column,name="shop-3-column"),
    path('shop-4-column/',w3music_views.shop_4_column,name="shop-4-column"),
    path('shop-wide-4-column/',w3music_views.shop_wide_4_column,name="shop-wide-4-column"),

    path('blog-grid-left-sidebar/',w3music_views.blog_grid_left_sidebar,name="blog-grid-left-sidebar"),
    path('blog-grid-right-sidebar/',w3music_views.blog_grid_right_sidebar,name="blog-grid-right-sidebar"),
    path('blog-list-left-sidebar/',w3music_views.blog_list_left_sidebar,name="blog-list-left-sidebar"),
    path('blog-list-right-sidebar/',w3music_views.blog_list_right_sidebar,name="blog-list-right-sidebar"),
    path('blog-detail-left-sidebar/',w3music_views.blog_detail_left_sidebar,name="blog-detail-left-sidebar"),
    path('blog-detail-right-sidebar/',w3music_views.blog_detail_right_sidebar,name="blog-detail-right-sidebar"),
    path('blog-grid/',w3music_views.blog_grid,name="blog-grid"),
    path('blog-large-left-sidebar/',w3music_views.blog_large_left_sidebar,name="blog-large-left-sidebar"),
    path('blog-list/',w3music_views.blog_list,name="blog-list"),
    path('blog-grid-2/',w3music_views.blog_grid_2,name="blog-grid-2"),
    path('blog-grid-3/',w3music_views.blog_grid_3,name="blog-grid-3"),
    path('blog-details/',w3music_views.blog_details,name="blog-details"),
    path('blog-open-gutenberg/',w3music_views.blog_open_gutenberg,name="blog-open-gutenberg"),
    path('blog-standard/',w3music_views.blog_standard,name="blog-standard"),
    path('blog-grid-3-masonary/',w3music_views.blog_grid_3_masonary,name="blog-grid-3-masonary"),
    path('blog-grid-4-masonary/',w3music_views.blog_grid_4_masonary,name="blog-grid-4-masonary"),
    path('blog-wide-grid-sidebar/',w3music_views.blog_wide_grid_sidebar,name="blog-wide-grid-sidebar"),
    path('blog-wide-list-sidebar/',w3music_views.blog_wide_list_sidebar,name="blog-wide-list-sidebar"),
    
    path('contact-us/',w3music_views.contact_us,name="contact-us"),

]