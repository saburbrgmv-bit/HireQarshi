from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy

from .forms import CategoryForm, JobForm
from.models import Category, Job

class JobListView(ListView):
  model = Job
  template_name = 'job/job_list.html'
  context_object_name = 'jobs'

  def get_queryset(self):
    queryset = super().get_queryset()

    query = self.request.GET.get
    if query:
      queryset = queryset.filter(title__icontains=query)


class JobCreateView(CreateView):
  model = Job
  template_name = 'job/job_create.html'
  success_url = reverse_lazy('employers')
  form_class = JobForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)


class JobUpdateView(UpdateView):
  model = Job
  template_name = 'job/job_update.html'
  success_url = reverse_lazy('employers')
  form_class = JobForm

  def form_valid(self, form):
    form.instance.user = self.request.user
    return super().form_valid(form)

class JobDeleteView(DeleteView):
  model = Job
  template_name = 'job/job_delete.html'
  success_url = reverse_lazy('employers')

class JobDetailView(DetailView):
  model = Job
  template_name = 'job/job_detail.html'
  context_object_name = 'jobs'
