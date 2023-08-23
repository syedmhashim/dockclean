import docker


def stop_all_running_containers(logger):
    print("Stopping all running containers.")
    client = docker.from_env()
    containers = client.containers.list()
    count = 0
    for container in containers:
        try:
            container.kill()
            logger.info(f"Stopped container -> {container.name}")
            count += 1
        except:
            logger.error(
                f"Exception occurred while stopping container -> {container.name}"
            )
    print(f"Total {count} running containers stopped.")


def remove_all_stopped_containers(logger):
    print("Removing all stopped containers.")
    client = docker.from_env()
    containers = client.containers.list(filters={"status": "exited"})
    count = 0
    for container in containers:
        try:
            container.remove()
            logger.info(f"Removed container -> {container.name}")
            count += 1
        except:
            logger.error(
                f"Exception occurred while removing container -> {container.name}"
            )
    print(f"Total {count} stopped containers removed.")


def remove_all_containers(logger):
    stop_all_running_containers(logger)
    remove_all_stopped_containers(logger)
