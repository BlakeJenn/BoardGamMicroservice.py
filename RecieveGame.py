import requests
import xml.etree.ElementTree as ET
import zmq


def text_num_split(item):
    """
    Turns an input into a list of one number string and one alpha string. Number
    must come first.

    :param item: a string in the form of a number and string (ex: '12345full_image')

    :return:     a list with a numeric string and alpha string (ex: ['12345', 'full_image'])
    """
    for index, letter in enumerate(item, 0):
        if letter.isalpha():
            return [item[:index], item[index:]]


def parse_xml(id, image_type):
    """
    Sends a link to either a full image or thumbnail of a
    board game based on input.

    :param id:         a number string indicating the id of the board game
    :param image_type: a string indicating 'full_image' or 'thumbnail'

    :return:           a link to the specified board game's thumbnail or full image
    """
    xml_url = f'https://boardgamegeek.com/xmlapi/boardgame/{int(id)}'

    response = requests.get(xml_url)

    if response.status_code == 200:

        url_root = ET.fromstring(response.content)

        if image_type == 'full_image':
            image_tag = url_root.find('.//image')
        else:
            image_tag = url_root.find('.//thumbnail')

        if image_tag is not None:
            socket.send_string(image_tag.text)


context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")

while True:
    items = text_num_split(socket.recv_string())
    parse_xml(items[0], items[1])
