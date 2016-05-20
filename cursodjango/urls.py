from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cursodjango.portal.views.home', name='home'),
    url(r'^cadastro/$', 'cursodjango.portal.views.cadastro', name='cadastro'),
    url(r'^sobre/$', 'cursodjango.portal.views.sobre', name='sobre'),
    url(r'^detalhes/$', 'cursodjango.portal.views.detalhes', name='detalhes'),
    url(r'^planos/$', include('cursodjango.planos.urls',namespace='planos')),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
