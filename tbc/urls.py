from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^$', 'tbc.views.Home', name='Home'),
    url(r'^internship-forms/$', 'tbc.views.InternshipForms', name='InternshipForms'),
    url(r'^about-pythontbc/$', 'tbc.views.AboutPytbc', name='AboutPytbc'),
    url(r'^register/$', 'tbc.views.UserRegister', name='UserRegister'),
    url(r'^login/$', 'tbc.views.UserLogin', name='UserLogin'),
    url(r'^logout/$', 'tbc.views.UserLogout', name='UserLogout'),
    url(r'^profile/$', 'tbc.views.UserProfile', name='UserProfile'),
    url(r'^forgot-password/$', 'tbc.views.ForgotPassword', name='ForgotPassword'),
    url(r'^update-password/$', 'tbc.views.UpdatePassword', name='UpdatePassword'),
    
    
    url(r'^submit-book/$', 'tbc.views.SubmitBook', name='SubmitBook'),
    url(r'^update-book/$', 'tbc.views.UpdateBook', name='UpdateBook'),
    url(r'^upload-content/(?P<book_id>\d+)$', 'tbc.views.ContentUpload', name='ContentUpload'),
    url(r'^update-content/(?P<book_id>\d+)$', 'tbc.views.UpdateContent', name='UpdateContent'),
    url(r'^get-zip/(?P<book_id>\d+)$', 'tbc.views.GetZip', name='GetZip'),
    url(r'^browse-books/$', 'tbc.views.BrowseBooks', name='BrowseBooks'),
    url(r'^browse-books/(?P<category>.+)$', 'tbc.views.BrowseBooks', name='BrowseBooks'),
    url(r'^convert-notebook/(?P<notebook_path>.+)$', 'tbc.views.ConvertNotebook', name='ConvertNotebook'),
    url(r'^book-details/(?P<book_id>\d+)/$', 'tbc.views.BookDetails', name='BookDetails'),
	url(r'^completed-books/$', 'tbc.views.CompletedBooks', name='CompletedBooks'),
	url(r'^completed-books/(?P<category>.+)$', 'tbc.views.CompletedBooks', name='CompletedBooks'),
	url(r'^books-under-progress/$', 'tbc.views.BooksUnderProgress', name='BooksUnderProgress'),
	url(r'^redirect-ipynb/(?P<notebook_path>.+)$', 'tbc.views.RedirectToIpynb', name='RedirectToIpynb'),
    
    
    url(r'^book-review/$', 'tbc.views.BookReview', name='BookReview'),
    url(r'^book-review/(?P<book_id>\d+)$', 'tbc.views.BookReview', name='BookReview'),
    url(r'^approve-book/(?P<book_id>\d+)$', 'tbc.views.ApproveBook', name='ApproveBook'),
    url(r'^notify-changes/(?P<book_id>\d+)$', 'tbc.views.NotifyChanges', name='NotifyChanges'),
)
