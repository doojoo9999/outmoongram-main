from django.views.generic.base import TemplateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from contetnts.models import Content

@method_decorator(login_required, name='dispatch')
class HomeView(TemplateView):
    template_name = 'home.html'
    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['context'] = Content.objects.select_related('user').prefetch_related('image_set').filter(user=self.request.user)

        return context
