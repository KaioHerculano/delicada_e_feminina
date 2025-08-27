from django.shortcuts import render, redirect
from django.contrib import messages
from django.conf import settings
import requests
from . import models
from django.views import View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import ProductForm


class ProductListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):
    model = models.Product
    template_name = 'product_list.html'
    context_object_name = 'products'
    paginate_by = 8
    permission_required = 'products.view_product'
    api_url = settings.API_URL

    def get_queryset(self):
        query = self.request.GET.get('q')
        local_products = models.Product.objects.all()
        if query:
            local_products = local_products.filter(title__icontains=query)

        api_products = []
        token = self.request.session.get('api_jwt_token')

        if token:
            try:
                headers = {'Authorization': f'Bearer {token}'}
                response = requests.get(f"{self.api_url}/api/v1/products/", headers=headers)
                if response.status_code == 200:
                    data = response.json()
                    for item in data:
                        item['is_external'] = True
                        item['api_id'] = item['id']
                        api_products.append(item)
            except Exception as e:
                print("Erro ao acessar API externa:", e)

        return list(local_products) + api_products


class ProductDetailView(View):
    api_url = settings.API_URL

    def get(self, request, *args, **kwargs):
        print("Acessando ProductDetailView")
        if 'external_id' in kwargs:
            print(f"Acessando produto API com external_id: {kwargs['external_id']}")
            return self.get_api_product(request, kwargs['external_id'])
        elif 'pk' in kwargs:
            print(f"Acessando produto local com pk: {kwargs['pk']}")
            return self.get_local_product(request, kwargs['pk'])
        else:
            messages.error(request, "Produto não encontrado")
            return redirect('product_list')
    
    def get_local_product(self, request, pk):
        try:
            product = models.Product.objects.get(pk=pk)
            return render(request, 'product_detail.html', {
                'product': product,
                'is_external': False
            })
        except models.Product.DoesNotExist:
            messages.error(request, "Produto local não encontrado")
            return redirect('product_list')
    
    def get_api_product(self, request, api_id):
        try:
            api_base_url = f"{self.api_url}"
            api_url = f'{api_base_url}/api/v1/public/products/1/{api_id}/'
            
            print(f"Chamando API: {api_url}")
            response = requests.get(api_url, timeout=5)
            
            print(f"Status da resposta da API: {response.status_code}")
            
            if response.status_code == 404:
                messages.error(request, "Produto não encontrado na API")
                return redirect('product_list')
            
            response.raise_for_status()
            product_data = response.json()
            
            print(f"Dados do produto recebidos: {product_data}")
            
            if 'photo' in product_data and product_data['photo']:
                photo_url_from_api = product_data['photo']
                if not photo_url_from_api.startswith('http') and not photo_url_from_api.startswith('/media/'):
                    product_data['photo'] = f'{api_base_url}/media/{photo_url_from_api}'
                elif photo_url_from_api.startswith('/media/'):
                    product_data['photo'] = f'{api_base_url}{photo_url_from_api}'

            return render(request, 'product_detail.html', {
                'product': product_data,
                'is_external': True
            })
        except requests.exceptions.HTTPError as http_err:
            print(f"HTTP error occurred: {http_err}")
            messages.error(request, f"Erro ao buscar produto na API: {str(http_err)}")
            return redirect('product_list')
        except Exception as e:
            print(f"Erro inesperado: {str(e)}")
            messages.error(request, f"Erro ao buscar produto na API: {str(e)}")
            return redirect('product_list')


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = models.Product
    form_class = ProductForm
    template_name = 'product_create.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.add_product'


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = models.Product
    form_class = ProductForm
    template_name = 'product_update.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.change_product'


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = models.Product
    template_name = 'product_delete.html'
    success_url = reverse_lazy('product_list')
    permission_required = 'products.delete_product'
