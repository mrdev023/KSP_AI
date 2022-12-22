import krpc

conn = krpc.connect(
    name='KSP',
    address='127.0.0.1',
    rpc_port=50000, stream_port=50001)

print(conn.krpc.get_status().version)

vessel = conn.space_center.active_vessel
flight = vessel.flight()
control = vessel.control

control.rcs = True
control.sas = True

control.activate_next_stage()

control.throttle = 1.0

while flight.mean_altitude < 10000:
    stage = control.current_stage - 1
    resources = vessel.resources_in_decouple_stage(stage, False)
    print("Stage: " + str(stage))
    print("Altitude: " + str(flight.mean_altitude))
    print("Resources:")
    for name in resources.names:
        print(name + ": " + str(resources.amount(name)))
    if resources.amount('LiquidFuel') == 0.0:
        control.activate_next_stage()

control.throttle = 0.0