# DevOps & System Administration Code-Challenge
## Requirements
### Application

Write a simple containerized OCI-compatible Ruby/Python/Java/JVM-compatible/C web server. The application should connect to an open-source SQL database. As a recommendation, don’t use microservices.

The database content can be anything you like and additionally, it must contain a timestamp column.

Depending on the requested web endpoint:

- If it’s a GET on /greetings, it shall respond with a simple text with the total number of rows in the DB and the last three rows' content.
- Otherwise, if it’s a POST on /messages, it should add a new row, using some default values and shall return the content of the newly added row.
- The / route should temporarily redirect to the /greetings route.
- All operations should return the appropriate HTTP status codes.
- (Optional) If the requested data contains a date-time previous to the current date, the application should show all matching rows limited to 10. If the date-time is after the current date, it should return a response message explaining the particular situation.

Server:

- Create a Vagrant virtual machine running a current Debian or Ubuntu Linux vanilla image.
- The VM shall be auto-provisioned using Ansible and configured with the following:
  - Docker Engine and Docker Compose.
  - The application shall be executed by Docker Compose using the file definition.
  - The database can run inside the same VM as a container (preferred) or as a network-attached VM (optional). PostgreSQL or MySQL/MariaDB database server shall be used.
  - The application shall run on a two-replica deployment and a load balancer or reverse proxy accessible from the VM host.
  - The application and services should be accessible by dynamic domain names.
  - An appropriately configured firewall.

The application building and deployment can be done either using Ansible or directly using Vagrant.

Expected outcome:

- The application source code.
- The Vagrantfile, Docker Compose file & Dockerfile.
- The Ansible playbook and roles.
- Idempotent and declarative Vagrant and Ansible.
- Completely reproducible setup and configuration.

You can host this using a cloud Git repository service.

## Run solution
In the root project directory run:

`vagrant up`

This command will download the Ubuntu image, provision the VM using Ansible, start the VM and the Python app.
