from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def word_count(request):
    return render(request, 'word_count.html')

def hello(request):
    name=request.GET['name']
    return render(request, 'hello.html',{'name':name})


def result(request):
    entered_text=request.GET['fulltext']
    word_list=entered_text.split()

    count_all_words=len(word_list) # split 된 word_list 이용해서 단어 수 세기 
    count_text=len(entered_text)  # fulltext 받아온 entered_text 이용해서서 모든 글자 수 세기
    count_no_space=len(entered_text.replace(" ","")) # 공백을 지우고 다시 길이 세기 
    
    word_dictionary={}
    
    for word in word_list:
        if word in word_dictionary:
            word_dictionary[word]+=1
        else:
            word_dictionary[word]=1
        
    max_count=max(word_dictionary.values()) # 딕셔너리의 단어 횟수가 가장 많을 때 값 찾기
    
    max_count_words=[] # 단어 최대 등장 횟수와 같은 횟수를 가지고 있는 단어를 저장하기 위한 리스트
    
    for word, count in word_dictionary.items(): # 리스트에 최대 횟수인 단어 넣기 
        if count==max_count:
            max_count_words.append(word) 
            
    return render(request, 'result.html',{'alltext':entered_text, 'dictionary':word_dictionary.items(),
                                          'count_all_words':count_all_words,'count_text':count_text,
                                          'count_no_space':count_no_space, 'max_count_words':max_count_words, 'max_count':max_count})