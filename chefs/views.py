from django.shortcuts import render
from .models import Chefs, HeadExpression, UnderChefsExpression


def chefs(request):
    """
        View function to render the chefs page with data about chefs and expressions.

        Args:
            request (HttpRequest): The HTTP request object.

        Returns:
            HttpResponse: The HTTP response containing the rendered chefs page.
        """
    chefs = Chefs.objects.filter(is_visible=True)
    head_expressions = HeadExpression.objects.filter(is_visible=True)
    under_chefs_expressions = UnderChefsExpression.objects.filter(is_visible=True)
    context = {'chefs': chefs, 'head_expressions': head_expressions, 'under_chefs_expressions': under_chefs_expressions}
    return render(request, 'chefs_index.html', context=context)
