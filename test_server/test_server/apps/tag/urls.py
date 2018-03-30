from django.urls import path,re_path

from rest_framework.urlpatterns import format_suffix_patterns


########## function-based views

# from .views import tag_list,tag_detail

# urlpatterns = [
#     re_path(r'^tags/$',tag_list),
#     re_path(r'^tags/(?P<pk>[0-9]+)/$',tag_detail),
#
# ]





########## class-based views

from .views import TagList,TagDetail
# from .views import UserList,UserDetail
# from .views import api_root

urlpatterns = [
    re_path(r'^tags/$', TagList.as_view()),
    re_path(r'^tags/(?P<pk>[0-9]+)/$', TagDetail.as_view()),

    # re_path(r'^users/$',UserList.as_view()),
    # re_path(r'^users/(?P<pk>[0-9]+)/$',UserDetail.as_view()),
    #
    # re_path(r'^$',api_root),
]

urlpatterns += [
    re_path(r'^api/tag?tag_id=[0-9]+/$', TagList.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)



########## Hyperlinked

# urlpatterns = format_suffix_patterns([
#     re_path(r'^$', api_root),
#     re_path(r'^tags/$',TagList.as_view(), name='tag-list'),
#     re_path(r'^tags/(?P<pk>[0-9]+)/$', TagDetail.as_view(),name='tag-detail'),
#     re_path(r'^users/$',UserList.as_view(),name='user-list'),
#     re_path(r'^users/(?P<pk>[0-9]+)/$', UserDetail.as_view(),name='user-detail'),
# ])



######### ViewSet

# from .views import TagViewSet,UserViewSet,api_root

# tag_list = TagViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
#
# tag_detail = TagViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
#
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
#
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })
#
#
# urlpatterns = format_suffix_patterns([
#     re_path(r'^$', api_root),
#     re_path(r'^tags/$', tag_list, name='tag-list'),
#     re_path(r'^tags/(?P<pk>[0-9]+)/$', tag_detail, name='tag-detail'),
#     re_path(r'^users/$', user_list, name='user-list'),
#     re_path(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail'),
# ])




######## routers
# from django.conf.urls import include
# from rest_framework.routers import DefaultRouter
#
# router = DefaultRouter()
# router.register(r'tags', TagViewSet)
# router.register(r'users', UserViewSet)
#
# urlpatterns = [
#     re_path(r'^', include(router.urls)),
# ]



######### query url

# from .views import TagList,TagDetail
#
#
# urlpatterns = [
#     re_path(r'^tags/$', TagList.as_view()),
#     # re_path(r'^tags/(?P<pk>[0-9]+)/$', TagDetail.as_view()),
#     re_path(r'^tags/detail/$', TagDetail.as_view()),
#
# ]

