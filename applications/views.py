from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import CreateView

from jobs.models import Job

from .forms import ApplicationForm
from .models import Application
from django.urls import reverse_lazy



class ApplicationCreateView(LoginRequiredMixin, CreateView):
    model = Application
    form_class = ApplicationForm
    success_url = reverse_lazy('workers')
    template_name = 'applications/applications_create.html'


    def form_valid(self, form):
        job = get_object_or_404(Job, pk=self.kwargs["job_pk"])
        form.instance.user = self.request.user
        form.instance.job = job
        return super().form_valid(form)



    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.object.job.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["job"] = get_object_or_404(Job, pk=self.kwargs["job_pk"])
        return context