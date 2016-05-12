import functools
from  bottle import template, view, BaseTemplate, DEBUG

class PlimTemplate(BaseTemplate):
    def prepare(self, **options):
        from mako.template import Template
        from mako.lookup import TemplateLookup
        from plim import preprocessor
        options.update({'input_encoding':self.encoding})
        options.setdefault('format_exceptions', bool(DEBUG))
        lookup = TemplateLookup(directories=self.lookup, **options)
        if self.source:
            self.tpl = Template(self.source, preprocessor = preprocessor, lookup=lookup, **options)
        else:
            self.tpl = Template(uri=self.name, preprocessor = preprocessor, filename=self.filename, lookup=lookup, **options)

    def render(self, *args, **kwargs):
        for dictarg in args: kwargs.update(dictarg)
        _defaults = self.defaults.copy()
        _defaults.update(kwargs)
        return self.tpl.render(**_defaults)


plim_template = functools.partial(template, template_adapter=PlimTemplate)
plim_view = functools.partial(view, template_adapter=PlimTemplate)
