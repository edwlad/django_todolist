from django.shortcuts import render  # noqa
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from django.views.generic import ListView
from .models import MyList
from datetime import datetime


def error(req: HttpRequest, *args, **kwargs):
    status = int(kwargs.get("status", 400))
    title = kwargs.get("title", "Ошибка")
    content = kwargs.get("content", f"Код ошибки: {status}")
    return render(
        req,
        "error.html",
        status=status,
        context={
            "title": title,
            "content": content,
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


def index(req: HttpRequest, *args, **kwargs):
    status = int(kwargs.get("status", 200))
    title = kwargs.get("title", "Список задач.")
    content = kwargs.get("content", "")
    return render(
        req,
        "index.html",
        status=status,
        context={
            "title": title,
            "content": content,
        },
    )


class MainIndex(ListView):
    template_name = "index.html"
    # queryset = MyList
    model = MyList
    # paginate_by = 2
    context_object_name = "context"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context["len"] = Book.objects.all()
        return context
