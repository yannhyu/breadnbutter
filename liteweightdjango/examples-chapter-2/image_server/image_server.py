import os
import sys

from django.conf import settings

DEBUG = os.environ.get('DEBUG', 'on') == 'on'

SECRET_KEY = os.environ.get('SECRET_KEY', '#1j$19^!c9qym=6m2k+l0a+td$k%8ah%lz@t+jf$t6r2p1nmp1')

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost').split(',')

BASE_DIR = os.path.dirname(__file__)

settings.configure(
    DEBUG=DEBUG,
    SECRET_KEY=SECRET_KEY,
    ALLOWED_HOSTS=ALLOWED_HOSTS,
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASSES=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
    ),
    INSTALLED_APPS=(
        'django.contrib.staticfiles',
    ),
    TEMPLATE_DIRS=(
        os.path.join(BASE_DIR, 'templates'),
    ),
    STATICFILES_DIRS=(
        os.path.join(BASE_DIR, 'static'),
    ),
    STATIC_URL='/static/',
)

from django import forms
from django.conf.urls import url
from django.core.cache import cache
from django.core.urlresolvers import reverse
from django.core.wsgi import get_wsgi_application
from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import render
from io import BytesIO
from PIL import Image, ImageDraw
# to make use of the browser’s built-in caching
import hashlib
from django.views.decorators.http import etag

class ImageForm(forms.Form):
    """Form to validate requested placeholder image."""
    height = forms.IntegerField(min_value=1, max_value=2000)
    width = forms.IntegerField(min_value=1, max_value=2000)
    def generate(self, image_format='PNG'):
        """Generate an image of the given type and return as raw bytes."""
        height = self.cleaned_data['height']
        width = self.cleaned_data['width']
        # get it from cache if possible
        key = '{}.{}.{}'.format(width, height, image_format)
        content = cache.get(key)
        if content is None:    # cache miss: generate image and cache it
            image = Image.new('RGB', (width, height))
            draw = ImageDraw.Draw(image)
            text = '{} X {}'.format(width, height)
            textwidth, textheight = draw.textsize(text)
            if textwidth < width and textheight < height:
                texttop = (height - textheight) // 2
                textleft = (width - textwidth) // 2
                draw.text((textleft, texttop), text, fill=(255, 255, 255))
            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            # the image is cached using the key for an hour
            cache.set(key, content, 60 * 60)
        return content

def generate_etag(request, width, height):
    content = 'Placeholder: {0} x {1}'.format(width, height)
    return hashlib.sha1(content.encode('utf-8')).hexdigest()

# The generate_etag function will be passed to the etag decorator
# With this decorator in place, the server will need to generate 
# the image the first time the browser requests it. 
# On subsequent requests, if the browser makes a request with
# the matching ETag, the browser will receive a 
# 304 Not Modified response for the image.
# The browser will use the image from the cache and 
# save bandwidth and time to re-generate the HttpResponse
@etag(generate_etag)    
def placeholder(request, width, height):
    # TODO: rest of the view goes here
    form = ImageForm({'height': height, 'width': width})
    if form.is_valid():
        # TODO: generate image of the requested size
        image = form.generate()
        return HttpResponse(image, content_type='image/png')
    else:
        return HttpResponseBadRequest('Invalid Image Request')

def index(request):
    # return HttpResponse('Hello ISO ISO')
    example = reverse('placeholder', kwargs={'width': 50, 'height':50})
    context = {'example': request.build_absolute_uri(example)}
    return render(request, 'home.html', context)


# incoming requests to the URL /image/30x25/ will be routed
# to the placeholder view and pass in those values 
# (e.g., width=30 and height=25 )
urlpatterns = (
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder,
        name='placeholder'),
    url(r'^$', index, name='homepage'),
)


application = get_wsgi_application()


if __name__ == "__main__":
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
