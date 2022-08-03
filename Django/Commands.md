# Commands in Django

## Django-admin

`django-admin` is Django’s command-line utility for administrative tasks

Usage:

```python
django-admin <command> [options]
manage.py <command> [options]
python -m django <command> [options]
```

### dbshell

Runs the command-line client for the database engine specified in your [`ENGINE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASE-ENGINE) setting, with the connection parameters specified in your [`USER`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER), [`PASSWORD`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD), etc., settings.

```shell
django-admin dbshell
```

- For PostgreSQL, this runs the `psql` command-line client.
- For MySQL, this runs the `mysql` command-line client.
- For SQLite, this runs the `sqlite3` command-line client.
- For Oracle, this runs the `sqlplus` command-line client.

## How Django processes a request

When a user requests a page from your Django-powered site, this is the algorithm the system follows to determine which Python code to execute

1. Django determines the root URLconf module to use. Ordinarily, this is the value of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-ROOT_URLCONF) setting, but if the incoming `HttpRequest` object has a [`urlconf`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.urlconf) attribute (set by middleware), its value will be used in place of the [`ROOT_URLCONF`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-ROOT_URLCONF) setting.
2. Django loads that Python module and looks for the variable `urlpatterns`. This should be a Python list of [`django.urls.path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path) and/or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.re_path) instances.
3. Django runs through each URL pattern, in order, and stops at the first one that matches the requested URL
4. Once one of the URL patterns matches, Django imports and calls the given view, which is a simple Python function (or a class-based view ). The view gets passed the following arguments:
   - An instance of [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest).
   - If the matched URL pattern returned no named groups, then the matches from the regular expression are provided as positional arguments.
   - The keyword arguments are made up of any named parts matched by the path expression, overridden by any arguments specified in the optional `kwargs` argument to [`django.urls.path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.path) or [`django.urls.re_path()`](https://docs.djangoproject.com/en/2.0/ref/urls/#django.urls.re_path).
5. If no URL pattern matches, or if an exception is raised during any point in this process, Django invokes an appropriate error-handling view

# Request and response objects

Django uses request and response objects to pass state through the system. When a page is requested, Django creates an [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest) object that contains metadata about the request. Then Django loads the appropriate view, passing the [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest) as the first argument to the view function. Each view is responsible for returning an [`HttpResponse`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpResponse) object.

## `HttpRequest` objects[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#httprequest-objects)

*class* `HttpRequest`[[source\]](https://docs.djangoproject.com/en/2.0/_modules/django/http/request/#HttpRequest)

### Attributes[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#attributes)

All attributes should be considered read-only, unless stated otherwise.

- `HttpRequest.``scheme`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.scheme)

  A string representing the scheme of the request (`http` or `https` usually).

- `HttpRequest.``body`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.body)

  The raw HTTP request body as a byte string. This is useful for processing data in different ways than conventional HTML forms: binary images, XML payload etc. For processing conventional form data, use [`HttpRequest.POST`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST).You can also read from an `HttpRequest` using a file-like interface. See [`HttpRequest.read()`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.read).

- `HttpRequest.``path`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.path)

  A string representing the full path to the requested page, not including the scheme or domain.

  Example: `"/music/bands/the_beatles/"`

- `HttpRequest.``path_info`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.path_info)

  Under some Web server configurations, the portion of the URL after the host name is split up into a script prefix portion and a path info portion. The `path_info` attribute always contains the path info portion of the path, no matter what Web server is being used. Using this instead of [`path`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.path) can make your code easier to move between test and deployment servers.

  For example, if the `WSGIScriptAlias` for your application is set to `"/minfo"`, then `path` might be `"/minfo/music/bands/the_beatles/"` and `path_info` would be `"/music/bands/the_beatles/"`

- `HttpRequest.``method`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.method)

  A string representing the HTTP method used in the request. This is guaranteed to be uppercase. For example:

  ```python
  if request.method == 'GET':
      do_something()
  elif request.method == 'POST':
      do_something_else()
  ```

- `HttpRequest.``encoding`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.encoding)

  A string representing the current encoding used to decode form submission data (or `None`, which means the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DEFAULT_CHARSET) setting is used). You can write to this attribute to change the encoding used when accessing the form data. Any subsequent attribute accesses (such as reading from [`GET`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.GET) or [`POST`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST)) will use the new `encoding` value. Useful if you know the form data is not in the [`DEFAULT_CHARSET`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DEFAULT_CHARSET) encoding.

- `HttpRequest.``POST`[¶](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.POST)

  A dictionary-like object containing all given HTTP POST parameters, providing that the request contains form data. See the [`QueryDict`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.QueryDict) documentation below. If you need to access raw or non-form data posted in the request, access this through the [`HttpRequest.body`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.body) attribute instead.



