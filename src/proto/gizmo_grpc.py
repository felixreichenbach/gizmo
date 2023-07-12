# Generated by the Protocol Buffers compiler. DO NOT EDIT!
# source: proto/gizmo.proto
# plugin: grpclib.plugin.main
import abc
import typing

import grpclib.client
import grpclib.const

if typing.TYPE_CHECKING:
    import grpclib.server

import google.api.annotations_pb2

from .. import proto


class GizmoServiceBase(abc.ABC):
    @abc.abstractmethod
    async def DoOne(self, stream: "grpclib.server.Stream[proto.gizmo_pb2.DoOneRequest, proto.gizmo_pb2.DoOneResponse]") -> None:
        pass

    @abc.abstractmethod
    async def DoOneClientStream(
        self, stream: "grpclib.server.Stream[proto.gizmo_pb2.DoOneClientStreamRequest, proto.gizmo_pb2.DoOneClientStreamResponse]"
    ) -> None:
        pass

    @abc.abstractmethod
    async def DoOneServerStream(
        self, stream: "grpclib.server.Stream[proto.gizmo_pb2.DoOneServerStreamRequest, proto.gizmo_pb2.DoOneServerStreamResponse]"
    ) -> None:
        pass

    @abc.abstractmethod
    async def DoOneBiDiStream(
        self, stream: "grpclib.server.Stream[proto.gizmo_pb2.DoOneBiDiStreamRequest, proto.gizmo_pb2.DoOneBiDiStreamResponse]"
    ) -> None:
        pass

    @abc.abstractmethod
    async def DoTwo(self, stream: "grpclib.server.Stream[proto.gizmo_pb2.DoTwoRequest, proto.gizmo_pb2.DoTwoResponse]") -> None:
        pass

    def __mapping__(self) -> typing.Dict[str, grpclib.const.Handler]:
        return {
            "/acme.component.gizmo.v1.GizmoService/DoOne": grpclib.const.Handler(
                self.DoOne,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.gizmo_pb2.DoOneRequest,
                proto.gizmo_pb2.DoOneResponse,
            ),
            "/acme.component.gizmo.v1.GizmoService/DoOneClientStream": grpclib.const.Handler(
                self.DoOneClientStream,
                grpclib.const.Cardinality.STREAM_UNARY,
                proto.gizmo_pb2.DoOneClientStreamRequest,
                proto.gizmo_pb2.DoOneClientStreamResponse,
            ),
            "/acme.component.gizmo.v1.GizmoService/DoOneServerStream": grpclib.const.Handler(
                self.DoOneServerStream,
                grpclib.const.Cardinality.UNARY_STREAM,
                proto.gizmo_pb2.DoOneServerStreamRequest,
                proto.gizmo_pb2.DoOneServerStreamResponse,
            ),
            "/acme.component.gizmo.v1.GizmoService/DoOneBiDiStream": grpclib.const.Handler(
                self.DoOneBiDiStream,
                grpclib.const.Cardinality.STREAM_STREAM,
                proto.gizmo_pb2.DoOneBiDiStreamRequest,
                proto.gizmo_pb2.DoOneBiDiStreamResponse,
            ),
            "/acme.component.gizmo.v1.GizmoService/DoTwo": grpclib.const.Handler(
                self.DoTwo,
                grpclib.const.Cardinality.UNARY_UNARY,
                proto.gizmo_pb2.DoTwoRequest,
                proto.gizmo_pb2.DoTwoResponse,
            ),
        }


class GizmoServiceStub:
    def __init__(self, channel: grpclib.client.Channel) -> None:
        self.DoOne = grpclib.client.UnaryUnaryMethod(
            channel,
            "/acme.component.gizmo.v1.GizmoService/DoOne",
            proto.gizmo_pb2.DoOneRequest,
            proto.gizmo_pb2.DoOneResponse,
        )
        self.DoOneClientStream = grpclib.client.StreamUnaryMethod(
            channel,
            "/acme.component.gizmo.v1.GizmoService/DoOneClientStream",
            proto.gizmo_pb2.DoOneClientStreamRequest,
            proto.gizmo_pb2.DoOneClientStreamResponse,
        )
        self.DoOneServerStream = grpclib.client.UnaryStreamMethod(
            channel,
            "/acme.component.gizmo.v1.GizmoService/DoOneServerStream",
            proto.gizmo_pb2.DoOneServerStreamRequest,
            proto.gizmo_pb2.DoOneServerStreamResponse,
        )
        self.DoOneBiDiStream = grpclib.client.StreamStreamMethod(
            channel,
            "/acme.component.gizmo.v1.GizmoService/DoOneBiDiStream",
            proto.gizmo_pb2.DoOneBiDiStreamRequest,
            proto.gizmo_pb2.DoOneBiDiStreamResponse,
        )
        self.DoTwo = grpclib.client.UnaryUnaryMethod(
            channel,
            "/acme.component.gizmo.v1.GizmoService/DoTwo",
            proto.gizmo_pb2.DoTwoRequest,
            proto.gizmo_pb2.DoTwoResponse,
        )