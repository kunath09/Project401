from viewflow import flow
from viewflow.base import this, Flow
from viewflow.flow.views import CreateProcessView, UpdateProcessView
from viewflow.lock import select_for_update_lock


from . import models, views
from .models import BuyMetProcess
from viewflow import frontend

@frontend.register
class BuyMetFlow(Flow):
    process_class = BuyMetProcess
    lock_impl = select_for_update_lock

    chef_start_order = (
        flow.Start(
            views.StartView,
            # CreateProcessView,
            # fields=["material","text","num"]
        ).Permission(
            auto_create=True
        ).Next(this.manager_approve_order)
    )

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
            UpdateProcessView,fields=["material","text"]
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
            UpdateProcessView,fields=["num"]
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
        .Else(this.complain)
    )

    complain = (
        flow.View(
            UpdateProcessView,fields=["text"]
        ).Permission(
            auto_create=True
        ).Next(this.end_flow)
    )

    end_flow = flow.End()