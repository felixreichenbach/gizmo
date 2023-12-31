"""
@generated by mypy-protobuf.  Do not edit manually!
isort:skip_file
"""
import builtins
import google.protobuf.descriptor
import google.protobuf.message
import sys

if sys.version_info >= (3, 8):
    import typing as typing_extensions
else:
    import typing_extensions

DESCRIPTOR: google.protobuf.descriptor.FileDescriptor

@typing_extensions.final
class DoOneRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARG1_FIELD_NUMBER: builtins.int
    name: builtins.str
    arg1: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        arg1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg1", b"arg1", "name", b"name"]) -> None: ...

global___DoOneRequest = DoOneRequest

@typing_extensions.final
class DoOneResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RET1_FIELD_NUMBER: builtins.int
    ret1: builtins.bool
    def __init__(
        self,
        *,
        ret1: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ret1", b"ret1"]) -> None: ...

global___DoOneResponse = DoOneResponse

@typing_extensions.final
class DoOneServerStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARG1_FIELD_NUMBER: builtins.int
    name: builtins.str
    arg1: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        arg1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg1", b"arg1", "name", b"name"]) -> None: ...

global___DoOneServerStreamRequest = DoOneServerStreamRequest

@typing_extensions.final
class DoOneServerStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RET1_FIELD_NUMBER: builtins.int
    ret1: builtins.bool
    def __init__(
        self,
        *,
        ret1: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ret1", b"ret1"]) -> None: ...

global___DoOneServerStreamResponse = DoOneServerStreamResponse

@typing_extensions.final
class DoOneClientStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARG1_FIELD_NUMBER: builtins.int
    name: builtins.str
    arg1: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        arg1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg1", b"arg1", "name", b"name"]) -> None: ...

global___DoOneClientStreamRequest = DoOneClientStreamRequest

@typing_extensions.final
class DoOneClientStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RET1_FIELD_NUMBER: builtins.int
    ret1: builtins.bool
    def __init__(
        self,
        *,
        ret1: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ret1", b"ret1"]) -> None: ...

global___DoOneClientStreamResponse = DoOneClientStreamResponse

@typing_extensions.final
class DoOneBiDiStreamRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARG1_FIELD_NUMBER: builtins.int
    name: builtins.str
    arg1: builtins.str
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        arg1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg1", b"arg1", "name", b"name"]) -> None: ...

global___DoOneBiDiStreamRequest = DoOneBiDiStreamRequest

@typing_extensions.final
class DoOneBiDiStreamResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RET1_FIELD_NUMBER: builtins.int
    ret1: builtins.bool
    def __init__(
        self,
        *,
        ret1: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ret1", b"ret1"]) -> None: ...

global___DoOneBiDiStreamResponse = DoOneBiDiStreamResponse

@typing_extensions.final
class DoTwoRequest(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    NAME_FIELD_NUMBER: builtins.int
    ARG1_FIELD_NUMBER: builtins.int
    name: builtins.str
    arg1: builtins.bool
    def __init__(
        self,
        *,
        name: builtins.str = ...,
        arg1: builtins.bool = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["arg1", b"arg1", "name", b"name"]) -> None: ...

global___DoTwoRequest = DoTwoRequest

@typing_extensions.final
class DoTwoResponse(google.protobuf.message.Message):
    DESCRIPTOR: google.protobuf.descriptor.Descriptor

    RET1_FIELD_NUMBER: builtins.int
    ret1: builtins.str
    def __init__(
        self,
        *,
        ret1: builtins.str = ...,
    ) -> None: ...
    def ClearField(self, field_name: typing_extensions.Literal["ret1", b"ret1"]) -> None: ...

global___DoTwoResponse = DoTwoResponse