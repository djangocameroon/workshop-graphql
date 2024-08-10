import uuid


def generate_uuid():
    """
    Function to generate a string UUID

    :return:
    """
    return uuid.uuid4().hex
