from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .rag_pipeline import run_query

    
def chat_view(request):
    user_question = None
    answer = None

    if request.method == "POST":
        user_question = request.POST.get('question')
        if user_question:
            answer, _ = run_query(user_question)

    return render(request, "chatbot/index.html", {
        "user_question": user_question,
        "answer": answer
    })


@csrf_exempt
def chat_api(request):
    if request.method == "POST":
        question = request.POST.get('question')
        if question:
            answer, _ = run_query(question)
            return JsonResponse({"answer": answer})
    return JsonResponse({"answer": "Sorry, no question received."})