from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from django.shortcuts import render, redirect

from django.views import View
from django.views.generic.base import TemplateView
from django.views.generic import DetailView, ListView, UpdateView, CreateView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.base import RedirectView

from django_tables2 import *

from business.models import *
from business.forms import *
from business.tables import *

from business.helper_backend import commonListView


class appStoreListCommonListView(commonListView):
    active_app = 'store'
    active_apptitle = 'Store Management'
    object_icon = 'shopping-cart'


class appStoreHome(View):
    def get(self, request):
        return redirect(reverse_lazy('business:app_store_brand_list'))


# bzBrand

class appStoreBrandList(appStoreListCommonListView):
    model = bzBrand
    table_class = bzBrandTable
    action_new = reverse_lazy('business:app_store_brand_create')
    object_name = "Brand"


class appStoreBrandCreate(CreateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_brand_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
        context['action_list'] = reverse_lazy('business:app_store_brand_list')
        return context


class appStoreBrandUpdate(UpdateView):
    model = bzBrand
    form_class = bzBrandForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_brand_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreBrandUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Brands"
        context['action_list'] = reverse_lazy('business:app_store_brand_list')
        return context


# pfStore

class appStorePFList(appStoreListCommonListView):
    model = pfStore
    table_class = pfStoreTable
    action_new = reverse_lazy('business:app_store_pf_create')
    object_name = "Printful Store"


class appStorePFCreate(CreateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_pf_list')

    def get_context_data(self, **kwargs):
        context = super(appStorePFCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        context['action_list'] = reverse_lazy('business:app_store_pf_list')
        return context


class appStorePFUpdate(UpdateView):
    model = pfStore
    form_class = pfStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_pf_list')

    def get_context_data(self, **kwargs):
        context = super(appStorePFUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "Printful Stores"
        context['action_list'] = reverse_lazy('business:app_store_pf_list')
        return context


# wpStore

class appStoreWPList(appStoreListCommonListView):
    model = wooStore
    table_class = wooStoreTable
    action_new = reverse_lazy('business:app_store_wp_create')
    object_name = "Brand"


class appStoreWPCreate(CreateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_wp_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreWPCreate,
                        self).get_context_data(**kwargs)
        context['mode'] = "create"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        context['action_list'] = reverse_lazy('business:app_store_wp_list')
        return context


class appStoreWPUpdate(UpdateView):
    model = wooStore
    form_class = wooStoreForm
    template_name = "business/object_form.html"
    success_url = reverse_lazy('business:app_store_wp_list')

    def get_context_data(self, **kwargs):
        context = super(appStoreWPUpdate,
                        self).get_context_data(**kwargs)
        context['mode'] = "update"
        context['active_app'] = "store"
        context['active_apptitle'] = "Store Management"
        context['object_icon'] = 'shopping-cart'
        context['object_name'] = "WordPress Sites"
        context['action_list'] = reverse_lazy('business:app_store_wp_list')
        return context
