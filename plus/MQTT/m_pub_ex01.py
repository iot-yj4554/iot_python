from m_pub import publish

host = 'localhost'

publish(host, 'iot/user1/temp', 5)
publish(host, 'iot/user1/humi', 7)
publish(host, 'iot/user1/illu', 10)
publish(host, 'iot/user1/dust', 12)
