from django.shortcuts import render


def calculate_PPC(request):
    # Инициализация переменных значениями по умолчанию
    F2 = E2 = F3 = E3 = F4 = E4 = F5 = E5 = A2 = B2 = C2 = D2 = 0
    result = None
    error = None

    if request.method == 'POST':
        try:
            F2 = float(request.POST.get('F2', 0))
            E2 = float(request.POST.get('E2', 0))
            F3 = float(request.POST.get('F3', 0))
            E3 = float(request.POST.get('E3', 0))
            F4 = float(request.POST.get('F4', 0))
            E4 = float(request.POST.get('E4', 0))
            F5 = float(request.POST.get('F5', 0))
            E5 = float(request.POST.get('E5', 0))
            A2 = float(request.POST.get('A2', 0))
            B2 = float(request.POST.get('B2', 0))
            C2 = float(request.POST.get('C2', 0))
            D2 = float(request.POST.get('D2', 0))

            # Вычисление результата
            result = (F2 * E2 + E3 * F3 + E4 * F4 + F5 * E5 + (A2 + B2 + C2)) * D2

        except ValueError:
            error = 'Ошибка: вводите только числа, через точку'

    # Передаем в шаблон значения, чтобы они отображались в полях
    return render(request, 'calculate.html', {
        'F2': F2 if F2 != 0 else '',
        'E2': E2 if E2 != 0 else '',
        'F3': F3 if F3 != 0 else '',
        'E3': E3 if E3 != 0 else '',
        'F4': F4 if F4 != 0 else '',
        'E4': E4 if E4 != 0 else '',
        'F5': F5 if F5 != 0 else '',
        'E5': E5 if E5 != 0 else '',
        'A2': A2 if A2 != 0 else '',
        'B2': B2 if B2 != 0 else '',
        'C2': C2 if C2 != 0 else '',
        'D2': D2 if D2 != 0 else '',
        'result': result,
        'error': error,
    })
