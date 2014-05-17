##Installation

Install bower from npm:

```
npm install -g bower
```

Install django-simple-bower with pip

```
pip install django-simple-bower
```

Add django-simple-bower to INSTALLED_APPS in your settings:

```
'simplebower',
```

Set path to bower components (use absolute path):

```
BOWER_COMPONENTS_ROOT = '/PROJECT_ROOT/static/components'
```

Set url to bower

```
BOWER_COMPONENTS_URL = '/static/components'
```

Load bower in your template

```
{% load bower %}
```

Finally call bower components

```
{% bower 'css' bootstrap %}

{% bower 'js' jquery %}
{% bower 'js' bootstrap %}
```

HTML Output
```
<link rel="stylesheet" href="/static/components/bootstrap/dist/css/bootstrap.css">

<script src="/static/components/jquery/dist/jquery.js"></script>
<script src="/static/components/bootstrap/dist/js/bootstrap.js"></script>
```

License:

[![WTFPL](http://www.wtfpl.net/wp-content/uploads/2012/12/wtfpl-badge-4.png)](http://www.wtfpl.net)