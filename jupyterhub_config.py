c.JupyterHub.spawner_class = 'jupyterhub.spawner.LocalProcessSpawner'




import sys
c.Authenticator.whitelist = {'ian', 'ianvie'}
c.Authenticator.admin_users = {'ian'}
c.JupyterHub.admin_access = True
c.LocalAuthenticator.create_system_users = True
c.JupyterHub.spawner_class='dockerspawner.SystemUserSpawner'
c.DockerSpawner.container_image = 'compmodels/systemuser'

#c.DockerSpawner.tls_cert = os.environ['DOCKER_TLS_CERT']
#c.DockerSpawner.tls_key = os.environ['DOCKER_TLS_KEY']
c.DockerSpawner.remove_containers = True
#c.DockerSpawner.volumes = {os.environ['NBGRADER_EXCHANGE']: os.environ['NBGRADER_EXCHANGE']}
#c.DockerSpawner.extra_host_config = {'mem_limit': '1g'}
c.DockerSpawner.container_ip = "0.0.0.0"



c.JupyterHub.proxy_api_ip = '0.0.0.0'
c.JupyterHub.hub_ip = '0.0.0.0'
#c.DockerSpawner.hub_ip_connect = os.environ['HUB_IP']
