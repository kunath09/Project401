from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow.lock import select_for_update_lock
from viewflow import rest
# from viewflow.rest import flow, views
from viewflow.rest import views

from . import models, views
from .models import BuyMaterialProcess
from viewflow import frontend

@rest.register
@frontend.register
class BuyMatFlow(Flow):
    process_class = BuyMaterialProcess
    lock_impl = select_for_update_lock

    chef_start_order = (
        flow.Start(
            views.StartView,
            # CreateProcessView,
            # fields=["text","num"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_approve_order)
    )

    # chef_Input_order = (
    #     flow.View(
    #         views.OrderView,
    #         # CreateProcessView,
    #         # fields=["material","text","num"]
    #     ).Permission(
    #         auto_create=True
    #     ).Next(this.chef_Input_order2)
    # )

    # chef_Input_order2 = (
    #     flow.View(
    #         views.Order2View,
    #         # CreateProcessView,
    #         # fields=["material","text","num"]
    #     ).Permission(
    #         auto_create=True
    #     ).Next(this.manager_approve_order)
    # )

    manager_approve_order = (
        flow.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_order)
    )

    check_order = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.sup_checkstock)
        .Else(this.chef_fix_order)
    )

    chef_fix_order = (
        flow.View(
            # UpdateProcessView,fields=["material","text"]
            # views.FixView,fields=["material","quantity"]
            views.FixView,
        ).Permission(
            auto_create=True
        ).Next(this.manager_approve_order)
    )

    sup_checkstock = (
        flow.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_stock)
    )

    check_stock = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.sup_deliverly)
        .Else(this.chef_fix_order)
    )

    sup_deliverly = (
        flow.View(
            views.DateView,fields=["datesent"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_check_deliverly)
    )

    manager_check_deliverly = (
        flow.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_deliverly)
    )

    check_deliverly = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.end_flow)
        .Else(this.manager_complain)
    )

    manager_complain = (
        flow.View(
            # views.DateView,fields=["reorder"]
            UpdateProcessView,fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.supplier_return_order)
    )

    supplier_return_order = (
        flow.View(
            views.DateView,fields=["datereturn"]
            # UpdateProcessView,fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_reorder)
    )

    manager_reorder = (
        flow.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_reorder)
    )

    check_reorder = (
        flow.If(lambda activation: activation.process.approved)
        .Then(this.sup_checkstock)
        .Else(this.end_flow)
    )

    end_flow = flow.End()