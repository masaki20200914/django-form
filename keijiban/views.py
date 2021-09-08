from django.shortcuts import render
from keijiban.forms import KakikomiForm

def kakikomi(request):
    f = KakikomiForm()
    return render(request, 'keijiban/kakikomiform.html', {'form1': f} )