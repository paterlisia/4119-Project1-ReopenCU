# ReopenCU health check process - Socket implementation

An implementation of a client/server application with TCP, UDP to model the health check process

## Four classes as total
- src
    - UDP
        - UDPclient.py
        - UDPserver.py
    - TCP
        - TCPclient.py
        - TCPserver.py

## Implementation details
*Have you experienced any COVID-19 symptoms in the past 14 days?*

*Have you been in close contact with anyone who has tested positive for COVID-19 in the past 14 days*

*Have you tested positive for COVID-19 in the past 14 days?*

After clients respond __Yes__ or __No__, the server respond __Green Pass__ or __Red Pass__.