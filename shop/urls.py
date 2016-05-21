from django.conf.urls import patterns, url

urlpatterns = patterns('',
        url(r'^$','shop.views.home', name='home'),
        url(r'^product/(?P<product_id>[0-9]+)/$',
            'shop.views.show_product', name='product'),
        url(r'^category/(?P<category_id>[0-9]+)/$',
        'shop.views.category', name='category'),
        # url(r'^search/(?P<product_name>.+)$',
        #     'shop.views.search_product', name='search')
                       )