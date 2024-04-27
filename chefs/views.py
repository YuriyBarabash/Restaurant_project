from django.shortcuts import render
from .models import Chefs, HeadExpression, UnderChefsExpression


def chefs(request):
    chefs = Chefs.objects.filter(is_visible=True)
    head_expressions = HeadExpression.objects.filter(is_visible=True)
    under_chefs_expressions = UnderChefsExpression.objects.filter(is_visible=True)
    context = {'chefs': chefs, 'head_expressions': head_expressions, 'under_chefs_expressions': under_chefs_expressions}
    return render(request, 'chefs_index.html', context=context)
