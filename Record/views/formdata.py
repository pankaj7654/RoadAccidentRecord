from django.views import View
from django.shortcuts import render , redirect
from Record.models.FormData import RecordFormData



class FormdataView(View):
    def post(self , request):
        fireno = request.POST.get('fireno')
        ipc = request.POST.get('ipc')
        allrecordno = RecordFormData.objects.all().count()
        print(allrecordno,"+++++++++++++++++++++++++++++++++++")
        recordobj = RecordFormData(fireno=fireno, ipc=ipc)
        recordobj.save()
        print("save successfully")
        return render(request, 'index.html') 


