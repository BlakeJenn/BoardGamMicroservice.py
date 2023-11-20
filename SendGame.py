import zmq

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")


def request_game(id, image_type):
    """
    Function to access xml microservice and receive an
    image based on its id and type.

    :param id:         an integer indicating the id of a board game
    :param image_type: a string indicating 'full_image' or 'thumbnail'

    :return:           image url of the indicated board game
    """
    combined = str(id) + image_type
    socket.send_string(combined)

    final = socket.recv_string()
    return final
