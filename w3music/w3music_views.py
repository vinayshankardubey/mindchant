from django.shortcuts import render


def index(request):
    context={
        "page_title":"Home 1",
        "preloader":"preloader",
        "header":"header-1",
        "footer":"footer-1",
    }
    return render(request,'w3music/index.html',context)

def index_2(request):
    context={
        "page_title":"Home 2",
        "preloader":"preloader-2",
        "header":"header-2",
        "footer":"footer-2",
    }
    return render(request,'w3music/index-2.html',context)

def index_3(request):
    context={
        "page_title":"Home 3",
        "preloader":"preloader-3",
        "header":"header-3",
        "footer":"footer-3",
    }
    return render(request,'w3music/index-3.html',context)

def index_4(request):
    context={
        "page_title":"Home 4",
        "preloader":"preloader-4",
        "header":"header-3",
        "footer":"footer-2",
    }
    return render(request,'w3music/index-4.html',context)

def about_me(request):
    context={
        "page_title":"About Me"
    }
    return render(request,'w3music/about-me.html',context)

def about_us(request):
    context={
        "page_title":"About Us"
    }
    return render(request,'w3music/about-us.html',context)

def faqs(request):
    context={
        "page_title":"Faqs"
    }
    return render(request,'w3music/faqs.html',context)

def tickets(request):
    context={
        "page_title":"Tickets"
    }
    return render(request,'w3music/tickets.html',context)

def team(request):
    context={
        "page_title":"Team"
    }
    return render(request,'w3music/team.html',context)

def artists_list(request):
    context={
        "page_title":"Artists List"
    }
    return render(request,'w3music/artists-list.html',context)

def artists_single(request):
    context={
        "page_title":"Artists Single"
    }
    return render(request,'w3music/artists-single.html',context)

def services(request):
    context={
        "page_title":"Services"
    }
    return render(request,'w3music/services.html',context)

def events(request):
    context={
        "page_title":"Events"
    }
    return render(request,'w3music/events.html',context)

def events_list(request):
    context={
        "page_title":"Events List"
    }
    return render(request,'w3music/events-list.html',context)

def events_table(request):
    context={
        "page_title":"Events Table"
    }
    return render(request,'w3music/events-table.html',context)

def events_detail(request):
    context={
        "page_title":"Events Detail"
    }
    return render(request,'w3music/events-detail.html',context)

def compact_album_single(request):
    context={
        "page_title":"Compact Album Single"
    }
    return render(request,'w3music/compact-album-single.html',context)

def minimal_album_single(request):
    context={
        "page_title":"Minimal Album Single"
    }
    return render(request,'w3music/minimal-album-single.html',context)

def gallery_2_columns(request):
    context={
        "page_title":"Gallery 2 Columns"
    }
    return render(request,'w3music/gallery-2-columns.html',context)

def gallery_3_columns(request):
    context={
        "page_title":"Gallery 3 Columns"
    }
    return render(request,'w3music/gallery-3-columns.html',context)

def gallery_4_columns(request):
    context={
        "page_title":"Gallery 4 Columns"
    }
    return render(request,'w3music/gallery-4-columns.html',context)

def gallery_4_columns_wide(request):
    context={
        "page_title":"Gallery Four Columns Wide"
    }
    return render(request,'w3music/gallery-4-columns-wide.html',context)

def gallery_5_columns_wide(request):
    context={
        "page_title":"Gallery Five Columns Wide"
    }
    return render(request,'w3music/gallery-5-columns-wide.html',context)

def standard_2_columns(request):
    context={
        "page_title":"Standard Two Columns"
    }
    return render(request,'w3music/standard-2-columns.html',context)

def standard_3_columns(request):
    context={
        "page_title":"Standard Three Columns"
    }
    return render(request,'w3music/standard-3-columns.html',context)

def standard_4_columns(request):
    context={
        "page_title":"Standard Four Columns"
    }
    return render(request,'w3music/standard-4-columns.html',context)

def standard_4_columns_wide(request):
    context={
        "page_title":"Standard Four Columns Wide"
    }
    return render(request,'w3music/standard-4-columns-wide.html',context)

def standard_5_columns_wide(request):
    context={
        "page_title":"Standard Five Columns Wide"
    }
    return render(request,'w3music/standard-5-columns-wide.html',context)

def error_404(request):
    context={
        "page_title":"Error 404"
    }
    return render(request,'404.html',context)

def under_maintenance(request):
    context={
        "page_title":"Under Maintenance"
    }
    return render(request,'w3music/under-maintenance.html',context)

def coming_soon(request):
    context={
        "page_title":"Coming Soon"
    }
    return render(request,'w3music/coming-soon.html',context)

def shop_cart(request):
    context={
        "page_title":"Shop Cart"
    }
    return render(request,'w3music/shop-cart.html',context)

def shop_wishlist(request):
    context={
        "page_title":"Shop Wishlist"
    }
    return render(request,'w3music/shop-wishlist.html',context)

def shop_checkout(request):
    context={
        "page_title":"Shop Checkout"
    }
    return render(request,'w3music/shop-checkout.html',context)

def shop_my_account(request):
    context={
        "page_title":"Shop My Account"
    }
    return render(request,'w3music/shop-my-account.html',context)

def shop_registration(request):
    context={
        "page_title":"Shop Registration"
    }
    return render(request,'w3music/shop-registration.html',context)

def product_detail(request):
    context={
        "page_title":"Product Detail"
    }
    return render(request,'w3music/product-detail.html',context)

def shop_sidebar(request):
    context={
        "page_title":"Shop Sidebar"
    }
    return render(request,'w3music/shop-sidebar.html',context)

def shop_3_column(request):
    context={
        "page_title":"Shop Three Column"
    }
    return render(request,'w3music/shop-3-column.html',context)

def shop_4_column(request):
    context={
        "page_title":"Shop Four Column"
    }
    return render(request,'w3music/shop-4-column.html',context)

def shop_wide_4_column(request):
    context={
        "page_title":"Shop Wide Four Column"
    }
    return render(request,'w3music/shop-wide-4-column.html',context)

def blog_grid_left_sidebar(request):
    context={
        "page_title":"Blog Grid Left Sidebar"
    }
    return render(request,'w3music/blog-grid-left-sidebar.html',context)

def blog_grid_right_sidebar(request):
    context={
        "page_title":"Blog Grid Right Sidebar"
    }
    return render(request,'w3music/blog-grid-right-sidebar.html',context)

def blog_list_left_sidebar(request):
    context={
        "page_title":"Blog List Left Sidebar"
    }
    return render(request,'w3music/blog-list-left-sidebar.html',context)

def blog_list_right_sidebar(request):
    context={
        "page_title":"Blog List Right Sidebar"
    }
    return render(request,'w3music/blog-list-right-sidebar.html',context)

def blog_detail_left_sidebar(request):
    context={
        "page_title":"Blog Details Left Sidebar"
    }
    return render(request,'w3music/blog-details-left-sidebar.html',context)

def blog_detail_right_sidebar(request):
    context={
        "page_title":"Blog Details Right Sidebar"
    }
    return render(request,'w3music/blog-details-right-sidebar.html',context)

def blog_grid(request):
    context={
        "page_title":"Blog Grid"
    }
    return render(request,'w3music/blog-grid.html',context)

def blog_large_left_sidebar(request):
    context={
        "page_title":"Large Left Sidebar"
    }
    return render(request,'w3music/blog-large-left-sidebar.html',context) 

def blog_list(request):
    context={
        "page_title":"Blog List"
    }
    return render(request,'w3music/blog-list.html',context)

def blog_grid_2(request):
    context={
        "page_title":"Blog Grid Two"
    }
    return render(request,'w3music/blog-grid-2.html',context)

def blog_grid_3(request):
    context={
        "page_title":"Blog Grid Three"
    }
    return render(request,'w3music/blog-grid-3.html',context)

def blog_details(request):
    context={
        "page_title":"Blog Details"
    }
    return render(request,'w3music/blog-details.html',context)

def blog_open_gutenberg(request):
    context={
        "page_title":"Blog Open Gutenberg"
    }
    return render(request,'w3music/blog-open-gutenberg.html',context)

def blog_standard(request):
    context={
        "page_title":"Blog Standard"
    }
    return render(request,'w3music/blog-standard.html',context)

def blog_grid_3_masonary(request):
    context={
        "page_title":"Blog Grid Three Masonary"
    }
    return render(request,'w3music/blog-grid-3-masonary.html',context)

def blog_grid_4_masonary(request):
    context={
        "page_title":"Blog Grid Four Masonary"
    }
    return render(request,'w3music/blog-grid-4-masonary.html',context)

def blog_wide_grid_sidebar(request):
    context={
        "page_title":"Blog Wide Grid Sidebar"
    }
    return render(request,'w3music/blog-wide-grid-sidebar.html',context)

def blog_wide_list_sidebar(request):
    context={
        "page_title":"Blog Wide List Sidebar"
    }
    return render(request,'w3music/blog-wide-list-sidebar.html',context)

def contact_us(request):
    context={
        "page_title":"Contact Us"
    }
    return render(request,'w3music/contact-us.html',context)





    

