from django.shortcuts import render

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def page(request, name):
    return render(request, "encyclopedia/page.html", {
        "name": name,
        "entry": util.get_entry(name),
    })