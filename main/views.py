from django.shortcuts import render  # noqa
from django.http.response import HttpResponse
from django.http.request import HttpRequest
from datetime import datetime

# Create your views here.


def empty(req: HttpRequest):
    return HttpResponse(
        f"""
        <h1>Ok</h1>
        <h3>Работает!</h3>
        <p>
            Дата: {datetime.now()}<br/>
            PATH: {req.path}; GET: {req.GET.dict()}; POST: {req.POST.dict()}<br/>
            HEADERS:<br/>
            <table><tr><td>
            {'</td></tr><tr><td>'.join(map('</td><td>'.join, req.headers.items()))}
            </td></tr></table>
        </p>
        """
    )