from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
import markdown2

def index(request):
    return render(request, 'converter/index.html')

def convert_markdown(request):
    if request.method == 'POST':
        markdown_text = request.POST['markdown']
        html_content = markdown2.markdown(markdown_text)

        if request.POST['output_option'] == 'download':
            # HTMLファイルをダウンロード
            response = HttpResponse(html_content, content_type='text/html')
            response['Content-Disposition'] = 'attachment; filename="converted.html"'
            return response
        else:
            # HTMLをページ上に表示
            return render(request, 'converter/index.html', {'html_content': html_content, 'markdown_text': markdown_text})
