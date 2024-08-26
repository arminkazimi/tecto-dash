from django.shortcuts import render


def switch_panel(request):
    return render(request=request, template_name='pages/switch_panel.html')
