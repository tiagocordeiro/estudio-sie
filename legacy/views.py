from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render

from .models import Os, Clientes, ClientesContatos, Enderecos


@login_required
def legacy_clientes_list(request):
    legacy_customers = Clientes.objects.using('legacy_db').all()
    context = {'legacy_customers': legacy_customers}
    return render(request, 'customer/list.html', context)


@login_required
def legacy_customer_detail(request, cli_codigo):
    customer = Clientes.objects.using('legacy_db').get(cli_codigo=cli_codigo)
    contacts = ClientesContatos.objects.using('legacy_db').filter(
        cli_codigo=cli_codigo)
    enderecos = Enderecos.objects.using('legacy_db').filter(
        cli_codigo=cli_codigo)
    os_list = Os.objects.using('legacy_db').filter(cli_codigo=cli_codigo)
    context = {'customer': customer,
               'contacts': contacts,
               'enderecos': enderecos,
               'os_list': os_list}
    return render(request, 'customer/detail.html', context)


@login_required
def legacy_os_list(request):
    legacy_os = Os.objects.using('legacy_db').all().order_by(
        '-os_dataabertura')
    page = request.GET.get('page', 1)

    paginator = Paginator(legacy_os, 20)
    try:
        ordens = paginator.page(page)
    except PageNotAnInteger:
        ordens = paginator.page(1)
    except EmptyPage:
        ordens = paginator.page(paginator.num_pages)

    context = {'legacy_os': ordens}
    return render(request, 'os/list.html', context)
