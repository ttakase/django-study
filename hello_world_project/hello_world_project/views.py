# djangoが用意しているレスポンスメソッド
# https://docs.djangoproject.com/en/3.1/ref/request-response/
from django.http import HttpResponse
from pathlib import Path
from django.views.generic import TemplateView

# request objectを受け取るのでrequestの記載が必要、文字列はなんでも良い
# functions based view
def helloworldfunction(request):
  returnedobject = HttpResponse('<h1>Hello World 😃</h1>')

  # resuponce objectを返している
  return returnedobject

def someview(request):
  print(Path())
  print('-----------')
  print(Path(__file__)) # 相対パスを返す
  print('-----------')
  print(Path(__file__).resolve) # 絶対パスを返す
  print('-----------')
  print(Path(__file__).resolve().parent.parent) # 親の親を表示

  return HttpResponse('someview check log')

# class based view
class HelloworldClass(TemplateView): # ()内でdjangoが準備しているTemplate継承をしている
  template_name = 'hello.html' # ファイルはどこに作成しても問題ないが、pathはsettingsのTEMPLATESのDIRSで設定する

