from django.shortcuts import render_to_response
from django.template.context import RequestContext
from django.http import Http404

def render(request, template_name, context=None):
    """
        This is a convenience method used for rendering view to template using 
        the RequestContext.
    """
    return render_to_response(template_name, context or {}, context_instance=RequestContext(request))

def get_object_or_404(obj_model, **kwargs):
    """
        Convenience method for retrieving an object or returning a 404.
        NOTE this works for mongoengine Document models too.
    """
    try:
        return obj_model.objects.get(**kwargs)
    except obj_model.DoesNotExist:
        raise Http404
