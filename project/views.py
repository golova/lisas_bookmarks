# Create your views here.


from django.http import HttpResponse

def main_page(request):
    output='''
<html>
<head><title>%s</title></head>
<body>
<h1>%s</h1><p>%s</p>
</body>
</html>
''' % ( 'Django Bookmarks', "Welcome to Lisa's site", 'Where you can share some really cool stuff :D')
    return HttpResponse(output)
        


