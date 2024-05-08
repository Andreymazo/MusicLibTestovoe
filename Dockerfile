FROM python:3.10.5
RUN pip install --root-user-action=ignore 
ENV PIP_ROOT_USER_ACTION=ignore
WORKDIR /musiclib
EXPOSE 8000
COPY . /musiclib
# COPY ./requirements.txt .
# COPY musiclib/requirements.txt .
