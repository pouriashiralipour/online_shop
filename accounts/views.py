from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from allauth.account.views import PasswordChangeView


class LoginAfterPasswordChangeView(PasswordChangeView):
    @property
    def success_url(self):
        return reverse_lazy('generic: password_change_success')


login_after_password_change = login_required(LoginAfterPasswordChangeView.as_view())


@login_required
def password_change_success(request):
    template = "account/password_change_success.html"
    return render(request, template)