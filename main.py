import krpc

conn = krpc.connect(
    name='KSP',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

print(conn.krpc.get_status().version)

vessel = conn.space_center.active_vessel
flight = vessel.flight()

altitude = conn.add_stream(getattr, flight, 'mean_altitude')

while altitude() < 1000:
    pass

print('Altitude reached 1000m')