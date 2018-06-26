from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

from .forms import UploadFileForm
# Create your views here.
"""class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'
	"""
def index(request):
	if request.method == 'POST':
		form = UploadFileForm(request.POST)
		
		if form.is_valid():
			return HttpResponseRedirect('/thanks/')
	else:
		form = UploadFileForm()
	return render(request, 'sidon:index.html', {'form': form})