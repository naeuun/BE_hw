from django.shortcuts import render
import random

# Create your views here.

app_name='password'

def index(request):
    
    return render(request, 'password/index.html')

def password_generator(request):
    len=request.GET.get('len')
    upper = "upper" in request.GET 
    lower = "lower" in request.GET
    digits = "digits" in request.GET
    special = "special" in request.GET
    
    #길이가 입력되지 않았을 경우, error1.html 렌더링 
    if len=="": 
        return render(request, 'password/error1.html')
    
    #길이가 입력되었을 경우, 정수형태로 바꿔줌
    len=int(len)
    
    #입력된 길이가 음수이 경우, error2. html 렌더링 
    if len<0: 
        return render(request, 'password/error2.html')
    
    #체크박스를 모두 선택하지 않았을 경우, error3.html 렌더링 
    if not any([upper, lower, digits, special]):  
        return render(request, 'password/error3.html')

    
    # 체크 박스에서 선택한 속성이 True일 경우 check_chars에 해당 문자열이 추가됨 
    check_chars = ""
    if upper:
        check_chars += "ABCDEFGHIJKLMNOPCRSTUVWXYZ"
    if lower:
        check_chars += "abcdefghijklmnopqrstuvwxyz"
    if digits:
        check_chars += "0123456789"
    if special:
        check_chars += "!@#$%^&*"
    
    #random.choices 이용하여 k값을 받아온 문자열 길이로 지정해주고, 
    #join을 이용해 문자열을 결합함 (앞의 세퍼레이터를 ""로 주면 이어지게 결합할 수 있음)
    password="".join(random.choices(check_chars, k=len))

    #변수가 하나밖에 없긴 하지만, 스터디에서 배웠으니 context로 뺐음!
    context={
        'password':password
    }
    
    return render(request, 'password/result.html', context)
