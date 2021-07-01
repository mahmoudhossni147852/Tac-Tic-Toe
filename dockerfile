FROM python

ADD human-vs-computer.py /

RUN pip install pystrich

CMD ["python","./human-vs-computer.py"]
