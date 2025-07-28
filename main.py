import requests

def download_html(url, output_file):
    try:
        # Имитация запроса от браузера
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }

        # Получение HTML
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Проверка на ошибки HTTP

        # Сохранение в файл
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(response.text)

        print(f"HTML успешно сохранен в {output_file}")

    except Exception as e:
        print(f"Ошибка: {e}")

# Пример использования
download_html('https://speedrun.pw/vtop/?yclid=9111225529503318015', 'page.html')