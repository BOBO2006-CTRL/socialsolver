from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Issue


@login_required
def issue_list(request):
    query = request.GET.get("q", "")
    category = request.GET.get("category", "")
    status = request.GET.get("status", "")

    issues = Issue.objects.all().order_by("-created_at")

    if query:
        issues = issues.filter(title__icontains=query)

    if category:
        issues = issues.filter(category=category)

    if status:
        issues = issues.filter(status=status)

    context = {
        "issues": issues,
        "query": query,
        "category": category,
        "status": status,
        "categories": Issue.CATEGORY_CHOICES,
    }

    return render(request, "issues/list.html", context)


@login_required
def issue_detail(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)

    return render(
        request,
        "issues/detail.html",
        {"issue": issue}
    )


@login_required
def issue_create(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        category = request.POST.get("category")

        Issue.objects.create(
            title=title,
            description=description,
            category=category
        )

        return redirect("/issues/")

    return render(request, "issues/create.html")

from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/accounts/login/")
    else:
        form = UserCreationForm()

    return render(request, "registration/register.html", {"form": form})

def about(request):
    return render(request, 'issues/about.html')