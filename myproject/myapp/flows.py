from viewflow import flow as f
from viewflow import frontend
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow.lock import select_for_update_lock
from viewflow import rest
from viewflow.rest import flow as rf
from viewflow.rest import views as v
from . import models, views
from .models import BuyMaterialProcess,BuyMaterialTask,ManageOrderProcess,ManageMenuProcess
from viewflow import frontend

@frontend.register
class BuyMatFlow(Flow):
    process_class = BuyMaterialProcess
    task_class = BuyMaterialTask
    lock_impl = select_for_update_lock

    chef_start_order = (
        f.Start(
            views.StartView,
        ).Permission(
            auto_create=True
        ).Next(this.manager_approve_order)
    )

    manager_approve_order = (
        f.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_order)
    )

    check_order = (
        f.If(lambda activation: activation.process.approved)
        .Then(this.sup_deliverly)
        .Else(this.chef_fix_order)
    )

    chef_fix_order = (
        f.View(
            views.FixView,
        ).Permission(
            auto_create=True
        ).Next(this.manager_approve_order)
    )

    sup_deliverly = (
        f.View(
            views.DateView,fields=["datesent"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_check_deliverly)
    )

    manager_check_deliverly = (
        f.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_deliverly)
    )

    check_deliverly = (
        f.If(lambda activation: activation.process.approved)
        .Then(this.end_flow)
        .Else(this.manager_complain)
    )

    manager_complain = (
        f.View(
            UpdateProcessView,fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.supplier_return_order)
    )

    supplier_return_order = (
        f.View(
            views.DateView,fields=["datereturn"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_reorder)
    )

    manager_reorder = (
        f.View(
            UpdateProcessView,fields=["approved"]
        ).Permission(
            auto_create=True
        ).Next(this.check_reorder)
    )

    check_reorder = (
        f.If(lambda activation: activation.process.approved)
        .Then(this.sup_deliverly)
        .Else(this.end_flow)
    )

    end_flow = f.End()

@rest.register
@frontend.register
class ManageOrderFlow(Flow):
    process_class = ManageOrderProcess
    lock_impl = select_for_update_lock

    chef_recieve_order = (
        rf.Start(
            v.CreateProcessView,
            fields=["menuitem"]
        ).Permission(
            auto_create=True
        ).Next(this.chef_cook)
    )

    chef_cook = (
        f.View(
            UpdateProcessView,fields=["cook"]
        ).Permission(
            auto_create=True
        ).Next(this.chef_serve)
    )

    chef_serve = (
        f.View(
            UpdateProcessView,fields=["serve"]
        ).Permission(
            auto_create=True
        ).Next(this.Is_return_item)
    )

    Is_return_item = (
        f.View(
            UpdateProcessView,fields=["returnitem"]
        ).Permission(
            auto_create=True
        ).Next(this.check_return)
    )

    check_return = (
        f.If(lambda activation: activation.process.returnitem)
        .Then(this.chef_serve)
        .Else(this.chef_pay)
    )

    chef_pay = (
        f.View(
            UpdateProcessView,fields=["pay"]
        ).Permission(
            auto_create=True
        ).Next(this.end_flow)
    )

    end_flow = f.End()

@frontend.register
class ManageMenuFlow(Flow):
    process_class = ManageMenuProcess
    lock_impl = select_for_update_lock

    manager_manage_menu = (
        f.Start(
            CreateProcessView,fields=["menu"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_edit_menu)
    )

    manager_edit_menu = (
        f.View(
            views.FixMenuView,fields=["name","description","price","image"]
        ).Permission(
            auto_create=True
        ).Next(this.end_flow)
    )

    end_flow = f.End()
