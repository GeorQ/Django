from collections import Counter

from django.shortcuts import render_to_response

# Для отладки механизма ab-тестирования используйте эти счетчики
# в качестве хранилища количества показов и количества переходов.
# но помните, что в реальных проектах так не стоит делать
# так как при перезапуске приложения они обнулятся
counter_show = Counter()
counter_click = Counter()


def index(request):
    # Реализуйте логику подсчета количества переходов с лендига по GET параметру from-landing
    state = request.GET.get("from-landing")
    if state is None:
        print(counter_click)
        return render_to_response('index.html')
    else:
        counter_click[state] += 1
        print(counter_click)
        return render_to_response('index.html')


def landing(request):
    # Реализуйте дополнительное отображение по шаблону app/landing_alternate.html
    # в зависимости от GET параметра ab-test-arg
    # который может принимать значения original и test
    # Так же реализуйте логику подсчета количества показов

    typeof = request.GET.get("ab-test-arg", "original")
    if typeof == "test":
        counter_show["test"] += 1
        print(counter_show)
        return render_to_response('landing_alternate.html')
    elif typeof == "original":
        counter_show["original"] += 1
        print(counter_show)
        return render_to_response('landing.html')


def stats(request):
    # Реализуйте логику подсчета отношения количества переходов к количеству показов страницы
    # Чтобы отличить с какой версии лендинга был переход
    # проверяйте GET параметр marker который может принимать значения test и original
    # Для вывода результат передайте в следующем формате:
    if counter_show["test"] == 0:
        test_ratio = 0
    else:
        test_ratio = counter_click["test"] / counter_show["test"]

    if counter_show["original"] == 0:
        original_ratio = 0
    else:
        original_ratio = counter_click["original"] / counter_show["original"]

    return render_to_response('stats.html', context={
        'test_conversion': test_ratio,
        'original_conversion': original_ratio,
    })
