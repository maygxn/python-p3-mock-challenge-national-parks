    # initialized with a name, as a string
class NationalPark:
    all = []

    def __init__(self, name):
        self._name = name

    @property
    def name(self):
        return self._name
    
    @name.getter
    def name(self):
        return self._name
    
    @name.setter
    # return national_park's name, be a type of (str), length greater or equal to 3
    # should NOT be able to change after instantiated (need hasattr())
    def name(self, val):
        if isinstance(val, str) and 3 <= len(val) and not hasattr(self, 'name'):
            self._name = val
    
    def trips(self):
        # return list of all trips at particular national park
        # iterate through all trips
        # must be type Trip
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        # return UNIQUE list of all visitors a particular national park has welcomed
        # Visitor must be of type Visitor
        # need list(set()) = unique list
        return list(set([trip.visitor for trip in self.trips()]))

    def total_visits(self):
        # return total number of times a park has been visited
        # returns 0 if park has not been visited
        return len(self.trips())
    
    def best_visitor(self):
        # returns Visitor instance that has visited park the most
        # grab all trips for this park
        trips = self.trips()
        # returns None if park has no visitors
        if len(trips) == 0:
            return None
        # need list comprehension
        # create list of visitors for each trip to national park
        visitors = [trip.visitor for trip in trips]
        # count each visitor visits
        visitor_counts = {visitor: visitors.count(visitor) for visitor in visitors}
        # visitor max count
        best_visitor = max(visitor_counts, key=visitor_counts.get)
        return best_visitor

    # visitor_counts = {}
    # for trip in self.trips():
        # (if visitor key already exists)
    # if trip.visitor in visitor_counts:
        # (add to the value)
        # visitor_counts[trip.visitor] += 1
    # (if the visitor key does NOT exist)
    # else:
        # (create that key, and set it to 1)
        # visitor_counts[trip.visitor] = 1
    # use max to find the greatest value
    # return max(visitor counts, key=visitor_counts.get)
class Trip:
    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        # append trip to national park's trips list
        Trip.all.append(self)

    # return trip's start_date
    @property
    def start_date(self):
        return self._start_date
    
    @start_date.getter
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    # start_date must be type(str)
    # length greater or lequal to 7 characters
    # should BE ABLE to change after trip is instantiated
    def start_date(self, val):
        if isinstance(val, str) and len(val) >= 7:
            # recursion error add _
            self._start_date = val

    # return trip's end_date
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.getter
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    # end_date must be type(str)
    # length greater or equal to 7 characters
    # should BE ABLE to change after trip is instantiated
    def end_date(self, val):
        if isinstance(val, str) and len(val) >= 7:
            # recursion error add _
            self._end_date = val

class Visitor:
    all = []

    # initialize Visitor with a name
    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name
    
    @name.setter
    def name(self, val):
        # returns visitor's name, name = str, between 1 and 15 characters (inclusive)
        # BE ABLE to change after visitor is instantiated
        if isinstance(val, str) and 1 <= len(val) <= 15:
            self._name = val

    def trips(self):
        # return list of all trips for that visitor
        # trip must be type Trip
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        # return UNIQUE list of all parks that visitor has visited (need list(set()))
        # park must be type NationalPark
        return list(set(trip.national_park for trip in self.trips()))
    
    def total_visits_at_park(self, park):
        # need NationalPark object as argument
        # return total # of times visitor visited park passed in argument
        # returns 0 if visitor has never visited the park
        # see what trips match self and park
        return len([trip for trip in self.trips() if trip.national_park == park])