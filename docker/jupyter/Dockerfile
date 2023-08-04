FROM jupyter/minimal-notebook

COPY . /home/umar/notebooks

WORKDIR /home/umar/notebooks

RUN pip install --trusted-host pypi.python.org -r requirements.txt

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''"]
