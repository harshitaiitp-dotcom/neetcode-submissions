class UndergroundSystem:

    def __init__(self):
        # Maps customer id to (stationName, time) when they check in
        self.check_ins = {}
        
        # Maps (startStation, endStation) to [total_duration, count_trips]
        self.journey_data = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.check_ins.pop(id)
        route = (start_station, stationName)
        duration = t - start_time
        
        if route not in self.journey_data:
            self.journey_data[route] = [0, 0] # [total_time, total_trips]
            
        self.journey_data[route][0] += duration
        self.journey_data[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total_time, total_trips = self.journey_data[(startStation, endStation)]
        return total_time / total_trips