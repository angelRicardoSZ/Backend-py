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

## `HttpResponse` objects

*class* `HttpRequest`

In contrast to [`HttpRequest`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpRequest) objects, which are created automatically by Django, [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) objects are your responsibility. Each view you write is responsible for instantiating, populating, and returning an [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse).

The [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) class lives in the [`django.http`](https://docs.djangoproject.com/en/4.1/ref/request-response/#module-django.http) module.

### Usage

#### Passing strings

Typical usage is to pass the contents of the page, as a string, bytestring, or [`memoryview`](https://docs.python.org/3/library/stdtypes.html#memoryview), to the [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) constructor:

```python
from django.http import HttpResponse
response = HttpResponse("Here's the text of the web page.")
response = HttpResponse("Text only, please.", content_type="text/plain")
response = HttpResponse(b'Bytestrings are also accepted.')
response = HttpResponse(memoryview(b'Memoryview as well.'))
```

Add content incrementally

```python
response = HttpResponse()
response.write("<p>Here's the text of the web page.</p>")
response.write("<p>Here's another paragraph.</p>")
```

#### Setting header fields

o set or remove a header field in your response, use [`HttpResponse.headers`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse.headers):

```python
response = HttpResponse()
response.headers['Age'] = 120
del response.headers['Age']
```

### Attributes

##### HttpResponse.content

A bytestring representing the content, encoded from a string if necessary

##### HttpResponse.headers

A  case insensitive, dict-like object that provides an interface to all HTTP headers on the response

##### HttpResponse.status_code

The [**HTTP status code**](https://datatracker.ietf.org/doc/html/rfc7231.html#section-6) for the response. Unless [`reason_phrase`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse.reason_phrase) is explicitly set, modifying the value of `status_code` outside the constructor will also modify the value of `reason_phrase`.

## `JsonResponse` objects

*class* `JsonResponse`**(***data***,** *encoder=DjangoJSONEncoder***,** *safe=True***,** *json_dumps_params=None***,** ***kwargs***)**

An [`HttpResponse`](https://docs.djangoproject.com/en/4.1/ref/request-response/#django.http.HttpResponse) subclass that helps to create a JSON-encoded response. It inherits most behavior from its superclass with a couple differences:

Its default `Content-Type` header is set to *application/json*. The first parameter, `data`, should be a `dict` instance. If the `safe` parameter is set to `False` (see below) it can be any JSON-serializable object.

```python
from django.http import JsonResponse
response = JsonResponse({'foo': 'bar'})
response.content
```

## Projects and applications

The term **project** describes a Django web application

The term **application** describes a Python package that provides some set of features. Applications include some combination of models, views, templates, template tags, static files, URLs, middleware, etc. They’re generally wired into projects with the [`INSTALLED_APPS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-INSTALLED_APPS) setting and optionally with other mechanisms such as URLconfs, the [`MIDDLEWARE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-MIDDLEWARE) setting, or template inheritance.

## Application configuration

Application configuration objects store metadata for an application. Some attributes can be configured in [`AppConfig`](https://docs.djangoproject.com/en/2.0/ref/applications/#django.apps.AppConfig) subclasses. Others are set by Django and read-only.

## Settings

### `DATABASES`

Default: `{}` (Empty dictionary)

A dictionary containing the settings for all databases to be used with Django. It is a nested dictionary whose contents map a database alias to a dictionary containing the options for an individual database.

The [`DATABASES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES) setting must configure a `default` database; any number of additional databases may also be specified.

The simplest possible settings file is for a single-database setup using SQLite. This can be configured using the following:

```json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
```

PostgreSQL

```json
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

#### `ENGINE`

Default: `''` (Empty string)

The database backend to use. The built-in database backends are:

```
'django.db.backends.postgresql'
'django.db.backends.mysql'
'django.db.backends.sqlite3'
'django.db.backends.oracle'
```

#### `HOST`

Default: `''` (Empty string)

Which host to use when connecting to the database. An empty string means localhost. Not used with SQLite.

If this value starts with a forward slash (`'/'`) and you’re using MySQL, MySQL will connect via a Unix socket to the specified socket. For example:

```
"HOST": '/var/run/mysql'
```

If you’re using MySQL and this value *doesn’t* start with a forward slash, then this value is assumed to be the host.

#### `NAME`

Default: `''` (Empty string)

The name of the database to use. For SQLite, it’s the full path to the database file. When specifying the path, always use forward slashes, even on Windows (e.g. `C:/homes/user/mysite/sqlite3.db`).

#### `CONN_MAX_AGE`[¶](https://docs.djangoproject.com/en/2.0/ref/settings/#conn-max-age)

Default: `0`

The lifetime of a database connection, in seconds. Use `0` to close database connections at the end of each request — Django’s historical behavior — and `None` for unlimited persistent connections.

#### `PASSWORD`[¶](https://docs.djangoproject.com/en/2.0/ref/settings/#password)

Default: `''` (Empty string)

The password to use when connecting to the database. Not used with SQLite.



#### `PORT`[¶](https://docs.djangoproject.com/en/2.0/ref/settings/#port)

Default: `''` (Empty string)

The port to use when connecting to the database. An empty string means the default port. Not used with SQLite.



#### `TIME_ZONE`[¶](https://docs.djangoproject.com/en/2.0/ref/settings/#time-zone)

Default: `None`

A string representing the time zone for datetimes stored in this database (assuming that it doesn’t support time zones) or `None`. This inner option of the [`DATABASES`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-DATABASES) setting accepts the same values as the general [`TIME_ZONE`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-TIME_ZONE) setting.

This allows interacting with third-party databases that store datetimes in local time rather than UTC. To avoid issues around DST changes, you shouldn’t set this option for databases managed by Django.

When [`USE_TZ`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USE_TZ) is `True` and the database doesn’t support time zones (e.g. SQLite, MySQL, Oracle), Django reads and writes datetimes in local time according to this option if it is set and in UTC if it isn’t.

When [`USE_TZ`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USE_TZ) is `True` and the database supports time zones (e.g. PostgreSQL), it is an error to set this option.

When [`USE_TZ`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USE_TZ) is `False`, it is an error to set this option.

### Connecting to the database

Refer to the [settings documentation](https://docs.djangoproject.com/en/2.0/ref/settings/).

Connection settings are used in this order:

1. [`OPTIONS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-OPTIONS).
2. [`NAME`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME), [`USER`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-USER), [`PASSWORD`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PASSWORD), [`HOST`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-HOST), [`PORT`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-PORT)
3. MySQL option files.

 if you set the name of the database in [`OPTIONS`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-OPTIONS), this will take precedence over [`NAME`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-NAME), which would override anything in a [MySQL option file](https://dev.mysql.com/doc/refman/en/option-files.html).

Here’s a sample configuration which uses a MySQL option file:

```
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'OPTIONS': {
            'read_default_file': '/path/to/my.cnf',
        },
    }
}


# my.cnf
[client]
database = NAME
user = USER
password = PASSWORD
default-character-set = utf8
```

# Model field reference

## Field options

### `null`

If `True`, Django will store empty values as `NULL` in the database. Default is `False`.

### `blank`

If `True`, the field is allowed to be blank. Default is `False`.

### `choices`

An iterable (e.g., a list or tuple) consisting itself of iterables of exactly two items (e.g. `[(A, B), (A, B) ...]`) to use as choices for this field. If this is given, the default form widget will be a select box with these choices instead of the standard text field.

The first element in each tuple is the actual value to be set on the model, and the second element is the human-readable name. For example:

```python
YEAR_IN_SCHOOL_CHOICES = (
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
)
```

Generally, it’s best to define choices inside a model class, and to define a suitably-named constant for each value

```python
from django.db import models

class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    YEAR_IN_SCHOOL_CHOICES = (
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
    )
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in (self.JUNIOR, self.SENIOR)
```

### `db_column`

The name of the database column to use for this field. If this isn’t given, Django will use the field’s name.

### `db_index`

 If `True`, a database index will be created for this field.

### `error_messages`

The `error_messages` argument lets you override the default messages that the field will raise. Pass in a dictionary with keys matching the error messages you want to override.

### `primary_key`

If `True`, this field is the primary key for the model.`primary_key=True` implies [`null=False`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.null) and [`unique=True`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.unique). Only one primary key is allowed on an object.

### `unique`

If `True`, this field must be unique throughout the table.

This is enforced at the database level and by model validation. If you try to save a model with a duplicate value in a [`unique`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.unique) field, a [`django.db.IntegrityError`](https://docs.djangoproject.com/en/2.0/ref/exceptions/#django.db.IntegrityError) will be raised by the model’s [`save()`](https://docs.djangoproject.com/en/2.0/ref/models/instances/#django.db.models.Model.save) method.

This option is valid on all field types except [`ManyToManyField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ManyToManyField) and [`OneToOneField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.OneToOneField).

Note that when `unique` is `True`, you don’t need to specify [`db_index`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.db_index), because `unique` implies the creation of an index.

## Field types

### `AutoField`

An [`IntegerField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.IntegerField) that automatically increments according to available IDs.

### `BigAutoField`

A 64-bit integer, much like an [`AutoField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.AutoField) except that it is guaranteed to fit numbers from `1` to `9223372036854775807`.

### `BigIntegerField`

A 64-bit integer, much like an [`IntegerField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.IntegerField) except that it is guaranteed to fit numbers from `-9223372036854775808` to `9223372036854775807`. The default form widget for this field is a [`TextInput`](https://docs.djangoproject.com/en/2.0/ref/forms/widgets/#django.forms.TextInput).

### `BooleanField`

A true/false field.

The default form widget for this field is a [`CheckboxInput`](https://docs.djangoproject.com/en/2.0/ref/forms/widgets/#django.forms.CheckboxInput).

If you need to accept [`null`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.null) values then use [`NullBooleanField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.NullBooleanField) instead.

The default value of `BooleanField` is `None` when [`Field.default`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.Field.default) isn’t defined.

### `CharField`

A string field, for small- to large-sized strings.

For large amounts of text, use [`TextField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.TextField).

The default form widget for this field is a [`TextInput`](https://docs.djangoproject.com/en/2.0/ref/forms/widgets/#django.forms.TextInput).

[`CharField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField) has one extra required argument:

`CharField.``max_length`[¶](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField.max_length)

The maximum length (in characters) of the field. The max_length is enforced at the database level and in Django’s validation.

### `DateField`

A date, represented in Python by a `datetime.date` instance. Has a few extra, optional arguments:

DateField.auto_now: Automatically set the field to now every time the object is saved. Useful for “last-modified” timestamps. Note that the current date is *always* used; it’s not just a default value that you can override.

### `DateTimeField`

A date and time, represented in Python by a `datetime.datetime` instance. Takes the same extra arguments as [`DateField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.DateField).

### `EmailField`

A [`CharField`](https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.CharField) that checks that the value is a valid email address. It uses [`EmailValidator`](https://docs.djangoproject.com/en/2.0/ref/validators/#django.core.validators.EmailValidator) to validate the input.

### `FileField`

A file-upload field. Has two optional arguments:

This attribute provides a way of setting the upload directory and file name, and can be set in two ways. In both cases, the value is passed to the [`Storage.save()`](https://docs.djangoproject.com/en/2.0/ref/files/storage/#django.core.files.storage.Storage.save) method.

```python
class MyModel(models.Model):
    # file will be uploaded to MEDIA_ROOT/uploads
    upload = models.FileField(upload_to='uploads/')
    # or...
    # file will be saved to MEDIA_ROOT/uploads/2015/01/30
    upload = models.FileField(upload_to='uploads/%Y/%m/%d/')
```

`FileField.``storage`

A storage object, which handles the storage and retrieval of your files

## Authentication in Web requests

Django uses [sessions](https://docs.djangoproject.com/en/2.0/topics/http/sessions/) and middleware to hook the authentication system into [`request objects`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest). These provide a [`request.user`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest.user) attribute on every request which represents the current user. If the current user has not logged in, this attribute will be set to an instance of [`AnonymousUser`](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.AnonymousUser), otherwise it will be an instance of [`User`](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User).

## Authenticating users

`authenticate`**(***request=None***,** ***credentials***)**[[source\]](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#authenticate)

Use [`authenticate()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.authenticate) to verify a set of credentials. It takes credentials as keyword arguments, `username` and `password` for the default case, checks them against each [authentication backend](https://docs.djangoproject.com/en/2.0/topics/auth/customizing/#authentication-backends), and returns a [`User`](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User) object if the credentials are valid for a backend. If the credentials aren’t valid for any backend or if a backend raises [`PermissionDenied`](https://docs.djangoproject.com/en/2.0/ref/exceptions/#django.core.exceptions.PermissionDenied), it returns `None`. For example:

```python
from django.contrib.auth import authenticate
user = authenticate(username='john', password='secret')
if user is not None:
    # A backend authenticated the credentials
else:
    # No backend authenticated the credentials
```

`request` is an optional [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest) which is passed on the `authenticate()` method of the authentication backends.

## How to log a user in

If you have an authenticated user you want to attach to the current session - this is done with a [`login()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login) function.

`login`**(***request***,** *user***,** *backend=None***)**[[source\]](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#login)

To log a user in, from a view, use [`login()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login). It takes an [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest) object and a [`User`](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User) object. [`login()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login) saves the user’s ID in the session, using Django’s session framework.

Note that any data set during the anonymous session is retained in the session after a user logs in.

This example shows how you might use both [`authenticate()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.authenticate) and [`login()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login):

```python
from django.contrib.auth import authenticate, login

def my_view(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        # Redirect to a success page.
        ...
    else:
        # Return an 'invalid login' error message.
        ...
```

## How to log a user out

`logout`**(***request***)**[[source](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/#logout)

To log out a user who has been logged in via [`django.contrib.auth.login()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.login), use [`django.contrib.auth.logout()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.logout) within your view. It takes an [`HttpRequest`](https://docs.djangoproject.com/en/2.0/ref/request-response/#django.http.HttpRequest) object and has no return value. Example:

```python
from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    # Redirect to a success page.
```

Note that [`logout()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.logout) doesn’t throw any errors if the user wasn’t logged in.

When you call [`logout()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.logout), the session data for the current request is completely cleaned out. All existing data is removed. This is to prevent another person from using the same Web browser to log in and have access to the previous user’s session data. If you want to put anything into the session that will be available to the user immediately after logging out, do that *after* calling [`django.contrib.auth.logout()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.logout).

## Limiting access to logged-in users

The simple, raw way to limit access to pages is to check [`request.user.is_authenticated`](https://docs.djangoproject.com/en/2.0/ref/contrib/auth/#django.contrib.auth.models.User.is_authenticated) and either redirect to a login page:

```python
from django.conf import settings
from django.shortcuts import redirect

def my_view(request):
    if not request.user.is_authenticated:
        return redirect('%s?next=%s' % (settings.LOGIN_URL, request.path))
    # ...
```

…or display an error message:

```python
from django.shortcuts import render

def my_view(request):
    if not request.user.is_authenticated:
        return render(request, 'myapp/login_error.html')
    # ...
```

### The `login_required` decorator

`login_required`**(***redirect_field_name='next'***,** *login_url=None***)**[[source\]](https://docs.djangoproject.com/en/2.0/_modules/django/contrib/auth/decorators/#login_required)[¶](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.decorators.login_required)

As a shortcut, you can use the convenient [`login_required()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.decorators.login_required) decorator:

```python
from django.contrib.auth.decorators import login_required

@login_required
def my_view(request):
    ...
```

[`login_required()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.decorators.login_required) does the following:

- If the user isn’t logged in, redirect to [`settings.LOGIN_URL`](https://docs.djangoproject.com/en/2.0/ref/settings/#std:setting-LOGIN_URL), passing the current absolute path in the query string. Example: `/accounts/login/?next=/polls/3/`.
- If the user is logged in, execute the view normally. The view code is free to assume the user is logged in.

By default, the path that the user should be redirected to upon successful authentication is stored in a query string parameter called `"next"`. If you would prefer to use a different name for this parameter, [`login_required()`](https://docs.djangoproject.com/en/2.0/topics/auth/default/#django.contrib.auth.decorators.login_required) takes an optional `redirect_field_name` parameter:

```python
from django.contrib.auth.decorators import login_required

@login_required(redirect_field_name='my_redirect_field')
def my_view(request):
    ...
```

