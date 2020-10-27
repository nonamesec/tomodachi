from tomodachi.__version__ import __version_info__ as __version_info__
from tomodachi.helpers.execution_context import (
    clear_execution_context as _clear_execution_context,
    clear_services as _clear_services,
    decrease_execution_context_value as decrease_execution_context_value,
    get_execution_context as get_execution_context,
    get_instance as get_instance,
    get_service as get_service,
    increase_execution_context_value as increase_execution_context_value,
    set_execution_context as set_execution_context,
    set_service as _set_service,
    unset_service as _unset_service,
)
from tomodachi.invoker import decorator as decorator
from tomodachi.transport.amqp import amqp as amqp, amqp_publish as amqp_publish
from tomodachi.transport.aws_sns_sqs import aws_sns_sqs as aws_sns_sqs, aws_sns_sqs_publish as aws_sns_sqs_publish
from tomodachi.transport.http import (
    HttpException as HttpException,
    Response as HttpResponse,
    get_http_response_status as get_http_response_status,
    http as http,
    http_error as http_error,
    http_static as http_static,
    websocket as websocket,
    ws as ws,
)
from tomodachi.transport.schedule import (
    daily as daily,
    heartbeat as heartbeat,
    hourly as hourly,
    minutely as minutely,
    monthly as monthly,
    schedule as schedule,
)
from typing import Any, Callable, Dict, Tuple, Type

def __getattr__(name: str) -> Any: ...

__author__: str = ...
__email__: str = ...

CLASS_ATTRIBUTE: str = ...

class TomodachiServiceMeta(type):
    def __new__(
        cls: Type[TomodachiServiceMeta], name: str, bases: Tuple[type, ...], attributedict: Dict
    ) -> TomodachiServiceMeta: ...

class Service(metaclass=TomodachiServiceMeta):
    _tomodachi_class_is_service_class: bool = ...
    name: str = ...
    uuid: str = ...
    log: Callable = ...
    log_setup: Callable = ...

def service(cls: Type[object]) -> Type[TomodachiServiceMeta]: ...
