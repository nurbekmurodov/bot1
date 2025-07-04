from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .models import Profile
from .forms import ProfileForm

class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'accounts/profile_form.html'
    success_url = reverse_lazy('profile')

    def get_object(self):
        return self.request.user.profile