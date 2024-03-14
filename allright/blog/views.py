from django.shortcuts import render
from django.views.generic import ListView
# from django.core.mail import send_mail
# from django.template.loader import render_to_string
from .models import Depoimento, Case
from .forms import CadastroHomePageForm

# Create your views here.
def LandingPageView(request):
    if request.method == 'POST':
        forms = CadastroHomePageForm(request.POST)
        if forms.is_valid:
            instance = forms.save()
            # html_message = render_to_string('email_novo_cadastro.html', context={'forms': instance})
            # send_mail(
            #     "Cadastro Allright Consultoria Site",
            #     f"Novo cadastro de {instance.nome}",
            #     "daniel@allright-consultoria.com.br",
            #     ["daniel@allright-consultoria.com.br"],
            #     fail_silently=False,
            #     html_message=html_message
            # )
            context = {
                'form': forms,
                'enviado': True
            }
            return render(request, 'index.html', context)

    forms = CadastroHomePageForm
    
    context = {
        'form': forms
    }
    return render(request, 'index.html', context)

class CaseListView(ListView):
    model = Case
    template_name = 'cases_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['depoimentos'] = Depoimento.objects.all()
        return context

