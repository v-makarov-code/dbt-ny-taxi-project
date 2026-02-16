import requests

# Это самая стабильная ссылка на данный момент
url = "https://raw.githubusercontent.com/DataTalksClub/data-engineering-zoomcamp/main/04-analytics-engineering/taxi_rides_ny/seeds/payment_type_lookup.csv"

filename = "payment_type_lookup.csv"

try:
    r = requests.get(url, timeout=10)
    r.raise_for_status()

    with open(filename, "wb") as f:
        f.write(r.content)

    print(f"Файл сохранён: {filename}")
    print(f"Размер: {len(r.content) / 1024:.1f} KB")

except Exception as e:
    print("Ошибка:", e)

