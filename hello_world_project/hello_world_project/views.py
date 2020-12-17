# djangoが用意しているレスポンスメソッド
# https://docs.djangoproject.com/en/3.1/ref/request-response/
from django.http import HttpResponse

#request objectを受け取るのでrequestの記載が必要、文字列はなんでも良い
def helloworldfunction(request):
  returnedobject = HttpResponse('<h1>Hello World 😃</h1>')

  # resuponce objectを返している
  return returnedobject
