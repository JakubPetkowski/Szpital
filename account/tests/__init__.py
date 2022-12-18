def get(self, request, *args, **kwargs):  # pylint: disable=W0613
    """
    GET request
    """

    index = int(kwargs['index'])
    render_type = kwargs['type']

    obj = registry._registry[index](*registry._registry[index].get_demo_args())  # pylint: disable=W0212

    context = obj.get_context_data()

    content = obj.render(render_type, context)

    render_type = "plain" if render_type == "text" else render_type
    charset = settings.DEFAULT_CHARSET

    return HttpResponse(content, content_type='text/{}; charset={}'.format(render_type, charset))