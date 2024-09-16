FROM python

RUN apt update

RUN pip install djangorestframework django-cors-headers

RUN pip install scikit-learn==1.4.1.post1
RUN pip install pandas==2.1.2
RUN pip install joblib==1.3.2

WORKDIR /app

COPY . /app

EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]