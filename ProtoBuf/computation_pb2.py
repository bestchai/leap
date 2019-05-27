# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: computation.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import any_pb2 as google_dot_protobuf_dot_any__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='computation.proto',
  package='protoBuf',
  syntax='proto3',
  serialized_options=None,
  serialized_pb=_b('\n\x11\x63omputation.proto\x12\x08protoBuf\x1a\x19google/protobuf/any.proto\"D\n\x0e\x43omputeRequest\x12\x0f\n\x07\x61lgo_id\x18\x01 \x01(\x05\x12!\n\x03req\x18\x02 \x01(\x0b\x32\x14.google.protobuf.Any\"9\n\x0f\x43omputeResponse\x12&\n\x08response\x18\x01 \x01(\x0b\x32\x14.google.protobuf.Any\"@\n\x10\x43omputeResponses\x12,\n\tresponses\x18\x01 \x03(\x0b\x32\x19.protoBuf.ComputeResponse\"\x1a\n\x0bIntResponse\x12\x0b\n\x03val\x18\x01 \x01(\x05\"U\n\x05Query\x12\x10\n\x08operator\x18\x01 \x01(\t\x12\r\n\x05\x66ield\x18\x02 \x01(\t\x12\x14\n\x0cstring_value\x18\x03 \x01(\t\x12\x15\n\rnumeric_value\x18\x04 \x01(\x05\"\xc1\x01\n\x07Patient\x12\x12\n\nfirst_name\x18\x01 \x01(\t\x12\x11\n\tlast_name\x18\x02 \x01(\t\x12\r\n\x05\x65mail\x18\x03 \x01(\t\x12\x0b\n\x03\x61ge\x18\x04 \x01(\x05\x12(\n\x06gender\x18\x05 \x01(\x0e\x32\x18.protoBuf.Patient.Gender\x12\x0e\n\x06weight\x18\x06 \x01(\x02\x12\x0e\n\x06height\x18\x07 \x01(\x05\")\n\x06Gender\x12\x08\n\x04MALE\x10\x00\x12\n\n\x06\x46\x45MALE\x10\x01\x12\t\n\x05OTHER\x10\x02\x62\x06proto3')
  ,
  dependencies=[google_dot_protobuf_dot_any__pb2.DESCRIPTOR,])



_PATIENT_GENDER = _descriptor.EnumDescriptor(
  name='Gender',
  full_name='protoBuf.Patient.Gender',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='MALE', index=0, number=0,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='FEMALE', index=1, number=1,
      serialized_options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='OTHER', index=2, number=2,
      serialized_options=None,
      type=None),
  ],
  containing_type=None,
  serialized_options=None,
  serialized_start=521,
  serialized_end=562,
)
_sym_db.RegisterEnumDescriptor(_PATIENT_GENDER)


_COMPUTEREQUEST = _descriptor.Descriptor(
  name='ComputeRequest',
  full_name='protoBuf.ComputeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='algo_id', full_name='protoBuf.ComputeRequest.algo_id', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='req', full_name='protoBuf.ComputeRequest.req', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=58,
  serialized_end=126,
)


_COMPUTERESPONSE = _descriptor.Descriptor(
  name='ComputeResponse',
  full_name='protoBuf.ComputeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='response', full_name='protoBuf.ComputeResponse.response', index=0,
      number=1, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=128,
  serialized_end=185,
)


_COMPUTERESPONSES = _descriptor.Descriptor(
  name='ComputeResponses',
  full_name='protoBuf.ComputeResponses',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='responses', full_name='protoBuf.ComputeResponses.responses', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=187,
  serialized_end=251,
)


_INTRESPONSE = _descriptor.Descriptor(
  name='IntResponse',
  full_name='protoBuf.IntResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='val', full_name='protoBuf.IntResponse.val', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=253,
  serialized_end=279,
)


_QUERY = _descriptor.Descriptor(
  name='Query',
  full_name='protoBuf.Query',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='operator', full_name='protoBuf.Query.operator', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='protoBuf.Query.field', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='string_value', full_name='protoBuf.Query.string_value', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='numeric_value', full_name='protoBuf.Query.numeric_value', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=281,
  serialized_end=366,
)


_PATIENT = _descriptor.Descriptor(
  name='Patient',
  full_name='protoBuf.Patient',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='first_name', full_name='protoBuf.Patient.first_name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='last_name', full_name='protoBuf.Patient.last_name', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='email', full_name='protoBuf.Patient.email', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='age', full_name='protoBuf.Patient.age', index=3,
      number=4, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='gender', full_name='protoBuf.Patient.gender', index=4,
      number=5, type=14, cpp_type=8, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='weight', full_name='protoBuf.Patient.weight', index=5,
      number=6, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='protoBuf.Patient.height', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
    _PATIENT_GENDER,
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=369,
  serialized_end=562,
)

_COMPUTEREQUEST.fields_by_name['req'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_COMPUTERESPONSE.fields_by_name['response'].message_type = google_dot_protobuf_dot_any__pb2._ANY
_COMPUTERESPONSES.fields_by_name['responses'].message_type = _COMPUTERESPONSE
_PATIENT.fields_by_name['gender'].enum_type = _PATIENT_GENDER
_PATIENT_GENDER.containing_type = _PATIENT
DESCRIPTOR.message_types_by_name['ComputeRequest'] = _COMPUTEREQUEST
DESCRIPTOR.message_types_by_name['ComputeResponse'] = _COMPUTERESPONSE
DESCRIPTOR.message_types_by_name['ComputeResponses'] = _COMPUTERESPONSES
DESCRIPTOR.message_types_by_name['IntResponse'] = _INTRESPONSE
DESCRIPTOR.message_types_by_name['Query'] = _QUERY
DESCRIPTOR.message_types_by_name['Patient'] = _PATIENT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

ComputeRequest = _reflection.GeneratedProtocolMessageType('ComputeRequest', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTEREQUEST,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.ComputeRequest)
  ))
_sym_db.RegisterMessage(ComputeRequest)

ComputeResponse = _reflection.GeneratedProtocolMessageType('ComputeResponse', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTERESPONSE,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.ComputeResponse)
  ))
_sym_db.RegisterMessage(ComputeResponse)

ComputeResponses = _reflection.GeneratedProtocolMessageType('ComputeResponses', (_message.Message,), dict(
  DESCRIPTOR = _COMPUTERESPONSES,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.ComputeResponses)
  ))
_sym_db.RegisterMessage(ComputeResponses)

IntResponse = _reflection.GeneratedProtocolMessageType('IntResponse', (_message.Message,), dict(
  DESCRIPTOR = _INTRESPONSE,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.IntResponse)
  ))
_sym_db.RegisterMessage(IntResponse)

Query = _reflection.GeneratedProtocolMessageType('Query', (_message.Message,), dict(
  DESCRIPTOR = _QUERY,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.Query)
  ))
_sym_db.RegisterMessage(Query)

Patient = _reflection.GeneratedProtocolMessageType('Patient', (_message.Message,), dict(
  DESCRIPTOR = _PATIENT,
  __module__ = 'computation_pb2'
  # @@protoc_insertion_point(class_scope:protoBuf.Patient)
  ))
_sym_db.RegisterMessage(Patient)


# @@protoc_insertion_point(module_scope)
