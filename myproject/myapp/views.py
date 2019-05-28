from django.shortcuts import render,redirect
from django.views import generic
# from material import Layout, Fieldset, Row, Span2, Span5, Span7
from viewflow.flow.views import StartFlowMixin, FlowViewMixin,FlowMixin

from .forms import MaterialForm
from .models import Material,BuyMaterialProcess,ManageMenuProcess,ManageOrderProcess,CheckStockProcess,AddStockProcess
from django.contrib.auth.decorators import login_required

from social_django.models import UserSocialAuth
from django.contrib.auth.forms import AdminPasswordChangeForm, PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from .models import Profile,Material,Menu,BuyMaterialProcess,MaterialItem,Restaurant,OrderMaterial,Stock

@login_required
def home(request):
    return render(request, '/home/kunat/Desktop/Project401/myproject/myapp/templates/home.html')

@login_required
def settings(request):
    user = request.user

    try:
        github_login = user.social_auth.get(provider='github')
    except UserSocialAuth.DoesNotExist:
        github_login = None

    try:
        twitter_login = user.social_auth.get(provider='twitter')
    except UserSocialAuth.DoesNotExist:
        twitter_login = None

    try:
        facebook_login = user.social_auth.get(provider='facebook')
    except UserSocialAuth.DoesNotExist:
        facebook_login = None

    can_disconnect = (user.social_auth.count() > 1 or user.has_usable_password())

    return render(request, '/home/kunat/Desktop/Project401/myproject/myapp/templates/settings.html', {
        'github_login': github_login,
        'twitter_login': twitter_login,
        'facebook_login': facebook_login,
        'can_disconnect': can_disconnect
    })

@login_required
def password(request):
    if request.user.has_usable_password():
        PasswordForm = PasswordChangeForm
    else:
        PasswordForm = AdminPasswordChangeForm

    if request.method == 'POST':
        form = PasswordForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            messages.success(request, 'Your password was successfully updated!')
            return redirect('password')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordForm(request.user)
    return render(request, '/home/kunat/Desktop/Project401/myproject/myapp/templates/password.html', {'form': form})
###############################
    
# def login(request):
#     return render(request, 'templates/login.html')
    
# def logout(request):
#     return render(request, 'templates/logout.html')

# class StartView(StartFlowMixin, generic.UpdateView):
#     form_class = CreatOrderForm
#     # model = BuyMetProcess
#     # fields = ['fields','form_class']

#     def get_object(self):
#         return self.activation.process.material

#     def activation_done(self, form):
#         material = form.save()
#         self.activation.process.material = material
#         super(StartView, self).activation_done(form)

# def InputMaterial():
#     area =[""]

class StartView(StartFlowMixin, generic.UpdateView):
    # form_class = RestaurantForm
    form_class = MaterialForm

    def get_object(self):
        return self.activation.process.ordermaterial

    def activation_done(self, form):
        ordermaterial = form.save()
        self.activation.process.ordermaterial = ordermaterial
        super(StartView, self).activation_done(form)

# class OrderView(FlowMixin, generic.UpdateView):
#     form_class = MaterialForm

#     def get_object(self):
#         return self.activation.process.ordermaterial

#     def activation_done(self, form):
#         ordermaterial = form.save()
#         print(f'------------------------{ordermaterial}------------------------')
#         self.activation.process.ordermaterial = ordermaterial
#         super(OrderView, self).activation_done(form)
        


# class Order2View(FlowMixin, generic.UpdateView):
#     form_class = Material2Form

#     def get_object(self):
#         return self.activation.process.ordermaterial

#     def activation_done(self, form):
#         ordermaterial = form.save()
#         print(f'------------------------{ordermaterial}------------------------')
#         self.activation.process.ordermaterial = ordermaterial
#         super(Order2View, self).activation_done(form)
        
    
class FixView(FlowMixin, generic.UpdateView):
    form_class = MaterialForm

    def get_object(self):
        return self.activation.process.ordermaterial

    def activation_done(self, form):
        ordermaterial = form.save()
        self.activation.process.ordermaterial = ordermaterial
        super(FixView, self).activation_done(form)

class DateView(FlowMixin, generic.UpdateView):
    
    def get_object(self):
        return self.activation.process.ordermaterial

class FixStockView(FlowMixin, generic.UpdateView):

    def get_object(self):
        return self.activation.process.stock

class FixMenuView(FlowMixin, generic.UpdateView):
    
    def get_object(self):
        return self.activation.process.menu
