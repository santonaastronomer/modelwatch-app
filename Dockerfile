FROM python:3.7

RUN pip install fastapi uvicorn mangum pydantic jinja2

EXPOSE 8080

COPY ./modelwatch_app /modelwatch_app
COPY ./modelwatch_app/static /static
COPY ./modelwatch_app/routers /routers
COPY ./modelwatch_app/templates /templates

CMD ["uvicorn", "modelwatch_app.main:app", "--host", "0.0.0.0", "--port", "8080"]
