"""
FastAPI applications.
"""

from typing import Any, Callable, Dict, List, Optional, Sequence, Tuple, Union

from fastapi import routing
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi
from fastapi.types import ASGIApp


class FastAPI:
    """
    The main FastAPI class.
    """

    def __init__(
        self,
        *,
        debug: bool = False,
        routes: Optional[List[routing.BaseRoute]] = None,
        title: str = "FastAPI",
        description: str = "",
        version: str = "0.1.0",
        openapi_url: Optional[str] = "/openapi.json",
        openapi_tags: Optional[List[Dict[str, Any]]] = None,
        servers: Optional[List[Dict[str, Union[str, Any]]]] = None,
        docs_url: Optional[str] = "/docs",
        redoc_url: Optional[str] = "/redoc",
        swagger_ui_oauth2_redirect_url: Optional[str] = "/docs/oauth2-redirect",
        swagger_ui_init_oauth: Optional[Dict[str, Any]] = None,
        middleware: Optional[Sequence[ASGIApp]] = None,
        exception_handlers: Optional[Dict[Union[int, type[Exception]], Callable]] = None,
        on_startup: Optional[Sequence[Callable]] = None,
        on_shutdown: Optional[Sequence[Callable]] = None,
        default_response_class: type = None,
        **extra: Any,
    ) -> None:
        self.debug: bool = debug
        self.routes: List[routing.BaseRoute] = list(routes) if routes else []
        self.title: str = title
        self.description: str = description
        self.version: str = version
        self.openapi_url: str = openapi_url
        self.openapi_tags: Optional[List[Dict[str, Any]]] = openapi_tags
        self.servers: Optional[List[Dict[str, Union[str, Any]]]] = servers
        self.docs_url: str = docs_url
        self.redoc_url: str = redoc_url
        self.swagger_ui_oauth2_redirect_url: str = swagger_ui_oauth2_redirect_url
        self.swagger_ui_init_oauth: Optional[Dict[str, Any]] = swagger_ui_init_oauth
        self.middleware: Sequence[ASGIApp] = list(middleware) if middleware else []
        self.exception_handlers: Dict[Union[int, type[Exception]], Callable] = (
            dict(exception_handlers) if exception_handlers else {}
        )
        self.on_startup: List[Callable] = list(on_startup) if on_startup else []
        self.on_shutdown: List[Callable] = list(on_shutdown) if on_shutdown else []
        self.default_response_class: type = default_response_class
        self.extra: Dict[str, Any] = extra

        self.router: routing.APIRouter = routing.APIRouter(
            routes=self.routes,
            dependency_overrides_provider=self,
            on_startup=self.on_startup,
            on_shutdown=self.on_shutdown,
            default_response_class=self.default_response_class,
        )

    def add_middleware(
        self,
        middleware_class: type,
        **kwargs: Any,
    ) -> None:
        self.middleware.append(middleware_class(**kwargs))

    def middleware(
        self, middleware_type: str
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            self.add_middleware(middleware_type, dispatch=func)
            return func

        return decorator

    def include_router(
        self,
        router: routing.APIRouter,
        *,
        prefix: str = "",
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        default_response_class: Optional[type] = None,
        callbacks: Optional[List[BaseModel]] = None,
        include_in_schema: bool = True,
    ) -> None:
        self.router.include_router(
            router,
            prefix=prefix,
            tags=tags,
            dependencies=dependencies,
            responses=responses,
            default_response_class=default_response_class,
            callbacks=callbacks,
            include_in_schema=include_in_schema,
        )

    def get(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.get(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def post(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.post(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def put(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
            response_model_exclude_defaults: bool = False,
            response_model_exclude_none: bool = False,
            include_in_schema: bool = True,
            response_class: type = None,
            name: Optional[str] = None,
            callbacks: Optional[List[BaseModel]] = None,
            openapi_extra: Optional[Dict[str, Any]] = None,
        ) -> Callable:
            return self.router.put(
                path,
                response_model=response_model,
                status_code=status_code,
                tags=tags,
                dependencies=dependencies,
                summary=summary,
                description=description,
                response_description=response_description,
                responses=responses,
                deprecated=deprecated,
                operation_id=operation_id,
                response_model_include=response_model_include,
                response_model_exclude=response_model_exclude,
                response_model_by_alias=response_model_by_alias,
                response_model_exclude_unset=response_model_exclude_unset,
                response_model_exclude_defaults=response_model_exclude_defaults,
                response_model_exclude_none=response_model_exclude_none,
                include_in_schema=include_in_schema,
                response_class=response_class,
                name=name,
                callbacks=callbacks,
                openapi_extra=openapi_extra,
            )

    def delete(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.delete(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def options(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.options(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def head(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.head(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def patch(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.patch(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def trace(
        self,
        path: str,
        *,
        response_model: Optional[type] = None,
        status_code: int = 200,
        tags: Optional[List[str]] = None,
        dependencies: Optional[Sequence[routing.Depends]] = None,
        summary: Optional[str] = None,
        description: Optional[str] = None,
        response_description: str = "Successful Response",
        responses: Optional[Dict[Union[int, str], Dict[str, Any]]] = None,
        deprecated: Optional[bool] = None,
        operation_id: Optional[str] = None,
        response_model_include: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_exclude: Optional[Union[SetIntStr, DictStrAny]] = None,
        response_model_by_alias: bool = True,
        response_model_exclude_unset: bool = False,
        response_model_exclude_defaults: bool = False,
        response_model_exclude_none: bool = False,
        include_in_schema: bool = True,
        response_class: type = None,
        name: Optional[str] = None,
        callbacks: Optional[List[BaseModel]] = None,
        openapi_extra: Optional[Dict[str, Any]] = None,
    ) -> Callable:
        return self.router.trace(
            path,
            response_model=response_model,
            status_code=status_code,
            tags=tags,
            dependencies=dependencies,
            summary=summary,
            description=description,
            response_description=response_description,
            responses=responses,
            deprecated=deprecated,
            operation_id=operation_id,
            response_model_include=response_model_include,
            response_model_exclude=response_model_exclude,
            response_model_by_alias=response_model_by_alias,
            response_model_exclude_unset=response_model_exclude_unset,
            response_model_exclude_defaults=response_model_exclude_defaults,
            response_model_exclude_none=response_model_exclude_none,
            include_in_schema=include_in_schema,
            response_class=response_class,
            name=name,
            callbacks=callbacks,
            openapi_extra=openapi_extra,
        )

    def add_event_handler(self, event_type: str, func: Callable) -> None:
        if event_type == "startup":
            self.on_startup.append(func)
        elif event_type == "shutdown":
            self.on_shutdown.append(func)

    def on_event(self, event_type: str) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_event_handler(event_type, func)
            return func

        return decorator

    def add_exception_handler(
        self,
        exc_class_or_status_code: Union[int, type[Exception]],
        handler: Callable,
    ) -> None:
        self.exception_handlers[exc_class_or_status_code] = handler

    def exception_handler(
        self,
        exc_class_or_status_code: Union[int, type[Exception]],
    ) -> Callable:
        def decorator(func: Callable) -> Callable:
            self.add_exception_handler(exc_class_or_status_code, func)
            return func

        return decorator

    def openapi(self) -> Dict[str, Any]:
        if not self.openapi_url:
            return {}
        return get_openapi(
            title=self.title,
            version=self.version,
            openapi_version=self.openapi_version,
            description=self.description,
            routes=self.routes,
            tags=self.openapi_tags,
            servers=self.servers,
        )

    def openapi_schema(self) -> Dict[str, Any]:
        return self.openapi()

    def docs(self, request: Request) -> Response:
        return get_swagger_ui_html(
            openapi_url=self.openapi_url,
            title=self.title + " - Swagger UI",
            oauth2_redirect_url=self.swagger_ui_oauth2_redirect_url,
            init_oauth=self.swagger_ui_init_oauth,
        )

    def redoc(self, request: Request) -> Response:
        return get_redoc_html(
            openapi_url=self.openapi_url,
            title=self.title + " - ReDoc",
        )
