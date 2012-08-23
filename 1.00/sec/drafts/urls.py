from django.conf.urls.defaults import *

urlpatterns = patterns('sec.drafts.views',
    url(r'^$', 'search', name='drafts'),
    url(r'^add/$', 'add', name='drafts_add'),
    #url(r'^approvals/$', 'approvals', name='drafts_approvals'),
    url(r'^dates/$', 'dates', name='drafts_dates'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/$', 'view', name='drafts_view'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/abstract/$', 'abstract', name='drafts_abstract'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/announce/$', 'announce', name='drafts_announce'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/authors/$', 'authors', name='drafts_authors'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/author_delete/(?P<oid>\d{1,6})$',
        'author_delete', name='drafts_author_delete'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/confirm/$', 'confirm', name='drafts_confirm'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/edit/$', 'edit', name='drafts_edit'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/extend/$', 'extend', name='drafts_extend'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/email/$', 'email', name='drafts_email'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/makerfc/$', 'makerfc', name='drafts_makerfc'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/replace/$', 'replace', name='drafts_replace'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/resurrect/$', 'resurrect', name='drafts_resurrect'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/revision/$', 'revision', name='drafts_revision'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/update/$', 'update', name='drafts_update'),
    url(r'^(?P<id>[A-Za-z0-9._\-\+]+)/withdraw/$', 'withdraw', name='drafts_withdraw'),
)
