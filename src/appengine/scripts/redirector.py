from google.appengine.ext import webapp
from google.appengine.ext.webapp.util import run_wsgi_app

NEWS_POSTS = {
    '/2012/01/26/revisiting-equality.html' :                     '/2012/01/proposed-changes-for-equality.html',
    '/2012/01/20/dart-language-spec-0.07.html' :                 '/2012/01/dart-language-spec-v007-now-available.html',
    '/2012/01/17/new-editor-build.html' :                        '/2012/01/new-dart-editor-build-3331.html',
    '/2012/01/10/new-editor-build.html' :                        '/2012/01/new-dart-editor-build-3101.html',
    '/2012/01/06/getting-started-with-dart.html' :               '/2012/01/getting-started-with-dart-screencast.html',
    '/2011/12/21/new-api-docs.html' :                            '/2011/12/new-api-docs-site.html',
    '/2011/12/19/new-editor-build.html' :                        '/2011/12/new-dart-editor-build-2380.html',
    '/2011/12/13/dart-language-spec-0.06.html' :                 '/2011/12/dart-language-spec-v006-now-available.html',
    '/2011/12/02/new-editor-build.html' :                        '/2011/12/new-dart-editor-build-1910.html',
    '/2011/11/23/dart-presentations-and-slides-available.html' : '/2011/11/new-dart-presentations-and-slides.html',
    '/2011/11/18/new-editor-build.html' :                        '/2011/11/new-dart-editor-build-1584.html',
    '/2011/11/14/dart-language-spec-0.05.html' :                 '/2011/11/dart-language-spec-v005-now-available.html',
    '/2011/11/09/new-editor-build.html' :                        '/2012/01/new-dart-editor-build.html',
    '/2011/11/01/dart-language-spec-0.04-now-available.html' :   '/2011/11/dart-language-spec-v004-now-available.html',
    '/2011/10/31/editor.html' :                                  '/2011/10/try-out-dart-editor.html',
    '/2011/10/28/style-guide.html' :                             '/2011/10/coding-style-guide.html',
    '/2011/10/26/dart-slides-from-senchacon.html' :              '/2011/10/posted-by-david-chandler-i-recently.html',
    '/2011/10/18/dart-language-spec-0.03-now-available.html' :   '/2011/10/dart-language-spec-v003-now-available.html'
}

class PlusRedirectPage(webapp.RequestHandler):
    def get(self):
        self.redirect('https://plus.google.com/109866369054280216564/posts', permanent=True)

class ApiRedirectPage(webapp.RequestHandler):
    def get(self):
        filename = self.request.path.split('/docs/api/')[1]
        if filename == '' or filename == 'index.html':
            self.redirect('http://api.dartlang.org/', permanent=True)
        else:
            self.redirect('http://api.dartlang.org/dart_core/' + filename, permanent=True)
            
class NewsRedirectPage(webapp.RequestHandler):
    def get(self):
        url = self.request.path[5:len(self.request.path)]
        if url == '' or url == '/' or url == '/index.html':
            self.redirect('http://news.dartlang.org', permanent=True)
        elif NEWS_POSTS.has_key(url):
            self.redirect('http://news.dartlang.org' + NEWS_POSTS[url], permanent=True)
        else:
            self.error(404)

class AtomFeedRedirectPage(webapp.RequestHandler):
    def get(self):
        self.redirect('http://news.dartlang.org/feeds/posts/default', permanent=True)

application = webapp.WSGIApplication(
                                     [('/docs/api/.*', ApiRedirectPage),
                                      ('/news.*', NewsRedirectPage),
                                      ('/atom.xml', AtomFeedRedirectPage),
                                      ('/%2B', PlusRedirectPage),
                                      ('/\+', PlusRedirectPage)],
                                     debug=True)

def main():
    run_wsgi_app(application)

if __name__ == "__main__":
    main()