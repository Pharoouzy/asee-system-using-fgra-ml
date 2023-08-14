FROM jupyter/minimal-notebook:latest

WORKDIR /home/jovyan/project

COPY ../.. /home/jovyan/project

RUN pip install -r requirements.txt --no-cache-dir

CMD ["start-notebook.sh", "--NotebookApp.token=''", "--NotebookApp.password=''", "--NotebookApp.notebook_dir=/home/jovyan/project/notebooks"]
