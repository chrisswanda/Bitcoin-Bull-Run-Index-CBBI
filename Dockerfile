FROM python:3.11.5-alpine 

WORKDIR /cbbi
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY . ./

CMD python cbbi.py