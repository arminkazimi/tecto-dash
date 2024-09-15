from django.shortcuts import render


def switch_panel_view(request):
    return render(request=request, template_name='pages/switch_panel.html')
