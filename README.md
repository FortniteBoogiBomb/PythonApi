# OAS specification with cpu
Following this specification will allow us to create a directory hierarchy of python files or modules that we can reference within a yaml file. This makes our applications clean and readily transferable. 

# OAS 
[Defining OAS 3.0](https://swagger.io/docs/specification/basic-structure/)
[Defining OAS 2.0](https://swagger.io/docs/specification/2-0/basic-structure/)
This documentation walks you through the basics of your YAML file, we will be using YAML exculsively, however if you want to use JSON feel free. 

# connexion
To conform to OAS standards we will be using connexion to handle the HTTP requests. The documentation is found here:
[connexion docs](https://connexion.readthedocs.io/en/latest/)

# start
`make docker-all`
now remember in order to stop the service use `make docker-stop` in a seperate terminal. This should work seamless. 
Look in os_pack there are two files. Looks at them. Redfine the operationid in the yaml file to point to the cpu_2020.py file.
