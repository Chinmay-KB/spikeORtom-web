FROM pytorch/pytorch:latest

# This is so we can do print() from Python without having to flush stdout afterward.
ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y git

# Removed  --cuda_ext
RUN git clone https://github.com/NVIDIA/apex.git
RUN git checkout 700d6825e205732c1d6be511306ca4e595297070 
RUN cd apex
RUN python setup.py install --cpp_ext

RUN pip install transformers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

# Expose the flask port
EXPOSE 5000

CMD [ 'python', './app.py' ]
