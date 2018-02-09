
{
    payload: {
                    type: status_update
                    data: { 
                            battery_info: {
                                            voltage:12.4
                                            consumption: 20
                                            mAh_remaining: 3000
                                          },
                            location:      {
                                            latitude: 24.333312,
                                            longitude: 55.1212212,
                                            altitude: 173
                                        },
                            velocity:       {
                                            x:2
                                            y:0.2
                                            z:0.1
                                        },
                            connection: "None",
                            current_action: { 
                                            "name": "searching",
                                            "data": { 
                                                        "percent_complete" : "34%",
                                                        "search_area" : [(lat,long), (lat,long)],
                                                     }
                        }          
              },
    "sender": "uas-321",
    "to": "server",
    "type": "drone"
}


Drone Payload

type: 
    status_update:
        gives update about the current status of the drone, includes everything
    event:
        Reports a specific event, such as human found, critical battery, action changed,
            human_found_event:
                event_desc: "Human Found"
                location: location_object
                picture_id: 
            critical_battery_event:
                battery: battery_data_object
                location: location_object
            lost_connection_event:
                location: location_object
    action:
        RTL:
            the drone comes back when this is issued
        upload_mission:
            a new mission is added to the drone.
        change_mission:
            The mission has changed and a new one is uploaded!
        execute_mission: 
            The mission is executed
    get_drone_info
        gives information about the drone that was polled for
    get_all_connected_drones
        gives a list of connected drones.
        
        
                
    