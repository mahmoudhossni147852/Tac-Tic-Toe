FROM python

ADD human-vs-computer.py /

RUN pip install pyStrich

CMD ["python","./human-vs-computer.py"]
