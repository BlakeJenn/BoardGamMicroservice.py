# BoardGamMicroservice.py
A microservice for a colleague's board game suggestion program. This service uses ZMQ
to send a board games id and image type (full image or thumbnail) and returns that
image type of the specified board game to be used as a visual aid for the
overall program.

Instructions for REQUEST:

1. Import ZMQ

2. Set up correct socket and port:
   
    context = zmq.Context()
   
    socket = context.socket(zmq.REQ)
   
    socket.connect("tcp://localhost:5555")

3. Send request via socket.send_string(combined)

  "Combined" is a string of the id and image type combined
  
   ( Ex: print(request_game(187645, 'full_image')) )

Instructions for RECIEVE:

1. Recieve through same set up as request, with socket.recv_string()
   
   Service will return a link to the full image or thumbnail

Example Return:

https://cf.geekdo-images.com/7SrPNGBKg9IIsP4UQpOi8g__original/img/GKueTbkCk2Ramf6ai8mDj-BP6cI=/0x0/filters:format(jpeg)/pic4325841.jpg

<img width="654" alt="Screenshot 2023-11-20 at 12 21 15 AM" src="https://github.com/BlakeJenn/BoardGamMicroservice.py/assets/122320850/94de9702-56a1-48ba-b62c-073b085dacc4">
