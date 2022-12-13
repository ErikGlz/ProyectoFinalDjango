from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    SEO1 = ["Proyecto Final con Django"]
    SEO2 = ["Proyecto Final con Django"]
    title = ["Proyecto Final con Django"]
    gsite = [""]
    uri = ["about"]
    desc = ["Sitio Web que ofrece servicios de creación de páginas web, aplicaciones móviles y aplicaciones de contabilidad de cajero de punto de venta"]
    img = ["https://1.bp.blogspot.com/-7O4lZT7kOdA/YY_Pf2DKTPI/AAAAAAAAR3E/_MbtNJ7BygUmq-8Ps_w6ve6R57xCcatOQCLcBGAsYHQ/s400/pembuatan%2Bwebsite%2Bdjanggo%2Bphyton1.png"]
    return render(request, "home/index.html",{"title": title,"uri": uri, "desc": desc, "img": img,"SEO1": SEO1,"SEO2": SEO2,"gsite": gsite,})


