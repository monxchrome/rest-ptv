from django.contrib.auth.mixins import LoginRequiredMixin
from django.core import exceptions
from django.shortcuts import render


class OwnerOrReadOnly(LoginRequiredMixin):

    def dispatch(self, request, slug, pk: int = None):
        obj = self.get_object()
        if not obj.user.id == request.user.id:
            # raise exceptions.PermissionDenied('YOU SHALL NOT PASS!')
            # return HttpResponse("YOU SHALL NOT PASS!")
            return render(request, 'gallery/403.html')
        return super(OwnerOrReadOnly, self).dispatch(request)
