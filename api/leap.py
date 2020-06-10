# This is the main API that users interact with LEAP. Users
# will create an instance of the LEAP class and can either
# set their own user defined functions or use one of the func-
# tions available in LEAP

from abc import ABC, abstractmethod
import json
import grpc
import proto as pb


class LocalCloudRequest:
    def __init__(self):
        self.req = None


# An abstract class that represents Leap.
class Leap(ABC):

    # Constructor that takes in a code representing one of
    # the available algorithms in Leap.
    #
    # leap_function: The algorithm that a user wants to rub
    #                in Leap.
    def __init__(self, leap_function):
        self.leap_function = leap_function

    # Gets the result of performing the selected algorithm
    # on the filtered data.
    def get_result(self):
        request = self._create_computation_request()
            
        compute_stub = self._get_compute_stub()

        # Computed remotely
        result = compute_stub.Compute(request, None)
        
        result = json.loads(result.response)
        return result

    # Uses protobuf to create a computation request.
    def _create_computation_request(self):
        request = self._create_request_obj()

        req = self.leap_function.create_request()
        request.req = json.dumps(req)
        if hasattr(self.leap_function, 'algo_code'):
            request.algo_code = self.leap_function.algo_code
        request.leap_type = self.leap_function.leap_type
        return request

    @abstractmethod
    def _get_compute_stub(self):
        pass
    
    @abstractmethod
    def _create_request_obj(self):
        pass
    

# Extends the base Leap class and mocks Leap being run in a
# distributed environment. This class is useful for debugging.
class LocalLeap(Leap):

    # Constructor
    #
    # leap_function: An algorithm to be run in Leap.
    # cloud: An instance of a class mocking the cloud.
    def __init__(self, leap_function, cloud):
        super().__init__(leap_function)
        self.cloud = cloud

    # Returns a stub that mocks sending a request to the
    # cloud.
    def _get_compute_stub(self):
        return self.cloud

    # Creates a request for a local leap computation.
    def _create_request_obj(self):
        request = LocalCloudRequest()
        return request 


# Extends the base Leap class and actually runs the Leap
# algorithms in a distributed environment.
class DistributedLeap(Leap):

    # Constructor
    #
    # leap_function: An algorithm to be run in Leap.
    def __init__(self, leap_function, coord_ip_port, auth_token):
        super().__init__(leap_function)
        self.coord_ip_port = coord_ip_port
        self.auth_token = auth_token

    # Gets the result of performing the selected algorithm
    # on the filtered data.
    def get_result(self, sites):
        request = self._create_computation_request(sites)

        compute_stub = self._get_compute_stub()

        # Computed remotely
        metadata = []
        metadata.append(('authorization', self.auth_token))
        result = compute_stub.Compute(request, None, metadata=metadata)

        result = json.loads(result.response)
        return result

    # Uses protobuf to create a computation request.
    def _create_computation_request(self, sites):
        request = self._create_request_obj()

        req = self.leap_function.create_request()
        request.req = json.dumps(req)

        if hasattr(self.leap_function, 'algo_code'):
            request.algo_code = self.leap_function.algo_code
        request.leap_type = self.leap_function.leap_type
        request.sites.extend(sites)
        return request

    # Gets the stub from the cloud grpc service. This stub
    # is used to send messages to the cloud algos.
    def _get_compute_stub(self):
        # TODO: Don't harcode ip address
        channel = grpc.insecure_channel(self.coord_ip_port)
        stub = pb.coordinator_pb2_grpc.CoordinatorStub(channel)
        return stub

    # Creates a protobuf request object for a Leap computation
    def _create_request_obj(self):
        request = pb.computation_msgs_pb2.ComputeRequest()
        return request
