from django.views.generic.edit import CreateView
from django.contrib.auth import get_user_model
from .forms import UserRegistrationForm
from django.urls import reverse_lazy


class CreateUserView(CreateView):
    model = get_user_model()
    form_class = UserRegistrationForm
    template_name = 'account/registration.html'
    success_url = reverse_lazy('rest_framework:login')
