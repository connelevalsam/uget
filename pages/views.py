from django.shortcuts import render

from pages.forms import OrderForm
from pages.models import Order, OrderImages


def home_view(request):
    order_form = OrderForm
    # call it pd(page data) or context
    pd = {
        'message': '',
        'css': '',
        'form': order_form,
    }
    if request.method == 'POST':
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            fullname = order_form.cleaned_data['fullname']
            email = order_form.cleaned_data['email']
            address = order_form.cleaned_data['address']
            description = order_form.cleaned_data['description']

            data = Order.objects.create(fullname=fullname, address=address, email=email, description=description)

            for file in request.FILES.getlist('images'):
                instance = OrderImages(
                    order_id=data.pk,
                    image=file
                )
                instance.save()

            if data.save():
                pd = {
                    'message': 'Failed to send request',
                    'css': 'bg-light-red pv2 pv3-ns',
                    'form': order_form,
                }
            else:
                order_form = OrderForm()
                pd = {
                    'message': 'Success',
                    'css': 'bg-light-green pv2 pv3-ns',
                    'form': order_form,
                }
        else:
            order_form = OrderForm()
            pd = {
                'message': 'Failed to send request, check required field',
                'css': 'bg-light-red pv2 pv3-ns',
                'form': order_form,
            }

    return render(request, 'index.html', pd)


def about_view(request):
    return render(request, 'about.html')
