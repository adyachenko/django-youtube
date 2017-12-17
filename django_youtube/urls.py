from django.conf.urls import url


urlpatterns = (
    # list of the videos
    url(r'^videos/?$', 'django_youtube.views.video_list', name="youtube_video_list"),

    # video  display page, convenient to use in an iframe
    url(r'^video/(?P<video_id>[\w.@+-]+)/$', 'django_youtube.views.video', name="youtube_video"),

    # upload page with a form
    url(r'^upload/?$', 'django_youtube.views.upload', name="youtube_upload"),

    # page that youtube redirects after upload
    url(r'^upload/return/?$', 'django_youtube.views.upload_return', name="youtube_upload_return"),

    # upload page with a form
    url(r'^direct-upload/?$', 'django_youtube.views.direct_upload', name="youtube_direct_upload"),

    # remove video, redirects to upload page when it's done
    url(r'^video/remove/(?P<video_id>[\w.@+-]+)/$', 'django_youtube.views.remove', name="youtube_video_remove"),

    # check video availability, returns json response
    url(r'^check-video-availability/(?P<video_id>[\w.@+-]+)$/?$', 'django_youtube.views.check_video_availability', name="youtube_check_video_availability"),
    url(r'^video/(?P<video_id>[\w.@+-]+)/$', 'django_youtube.views.video', name="youtube_video"),
)
