# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import message_pb2 as message__pb2


class SiteCoordinatorStub(object):
  """To compile the protobuf to Go run the following inside the protoBuf folder:
  protoc -I=. --go_out=plugins=grpc:.  message.proto

  To compile the protobuf to Python run the following inside the protoBuf folder:
  python -m grpc_tools.protoc -I=. --python_out=../cloud-algos/ --grpc_python_out=../cloud-algos/ message.proto

  RPC service at the coordinator that will handle requests from sites
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterSiteAlgo = channel.unary_unary(
        '/protoBuf.SiteCoordinator/RegisterSiteAlgo',
        request_serializer=message__pb2.SiteAlgoRegReq.SerializeToString,
        response_deserializer=message__pb2.SiteAlgoRegRes.FromString,
        )


class SiteCoordinatorServicer(object):
  """To compile the protobuf to Go run the following inside the protoBuf folder:
  protoc -I=. --go_out=plugins=grpc:.  message.proto

  To compile the protobuf to Python run the following inside the protoBuf folder:
  python -m grpc_tools.protoc -I=. --python_out=../cloud-algos/ --grpc_python_out=../cloud-algos/ message.proto

  RPC service at the coordinator that will handle requests from sites
  """

  def RegisterSiteAlgo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_SiteCoordinatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterSiteAlgo': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterSiteAlgo,
          request_deserializer=message__pb2.SiteAlgoRegReq.FromString,
          response_serializer=message__pb2.SiteAlgoRegRes.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protoBuf.SiteCoordinator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CloudCoordinatorStub(object):
  """RPC service at the coordinator that will handle requests from cloud algorithms
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.RegisterCloudAlgo = channel.unary_unary(
        '/protoBuf.CloudCoordinator/RegisterCloudAlgo',
        request_serializer=message__pb2.CloudAlgoRegReq.SerializeToString,
        response_deserializer=message__pb2.CloudAlgoRegRes.FromString,
        )
    self.AlgoRequest = channel.unary_unary(
        '/protoBuf.CloudCoordinator/AlgoRequest',
        request_serializer=message__pb2.ComputeRequest.SerializeToString,
        response_deserializer=message__pb2.ComputeResponses.FromString,
        )


class CloudCoordinatorServicer(object):
  """RPC service at the coordinator that will handle requests from cloud algorithms
  """

  def RegisterCloudAlgo(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def AlgoRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CloudCoordinatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'RegisterCloudAlgo': grpc.unary_unary_rpc_method_handler(
          servicer.RegisterCloudAlgo,
          request_deserializer=message__pb2.CloudAlgoRegReq.FromString,
          response_serializer=message__pb2.CloudAlgoRegRes.SerializeToString,
      ),
      'AlgoRequest': grpc.unary_unary_rpc_method_handler(
          servicer.AlgoRequest,
          request_deserializer=message__pb2.ComputeRequest.FromString,
          response_serializer=message__pb2.ComputeResponses.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protoBuf.CloudCoordinator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class AlgoConnectorStub(object):
  """RPC service at a site connector that will handle requests from site algorithms
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """


class AlgoConnectorServicer(object):
  """RPC service at a site connector that will handle requests from site algorithms
  """


def add_AlgoConnectorServicer_to_server(servicer, server):
  rpc_method_handlers = {
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protoBuf.AlgoConnector', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))


class CoordinatorConnectorStub(object):
  """RPC service at a site connector that will handle requests from coordinator
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.AlgoRequest = channel.unary_unary(
        '/protoBuf.CoordinatorConnector/AlgoRequest',
        request_serializer=message__pb2.ComputeRequest.SerializeToString,
        response_deserializer=message__pb2.ComputeResponse.FromString,
        )


class CoordinatorConnectorServicer(object):
  """RPC service at a site connector that will handle requests from coordinator
  """

  def AlgoRequest(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CoordinatorConnectorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'AlgoRequest': grpc.unary_unary_rpc_method_handler(
          servicer.AlgoRequest,
          request_deserializer=message__pb2.ComputeRequest.FromString,
          response_serializer=message__pb2.ComputeResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'protoBuf.CoordinatorConnector', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))