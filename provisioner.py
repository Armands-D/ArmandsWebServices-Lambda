import docker
from docker.models.images import Image
import os, shutil
from pathlib import Path
import typing

optional_dict_arg = lambda dic, condition: dic if condition else {}

class DockerBuildFiles():

  def __init__(self, build_folder: str, dockerfile: str) -> None:
    if not isinstance(build_folder, str):
      raise ValueError('build folder path must be a string')
    if not isinstance(dockerfile, str):
      raise ValueError('dockerfile path must be a string (relative to the build folder)')

    DockerBuildFiles._validateInitArgs(
      build_folder=build_folder,
      dockerfile=dockerfile,
    )
    self._build_folder_path = Path(build_folder)
    self._dockerfile_path = Path(self.getBuildFolderPath()) / Path(dockerfile)

  @staticmethod
  def _validateInitArgs(build_folder: str, dockerfile: str):

    build_folder_path = Path(build_folder)
    dockerfile_path = Path(dockerfile)
    if not build_folder_path.exists():
      raise FileExistsError(f"Template folder not found: default: {build_folder}")

    dockerfile_exists_in_build_folder = False
    dockerfile_path = Path(build_folder_path / dockerfile_path)
    dockerfile_exists_in_build_folder = dockerfile_path.exists() and dockerfile_path.is_file()

    if not dockerfile_exists_in_build_folder:
      raise FileExistsError(f"Dockerfile not found in build folder: {dockerfile_path}")

  def getDockerFilePath(self, relative: bool = True) -> str:
    if not relative:
      path = self._dockerfile_path
    else:
      path =self._dockerfile_path.relative_to(self._build_folder_path)

    return str(path)

  def setDockerFilePath(self, dockerfile):
    DockerBuildFiles._validateInitArgs(
      build_folder=str(self._build_folder_path),
      dockerfile=dockerfile,
    )
    self._dockerfile_path = Path(self._build_folder_path/dockerfile)

  def getBuildFolderPath(self) -> str:
    return str(self._build_folder_path)

  def setBuildFolderPath(self, build_folder):
    DockerBuildFiles._validateInitArgs(
      build_folder=build_folder,
      dockerfile=str(self.getDockerFilePath()),
    )
    self._build_folder_path = Path(build_folder)

class DockerClientWrapper():

  def __init__(self, client: docker.DockerClient):
    self.docker_client = client
    pass

  def build(self,
    build_files:DockerBuildFiles,
    name=None,
    tag=None
  ) -> tuple[Image, typing.Iterator[typing.Any]]:
    if not (isinstance(name, str) and isinstance(tag, str)):
      ValueError('Name and tag must be string values')

    full_tag = "" if name is None else name
    if name is not None:
      full_tag += "" if tag is None else f":{tag}"

    build_kwargs : dict[str, typing.Any] = {
      "path":build_files.getBuildFolderPath(),
      "dockerfile":build_files.getDockerFilePath(relative=True),
      **optional_dict_arg({'tag': full_tag}, tag)
    }

    image = self.docker_client.images.build(**build_kwargs)
    return image

  def run(self, image_name: str, tag=None):
    res = self.docker_client.containers.run(
      image=image_name,
      network_mode='host',
      tty=True,
      detach=True,
      remove=True,
      name='prov'
    )
    return res

class DockerTemplateProvider():

  def __init__(self, build_files: DockerBuildFiles) -> None:
    self.build_files = build_files
  
  def copyBuildTemplateTo(self, destination: str):
    # fails if path / files already exists, has flag to disable
    # https://docs.python.org/3/library/shutil.html#shutil.copytree 
    shutil.copytree(
      self.build_files.getBuildFolderPath(),
      destination,
      dirs_exist_ok=True,
    )

class Provisioner():

  def __init__(self,
    docker_build_files : DockerBuildFiles,
    docker_client: docker.DockerClient,
  ) -> None:

    if docker_client is None or not isinstance(docker_client, docker.DockerClient):
      raise ValueError('Docker client cannot be None')
    if docker_build_files is None or not isinstance(docker_build_files, DockerBuildFiles):
      raise ValueError('Docker client cannot be None')

    self.docker_client = docker_client
    self.docker_build_files = docker_build_files

  # def createInstance(self,):
  #   self.generateFolderStructure()
  #   self.copyTemplateFiles(self.docker_build_files)


  # def buildInstanceImage(self, path, dockerfile):
  #   image = self.docker_client.images.build(
  #     path=str(path),
  #     dockerfile=str(dockerfile),
  #     tag='provisioned',
  #   )
  #   print(image)
  #   return image

class FrontEnd():
  
  def createLambda(self, name, file):
    ...

  def updateLambda(self, name, file):
    ...
  
  def removeLambda(self, name):
    ...
  

if_not_exists_create_folder = lambda str_p : os.mkdir(str_p) if not Path(str_p).exists() else None

def main():
  _base_url_docker_default = 'unix://var/run/docker.sock'
  _default_template_build_folder = './ProvisionerTemplates'
  _default_template_dockerfile = 'lambda.dockerfile'
  _default_dst_build_folder = './LambdaInstances/1/moved'
  _default_dst_dockerfile = 'lambda.dockerfile'

  docker_client = docker.DockerClient(base_url=_base_url_docker_default)
  template_provider = DockerTemplateProvider(
    DockerBuildFiles(
      build_folder=_default_template_build_folder,
      dockerfile=_default_template_dockerfile,
  ))

  template_provider.copyBuildTemplateTo(_default_dst_build_folder)
  # Copy user file to build folder
  ...

# TODO:
# - Figure out docker debugging
# - Make first container communication
#   - Fix rabbitMQ connection error?
# - Figue out file upload
#   - Filestream?
#   - How do website upload files?
# - Lambda Config
#   - Config class for defining, file location, source file name,
# - How to communicate with docker network without host network

if __name__ == '__main__':
  main()

# docker container stop prov &&  docker container rm prov