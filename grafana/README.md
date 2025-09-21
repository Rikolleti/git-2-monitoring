# Обязательные задания
## Задание 1
Используя директорию help внутри этого домашнего задания, запустите связку prometheus-grafana.
Зайдите в веб-интерфейс grafana, используя авторизационные данные, указанные в манифесте docker-compose.
Подключите поднятый вами prometheus, как источник данных.
Решение домашнего задания — скриншот веб-интерфейса grafana со списком подключенных Datasource.

Ответ:
<img width="1499" height="697" alt="Снимок экрана 2025-09-21 в 19 27 59" src="https://github.com/user-attachments/assets/6101965c-b9d6-4b2c-8fb5-634ea26c5c43" />



## Задание 2
Изучите самостоятельно ресурсы:
1. PromQL tutorial for beginners and humans.
2. Understanding Machine CPU usage.
3. Introduction to PromQL, the Prometheus query language.

Создайте Dashboard и в ней создайте Panels:

1. утилизация CPU для nodeexporter (в процентах, 100-idle);
2. CPULA 1/5/15;
3. количество свободной оперативной памяти;
4. количество места на файловой системе.

Для решения этого задания приведите promql-запросы для выдачи этих метрик, а также скриншот получившейся Dashboard.

Ответ:
1. "100 - (avg by (instance) (rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)".
2. node_load1/node_load5/node_load15
3. node_memory_MemAvailable_bytes / 1024 / 1024 (в мегабайтах)
4. node_filesystem_free_bytes{fstype!~"tmpfs|overlay"} / 1024 / 1024 (в мегабайтах)

<img width="1499" height="697" alt="Снимок экрана 2025-09-21 в 19 30 51" src="https://github.com/user-attachments/assets/1541541b-c678-42d8-b00e-1cbfcfb94425" />


## Задание 3
Создайте для каждой Dashboard подходящее правило alert — можно обратиться к первой лекции в блоке «Мониторинг».
В качестве решения задания приведите скриншот вашей итоговой Dashboard.

Ответ:
<img width="1499" height="697" alt="Снимок экрана 2025-09-21 в 19 42 22" src="https://github.com/user-attachments/assets/b592f9d8-bcf6-4d2b-ae8f-f46828630ec5" />


## Задание 4
1. Сохраните ваш Dashboard.Для этого перейдите в настройки Dashboard, выберите в боковом меню «JSON MODEL». Далее скопируйте отображаемое json-содержимое в отдельный файл и сохраните его.
2. В качестве решения задания приведите листинг этого файла.
