import json
import os
from classytags.arguments import Argument
from classytags.core import Tag, Options
from django import template
from django.conf import settings

register = template.Library()


class Bower(Tag):
    """
    Create js and css html tags for installed bower.js components
    """
    options = Options(
        Argument('media_type', required=True),
        Argument('name', required=True),
    )

    bower_root = getattr(settings, 'BOWER_COMPONENTS_ROOT')
    bower_url = getattr(settings, 'BOWER_COMPONENTS_URL')
    js_template = '<script src="%s"></script>'
    css_template = '<link rel="stylesheet" href="%s">'

    def _make_singular_to_list(self, obj):
        """
        Converts unicode object to list object
        """
        return obj if type(obj) == list else [obj]

    def get_main_js(self, name):
        """
        Retrieve main file paths from components bower.json file
        """
        bower_json = open(os.path.join(self.bower_root, name, 'bower.json'), 'r').read()
        main_js_obj = json.loads(bower_json)['main']
        return self._make_singular_to_list(main_js_obj)

    def normalize_file_paths(self, path):
        """
        Removes the './' in file paths
        """
        return path[2:]

    def get_parsed_html(self, path):
        """
        Render the html string according to file extension
        """
        if os.path.splitext(path)[1] == '.js':
            return self.js_template % path
        if os.path.splitext(path)[1] == '.css':
            return self.css_template % path
        else:
            return ''

    def render_tag(self, context, name, media_type):
        files = self.get_main_js(name)
        paths = []
        response = ''

        for f in files:
            paths.append(os.path.join(self.bower_url, name, self.normalize_file_paths(f)))

        for path in paths:
            if media_type == 'js' and '.js' in path:
                response += '%s\n' % self.get_parsed_html(path)

            if media_type == 'css' and '.css' in path:
                response += '%s\n' % self.get_parsed_html(path)

        return response


register.tag(Bower)
