from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    SEO1 = ["Acerca de"]
    SEO2 = ["Acerca de"]
    gsite = [""]
    title = ["Servicio de creación de tu aplicación android, sitio web y cajero punto de venta"]
    desc = ["Ahora es el momento de desarrollar su tecnología con nosotros para el mejor futuro, las necesidades de desarrollo de proyectos e implementación de sitios web modernos con tecnología moderna para aplicaciones de Android, además de aplicaciones de contabilidad de cajero de punto de venta para tiendas y restaurantes, están listas para que las use."]
    himg = ["https://1.bp.blogspot.com/-UfbS7fzia0s/YY_T9KGzogI/AAAAAAAAR3M/f5fyHLwcM5IpeCEpImdvFkVaig_B9RL7gCLcBGAsYHQ/s1712/pembuatan%2Bwebsite%2Bterbaru%2Bmodern.png"]
    aimg = ["https://1.bp.blogspot.com/-YbzqygBEcxY/YY_VwwqTieI/AAAAAAAAR3U/z-d69ct02KwLTevk6ztSmUpSnzdr6sDZQCLcBGAsYHQ/s666/pembuatan%2Bandroid%2Bterbaru.png"]
    bimg = ["https://1.bp.blogspot.com/-YN5d4Sv9P8s/YY_awY9_ojI/AAAAAAAAR3o/ZjImPTro0gEEV0JPJvNqsaU8U8JbGCn-QCLcBGAsYHQ/s519/pembuatan%2Bwebsite.png"]
    cimg = ["https://1.bp.blogspot.com/-udm1kuJJ_YM/YY_akT1oZHI/AAAAAAAAR3c/k8EXsbU3J4oqNYOMDt_EhT8pH0HqwndSACLcBGAsYHQ/s626/aplikasi%2Bbisnis.jpg"]
    fotimg = ["https://1.bp.blogspot.com/-4qdfwtJupvQ/YY_akT-SY0I/AAAAAAAAR3k/tTvsBrwJvKAbeQP9Xzwiw056E1fIVoyLwCLcBGAsYHQ/s1200/website%2Bapplikasi.jpg"]
    hsec1 = ["Aplicaciones Android"]
    sec1 = ["La necesidad de crear aplicaciones android para subir a Google Playstore permite el progreso de tu empresa y negocio, tener tu propio paquete APK de Android te facilitará acercarte a tus clientes para brindarles información detallada sobre negocios y otros negocios. El desarrollo con flutter dart nativo de Java Kotlin facilita la carga rápida de Google Playstore."]
    uri1 = ["/services/pembuatanandroid"]
    hsec2 = ["Websites Modernos"]
    sec2 = ["Desarrolle la creación de su sitio web de información y tienda en línea compre con nosotros los mejores resultados utilizando varias tecnologías que puede elegir en el desarrollo y despliegue moderno de su sitio, con laravel, django, angular, react, gatsby, jekyll, modx, symfony, getaxcora cms y otros, además de soporte completo para la última tecnología para su sitio web moderno."]
    uri2 = ["/services/pembuatanwebsite"]
    hsec3 = ["Aplicaciones Online."]
    sec3 = ["Y satisfaga la necesidad de trabajar fácilmente a través de aplicaciones en línea, independientemente de su línea de negocio, esta aplicación en línea está disponible en varias variantes basadas en campos comerciales industriales y educativos, que van desde aplicaciones de cajero de punto de venta hasta tiendas, restaurantes, facturación, contabilidad contabilidad , reservas de reserva en línea, escuelas de ERP y muchos otros que pueden usarse para acelerar las transacciones de caja, ya que su contabilidad digital más el monitoreo del rendimiento a través de informes detallados están presentes en él."]
    uri3 = ["/services/pembuatanaplikasi"]
    hfoot = ["Todo en una aplicación de Sitio Web"]
    cfoot = ["O mejórelo con un sitio web moderno todo en uno, su sitio está integrado con aplicaciones de caja, facturas de tiendas, contabilidad escolar a aplicaciones de Android en un solo paquete para estar listo para avanzar en su negocio, con nosotros cuando comience la era digital."]
    wa = ["https://www.whatsapp.com/?lang=es"]
    call = ["https://zoom.us/"]
    mail = ["mailto:erikglez_ipn@hotmail.com"]
    return render(request, "about/index.html" , {"SEO1": SEO1,"SEO2": SEO2,"gsite": gsite,"title": title,"himg": himg,"desc": desc,"aimg": aimg,"bimg": bimg,"cimg": cimg,"fotimg": fotimg,"hsec1": hsec1,"hsec2": hsec2,"hsec3": hsec3, "hfoot": hfoot,"cfoot": cfoot,"sec1": sec1,"sec2": sec2,"sec3": sec3,"uri1": uri1,"uri2": uri2,"uri3": uri3,"wa": wa,"call": call,"mail": mail})
  


