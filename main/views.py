from django.shortcuts import render  # noqa
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from django.urls import reverse, reverse_lazy
from .models import MyList
from datetime import datetime


def error(req: HttpRequest, *args, **kwargs):
    status = int(kwargs.get("status", 400))
    title = kwargs.get("title", "Ошибка")
    content = kwargs.get("content", f"<p>Код ошибки: {status}</p>")
    return render(
        req,
        "error.html",
        status=status,
        context={
            "title": title,
            "content": content,
            "buttons": ("back", "index"),
            "is_error": True,
        },
    )


def empty(req: HttpRequest):
    out = HttpResponse(
        f"""
        <h1>Ok</h1>
        <h3>Работает!</h3>
        <div>
            <p>Дата: {datetime.now()}<br/>
            PATH: {req.path}; GET: {req.GET.dict()}; POST: {req.POST.dict()}<br/>
            HEADERS:</p>
            <table><tr><td>
            {'</td></tr><tr><td>'.join(map('</td><td>'.join, req.headers.items()))}
            </td></tr></table>
        </div>
        """
    )
    return out


class MainIndex(ListView):
    template_name = "index.html"
    model = MyList
    # paginate_by = 2
    context_object_name = "context"

    def get_queryset(self):
        filt = self.request.GET.get("f", "off")
        queryset = self.model.objects.all()
        if filt == "on":
            return queryset.filter(chk_end=True)
        elif filt == "all":
            return queryset
        return queryset.filter(chk_end=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = ("add", "items")
        context["is_index"] = True
        return context


class MainDetail(DetailView):
    template_name = "detail.html"
    context_object_name = "context"
    model = MyList

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = ("back", "add", "edit", "delete", "index")
        context["is_detail"] = True
        return context


class MainEdit(UpdateView):
    template_name = "edit.html"
    fields = ("desc", "chk_end")
    context_object_name = "context"
    model = MyList

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = ("back", "add", "detail", "delete", "index")
        context["is_edit"] = True
        return context


class MainAdd(CreateView):
    template_name = "add.html"
    fields = ("desc",)
    context_object_name = "context"
    model = MyList

    def get_success_url(self):
        return reverse("detail", kwargs={"pk": self.object.id})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = ("back", "index")
        context["is_add"] = True
        return context


class MainDelete(DeleteView):
    template_name = "delete.html"
    context_object_name = "context"
    model = MyList

    def get_success_url(self):
        return reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["buttons"] = ("back", "add", "edit", "detail", "index")
        context["is_delete"] = True
        return context
