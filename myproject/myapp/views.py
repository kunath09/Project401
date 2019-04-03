from django.shortcuts import render
from django.views import generic
# from material import Layout, Fieldset, Row, Span2, Span5, Span7
from viewflow.flow.views import StartFlowMixin, FlowViewMixin,FlowMixin

from .forms import CreatOrderForm
from .models import Material,BuyMetProcess

class StartView(StartFlowMixin, generic.UpdateView):
    form_class = CreatOrderForm
    # model = BuyMetProcess
    # fields = ['fields','form_class']

    def get_object(self):
        return self.activation.process.material

    def activation_done(self, form):
        material = form.save()
        self.activation.process.material = material
        super(StartView, self).activation_done(form)

# def InputMaterial():
#     area =[""]

    
    
