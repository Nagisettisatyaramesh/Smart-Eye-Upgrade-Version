from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect, render

from .forms import LeadForm

# Sample data for the authenticated workspace. This is presentation
# content only; it is not backed by real quality records.
WORKSPACE_METRICS = [
    {'label': 'Open CAPAs', 'value': 7, 'trend': '-2 this week'},
    {'label': 'Documents pending review', 'value': 12, 'trend': '+3 this week'},
    {'label': 'Overdue training assignments', 'value': 3, 'trend': 'no change'},
    {'label': 'Upcoming internal audits', 'value': 2, 'trend': 'next in 9 days'},
]

WORKSPACE_QUEUE = [
    {'title': 'Approve DHF update — Infusion Pump Model IX', 'owner': 'Design Control', 'due': 'Due in 2 days'},
    {'title': 'Close CAPA-0114 — Labeling deviation', 'owner': 'CAPA', 'due': 'Due in 3 days'},
    {'title': 'Review risk file RA-208 — Software update', 'owner': 'Risk Management', 'due': 'Due in 5 days'},
    {'title': 'Sign off complaint COMP-3391', 'owner': 'Complaint Handling', 'due': 'Due in 6 days'},
    {'title': 'Confirm supplier audit schedule — Q3', 'owner': 'Supplier Quality', 'due': 'Due in 9 days'},
]

# Sample article and media summaries for the Resources page. Original
# writing for this project; not implemented content or real publications.
RESOURCE_ARTICLES = [
    {
        'tag': 'Audits',
        'date': 'Feb 2026',
        'title': 'Preparing for your first ISO 13485 audit',
        'excerpt': 'The gaps that trip up first-time audits most often aren’t missing documents — they’re documents that exist but were never linked back to a design record.',
    },
    {
        'tag': 'ISO 13485',
        'date': 'Jan 2026',
        'title': 'ISO 13485 in plain terms',
        'excerpt': 'A short walkthrough of what the standard actually asks a quality system to do, without the clause-number scavenger hunt.',
    },
    {
        'tag': 'EU MDR',
        'date': 'Dec 2025',
        'title': 'EU MDR and FDA 21 CFR 820: where the paperwork overlaps',
        'excerpt': 'Most design control evidence satisfies both frameworks at once. Here’s where the overlap actually holds and where it doesn’t.',
    },
    {
        'tag': 'Document Control',
        'date': 'Nov 2025',
        'title': 'Six signs your document control process needs an upgrade',
        'excerpt': 'Version conflicts, stale approvals, and "who has the current copy" threads are usually symptoms of the same underlying gap.',
    },
    {
        'tag': 'Risk Management',
        'date': 'Oct 2025',
        'title': 'What reviewers actually look for in a risk file',
        'excerpt': 'ISO 14971 reviewers read hazard-to-mitigation traceability first. Everything else in the file supports that one thread.',
    },
    {
        'tag': 'CAPA',
        'date': 'Sep 2025',
        'title': 'Root cause analysis mistakes we see most often',
        'excerpt': 'Stopping at the first plausible cause is the most common reason a CAPA reopens six months later.',
    },
]

RESOURCE_MEDIA = [
    {'title': 'A tour of the workspace', 'length': '4 min'},
    {'title': 'Design controls, start to finish', 'length': '6 min'},
    {'title': 'What auditors ask for first', 'length': '3 min'},
]


def _lead_form_view(request, template_name):
    if request.method == 'POST':
        form = LeadForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('website:thanks')
    else:
        form = LeadForm()
    return render(request, template_name, {'form': form})


def home(request):
    return _lead_form_view(request, 'website/home.html')


def thanks(request):
    return render(request, 'website/thanks.html')


def why_smarteye(request):
    return render(request, 'website/why_smarteye.html')


def who_we_are(request):
    return render(request, 'website/who_we_are.html')


def contact(request):
    return _lead_form_view(request, 'website/contact.html')


def resources(request):
    context = {
        'articles': RESOURCE_ARTICLES,
        'media': RESOURCE_MEDIA,
    }
    return render(request, 'website/resources.html', context)


def login_view(request):
    if request.user.is_authenticated:
        return redirect('website:workspace')

    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('website:workspace')
        messages.error(request, 'Incorrect username or password.')

    return render(request, 'website/login.html')


def logout_view(request):
    logout(request)
    return redirect('website:home')


@login_required
def workspace(request):
    context = {
        'metrics': WORKSPACE_METRICS,
        'queue': WORKSPACE_QUEUE,
    }
    return render(request, 'website/workspace.html', context)
