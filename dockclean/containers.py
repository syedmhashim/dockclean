import docker


def stop_all_running_containers(logger):
    logger.info("Stopping all running containers.")
    client = docker.from_env()
    containers = client.containers.list()
    count = 0
    for container in containers:
        try:
            container.kill()
            logger.debug(f"Stopped container -> {container.name}")
            count += 1
        except:
            logger.error(
                f"Exception occurred while stopping container -> {container.name}"
            )
    logger.info(f"Total {count} running containers stopped.")


def remove_all_stopped_containers(logger):
    logger.info("Removing all stopped containers.")

    client = docker.from_env()
    deleted_containers = client.containers.prune()

    containers = deleted_containers['ContainersDeleted']

    if containers is not None:
        [logger.debug(f"Removed container -> {container}") for container in containers]
        logger.info(f"Total {len(containers)} stopped containers removed.")

    else:
        logger.info(f"There isn't any stopped container!")

    logger.info(
        f"The space reclaimed after removing all stopped containers is {deleted_containers['ContainersDeleted']}"
    )


def remove_all_containers(logger):
    stop_all_running_containers(logger)
    remove_all_stopped_containers(logger)
