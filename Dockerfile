FROM python:3.5
ENV PYTHONUNBUFFERED 1

# install psql
RUN apt-get update && apt-get install -y postgresql-client

# geo support
RUN apt-get update && apt-get install -y binutils libproj-dev gdal-bin
RUN wget -P /tmp/ http://download.osgeo.org/geos/geos-3.4.2.tar.bz2; \
	cd /tmp; tar xjf geos-3.4.2.tar.bz2; cd geos-3.4.2; ./configure; make; make install; cd /tmp

RUN wget -P /tmp/ http://download.osgeo.org/proj/proj-4.9.1.tar.gz; \
	wget -P /tmp/ http://download.osgeo.org/proj/proj-datumgrid-1.5.tar.gz; \
	cd /tmp; tar xzf proj-4.9.1.tar.gz; \
	cd proj-4.9.1/nad; \
	tar xzf ../../proj-datumgrid-1.5.tar.gz; cd ..; \
	./configure; make; make install; cd /tmp

RUN wget -P /tmp/ http://download.osgeo.org/gdal/1.11.2/gdal-1.11.2.tar.gz; \
	cd /tmp; tar xzf gdal-1.11.2.tar.gz; \
	cd gdal-1.11.2; \
	./configure; make; make install; cd /tmp
RUN ldconfig

RUN mkdir /code
COPY . /code/
WORKDIR /code

RUN pip install --no-cache-dir -r /code/project/requirements.txt
EXPOSE 8000

# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]