#!/bin/bash

cp /code/postgresql.conf /etc/postgresql/9.5/main/postgresql.conf
cp /code/pg_hba.conf /etc/postgresql/9.5/main/pg_hba.conf

/etc/init.d/postgresql start

